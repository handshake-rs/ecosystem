# Dependency publication

## Policy

Development uses explicit path dependencies inside the coordination root.
Release candidates must use one immutable `hns-rs` revision or published crate
set and must record the registry fingerprint. No consumer may silently vendor
and modify canonical protocol logic.

Planned release order:

1. `hns-rs` primitive/protocol crates and registry artifacts.
2. `hns-node-rs`, pinned to the exact compatible `hns-rs` release.
3. `hns-dane-engine`, including `hns-icann-dane`, pinned to the same
   compatible protocol release.
4. MeshMine external-node adapter and the mobile/extension native packages.

The canonical `hns-rs` and `hns-dane-engine` workspaces target Rust 1.89,
edition 2024, resolver 3, and `MIT OR Apache-2.0` where newly created.
Historical consumer workspaces retain their audited toolchain pins until
their broader shared-engine consolidation is complete.

## Dependency constraints

- Shared primitives do not depend on Tokio, RocksDB, SQLite, Quinn, JNI,
  Kotlin, Swift, Chromium, wallet persistence, or MeshMine.
- `hns-node-rs` may own runtimes and storage but not browser/platform shells.
- `hns-dane-engine` exposes stable platform ABIs; TypeScript/Kotlin/Swift do not
  reimplement consensus, DNSSEC, DANE, HPKE, or P2P protocols.
- `hns-icann-dane` owns TLSA service-owner derivation and the typed ICANN
  DNSSEC-to-browser decision. Both browser clones may adapt network and
  platform APIs, but must consume that shared decision and preserve it through
  TLS verification and connection-cache keys.
- MeshMine calls the external node API/bridge. Its mining database fast paths
  remain local to the mining/node implementations.
- Dependency cycles are forbidden.

The two browser workspaces currently consume `hns-icann-dane` through an
explicit coordination-root path dependency. That is permitted for this
development checkpoint only. A release artifact must replace it with the
recorded immutable engine revision or the corresponding published crate and
must reproduce the same lockfile graph.

## Release evidence required

- clean lockfiles and reproducible release builds;
- SBOM/license/provenance inventory;
- canonical registry binary/hash equality in every Rust binary;
- cross-project API/ABI compatibility tests;
- artifact checksums for Android, iOS, extension, and node packages;
- no unpublished Git dependency in a release artifact.

No crate or package has been published by this execution.
