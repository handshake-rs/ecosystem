# Dual-root browser namespace policy

Status: shared contract and portable browser adapters implemented; installed
browser/device qualification remains in progress

## Authority boundary

The IANA root-zone snapshot is never authoritative for browser namespace
selection. It may be used only to order or prewarm lookups. Every valid
DNS-named browser origin is independently resolved through HNS and ICANN before
one root is selected.

PAC, Kotlin, Swift, JavaScript, and synchronous native-messaging classifiers
perform syntax and special-use checks only. They cannot decide whether a
complete hostname exists in HNS or ICANN.

## Typed root results

Each independent lookup produces exactly one of:

- a validated, internally coherent origin plan;
- authenticated absence; or
- a typed failure.

Authenticated absence includes current HNS Urkel non-inclusion,
DNSSEC-authenticated ICANN NXDOMAIN/no usable endpoint, and separately labeled
insecure-delegation absence received from the authenticated validating ICANN
DoH resolver.

Timeout, transport failure, stale HNS state, malformed DNS, unauthenticated
resolver responses, bogus DNSSEC, and indeterminate DNSSEC are failures. A
failure is never converted into absence, even when the other root succeeds.

## Authoritative outcomes

| HNS result | ICANN result | Outcome |
| --- | --- | --- |
| present | absent | HNS only |
| absent | present | ICANN only |
| present | present, equivalent | convergent |
| present | present, different | divergent |
| absent | absent | neither |
| failure | any | indeterminate/fail closed |
| any | failure | indeterminate/fail closed |

`Neither` is a resolution failure at the browser boundary. `Divergent` carries
both plans, the selected namespace, the precedence source, and a bounded
difference mask.

## Complete origin plan

One root's plan contains all connection- and trust-affecting state:

- the complete scheme, host, effective origin port, and supported-protocol
  query;
- the bounded origin CNAME/HTTPS AliasMode path and terminal HTTPS/SVCB owner;
- the normalized HTTPS/SVCB ServiceMode TargetName, its separate CNAME path,
  and final A/AAAA owner;
- the sorted, deduplicated usable A/AAAA endpoint set;
- selected HTTPS/SVCB priority, mandatory parameters, ALPN, effective port,
  transport, connection-used hints, and supported ECH configuration;
- HNS DANE or ICANN automatic-DANE/WebPKI trust action;
- canonical sorted TLSA RDATA for the effective service;
- exact HNS proof-anchor or authenticated ICANN DNSSEC-chain provenance; and
- absolute observation/expiry bounds that are never renewed merely by loading
  cached evidence.

Records from different roots are never combined. The selected plan governs
address, HTTPS/SVCB, TLSA, redirect, subresource, Service Worker, download, and
WebSocket processing for that origin.

Convergence ignores TTL values, record order, RRSIG bytes, proof encoding, and
resolver identity. It requires exact equality of every connection- and
trust-affecting field. Partial address overlap is divergent. Alias cycles,
terminal AliasMode records, unsupported mandatory SVCB parameters, malformed
or unsupported secure TLSA records, and inconsistent port, protocol,
transport, hint, or endpoint state fail closed.

## Divergence precedence

The precedence order is:

1. an explicit, valid per-origin user pin;
2. a persistent successful binding for the same origin;
3. ICANN as the first-use default.

A stricter require-explicit-selection mode may fail closed instead of applying
step 3; there is no unpinned HNS-first mode. A pin or binding selects only
between two valid plans. It cannot override a failed, bogus, or stale root. If
its selected root is authentically absent, the browser reports that condition
and requires the explicit state-isolated switch workflow rather than silently
using the other root.

Persistent bindings prevent a later ICANN root addition from silently moving a
previously successful HNS origin. The selected namespace, outcome, precedence
source, and divergence state must remain visible in browser security UI.

Changing a namespace pin for the same URL origin requires:

- clearing or partitioning cookies, cache, HSTS, Alt-Svc, and Service Workers
  for that exact origin;
- revoking the old proxy/runtime generation; and
- invalidating namespace decisions, connection pools, TLS verifiers, and
  resumption state before the new pin takes effect.

If a platform cannot guarantee that sequence, it must expose selection as
read-only rather than provide an unsafe switch.

## Routing and cache binding

Chromium PAC and mobile whole-browser proxy configuration route every valid
DNS-named HTTP, HTTPS, WS, and WSS request to the authenticated Rust boundary.
IP literals and special-use names retain their separate lexical/network-policy
handling. No PAC or platform component performs DNS to choose a namespace.

Connection pools, TLS sessions, verifiers, resumption, Alt-Svc, and cached
decisions are partitioned by a stable namespace-decision fingerprint and the
runtime/policy generation.

The dual-result cache key is derived from the actual query-, policy-,
selected-root-, and whole-plan-bound decision. It additionally includes the
canonical HNS network, resolver/trust configuration, authority/binding
generation, and comparison-schema version, so callers cannot key one decision
as another query, network, or policy. Expiry is bounded by the earliest
relevant DNS TTL, negative proof lifetime, DNSSEC signature expiry, HNS anchor
currency, or binding validity. Errors may receive a short backoff entry but
never a negative-answer entry.

## Required status

Trusted, generation-bound status exposes at least:

- outcome;
- selected namespace, when any;
- selection source;
- HNS and ICANN evidence states;
- divergence mask;
- decision fingerprint and expiry.

Legacy `nameClass` fields may remain for compatibility only when populated
from the actual selected namespace. They must never be populated from the IANA
snapshot.

## Qualification gates

- all five successful/negative outcomes and every one-root/two-root failure
  combination;
- secure and insecure denial, bogus, indeterminate, timeout, and stale HNS
  anchor cases;
- record-order/TTL/RRSIG equivalence and address/CNAME/SVCB/port/ALPN/TLSA
  divergence;
- explicit pin, sticky binding, ICANN default, expiry, reorg, resolver change,
  and stale completion behavior;
- no DNS-name `DIRECT` PAC route, system target DNS, cross-root record mixing,
  or cross-fingerprint connection/session reuse;
- navigation, redirects, iframes/subresources, Service Workers, downloads,
  HTTP/WS, HTTPS/WSS, non-default ports, and HTTP/3 across Chromium, Android,
  and iOS;
- visible divergent selection and fail-closed `neither`/indeterminate UI.
