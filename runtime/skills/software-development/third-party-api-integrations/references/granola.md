# Granola API

Official docs: `https://docs.granola.ai/introduction`

## Connection

- Base URL: `https://public-api.granola.ai`
- Authentication: `Authorization: Bearer <grn_...>`
- Recommended secret variable: `GRANOLA_API_KEY`
- API access requires a Business or Enterprise workspace.
- Keys can include personal notes, public notes, or both. Workspace keys are scoped differently from personal keys.

## Safe validation

Use the read-only notes listing endpoint and return only status/count metadata:

```text
GET /v1/notes?limit=1
```

Success is HTTP 200 with a JSON object containing `notes`, `hasMore`, and optionally `cursor`. Do not print note titles, summaries, owners, or transcripts during a connection probe.

## Useful reads

- List notes: `GET /v1/notes`
- Retrieve one note: `GET /v1/notes/{not_id}`
- Include transcript only when requested: `?include=transcript`
- Note IDs use the `not_` form from list responses.

The public API only returns notes with generated AI summaries and transcripts. A valid key may therefore return an empty list.

## Limits and safety

- API is focused on reading meeting notes, summaries, and transcripts.
- Burst: 25 requests per 5 seconds.
- Sustained: 5 requests/second.
- Respect note privacy and avoid exposing meeting content in diagnostics.
- No gateway restart is needed for direct API calls; a custom/native tool would have separate loading requirements.
