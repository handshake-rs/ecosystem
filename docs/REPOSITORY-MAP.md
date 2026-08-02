# Repository Map

## Maintained products

| Repository | Responsibility |
| --- | --- |
| [`hns-rs`](https://github.com/handshake-rs/hns-rs) | Runtime-independent Handshake protocol, consensus, wire, proof, registry, and role-specific consent types |
| [`hns-node-rs`](https://github.com/handshake-rs/hns-node-rs) | Standalone node runtime/networking under construction: chain state, storage, synchronization, mining, and RPC |
| `hns-wallet-rs` (local repository; no remote configured) | Experimental encrypted Handshake-first wallet foundation, origin-bound Provider schema, Shakedex/market state machines, Kyoto boundary, and Helios-selected Ethereum evidence policy |
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

Current compiled dependency direction and blocked integration joins:

```text
hns-rs 0.1 published crates ──> hns-wallet-rs foundation
hns-rs immutable pin ─────────> hns-node-rs ──> MeshMine
hns-rs immutable pin ─────────> hns-dane-engine ──> browser authority adapters

hns-rs 0.2 marketplace candidate - - > node/wallet V2 adoption (blocked: unpublished)
hns-node-rs typed backend       - - > hns-wallet-rs runtime (interface shapes only)
hns-wallet-rs ABI artifact      - - > mobile/Chromium (blocked: not released/wired)

hns-dane-crawler ── observational gap/handoff ──> hns-dane-bootstrap-generator
```

Solid arrows are compiled, immutable dependencies at the stated checkpoint.
Dashed arrows are designed joins that are unavailable and must not be inferred
from compatible type names or source adapters. No maintained repository uses
a committed sibling-checkout dependency.

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

## Current non-mobile publication checkpoints

- All 14 allowlisted `hns-rs` crates are published and non-yanked at `0.1.0`.
  Their Cargo VCS metadata records source
  `0ea5994c336642ea7d01c51c0e22df2008985426`; documentation head is
  `f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`, and no `v0.1.0` tag exists.
- A locally qualified 15-package `hns-rs` 0.2.0 marketplace candidate exists,
  but it is not tagged, pushed, or published. The node and wallet therefore do
  not advertise or consume its Denuo V2 wire protocol through a released
  boundary.
- `hns-wallet-rs` exists only as a local independent `main` repository. Its
  source-level ABI and wallet foundations are experimental; no remote,
  published crate, browser ABI artifact, or product release exists.
- `hns-dane-engine` remote `main` remains
  `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`. Local release preparation
  ending at `1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75` is unpublished and
  unpushed.
- Chromium v0.5.5 is public from source/tag
  `86b18497285753944ec1b9196ec05ee359c6db11` with 29 assets. macOS artifacts
  are signed and notarized; Windows artifacts are unsigned. Documentation
  head `3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` passed CI `30439859541`.
- MeshMine documentation head
  `9f781a00ee8fc3b7c6773538434235a65f167ca3` passed CI `30440116148`
  without changing its immutable external-node boundary.
- Bootstrap-generator CI `30401402868` exists but failed at `npm ci` because
  `@emnapi/runtime@1.11.3` is missing from `package-lock.json`.

## Current mobile publication checkpoint

- Android 0.5.5 version code 46 from source
  `d24f85158854abb8be4a7bb9e914aebe5e7e4679` is deployed to Google Play
  production.
- The iOS 0.5.5 build 57 source and annotated `v0.5.5` tag are
  `d926561091634cd69fc9b7e79a4b76003fa4ee47`. Exact Apple CI run
  `30454904736` and live-screenshot run `30454926117` passed.
- Build `57` is `VALID` and its direct App Review submission is
  `WAITING_FOR_REVIEW` after protected upload run `30456522039`. The intended
  App Store path is direct App Review with
  manual release; no TestFlight or beta group is part of this release.
- Public GitHub Release `v0.5.5` retains the verified code 46 APK and build 57
  App Store IPA.
- Signed-device Android/iOS qualification remains open independently of store
  build and publication evidence.

Exact artifact and claim boundaries are recorded in
[`mobile-v0.5.5-release-checkpoint-2026-07-29.md`](../evidence/mobile-v0.5.5-release-checkpoint-2026-07-29.md).

## External references

`hsd`, `hs-client`, HIPs, Shakedex, Bob Wallet, and Handshake documentation
remain upstream-owned reference inputs. Mirrors or forks require an explicit
maintenance reason and must preserve attribution and licensing.
