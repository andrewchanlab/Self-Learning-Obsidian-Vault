---
title: "2026-03-25 - Certificate Signing - Learning Point 3"
tags:
  - learning
  - cert-signing
created: 2026-03-25
---

# Certificate Revocation: CRL, OCSP, and OCSP Stapling

What happens when a certificate is compromised? The CA publishes a Certificate Revocation List (CRL) — a signed list of revoked serial numbers — and/or serves revocation status via OCSP (Online Certificate Status Protocol). The problem: CRLs grow unbounded and clients must download the entire list; OCSP forces clients to make a live network request to the CA (a privacy and reliability issue). OCSP Stapling solves this: the web server periodically fetches its own revocation status from the CA and "staples" it to the TLS handshake, so the client gets the answer without contacting the CA. Modern browsers also use CRLSets (Chrome) and OneCRL (Firefox) — locally-cached revocation lists compiled from reported compromises.

## Key Takeaway
Certificate revocation is notoriously hard — OCSP Stapling is the practical solution for production servers, combining live checking with zero client-side network overhead.

## Related Concepts
- CRL distribution points
- OCSP responder and stapling
- HSTS and Certificate Transparency logs
