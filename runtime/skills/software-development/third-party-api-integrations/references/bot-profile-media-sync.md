# Bot profile media synchronization through platform APIs

Use this reference when copying a bot avatar or display identity between messaging platforms. Platform profile mutations are global account changes unless the API explicitly targets a guild/workspace nickname.

## Safety and scope

- Confirm whether the requested change is global or server/workspace-specific.
- Do not print bot tokens, authorization headers, user IDs or full API responses.
- Read the source image first, inspect it, then mutate the destination.
- Preserve a durable local copy outside ephemeral caches when the asset is an approved brand artifact.
- Verify the destination by reading the account object and downloading the asset from the destination CDN.

## Telegram source pattern

For a bot’s current profile image:

1. call `getMe` to obtain the bot user ID;
2. call `getUserProfilePhotos` with that user ID;
3. choose the largest variant of the newest photo;
4. call `getFile` with its `file_id`;
5. download using the returned `file_path`;
6. validate dimensions, file type and integrity before reuse.

Telegram Bot API can change the bot’s visible name (`setMyName`), but the username is managed separately (normally through BotFather). Do not claim a username was changed merely because the visible name changed.

## Discord destination pattern

To update a bot’s global avatar:

1. GET `/api/v10/users/@me` and record only sanitized metadata plus the pre-change avatar hash;
2. encode the approved image as a `data:<mime>;base64,...` URI;
3. PATCH `/api/v10/users/@me` with the `avatar` field;
4. GET `/users/@me` again;
5. require a present avatar hash and verify that it changed;
6. download the resulting image from the Discord CDN and inspect it.

The global bot username and avatar affect every guild. A guild nickname is a different, scoped operation.

## CDN verification pitfall

A Discord API mutation can succeed while an immediate anonymous CDN fetch returns HTTP 403. Retry the CDN fetch with a normal `User-Agent` (and, when needed, a Discord referer) before treating verification as failed. The durable lesson is the verified retry pattern—not a claim that the CDN is broken.

Choose `.gif` for avatar hashes beginning with `a_`; otherwise use `.png`. Request a supported square size and compare visual content, not file bytes, because the CDN may re-encode the image.

## Visual QA

Before upload and again from the destination CDN, verify:

- square dimensions and supported format;
- readable face/symbol at small size;
- safe margin for circular cropping;
- no clipped logo, text or facial features;
- sufficient foreground/background contrast;
- no unintended substitution, deformation or material quality loss.

Report success only after both API state verification and destination-asset verification pass. If the mutation succeeded but secondary verification failed, say so, retry safely, and do not falsely report total failure or total success until resolved.
