# Hostinger API

Official reference: `https://developers.hostinger.com/`

## Connection

- Production base URL: `https://developers.hostinger.com`
- Authentication: `Authorization: Bearer <token>`
- Send `Accept: application/json` and `Content-Type: application/json`.
- A stable user agent can avoid WAF inconsistencies during repeated probes.
- Recommended secret variable: `HOSTINGER_API_TOKEN`

Hostinger user tokens have the same permissions as the owning user. A successful read-only probe does **not** prove the token itself is read-only.

## Safe validation

Use VPS inventory when VPS access is expected:

```text
GET /api/vps/v1/virtual-machines
```

Return only HTTP status, authentication result, and resource count. Do not disclose VPS IPs, hostnames, subscription IDs, SSH keys, or detailed infrastructure unless requested.

## Useful read-only areas

The OpenAPI reference includes inventory/details for:

- virtual machines;
- backups and snapshots;
- firewalls;
- public keys;
- data centers and OS templates;
- PTR records;
- Docker Manager projects and containers where supported.

Always inspect the current OpenAPI document before using a path because the API evolves.

## Safety

- Treat all non-GET operations as potentially impactful.
- Reinstall, delete, reset, recovery, firewall mutation, hostname/PTR changes, and lifecycle actions require explicit user intent and scope confirmation.
- If a repeated authenticated request unexpectedly returns 403 after a prior success, retry once with the documented content headers and a stable user agent; do not assume the token is revoked from one WAF-shaped response.
