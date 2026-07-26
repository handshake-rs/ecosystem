# Dependency publication

## Policy

Cross-repository consumers use exact immutable Git revisions until compatible
crate releases exist. Release candidates must use one immutable `hns-rs`
revision or published crate set and must record the registry fingerprint. No
consumer may silently vendor and modify canonical protocol logic.

Planned release order:

1. `hns-rs` primitive/protocol crates and registry artifacts.
2. `hns-node-rs`, pinned to the exact compatible `hns-rs` release.
3. `hns-dane-engine`, including `hns-icann-dane` and
   `hns-namespace-resolution`, pinned to the same compatible protocol release.
4. MeshMine external-node adapter and the mobile/extension native packages.
5. Independently versioned crawler snapshots/services and bootstrap-generator
   web/appliance artifacts after their own provenance and deployment gates.

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
- `hns-namespace-resolution` owns complete-origin HNS/ICANN comparison,
  absence/failure semantics, divergence precedence, and normalized
  decision/cache identity. Browser adapters may construct typed root evidence
  but may not reimplement or bypass that decision in Kotlin, Swift,
  JavaScript, PAC, or platform networking code.
- MeshMine calls the external node API/bridge. Its mining database fast paths
  remain local to the mining/node implementations.
- The browser engine and clients must not consume crawler snapshots or
  bootstrap-generator output as runtime trust evidence. The crawler-to-
  generator path is an optional operator workflow with separately versioned
  artifacts.
- Dependency cycles are forbidden.

Both browser workspaces consume `hns-icann-dane` and
`hns-namespace-resolution` from exact
`handshake-rs/hns-dane-engine` revision
`127b9ad55852df00b4df40826517715048dc3571`, allowlist only that Git source in
`cargo-deny`, and record the full source revision in their lockfiles.
`hns-node-rs` consumes exact `handshake-rs/hns-rs` revision
`dde2da81f29df935f043978a6d517c1d60ceff31`, and MeshMine consumes exact
`handshake-rs/hns-node-rs` revision
`504d3fed035feb8a637ca09c4e0816b6e1144622`. Published compatible crate
versions may replace those pins later, but an unpinned branch, sibling path,
embedded copy, or silent fallback is forbidden.

## Release evidence required

- clean lockfiles and reproducible release builds;
- SBOM/license/provenance inventory;
- canonical registry binary/hash equality in every Rust binary;
- cross-project API/ABI compatibility tests;
- artifact checksums for Android, iOS, extension, and node packages;
- no unpublished Git dependency in a release artifact.

No crate or package has been published by this execution.
