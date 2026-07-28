# Repository Map

## Maintained products

| Repository | Responsibility |
| --- | --- |
| [`hns-rs`](https://github.com/handshake-rs/hns-rs) | Runtime-independent Handshake protocol, consensus, wire, proof, registry, and role-specific consent types |
| [`hns-node-rs`](https://github.com/handshake-rs/hns-node-rs) | Standalone node runtime/networking under construction: chain state, storage, synchronization, mining, and RPC |
| [`MeshMine`](https://github.com/handshake-rs/MeshMine) | Mining overlay, work scheduling, operator UI, and exact external-node consumer |
| [`hns-dane-engine`](https://github.com/handshake-rs/hns-dane-engine) | DNSSEC, TLSA/DANE, validating resolution, full-host dual-root policy, canonical browser authority lifecycle, and shared observability |
| [`hns-dane-browser-mobile`](https://github.com/handshake-rs/hns-dane-browser-mobile) | Android/iOS lifecycle, UI, FFI, proxy, store packaging, staged header publication, and shared-engine adapters |
| [`hns-dane-browser-extension`](https://github.com/handshake-rs/hns-dane-browser-extension) | Chromium MV3 extension, mandatory PAC/proxy, native host, cross-platform Setup, release signing, and shared-engine adapters |
| [`hns-dane-crawler`](https://github.com/handshake-rs/hns-dane-crawler) | HSD-derived topology snapshots, stored DNS evidence, readiness queues, reports, and optional live directory |
| [`hns-dane-bootstrap-generator`](https://github.com/handshake-rs/hns-dane-bootstrap-generator) | Operator-authored delegation, DNSSEC/DS, authoritative DoH, TLSA, verification, and appliance material |

## Coordination

This repository owns cross-project architecture decisions, pinned integration
manifests, source-audit reports, compatibility matrices, and release
qualification. It must not become a copy of every product repository.

Current implemented dependency direction:

```text
hns-rs ────────────> hns-node-rs
  └────────────────> hns-dane-engine
hns-dane-engine ──> mobile and Chromium browser adapters
hns-node-rs ──────> MeshMine
hns-dane-crawler ── observational gap/handoff ──> hns-dane-bootstrap-generator
```

`hns-node-rs` pins the exact canonical `hns-rs` checkpoint that defines its
live Denuo registry negotiation and role-safe HIP-76 session policy.
`hns-dane-engine` independently pins the canonical protocol packages used by
its light-chain, resolver, and P2P transport graph. The node transport returns
remote DNS bytes as untrusted; DNSSEC/DANE acceptance remains a separate
resolver authority.

Both browser products pin one immutable engine revision for ICANN DANE,
namespace, transport-policy, authority-runtime, and observability contracts.
The engine owns their canonical security generation/event clock and status
schema; platform adapters bind and render those contracts while retaining
sockets, storage, proxy integration, native interfaces, UI, and packaging.
Their current platform runtimes stage header synchronization and publish
validated header/peer/readiness generations atomically. Chromium also binds
PAC and native-host replacement to explicit connection/control generations;
this remains product-adapter code rather than completion of the planned shared
engine proxy-core migration.

The crawler/generator arrow is an optional operator workflow, not a runtime
trust dependency. Portable whole-request browser boundaries require and test
independent resolution and DNSSEC validation; crawler snapshots and generated
instructions cannot authorize a connection. Installed-browser and
signed-device matrices remain open.

## External references

`hsd`, `hs-client`, HIPs, Shakedex, Bob Wallet, and Handshake documentation
remain upstream-owned reference inputs. Mirrors or forks require an explicit
maintenance reason and must preserve attribution and licensing.
