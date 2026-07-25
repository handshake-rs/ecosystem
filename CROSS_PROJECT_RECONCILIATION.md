# Cross-project reconciliation

## Dependency direction

```text
hns-rs
  ├──> hns-node-rs ──> MeshMine bridge
  └──> hns-dane-engine
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
| Android/iOS lifecycle and UI | mobile clone |
| native messaging, PAC/proxy lifecycle, Chromium UI | extension clone |

## Reconciliation rules

- No protocol number is duplicated as an untyped literal outside a
  compatibility fixture.
- Standard HSD packet types and Denuo assignments occupy separate semantic
  namespaces.
- Draft HIP provider roles are operator opt-in. Requester defaults and
  persistent opt-outs are independent.
- Direct authoritative DNS remains first. Relay transport never confers
  validation authority; DNSSEC, TLSA, and DANE are local.
- ODoH-required never falls back to a plaintext relay.
- HNSR remains inactive until enabled and transports an inner Brontide session;
  it does not turn a relay into chain/DNS/application authority.
- Marketplace discovery is best-effort untrusted gossip. Every listing and
  fulfillment is locally verified against chain state and the seller proof.
- Mining authority consumes only a coherent committed node snapshot and is
  rechecked before publication.

## Current unresolved joins

- The extracted node has not yet adopted released/path `hns-rs` crates.
- MeshMine has not yet been changed to run exclusively through the standalone
  external-node boundary.
- The DANE engine repository is still unborn.
- Both browser clones remain at their common starting revision.
- The end-to-end regtest topology and prohibition on public recursive resolver
  contact have not yet been demonstrated.
