# Wallet and Marketplace Audit

Audit date: 2026-08-02

This audit is the milestone-zero input for the modular wallet, provider,
Shakedex, Denuo market-board, and native cross-chain settlement program. It
records what can be reused and where a new release boundary is required. It is
not a production-readiness claim.

## Audited repository heads

All wallet-program implementation repositories in scope were already on
`main` when this audit began. The unaffected MeshMine, crawler, bootstrap
generator, and organization-profile repositories remain recorded in
`REFERENCE_COMMITS.md`.

| Repository | Audited head | Initial tree |
| --- | --- | --- |
| `ecosystem` | `1f9ca1686923fa77d1a696e112ce11d15fbde867` | clean |
| `hns-rs` | `f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0` | clean |
| `hns-node-rs` | `6e8be54fdc9ed4492175757d9fc67ce37fc340aa` | clean |
| `hns-dane-engine` | `02c063ac3e94a91b222201fb51d95ff3ac19f026` | clean |
| `hns-dane-browser-mobile` | `e5a54402789aaa13061b17f89c0e146b2acb16ea` | clean |
| `hns-dane-browser-extension` | `a36dc754b10d653f2bb23874e3c5743859dcf82a` | pre-existing changes |

The Chromium tree already contained an unrelated ICANN insecure-delegation
fix in `hns-chromium-platform-runtime`, its documentation and changelog, plus
an untracked `dist/` directory. Wallet work must not overwrite or silently
include those changes in a wallet commit.

Read-only implementation references were pinned locally at:

| Reference | Head |
| --- | --- |
| HSD / Denuo HSD | `698e252ebc7b5c1dd0a9587e342fdd153d020ae4` |
| hs-client | `03a243a7fc38e2032950e6bec32d9137d2f74355` |
| HIPs working branch | `c0487e5af779158cbef0591ac363b7e956255c7d` |
| Shakedex | `ab5687b04cb61d2548937b8cee3c056c1c75bbdc` |
| Bob Wallet | `0432158e5bc55c9d5aa24e0f256e468c44459d15` |
| Handshake documentation | `b8611a6bd4e9208ec0561f0a5042c6bbc532e3a1` |

## Existing code to reuse

### `hns-rs`

- `hns-transaction`, `hns-covenants`, `hns-script`, `hns-primitives`, and
  `hns-urkel-proof` are the runtime-independent Handshake authority. Wallet
  code must consume these crates and must not fork their consensus encodings.
- `hns-swap` already implements HIP-0001/Shakedex v2 fixed-price and bounded
  reverse-Dutch proof primitives, exact script construction, signature-hash
  behavior, offer identifiers, and compatibility vectors. Fixed-price wallet
  orchestration should wrap this crate rather than recreate presigns.
- `hns-p2p-experimental` already provides bounded Denuo extension envelopes,
  registry negotiation, mismatch isolation types, and the generated
  experimental registry. Protocol `0x0001` is already assigned to the atomic
  name marketplace. Cross-chain messages require a distinct negotiated
  protocol and a regenerated fingerprint.
- The repository is Rust 1.89, edition 2024, resolver 3. Protocol crates are
  intentionally independent of Tokio, databases, wallets, HTTP clients, and
  platform ABIs. That boundary remains unchanged.

### `hns-node-rs`

- The node already persists raw validated blocks, block indexes, an active
  transaction index, UTXO state, name state, Urkel state/proofs, mempool data,
  and reorg undo information.
- Existing JSON-RPC coverage includes raw transaction lookup, transaction
  broadcast, UTXO lookup, name information/resource lookup, peer/network
  status, and node readiness. The wallet API can be added as typed methods over
  these stores instead of a second node database.
- Live Denuo envelope negotiation and bounded HIP-76 request/response sessions
  already exist in `hns-p2p`. Marketplace relays should reuse that negotiated
  session and peer-policy machinery; Brontide identity is connection
  provenance only.
- Missing wallet functionality is primarily script history, output-spender
  lookup, explicit transaction inclusion/confirmation summaries, fee-rate
  estimation, current name proof/owner-transaction methods, configurable
  wallet index profiles, and bounded name/cross-chain marketplace relay
  stores.

### Browser authority and product adapters

- `hns-dane-engine` already owns the canonical browser authority lifecycle,
  namespace decisions, authenticated security results, runtime/session and
  policy generations, and stale-publication rejection. Only a small typed
  provider-injection decision belongs there.
- The Chromium product already has a Rust native host, a generation-bound
  native messaging protocol, an MV3 service worker, install/update/removal
  flows, and bounded security-result parsing. The wallet database and secrets
  belong in the native process; the extension should retain only UI,
  permissions, request routing, and notifications.
- The mobile product already has Android and iOS Rust FFIs, native browser
  runtimes, WebView/WKWebView navigation policy, persistent application
  storage, and platform UI shells. Wallet operations should cross a separate
  versioned typed ABI and must not weaken the browser-authority path.
- Neither browser currently has wallet, Provider API, Shakedex, Denuo market
  board, Bitcoin, Ethereum, or persisted swap-session implementation.

### Reference applications

- HSD and Bob Wallet contain mature wallet restoration, coin selection, name
  lifecycle, and RPC behavior useful as compatibility oracles. They remain
  read-only references and are not copied wholesale.
- Shakedex is the semantic oracle for seller transfer/finalize/presign and
  buyer fulfillment/finalization. `hns-swap` is the canonical Rust primitive
  boundary used by the new wallet.

## New repository boundary

No existing maintained repository owns encrypted user keys, local wallet
workflow persistence, origin permissions, external-chain synchronization, or
chain-neutral settlement. A standalone `hns-wallet-rs` workspace is therefore
required. It may consume published `hns-rs` crates, but maintained repositories
must not gain committed sibling-path dependencies. Browser products consume
its versioned ABI/artifacts at release boundaries.

The wallet store uses SQLite for transactional workflow state and
authenticated per-record encryption for sensitive columns. This is distinct
from claiming that every SQLite page, filename, row key, or non-sensitive
index is opaque. A production platform must supply or wrap the database key;
the standalone wallet did not have that platform integration at audit time.

## Bitcoin implementation audit

The selected production stack is the current Kyoto line:

- `bip157` 0.6.3 for direct Bitcoin P2P, header proof-of-work validation,
  compact-filter-header synchronization, BIP157/158 filters, relevant-block
  retrieval, peer consistency, and broadcasting;
- `bdk_kyoto` 0.17.0 with `bdk_wallet` 3.x for descriptor wallet integration;
- wallet-owned encrypted SQLite tables for birthday, scan progress, relevant
  transactions, UTXOs, spends, and reorg checkpoints.

The older `kyoto-cbf` package is not a second backend. Esplora, Electrum,
hosted indexers, and production Bitcoin Core RPC are excluded. Bitcoin Core is
permitted only as a deterministic regtest fixture source. Mainnet settlement
remains disabled until the complete Kyoto restore, reorg, HTLC, resource, and
mobile benchmarks pass.

## Ethereum implementation audit

The selected synchronization design is Helios, pinned for evaluation to
upstream revision `43a8c9f3cdda41a6f383c4db41d9a83f102638b1` (workspace
version 0.11.1 at audit time). It combines a beacon-chain light client with
proof-checked execution queries while using configured consensus and execution
data providers.

Trust and availability boundaries remain explicit:

- a recent trusted weak-subjectivity checkpoint is required;
- sync-committee signatures and finality updates verify consensus headers;
- account, code, storage, transaction, receipt, and event evidence must bind
  to verified execution roots where the selected API supports it;
- providers can censor, omit, delay, correlate, or make the wallet unavailable
  even when they cannot forge accepted proofs;
- conflicting, stale, wrong-chain, or proof-incomplete evidence fails closed;
- mainnet HNS/ETH settlement remains disabled until the pinned Helios revision,
  proof coverage, persistence/restart behavior, and the contract bytecode are
  independently audited and qualified.

No Helios database-size, startup-latency, or time-to-verified-head measurement
was available. Startup depends on a sufficiently recent trusted checkpoint and
reachable consensus/execution providers, and the wallet must remain unusable
for Ethereum settlement until verified evidence reaches the configured
freshness/finality policy. A fixed storage-size estimate would be misleading.

Trin was considered as a direct Portal Network client. It is a promising
low-storage Rust daemon, but embedding its broader JSON-RPC/Portal runtime is a
larger product and operational surface than the first narrow native-ETH wallet
requires. It is not implemented as an alternate selectable backend.

The contract toolchain is a pinned `solc` standard-JSON build for one
non-upgradeable native-ETH-only HTLC. No generic contract deployment or
calldata surface is exposed to websites.

## Dependency and publication policy

- Each repository keeps its own lockfile, license audit, version, CI, and
  release evidence.
- Cross-repository Rust dependencies use published versions or immutable Git
  revisions; no committed `../sibling` dependency is allowed.
- New canonical protocol crates must be released from `hns-rs` before a
  downstream release can consume them. Until then, downstream integration is
  experimental and must not be described as a published build.
- The browser engine remains free of wallet databases, chain runtimes, and
  UI. Browser products integrate only the provider-injection authority result
  and the wallet ABI.

## Qualification baseline and immediate gaps

Existing full gates are `scripts/check.sh` in `hns-rs`, `hns-node-rs`,
`hns-dane-engine`, both browser repositories, and `ecosystem`. They include
locked dependency checks, formatting, warning-denied Clippy, unit tests,
release builds, registry generation, ABI/source-boundary checks, and selected
fuzz smoke tests.

The following evidence did not exist at audit time and cannot be inferred from
the mature browser/node foundations:

- encrypted wallet migrations and deterministic multi-role recovery;
- a dedicated Bitcoin atomic-swap derivation branch and complete published
  cross-module recovery vectors;
- full Handshake wallet restoration and name transfer/finalization;
- complete fixed-price Shakedex lifecycle and name recovery;
- Provider API hostile-origin and approval tests;
- Kyoto birthday, reorg, bandwidth, disk, and mobile-memory measurements;
- Ethereum HTLC deterministic bytecode and local-chain execution results;
- HNS/BTC or HNS/ETH success, restart, reorg, and refund demonstrations;
- price reporter governance and qualified price rounds;
- signed-device mobile and installed-browser marketplace testing.

The audit also found no complete runtime implementation of the chain
capability traits, no node Shakedex/HTLC/preimage tracker, and no existing
browser ABI that could execute provider methods. Those joins require code and
evidence; protocol schemas or adapter stubs cannot be counted as integration.

Those items must stay marked experimental, disabled, unavailable, or deferred
until code and evidence exist. Unit tests alone do not authorize mainnet funds.
