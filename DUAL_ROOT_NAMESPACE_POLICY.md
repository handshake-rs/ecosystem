# Dual-root browser namespace policy

Status: shared contract and portable browser adapters implemented; installed
browser/device qualification remains in progress

## Authority boundary

The IANA root-zone snapshot is never authoritative for browser namespace
selection. It may remain only as a non-authoritative performance or
compatibility/diagnostic hint; it cannot alter lookup, routing, root choice,
trust, or trusted status. Every valid DNS-named browser origin is independently
resolved through HNS and ICANN before one root is selected.

PAC, Kotlin, Swift, JavaScript, and synchronous native-messaging components
cannot decide whether a complete hostname exists in HNS or ICANN. They may
perform syntax/special-use checks or expose a clearly labeled legacy
IANA-snapshot diagnostic hint, but that hint cannot select a root, route a
request, or populate trusted status.

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

## Transport and role admission

Both browser products consume the same exact-pinned
`hns-resolution-policy` contract. Their stable relay preference controls
requester consumption only:

- new and persisted browser profiles start false/off and require explicit user
  opt-in;
- off maps to `DnsRelayRequesterPolicy::Disabled`;
- on maps to `DnsRelayRequesterPolicy::Auto`;
- direct authoritative UDP and TCP precede authenticated authoritative DoH;
- an admitted P2P DNS relay remains a later, untrusted transport whose answer
  requires local DNSSEC, TLSA, and DANE validation; and
- unsupported ODoH, HNSR, provider, output, market, and legacy roles are
  explicitly disabled by both browser adapters.

The generic ecosystem policy independently keeps opaque forwarding
default-on/opt-out and every plaintext or external output role explicit
opt-in. No browser requester setting grants provider or output consent.

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

- schema version and one engine-issued runtime snapshot;
- checked nonzero per-start runtime session;
- runtime generation, policy generation, event sequence, and authority state;
- outcome;
- selected namespace, when any;
- selection source;
- typed name-free root failures when classification has no outcome;
- HNS and ICANN evidence states;
- a nonzero name-free decision fingerprint whenever classification produced an
  outcome, including `Neither`;
- actual transport and exact intermediary identity topology; and
- typed ICANN DNSSEC and DANE/WebPKI/fail-closed action.

The request-local namespace decision—not the status view—retains the complete
query, both validated plans, divergence details, and expiry needed for
connection and cache enforcement. Those name-bearing fields are deliberately
excluded from the trusted status schema.

Policy change or entry into degraded, revoked, or stopped authority
permanently invalidates older admitted work. A stale session, generation,
event, proxy binding, redirect, subresource, Service Worker operation,
download, or WebSocket completion cannot publish a response or trusted status
after recovery. Bogus or indeterminate ICANN DNSSEC is reported as a
name-free root failure with validating-DoH provenance and an explicit
fail-closed action; it is never relabeled as absence or an ICANN-only outcome.

Legacy `nameClass` fields inside routing or trusted status may remain only when
populated from the actual selected namespace. A standalone diagnostic ABI may
expose an explicitly non-authoritative IANA-snapshot hint, but that value must
never select a root, admit a connection, or create trusted status.

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
