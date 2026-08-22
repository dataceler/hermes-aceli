# Banco Inter — Banking read-only via mTLS

Use this reference when connecting a Banco Inter application to read balance or statement data.

## Confirmed authentication flow

Required material:

- application Client ID;
- application Client Secret;
- client certificate and matching private key;
- Inter CA chain for TLS verification.

Keep all four outside Git and runtime export. Store under a restricted secrets directory (directory `700`, files `600`). Do not paste or print the Client Secret, private key, bearer token, account identifier, or raw API response.

## Production token request

```text
POST https://cdpj.partners.bancointer.com.br/oauth/v2/token
Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials
scope=extrato.read
```

Use mutual TLS with the client certificate/key and HTTP Basic authentication with Client ID and Client Secret.

### Important scope correction

Do **not** infer the balance scope as `saldo.read`. The Inter Banking reference for `GET /banking/v2/saldo` specifies `extrato.read`. A request for `saldo.read` can be rejected with a registered-scope error even when the application credentials and mTLS certificate are valid.

## Read-only balance validation

After token issuance, call:

```text
GET https://cdpj.partners.bancointer.com.br/banking/v2/saldo
Authorization: Bearer <temporary-token>
```

Use the same mTLS certificate/key and CA chain. Report only the requested financial fields (for example, `disponivel` and `limite`), never the raw JSON or account identifiers.

## Safe implementation pattern

1. Verify certificate validity and that the client certificate public key matches the private key before any network request.
2. Put HTTP Basic credentials and bearer token in a mode-`600` temporary curl config or equivalent secure request configuration; do not place secrets in shell history, command arguments, source control, logs, chat, or YAML.
3. Validate token issuance before querying an account endpoint.
4. Make only `GET` requests during the initial integration.
5. Delete token responses, raw balance responses, curl configs, and error bodies immediately after extracting the minimal required metadata. Retain only durable credential files in the protected secrets directory.
6. If credentials or private key were transmitted through chat, recommend rotating them in the Inter portal after the immediate validation; accept replacement material only through a secure file-transfer channel.

## Statement history and aggregated dashboards

### API contract verified

- `GET /banking/v2/extrato` requires `extrato.read` and accepts `dataInicio` and `dataFim` in `YYYY-MM-DD`.
- Each request may cover at most **90 days**. For a longer history, split the range into contiguous 90-day windows; do not overlap or leave gaps.
- The basic response is `transacoes`. Its aggregation fields are `dataEntrada`, `tipoOperacao` and `valor`:
  - `C` is a credit / entry.
  - `D` is a debit / outflow.
- The enriched statement endpoint supports pagination, but do not use it merely to build a high-level dashboard when the basic endpoint provides the required aggregates.

### Safe dashboard pattern

1. Confirm the period and intended output before reading broad financial history. If account-opening date is uncertain, begin at the earliest confirmed date.
2. Fetch read-only 90-day windows, reuse one short-lived token only in memory, and aggregate entries, outflows, net result, monthly totals and transaction count in memory.
3. For an aggregate dashboard, do **not** retain descriptions, counterparties, account identifiers or raw API response files. Save only the user-approved aggregate artifact, using restrictive file permissions such as `600`.
4. Label the dashboard as an API snapshot with its exact period. Do not infer account-opening date from the first returned transaction alone.
5. Delete temporary token, response and error files after extracting the approved aggregates.

## Revocation verification

When a user says an Inter integration was cancelled or revoked:

1. Attempt only the mTLS token request with `extrato.read`.
2. If token issuance is refused, report that practical API access is revoked or unavailable; do not attempt an account read.
3. If a token is still issued, make one minimal `GET /banking/v2/saldo` request and report only whether it succeeds, never the balance unless expressly requested.
4. Remove temporary authentication artifacts. Do not delete long-lived local credential files without explicit confirmation, even if they are no longer usable.

## Scope boundary

Default allowed capabilities: balance and statement read access only. Do not enable or invoke Pix, transfers, payments, collections, webhooks that trigger movement, or other write-capable endpoints without explicit user instruction and a separate permission review.

## Evidence boundary

This procedure was validated against the public Inter developer reference embedded in the Banking documentation and with a successful mTLS token + `GET /banking/v2/saldo` read-only call. Endpoint labels and available products in the Internet Banking UI can change; confirm current product permissions in the portal before expanding scope.
