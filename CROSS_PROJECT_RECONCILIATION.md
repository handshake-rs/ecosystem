# Cross-project reconciliation

## Authority and dependency direction

```text
hns-rs ── exact immutable protocol pin ──> hns-node-rs ──> MeshMine bridge

hns-dane-engine
  ├──> hns-icann-dane
  ├──> hns-namespace-resolution
  │       ├──> Android/iOS browser adapters
  │       └──> Chromium browser adapter
  ├──> mobile shell
  └──> Chromium extension

hns-dane-crawler ── optional observed remediation handoff
                  └──> hns-dane-bootstrap-generator ──> operator-published DNS
```

The wallet and atomic market belong in `hns-node-rs`; their gossip protocol
uses the canonical Denuo extension registry. MeshMine must not become a
dependency of `hns-rs`, `hns-node-rs`, the wallet/market, the DANE engine, or
either browser shell.

## One owner per concern

| Concern | Canonical owner |
| --- | --- |
| semantic consensus/wire/registry types | `hns-rs` |
| chain, P2P runtime, storage, wallet, auctions, atomic market | `hns-node-rs` |
| mining application, DAG/settlement, external-node adapter | `MeshMine` |
| DNS wire, DNSSEC, authenticated resolution, TLSA/DANE, policy ABI | `hns-dane-engine` |
| ICANN TLSA-owner derivation and browser trust decision | `hns-dane-engine/crates/hns-icann-dane` |
| full-host HNS/ICANN comparison and namespace precedence | `hns-dane-engine/crates/hns-namespace-resolution` |
| Android/iOS lifecycle and UI | mobile clone |
| native messaging, PAC/proxy lifecycle, Chromium UI | extension clone |
| namespace topology snapshots and observational DANE-readiness reports | `hns-dane-crawler` |
| operator-authored delegation, DNSSEC/DS, TLSA, and appliance material | `hns-dane-bootstrap-generator` |

## Reconciliation rules

The 2026-07-25 user clarification refines the assignment's broad
requester/provider wording: consent follows whether a node is merely an opaque
P2P forwarder or can act as an output, not a blanket “all provider roles
opt-in” rule.

- No protocol number is duplicated as an untyped literal outside a
  compatibility fixture.
- Standard HSD packet types and Denuo assignments occupy separate semantic
  namespaces.
- Opaque P2P forwarding is installed and enabled by default with a durable
  opt-out. A role that can see the plaintext request, originate an external
  request, terminate a circuit, or otherwise act as an output node remains
  explicit opt-in. Relay consent never grants output-node consent.
- Concretely, the HIP 76 DNS relay is an output node and defaults off; the HIP
  77 ODoH proxy is an opaque relay and defaults on with opt-out; the HIP 77
  target defaults off; the HNSR opaque relay defaults on with opt-out; and
  HNSR endpoint/output and rendezvous roles default off. Requester/client
  policy is represented and revoked independently. HIP 76 requester
  eligibility defaults to `Auto` with independent opt-out and never advertises
  output capacity; durable node-policy reload remains a separate gate.
- Direct authoritative DNS remains first. Relay transport never confers
  validation authority; DNSSEC, TLSA, and DANE are local.
- ODoH-required never falls back to a plaintext relay.
- HNSR requester and output roles remain inactive until independently enabled.
  An enabled opaque relay transports an inner Brontide session and never
  becomes chain, DNS, application, or output authority.
- Every DNS-named ICANN HTTPS/WSS origin derives its TLSA owner from the
  effective host, port, and transport. Secure presence enforces DANE; WebPKI
  is allowed only after authenticated absence or a proven insecure
  delegation; bogus and indeterminate DNSSEC fail closed.
- That ICANN decision is made below the browser shells and applies at their
  request boundary to navigations, redirects, subresources, Service Workers,
  downloads, and WebSockets. The accurate transport label is **DANE via ICANN
  DoH**.
- Namespace ownership is decided from two independently validated complete
  origin plans, never from an IANA suffix list. The shared classifier retains
  HNS-only, ICANN-only, convergent, divergent, neither, and indeterminate
  states; applies exact-origin pin, successful sticky binding, then ICANN
  first-use precedence; and never combines address, service, or trust records
  across roots.
- Crawler snapshots are observational inputs only. They may identify a
  remediation candidate and populate a generator handoff, but they never
  classify a live browser hostname or authorize TLS.
- Bootstrap-generator output remains an operator-reviewed control-plane
  artifact. A published record becomes security policy only when obtained and
  validated through the applicable live DNSSEC chain.
- Marketplace discovery is best-effort untrusted gossip. Every listing and
  fulfillment is locally verified against chain state and the seller proof.
- Mining authority consumes only a coherent committed node snapshot and is
  rechecked before publication.

## Current unresolved joins

- The node consumes the exact canonical `hns-rs` Denuo/HIP-76 checkpoint and
  now runs bounded live HIP-76 sessions. A production recursive and
  DNSSEC-validating output backend, durable operator-policy restart, HIP 77/78,
  wallets, marketplace messages, and broader shared primitive adoption remain.
- MeshMine now consumes an exact immutable `handshake-rs/hns-node-rs` revision
  through its bridge, but the coherent parent/job topology has not yet been
  demonstrated end to end.
- Both browser adapters now submit independently resolved complete HNS and
  ICANN plans to the shared full-host policy and expose the selected namespace.
  Installed-browser and signed-device matrices still need to prove those
  semantics through platform network processes, restarts, redirects, workers,
  downloads, and WebSockets.
- Browser adapters still contain historical gateway/runtime code around the
  canonical ICANN policy crate; broader shared-engine consolidation remains.
- Crawler production snapshots/live-directory operation and a deployed,
  hash-pinned bootstrap appliance still need independent release
  qualification; their unit/build gates do not upgrade browser trust rows.
- Signed-device Android/iOS and installed-browser Chromium matrices remain
  release gates even after portable builds and tests pass.
- The end-to-end regtest topology and prohibition on public recursive resolver
  contact have not yet been demonstrated.
