# Live ICANN DANE qualification: `dane-test.denuoweb.com`

Date: 2026-07-25
Trust path under test: **DANE via ICANN DoH**, with the browser deriving the
TLSA owner from the HTTPS origin and using an authenticated validating ICANN
DoH resolver.

## Secure TLSA presence

Command:

```sh
delv _443._tcp.dane-test.denuoweb.com. TLSA
```

Observed:

```text
; fully validated
_443._tcp.dane-test.denuoweb.com. 7467 IN TLSA 3 1 1 369E0DBBA20489BDEE1A963239716DD16C6FECC6EFC30116889AB6AD6DC18BAE
_443._tcp.dane-test.denuoweb.com. 7467 IN RRSIG TLSA 8 5 14400 20260815163032 20260724163032 8746 denuoweb.com. ...
```

The owner name follows directly from HTTPS port 443 and TCP:
`_443._tcp.dane-test.denuoweb.com.`. No gateway-specific discovery record is
involved.

## Parent DS

Command:

```sh
delv denuoweb.com. DS
```

Observed:

```text
; fully validated
denuoweb.com. 25095 IN DS 56057 8 2 4B141B6F866A31726BF9687CE58F49E43673FA0C49BDA1DC0A956674485A14EF
denuoweb.com. 25095 IN RRSIG DS 13 2 86400 20260731030453 20260724015453 41446 com. ...
```

## Live certificate association

Command:

```sh
openssl s_client -connect dane-test.denuoweb.com:443 \
  -servername dane-test.denuoweb.com -showcerts </dev/null 2>/dev/null |
  openssl x509 -pubkey -noout |
  openssl pkey -pubin -outform DER |
  openssl dgst -sha256
```

Observed:

```text
SHA2-256(stdin)= 369e0dbba20489bdee1a963239716dd16c6fecc6efc30116889ab6ad6dc18bae
```

This exactly matches the TLSA association data. The record therefore expresses
a live DANE-EE, SPKI, SHA-256 binding (`3 1 1`), not merely a signed but stale
RRset.

## Distinct negative states

These live controls demonstrate why the classifier must not reduce discovery
to a `has_tlsa` Boolean:

```sh
delv _443._tcp.example.com. TLSA
```

```text
;; resolution failed: ncache nxrrset
; negative response, fully validated
```

This is authenticated absence and may follow the defined WebPKI fallback.

```sh
delv _443._tcp.neverssl.com. TLSA
```

```text
;; resolution failed: ncache nxrrset
; negative response, unsigned answer
```

This is an insecure/unsigned zone result and may follow the separately reported
WebPKI fallback.

```sh
delv _443._tcp.dnssec-failed.org. TLSA
```

```text
;; resolution failed: failure
```

This is a validation failure. It must fail closed and must never be represented
as TLSA absence.

## Required runtime disposition

| Validated DNS result | Browser trust disposition |
| --- | --- |
| Secure, supported TLSA RRset | Enforce DANE; a mismatch is fatal |
| Secure authenticated denial | Explicit WebPKI fallback |
| Proven insecure/unsigned delegation | Explicit WebPKI fallback |
| Bogus, indeterminate, malformed, transport failure, or timeout | Fail closed |

The same decision must bind every HTTPS/WSS request boundary: main-frame and
redirect navigation, subresources, Service Workers, downloads, and WebSockets.
