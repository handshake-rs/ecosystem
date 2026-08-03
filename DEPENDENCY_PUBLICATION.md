# Dependency publication

## Policy

Cross-repository consumers use exact immutable Git revisions until compatible
crate releases exist. Release candidates must use one immutable `hns-rs`
revision or published crate set and must record the registry fingerprint. No
consumer may silently vendor and modify canonical protocol logic.

Release progression:

1. `hns-rs` primitive/protocol crates: the original 14 allowlisted `0.1.0`
   packages are published; `b66470a6` is the last locally qualified lockstep
   15-package `0.2.0` predecessor, while current self-contained
   fee/name/Shakedex release source at `4b989aab` is unqualified and unpublished.
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
  authority/UI code. The authenticated node RPC v1 plus fee-quote contract is
  frozen at node `5ed38d15`, contained in current node `3d346e3d`, and consumed
  by wallet `5b540963` and retained at current `604a3577`; it is deliberately
  not a Cargo dependency and remains unqualified. The browser join is not a
  compiled dependency. Helios is selected policy rather than an embedded
  runtime, and caller-serializable evidence cannot replace the opaque provenance
  permit that only a future embedded verifier may mint.
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
The wallet repository has configured `origin`
`https://github.com/denuoweb/hns-wallet-rs.git`, whose remote-tracking `main` is
`1206a8ab550cf67ff43dc162091e371946278641`. Current local `main`
`604a35771a9427696b6ecf533368205392e62979` is ahead by seven commits,
unpushed, and has no push authorization. It publishes no crate or ABI artifact.
Private ABI v2 exists only as source. Its typed private capability snapshot and
result/prompt/event binding are not the public website capability result, and
no generated native projection consumes them; browser provider scaffolds
therefore remain unavailable.

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
`4b989aabc132e7e79b8fd57a10f2465073faf588` retains the corrected marketplace,
NameState/resource, fee, TRANSFER/FINALIZE, empty-inventory, and
listing-independent recovery boundary landed through `81f2df2`; it adds
package-local licenses/fixtures/registries, deterministic mirror checks,
complete listing/cancellation and recovery-FINALIZE vectors, batching-safe
index-zero APIs, and release/fuzz dependency hygiene. It has not received that
gate. The shared 0.2 packages remain unpublished and untagged.

Annotated local and `origin` `v0.1.0` tag object
`354b286ff623424d24376f20885fb05407561d70` dereferences to follow-up
publication-record commit `f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`.
The published archives still identify its parent
`0ea5994c336642ea7d01c51c0e22df2008985426` as their release source.

`hns-dane-engine` remains unpublished. Canonical remote `main` is
`7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`; the older local release-
preparation predecessor is `1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75`,
while latest local source head `6eb0174ae743e6bd01c516be7a534d94be94b4bd`
adds opaque provider authority, bounded proxy admissions, and retention across
unrelated admitted work. It is unqualified, unpushed, and not a registry
release.

`hns-wallet-rs` remains an independent repository with configured `origin`
`https://github.com/denuoweb/hns-wallet-rs.git` at remote-tracking `main`
`1206a8ab550cf67ff43dc162091e371946278641`. Latest local source head
`604a35771a9427696b6ecf533368205392e62979` is ahead by seven commits,
unpushed, and has no push authorization. It adds an encrypted same-snapshot
`HnsName` scan and authoritative-account CAS hardening plus receive-only
Ethereum containment, and now gives private ABI-v2 results, prompts, and events
one exact authority/wallet/permission binding with tombstone-preserving
permission snapshots. The canonical 43-name vocabulary is shared, but
`hns_requestAccounts` remains unavailable. False Shakedex/value gates remain.
This source received static review only; its added tests were not run. It has no
published crate, signed browser artifact, or current qualification result.

`hns-node-rs` local and remote-tracking `main` are
`3d346e3dadc716b5c367eee050308e71a0693a64`; tag `v0.3.4` points to
`40b456fa0772729542118a69f27edc37bf42a3d7`. The tag contains the resolver
sidecar and exact fee-quote contract; later `main` commits correct release-CI
port verification. This provenance does not substitute for the program's
consolidated node/wallet/product qualification.
