# NFS-e SOAP integration with ICP-Brasil certificates

Use this reference when integrating municipal NFS-e providers that expose SOAP/XML services protected by ICP-Brasil certificates. It captures a reusable safety and implementation pattern; always re-check the current municipality manual, XSD, WSDL, and fiscal rules.

## Core distinction

An official NFS-e “API” may not use an API key. Common requirements are:

- SOAP requests carrying schema-conformant XML;
- mutual TLS (client certificate during transport);
- XML Digital Signature on each DPS and, when applicable, on the containing batch;
- an ICP-Brasil A1 or A3 certificate whose subject matches the authorized transmitter/emitter rules;
- municipality-specific business validation in addition to national schemas.

A WSDL returning HTTP 403 without a client certificate can be expected behavior under mutual TLS. Do not conclude that the service is unavailable until probing with the documented certificate flow.

## A1 versus A3

- **A1 (`.pfx`/`.p12`)**: suitable for controlled headless automation when encrypted at rest, access-restricted, monitored, and loaded only at runtime.
- **A3 (token/card/HSM-backed)**: often requires attached hardware, middleware and PIN interaction. Do not promise unattended VPS operation without proving the device and PKCS#11 path.

## Safe credential intake

Never request or accept the certificate password in chat. Never print certificate contents, subject identifiers, private-key metadata, or secret paths unnecessarily.

Preferred order:

1. managed secret store (for example, 1Password service account or another approved vault);
2. SSH/SFTP transfer to a root-only directory plus interactive secret entry;
3. plaintext secret file only as an explicitly accepted fallback, mode `600`, outside source control.

For local storage:

- parent directory mode `700`;
- certificate mode `600`;
- keep password separate from the certificate;
- exclude both from repositories, backups without encryption, logs, shell history and support bundles;
- validate expiry and intended key usage without exposing CPF/CNPJ in output.

## Implementation sequence

1. Obtain current official manual, WSDL, XSDs, XML examples and auxiliary code tables.
2. Identify transport authentication, XML signature algorithm, canonicalization, namespaces and element IDs from the current manual—never copy old defaults blindly.
3. Obtain homologation access before touching production.
4. Validate the certificate locally: parseability, expiry, chain, key usage and private-key availability.
5. Generate XML from typed input, not string concatenation.
6. Validate unsigned structures against XSD.
7. Sign exactly the elements required by the provider (for example each DPS, then the batch) and revalidate.
8. Submit to homologation using mutual TLS.
9. Exercise non-destructive calls first: identity/cadastro, schema validator, consultation or URL lookup where available.
10. Test emission only in homologation with explicit authorization and clearly synthetic data accepted by that environment.
11. Compare returned protocol, errors and generated XML with the submitted payload.
12. Enable production behind a separate explicit confirmation gate.

## Fiscal safety gate

Do not infer or silently default:

- service code or list item;
- municipality of incidence;
- tax regime;
- ISS retention;
- rate;
- deductions;
- PIS/COFINS/CSLL/IRRF/INSS or IBS/CBS fields;
- competence date or substitution/cancellation reason.

Before each production issuance, present a concise immutable summary of emitter, customer, service, amount, competence, incidence, taxes/withholdings and destination. Require explicit confirmation tied to that exact summary. A general authorization to “use the API” is not authorization to emit a specific document.

## Verification after issuance

Treat HTTP success as transport success, not fiscal success. Verify:

- application-level status and error list;
- protocol/lot identifiers;
- generated NFS-e number and verification code;
- returned XML signature and issuer identity where available;
- official visualization/authenticity URL;
- downloaded XML/PDF integrity;
- idempotency or duplicate-DPS behavior before retrying.

Never blindly retry an issuance after timeout. Query by DPS/RPS/lote first; otherwise a retry can create a duplicate fiscal document.

## Cancellation and substitution

Model issuance, cancellation and substitution as distinct privileged operations. Each requires its own explicit approval and post-operation verification. Do not treat cancellation as a harmless cleanup step for a failed test.
