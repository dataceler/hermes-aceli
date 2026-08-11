# Google OAuth, API enablement, and YouTube read-only

Use this reference when a Google API has been enabled in Cloud Console but Hermes still cannot access it, or when adding YouTube Data API access without granting channel-management permissions.

## Three separate gates

1. **API enabled in the correct Google Cloud project** — Library → enable the target API (for example YouTube Data API v3).
2. **Credential belongs to that project** — the installed OAuth client or API key must come from the same project.
3. **Credential is authorized for the needed operation** — enabling an API does not add scopes to an already-issued OAuth token.

A user saying “I enabled the API” confirms only gate 1. Inspect the current token scopes before diagnosing the service as unavailable.

## Choose the credential model

- **Public YouTube data only:** an API key can query public channels, videos, playlists, comments, and search results. It does not identify the user's account.
- **Authenticated account, read-only:** request `https://www.googleapis.com/auth/youtube.readonly` through OAuth.
- **Write/upload/management:** requires broader scopes such as `youtube`, `youtube.force-ssl`, or `youtube.upload`. Do not add these by default.

For a least-privilege Workspace bundle, preserve the user's existing exact scopes and append only `youtube.readonly`. Re-consent is required; an old token does not gain a new scope automatically.

## Reauthorization workflow

1. Read the current authorized scope set and preserve it exactly.
2. Add only the requested new scope.
3. Generate a new OAuth URL with offline access and explicit consent.
4. The localhost redirect may fail in the browser; exchange the complete redirected URL/code using the pending PKCE state.
5. Save the new token with POSIX mode `600`.
6. Verify that expected scopes are present and that write scopes are absent.
7. Perform a real read-only API call before declaring success.

If refresh returns `invalid_grant` (expired or revoked token), stop retrying and run a fresh authorization flow. Do not describe API enablement as the cause unless a real request returns `accessNotConfigured` or equivalent.

## YouTube verification

Use an authenticated request equivalent to:

```text
GET https://www.googleapis.com/youtube/v3/channels
  ?part=id,snippet,statistics
  &mine=true
```

Success criteria:

- HTTP 200;
- one or more authenticated channels when the account owns a channel;
- `youtube.readonly` present;
- `youtube`, `youtube.force-ssl`, and `youtube.upload` absent unless explicitly requested.

OAuth read-only access can also query public resources belonging to other channels. It does not expose other channels' private data.

## Efficient “most viewed videos” workflow

Avoid `search.list` for complete channel inventories because it is quota-expensive and may not enumerate the channel as cleanly.

1. Resolve the handle with `channels.list(forHandle=...)`.
2. Read `contentDetails.relatedPlaylists.uploads`.
3. Enumerate all video IDs with paginated `playlistItems.list` (50 per page).
4. Fetch metadata and statistics using `videos.list` in batches of 50.
5. Parse `statistics.viewCount` as an integer and sort descending.
6. Report how many uploads were enumerated and timestamp the result conceptually, since view counts change.

## Verification pitfalls

- A successful public health/discovery request is not proof that the user's OAuth credential works.
- `--check-live` for a multi-service helper may validate only one API; test important services individually.
- Some APIs require a resource ID. Prefer an existing resource discovered through Drive. If none exists, an authenticated request for a syntactically valid nonexistent ID may return expected 404, which distinguishes it from project-level `403 accessNotConfigured`, but does not prove every resource-specific permission.
- Local helper interfaces may drift from skill prose. Run the helper's `--help` before relying on optional flags such as `--format`; do not repeatedly retry an unsupported flag.
- Never print access tokens, refresh tokens, OAuth callback codes, or client secrets. OAuth authorization URLs and callback codes are temporary but should still be handled as sensitive and not preserved in long-term notes.
