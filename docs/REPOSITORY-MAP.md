# Repository Map

## Maintained products

| Repository | Responsibility |
| --- | --- |
| [`hns-rs`](https://github.com/handshake-rs/hns-rs) | Runtime-independent Handshake protocol, consensus, wire, proof, registry, and role-specific consent types |
| [`hns-node-rs`](https://github.com/handshake-rs/hns-node-rs) | Full-node networking, chain state, storage, synchronization, mining, and RPC |
| [`MeshMine`](https://github.com/handshake-rs/MeshMine) | Mining overlay, work scheduling, operator UI, and exact external-node consumer |
| [`hns-dane-engine`](https://github.com/handshake-rs/hns-dane-engine) | DNSSEC, TLSA/DANE, validating resolution, and full-host dual-root policy |
| [`hns-dane-browser-mobile`](https://github.com/handshake-rs/hns-dane-browser-mobile) | Android/iOS lifecycle, UI, FFI, proxy, packaging, and shared-engine adapters |
| [`hns-dane-browser-extension`](https://github.com/handshake-rs/hns-dane-browser-extension) | Chromium MV3 extension, PAC/proxy, native host, installers, and shared-engine adapters |
| [`hns-dane-crawler`](https://github.com/handshake-rs/hns-dane-crawler) | HSD-derived topology snapshots, stored DNS evidence, readiness queues, reports, and optional live directory |
| [`hns-dane-bootstrap-generator`](https://github.com/handshake-rs/hns-dane-bootstrap-generator) | Operator-authored delegation, DNSSEC/DS, authoritative DoH, TLSA, verification, and appliance material |

## Coordination

This repository owns cross-project architecture decisions, pinned integration
manifests, source-audit reports, compatibility matrices, and release
qualification. It must not become a copy of every product repository.

Current implemented dependency direction:

```text
hns-rs ────────────> hns-node-rs
hns-dane-engine ──> mobile and Chromium browser adapters
hns-node-rs ──────> MeshMine
hns-dane-crawler ── observational gap/handoff ──> hns-dane-bootstrap-generator
```

`hns-node-rs` pins the exact canonical `hns-rs` checkpoint that defines its
live Denuo registry negotiation.

The crawler/generator arrow is an optional operator workflow, not a runtime
trust dependency. Browsers independently resolve and DNSSEC-validate every
request; crawler snapshots and generated instructions cannot authorize a
connection.

## External references

`hsd`, `hs-client`, HIPs, Shakedex, Bob Wallet, and Handshake documentation
remain upstream-owned reference inputs. Mirrors or forks require an explicit
maintenance reason and must preserve attribution and licensing.
