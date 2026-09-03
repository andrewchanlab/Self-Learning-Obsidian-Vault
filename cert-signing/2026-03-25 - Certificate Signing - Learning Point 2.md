---
title: "2026-03-25 - Certificate Signing - Learning Point 2"
tags:
  - learning
  - cert-signing
created: 2026-03-25
---

# X.509 Certificates: What a Certificate Actually Contains

An X.509 certificate is a structured data format (ASN.1/DER) that binds a public key to an identity via a digital signature. The key fields: Subject (CN=`github.com`, O=`GitHub, Inc.`), Issuer (the CA that signed it), Validity period (not before / not after — certificates expire), Subject Alternative Names (SAN — additional domains the cert is valid for), and the Signature (the issuer's digital signature over all the above fields). The signature proves the CA vouching for this identity — when you trust the CA's root certificate in your trust store, you trust every certificate that chain-of-trusts up to it.

## Key Takeaway
An X.509 certificate is essentially a signed statement: "I (the Issuer CA) confirm that this public key belongs to this entity (the Subject)."

## Related Concepts
- ASN.1 and DER encoding formats
- Common Name (CN) vs Subject Alternative Names
- Certificate fingerprints and serial numbers
