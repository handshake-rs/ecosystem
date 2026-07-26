# Cross-project reconciliation

## Dependency direction

```text
hns-rs
  ├──> hns-node-rs ──> MeshMine bridge
  └──> hns-dane-engine
          ├──> hns-icann-dane
          │       ├──> Android/iOS browser adapters
          │       └──> Chromium browser adapter
          ├──> mobile shell
          └──> Chromium extension
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
| Android/iOS lifecycle and UI | mobile clone |
| native messaging, PAC/proxy lifecycle, Chromium UI | extension clone |

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
  policy is represented and revoked independently.
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
- Marketplace discovery is best-effort untrusted gossip. Every listing and
  fulfillment is locally verified against chain state and the seller proof.
- Mining authority consumes only a coherent committed node snapshot and is
  rechecked before publication.

## Current unresolved joins

- The extracted node has not yet adopted released/path `hns-rs` crates.
- MeshMine has not yet been changed to run exclusively through the standalone
  external-node boundary.
- Browser namespace selection still uses the IANA suffix snapshot as an
  authoritative shortcut. It must resolve the complete hostname independently
  through HNS and ICANN, distinguish only/convergent/divergent/neither states,
  and expose the selected namespace under an explicit precedence policy.
- Browser adapters still contain historical gateway/runtime code around the
  canonical ICANN policy crate; broader shared-engine consolidation remains.
- Signed-device Android/iOS and installed-browser Chromium matrices remain
  release gates even after portable builds and tests pass.
- The end-to-end regtest topology and prohibition on public recursive resolver
  contact have not yet been demonstrated.
