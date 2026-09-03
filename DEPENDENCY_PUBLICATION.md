# Dependency publication

> **Current publication state (2026-09-02):** `hns-rs 0.4.1` and
> `hns-wallet-rs 0.2.1` are published cohorts, and the browser products consume
> exact published protocol/engine/wallet packages. See
> [`CURRENT_STATE.md`](CURRENT_STATE.md). The candidate sequence below is kept
> as publication history and does not describe the current registry state.

## Policy

Cross-repository consumers must prefer exact compatible published crates and
record registry checksums and VCS provenance. An exact immutable Git revision
is permitted only where no compatible crate release exists and must remain an
explicit, reviewed exception. No consumer may silently vendor and modify
canonical protocol logic.

Release progression:

1. `hns-rs` primitive/protocol crates: the original 14 allowlisted `0.1.0`
   packages are published; `b66470a6` is the last locally qualified lockstep
   15-package `0.2.0` predecessor, while current self-contained HNSA/HNSR/chat/
   fee/name/Shakedex source predecessor `b33b346` passes exact-head hosted
   protocol and RustSec qualification; current documentation-only head
   `a93ba7a` also has green CI, and the packages remain unpublished.
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
  frozen at node `5ed38d15`, contained in current node `063ba6b`, and consumed
  by wallet `5b540963` and retained at current `4cd9a61`; it is deliberately
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

Both browser workspaces retain the five base authority/observability contracts
at exact engine revision `1ab4ab626f945712b0f960945986cb52efefef7c` and now
consume the centralized cache, primitives, Urkel, durable chain, P2P, strict
DNSSEC/DANE, synchronization, resolver, and network adapter graph at exact
engine revision `b8bdfbf7e234e64166886ade6f79d698e23056af`. Their source
policies and lockfiles validate the complete reviewed engine closure. They do
not yet consume current engine `84005f1` or its HNSA admission boundary.
`hns-node-rs` consumes exact `handshake-rs/hns-rs` revision
`b33b346780c8f6a9bb18a54390019486cdab0221`, and MeshMine consumes exact
`handshake-rs/hns-node-rs` revision
`504d3fed035feb8a637ca09c4e0816b6e1144622`. Published compatible crate
versions may replace those pins later, but an unpinned branch, sibling path,
embedded copy, or silent fallback is forbidden.

Current `hns-wallet-rs` consumes the reviewed immutable canonical `hns-rs`
source at `4331eee2265ebc43a28390517c24a958fa4b7733`; the current marketplace
protocol and Denuo V2 crates are not yet published, so downstream live board
integration remains disabled rather than using a sibling path or copied wire
implementation. The wallet repository's canonical `origin` is
`https://github.com/handshake-rs/hns-wallet-rs.git`; remote `main` is
`4cd9a61a8520c4d3bddd15b3fffcad0d02aafd36`. It publishes no crate or ABI
artifact.
Private ABI v2 exists only as source. Its typed private capability snapshot and
result/prompt/event binding are not the public website capability result. The
caller-side host and machine-readable contracts are likewise source only: the
manifest schema supplies no trusted key, verifier, durable rollback state, or
artifact-to-process binding. No generated native projection consumes them;
browser provider scaffolds therefore remain unavailable.

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
for every archive. Current source head
`a93ba7a806a921a8ce2d13d9c5fc041ff0ecf6e7` retains the corrected marketplace,
NameState/resource, fee, TRANSFER/FINALIZE, empty-inventory, and
listing-independent recovery boundary and adds HNSA named rendezvous, HNSR
route/circuit runtimes, owner-bound chat, and final protocol corrections. Its
source predecessor `b33b346` passed exact-head hosted protocol qualification
and RustSec in run `31369025777`; `a93ba7a` is a documentation-only successor
whose exact-head CI `31372546141` passed. The shared 0.2 packages
remain unpublished and untagged.

Annotated local and `origin` `v0.1.0` tag object
`354b286ff623424d24376f20885fb05407561d70` dereferences to follow-up
publication-record commit `f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`.
The published archives still identify its parent
`0ea5994c336642ea7d01c51c0e22df2008985426` as their release source.

`hns-dane-engine` remains unpublished. Canonical remote `main` is
`84005f1df21a30ea9dda7fafb95f9488b8f5da4b`; it includes opaque provider
authority, bounded proxy admissions, private transport runtimes, consolidated
browser adapters, and durable HNSA named-route admission pinned to `hns-rs`
`b33b346`. The implementation predecessor `3c12ace` passed local locked
workspace tests, warning-denied Clippy, and release build. Exact-head hosted CI
`31372280327` and CodeQL `31372280387` passed, and no engine crate is a
registry release.

`hns-wallet-rs` remains independently versioned, now with canonical `origin`
`https://github.com/handshake-rs/hns-wallet-rs.git` and remote `main`
`4cd9a61a8520c4d3bddd15b3fffcad0d02aafd36`. Current source includes encrypted
HNS/name/Shakedex state, persistent wallet control, library-only exact-account
and synchronized-read compositions, approval-schema-v3 name consent, and an
encrypted account-authenticated BDK aggregate. The checked-in executable is
still control-only; browser creation/restoration and native product dispatch
remain unavailable, and every value/Shakedex release gate remains false.
Exact-head hosted run `31372389330` failed strict Clippy in the HNS workflows;
a successor correction is in progress. It has no published crate, signed
browser artifact, or installed-product qualification.

`hns-node-rs` local and remote-tracking `main` are
`063ba6b82b4b34ea0e56992aa0c0d48855e03e71`; tag `v0.3.4` points to
`40b456fa0772729542118a69f27edc37bf42a3d7`. The tag contains the resolver
sidecar and exact fee-quote contract. Current `main` is the unpublished `0.3.5`
candidate, pins `hns-rs` `b33b346`, and adds action-context/MTP binding,
tracked-contract retirement/reclamation, outbound/private transport, durable
policy opt-outs, and resource/compaction hardening. A focused Rust 1.97.1
strict-Clippy run passes for `hns-store` at current head using the mandated
prebuilt RocksDB; exact-head hosted CI `31373528053` and container
`31373528055` are pending. Neither fact substitutes for consolidated
node/wallet/product qualification.
