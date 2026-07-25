# Dependency publication

## Policy

Development uses explicit path dependencies inside the coordination root.
Release candidates must use one immutable `hns-rs` revision or published crate
set and must record the registry fingerprint. No consumer may silently vendor
and modify canonical protocol logic.

Planned release order:

1. `hns-rs` primitive/protocol crates and registry artifacts.
2. `hns-node-rs`, pinned to the exact compatible `hns-rs` release.
3. `hns-dane-engine`, pinned to the same compatible protocol release.
4. MeshMine external-node adapter and the mobile/extension native packages.

All Rust packages currently use edition 2024, resolver 3, Rust 1.89, and
`MIT OR Apache-2.0` where newly created.

## Dependency constraints

- Shared primitives do not depend on Tokio, RocksDB, SQLite, Quinn, JNI,
  Kotlin, Swift, Chromium, wallet persistence, or MeshMine.
- `hns-node-rs` may own runtimes and storage but not browser/platform shells.
- `hns-dane-engine` exposes stable platform ABIs; TypeScript/Kotlin/Swift do not
  reimplement consensus, DNSSEC, DANE, HPKE, or P2P protocols.
- MeshMine calls the external node API/bridge. Its mining database fast paths
  remain local to the mining/node implementations.
- Dependency cycles are forbidden.

## Release evidence required

- clean lockfiles and reproducible release builds;
- SBOM/license/provenance inventory;
- canonical registry binary/hash equality in every Rust binary;
- cross-project API/ABI compatibility tests;
- artifact checksums for Android, iOS, extension, and node packages;
- no unpublished Git dependency in a release artifact.

No crate or package has been published by this execution.
