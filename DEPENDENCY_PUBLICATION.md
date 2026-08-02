# Dependency publication

## Policy

Cross-repository consumers use exact immutable Git revisions until compatible
crate releases exist. Release candidates must use one immutable `hns-rs`
revision or published crate set and must record the registry fingerprint. No
consumer may silently vendor and modify canonical protocol logic.

Release progression:

1. `hns-rs` primitive/protocol crates: the original 14 allowlisted `0.1.0`
   packages are published; `b66470a6` is the last locally qualified lockstep
   15-package `0.2.0` predecessor, while the latest marketplace/NameState codec
   source at `825f212d` is unqualified and unpublished.
2. `hns-node-rs`, pinned to the exact compatible `hns-rs` release.
3. `hns-wallet-rs`, consuming published canonical protocol crates or one
   immutable `hns-rs` revision and publishing its versioned typed ABI.
4. `hns-dane-engine`, including `hns-icann-dane`,
   `hns-namespace-resolution`, `hns-resolution-policy`,
   `hns-browser-runtime`, and `hns-browser-observability`, pinned to the same
   compatible protocol release.
5. MeshMine external-node adapter and the mobile/extension native packages.
6. Independently versioned crawler snapshots/services and bootstrap-generator
   web/appliance artifacts after their own provenance and deployment gates.

The canonical `hns-rs` and `hns-dane-engine` workspaces target Rust 1.89,
edition 2024, resolver 3, and `MIT OR Apache-2.0` where newly created.
Historical consumer workspaces retain their audited toolchain pins until
their broader shared-engine consolidation is complete.

## Dependency constraints

- Shared primitives do not depend on Tokio, RocksDB, SQLite, Quinn, JNI,
  Kotlin, Swift, Chromium, wallet persistence, or MeshMine.
- `hns-node-rs` may own runtimes and storage but not browser/platform shells.
- `hns-wallet-rs` owns encrypted user keys and workflow persistence. It may
  consume canonical published protocol crates, connect to the node through a
  typed noncustodial adapter, use Kyoto, and embed the one selected Ethereum
  light-client boundary, but it may not embed node consensus/P2P or browser
  authority/UI code. The authenticated node RPC v1/process adapter join is
  source-complete at node `74f7ae36` and wallet `76885098`; it is deliberately
  not a Cargo dependency and remains unqualified. The browser join is not a
  compiled dependency, and Helios is selected policy rather than an embedded
  runtime.
- `hns-dane-engine` exposes stable platform ABIs; TypeScript/Kotlin/Swift do not
  reimplement consensus, DNSSEC, DANE, HPKE, or P2P protocols.
- `hns-icann-dane` owns TLSA service-owner derivation and the typed ICANN
  DNSSEC-to-browser decision. Both browser products may adapt network and
  platform APIs, but must consume that shared decision and preserve it through
  TLS verification and connection-cache keys.
- `hns-namespace-resolution` owns complete-origin HNS/ICANN comparison,
  absence/failure semantics, divergence precedence, and normalized
  decision/cache identity. Browser adapters may construct typed root evidence
  but may not reimplement or bypass that decision in Kotlin, Swift,
  JavaScript, PAC, or platform networking code.
- `hns-browser-runtime` owns the authority state graph, checked nonzero runtime
  session, lifecycle invalidation, generation/event admission, and stale-work
  rejection. Platform adapters may bind those capabilities to one active
  listener/proxy generation but may not publish work after canonical
  revocation.
- `hns-browser-observability` owns schema-v2 trusted status, typed root
  failures, ICANN DNSSEC/trust actions, transport/intermediary topology, and
  authority provenance. Platform UI may render that status but may not infer a
  more favorable trust state.
- MeshMine calls the external node API/bridge. Its mining database fast paths
  remain local to the mining/node implementations.
- The browser engine and clients must not consume crawler snapshots or
  bootstrap-generator output as runtime trust evidence. The crawler-to-
  generator path is an optional operator workflow with separately versioned
  artifacts.
- Dependency cycles are forbidden.
- Sibling-checkout paths are forbidden across maintained repositories. Browser
  products consume a released wallet ABI artifact; they never link an
  uncommitted `../hns-wallet-rs` path.

Both browser workspaces consume `hns-browser-runtime`,
`hns-browser-observability`, `hns-icann-dane`,
`hns-namespace-resolution`, and `hns-resolution-policy` from exact
`handshake-rs/hns-dane-engine` revision
`7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`, allowlist only that Git source in
their source policies and `cargo-deny`, and record the full source revision in
their lockfiles.
`hns-node-rs` consumes exact `handshake-rs/hns-rs` revision
`dde2da81f29df935f043978a6d517c1d60ceff31`, and MeshMine consumes exact
`handshake-rs/hns-node-rs` revision
`504d3fed035feb8a637ca09c4e0816b6e1144622`. Published compatible crate
versions may replace those pins later, but an unpinned branch, sibling path,
embedded copy, or silent fallback is forbidden.

The initial `hns-wallet-rs` workspace consumes the existing published
`hns-rs` 0.1.0 primitives exactly. The new marketplace protocol and Denuo V2
types are not yet published, so downstream live board integration remains
disabled rather than using a sibling path or copied wire implementation.
The wallet repository itself has no configured remote and publishes no crate
or ABI artifact. Browser provider scaffolds therefore remain unavailable.

## Release evidence required

- clean lockfiles and reproducible release builds;
- SBOM/license/provenance inventory;
- canonical registry binary/hash equality in every Rust binary;
- cross-project API/ABI compatibility tests;
- artifact checksums for Android, iOS, extension, and node packages;
- no unpublished Git dependency in a release artifact.

## Current publication state

All 14 allowlisted `hns-rs` crates at version `0.1.0` were published to
crates.io on 2026-07-29 and are non-yanked. Every published package records
release-source commit
`0ea5994c336642ea7d01c51c0e22df2008985426` in its Cargo VCS metadata. The
later documentation head is
`f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`.

The locally qualified marketplace candidate is
`b66470a6a07f0211e3e7fa9aef7d034c8486e75b`. It advances all public workspace
packages and internal version requirements to `0.2.0`, adds the fifteenth
allowlisted package `hns-marketplace-protocol`, and passes publication dry-run
for every archive. The latest source successor
`825f212de49d57b0ae7b5bbd0c038ddec5d52ce2` additionally contains the corrected
marketplace boundary and canonical HSD-compatible NameState/resource codecs;
it has not received that gate. Neither revision is a crates.io release, remote
checkpoint, or tag.

No local or remote `v0.1.0` Git tag exists. Registry version `0.1.0` must
therefore be attributed to its embedded source commit, not described as a
Git-tagged release.

`hns-dane-engine` remains unpublished. Canonical remote `main` is
`7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`; the older local release-
preparation predecessor is `1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75`,
while latest local source head `f76ad37232bcadc85eb9b9bee5f45bff8405b583`
adds opaque provider authority and bounded proxy admissions. It is unbuilt,
untested, unpushed, and not a registry release.

`hns-wallet-rs` remains an independent local repository without a configured
remote. Latest local source head
`768850982b37dc84030ab408de0f1f010cf42ed1` has no published crate or browser
ABI artifact and was not built or tested at that revision.
