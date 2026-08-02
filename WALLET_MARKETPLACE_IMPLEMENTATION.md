# Wallet and Marketplace Implementation Report

Snapshot: 2026-08-02

Overall status: **experimental foundation delivered; not release-ready and not
authorized for mainnet settlement**. This update supplies independently
buildable protocol, node, authority, wallet, and browser-adapter slices. It
does not claim a complete wallet product or complete bilateral swap because
the real multi-process, restart, reorg, device, benchmark, and independent
security gates listed below have not passed.

Status terms in this report are strict: **implemented** means source exists;
**tested** means only the named local test evidence passed; **experimental**
means the source is not a supported release; **disabled** means a deliberate
runtime guard prevents use; **unavailable** means no executable product path
exists; and **deferred** means intentionally outside this update. A schema,
trait, parser, state-machine unit, or UI-state enum does not by itself make a
wallet operation available.

## Repository and crate delivery

Modified repositories:

- `hns-rs`: canonical marketplace/price/session wire types, fixed-price
  listing records, HNS HTLCs, and additive Denuo V2 artifacts;
- `hns-node-rs`: optional wallet indexes, typed noncustodial wallet backend,
  and a bounded five-role Denuo marketplace relay core;
- `hns-dane-engine`: exact authenticated-origin context and all-outcomes
  provider-injection authority decision;
- `hns-dane-browser-extension`: authority-gated Provider API bridge, approval
  window, and demonstration dapp;
- `hns-dane-browser-mobile`: source-level Android/iOS wallet-provider,
  unconnected secure-key-wrapper, and UI-state adapters;
- `ecosystem`: architecture, dependency, registry, qualification, gap,
  revision, and implementation evidence.

New repository: `hns-wallet-rs`, an independent workspace on `main`. It has
its own lockfile, licenses, gate, release boundary, and no committed sibling
path dependency, configured Git remote, or remote publication. Its eleven
crates are:

1. `hns-wallet-types`
2. `hns-wallet-store`
3. `hns-wallet-chain-api`
4. `hns-wallet-hns`
5. `hns-wallet-provider`
6. `hns-wallet-shakedex`
7. `hns-wallet-market`
8. `hns-wallet-bitcoin-kyoto`
9. `hns-wallet-ethereum`
10. `hns-wallet-ffi`
11. `hns-wallet-testkit`

Three additional crates were added at their canonical repository boundaries:
`hns-marketplace-protocol` in `hns-rs`, and `hns-wallet-index` plus
`hns-denuo-market-relay` in `hns-node-rs`. In total this update adds fourteen
crates across the three repositories.

To avoid a second set of drifting documents, the requested documentation
topics are consolidated into canonical files. `ARCHITECTURE.md`,
`WALLET_ARCHITECTURE.md`, `CHAIN_MODULES.md`, and `KEY_DERIVATION.md` map to
`work/hns-wallet-rs/docs/ARCHITECTURE.md` plus its security model;
`WALLET_STORAGE.md` and `RECOVERY.md` map to
`docs/PERSISTENCE_AND_RECOVERY.md`; `HNS_PROVIDER_API.md` maps to
`docs/PROVIDER_API.md`; and `PROVIDER_SECURITY.md`, `PRIVACY.md`, and
`THREAT_MODEL.md` map to `docs/SECURITY.md`. Shakedex, Denuo name/cross-chain,
atomic-settlement, intent, and price-round topics map to
`docs/SHAKEDEX_AND_MARKET.md`; Ethereum module/HTLC topics map to
`docs/ETHEREUM.md`; Kyoto, qualification, implementation status, and future
work retain their directly named canonical documents. The node index has its
own `work/hns-node-rs/docs/HNS_NODE_WALLET_INDEX.md`. Literal alias files were
not added because they would duplicate the same incomplete-status claims.

The future-chain boundary is expressed through `ChainModule`,
`UtxoChainModule`, `AccountChainModule`, and `AtomicSettlement`. Capabilities
describe receive/send/history/settlement plus hash, locktime, finality, and fee
models. Adding Litecoin or another chain must not change provider dispatch or
canonical market/session objects, but no new pair is enabled until that
module's full settlement suite passes. At this checkpoint those traits are
compiled interfaces; the HNS, Bitcoin, and Ethereum crates expose focused
operations but do not yet register complete runtime objects implementing the
capability traits end to end.

| Surface | Status at this snapshot |
| --- | --- |
| canonical marketplace protocols | implemented and locally tested; experimental, unpublished |
| node confirmed indexes/backend | implemented and locally tested; disabled by default; no complete wallet-mempool/HTLC tracker |
| node marketplace relay | implemented and locally tested cache/policy core; live V2 wire unavailable |
| encrypted store/provider policy | implemented and locally tested foundation; experimental |
| usable HNS/name wallet | experimental; unavailable as a browser product |
| fixed-price Shakedex | experimental and disabled; complete lifecycle unavailable |
| Kyoto Bitcoin wallet/settlement | experimental and disabled; complete runtime unavailable |
| native-ETH wallet/contract | experimental and disabled; verified synchronization/deployment unavailable |
| HNS/BTC and HNS/ETH | disabled; end-to-end settlement unavailable |
| Chromium provider | source bridge implemented and tested; injection disabled by unavailable ABI |
| Android/iOS provider | inactive source scaffold; Android compile-tested, iOS compile untested; unavailable |
| excluded product families | deferred or deliberately unavailable as enumerated below |

## Canonical protocols and Denuo registry

Denuo V1 remains byte-for-byte identified by
`95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d`.
The additive generated V2 registry is version 2, protocol version 1, with
fingerprint
`734226e866435821e40be7bde85fb19dd6eb867c5620abb8347ac8cd23da4f2c`.

| Protocol | ID | Availability | Maximum payload |
| --- | ---: | --- | ---: |
| registry negotiation | `0x0000` | V1 and V2 | 16,384 |
| atomic name marketplace | `0x0001` | V1 and V2 | 1,048,576 |
| cross-chain marketplace | `0x0002` | V2 only | 524,288 |

V1 continues to reserve `0x0002..=0xffff`; V2 reserves
`0x0003..=0xffff`. Version negotiation therefore rejects, rather than
reinterprets, the new protocol on a V1 peer.

The atomic-name protocol has typed hello, offer inventory/get/list/single,
offer, and cancellation messages. The cross-chain protocol has the required
fifteen typed message kinds: intent inventory/get/object/cancel; observation
inventory/get/object and price round; match request, fill grant, and reject;
session hello; and funding, redeem, and refund status.

The new, unpublished lockstep `hns-rs` 0.2.0 release candidate and its
runtime-independent `hns-marketplace-protocol` crate own bounded
chain/asset/network bindings, unsigned integer native amounts, reduced
rational prices, signed observations/intents/cancellations/matches/grants,
deterministic quorum/outlier/age/link/movement checks, session terms/status,
and typed Denuo codecs. `hns-swap` now owns signed fixed-price listings and
cancellations plus SHA-256 HNS HTLC descriptor, funding, redeem, refund, and
preimage primitives. Runtime persistence, reporter admission, chain evidence,
fees, timeout margins, and execution remain downstream policy.

## `hns-node-rs`

Four configuration-controlled index modes are present:

- transaction index;
- script-history index;
- output-spender index; and
- complete wallet index, which includes active script UTXOs and implies the
  first three components.

Index writes are staged in the same atomic store batch as UTXO, name, undo,
canonical-height, and best-block changes. Disconnect uses validated block undo
to remove connected rows and restore spent script UTXOs. Profile records are
checksummed; startup refuses a partially built profile, and enabling a missing
component after history exists requires an explicit offline reindex or new
data directory. Query pages are bounded to 4,096 rows and 16 MiB. Exact disk
use and indexing time were not measured.

The typed, noncustodial backend exposes all twelve requested calls:

`get_chain_tip`, `get_raw_transaction`, `get_transaction_status`,
`get_transaction_inclusion`, `get_script_history`, `get_script_utxos`,
`get_spending_transaction`, `broadcast_transaction`, `estimate_fee_rate`,
`get_name_state`, `get_name_proof`, and `get_name_owner_transaction`.

Broadcast uses real contextual mempool admission and only then announces
transaction inventory to live peers. Rejection/orphan results are typed; an
idempotent already-admitted transaction is not fabricated as newly accepted.
Fee estimation samples at most 4,096 immutable mempool entries and otherwise
returns the pinned relay minimum; it is not a confirmation guarantee.

The Denuo relay core has independently opt-in roles for name listings,
cross-chain intents, observations/rounds, match/fill rendezvous, and bounded
session status. It implements hash-first fetch, object/aggregate limits,
expiry, duplicate and monotonic-sequence checks, peer/signer rates and policy,
timeouts, scoring, malformed penalties, and bounded progressive bans. It does
not sign, choose matches, calculate an authoritative price, store keys, hold
funds, or advance a swap. The current node dependency pin is still Denuo V1,
so live V2 advertisement and typed wire dispatch remain disabled until the new
canonical crate is released and pinned.

The confirmed indexes do not merge wallet-relevant mempool transactions or
unconfirmed spends into history/UTXO pages, persist a wallet mempool recovery
journal, or provide subscriptions. No Shakedex order index, script-scoped
Shakedex mempool restoration, HTLC funding/redemption/refund tracker, or
verified witness/preimage extractor is implemented in the node. A relayed
swap-status object remains an untrusted bounded hint, not chain tracking.

Wallet-index profile V1 is checksummed and fails closed on missing, corrupt,
or partially built components. There is no online backfill: an existing chain
requires a new synchronized data directory or a future version-matched offline
reindex tool. Index rows survive raw block pruning, but historical raw
transaction and owner-transaction retrieval can return `PayloadPruned`; exact
disk and indexing costs remain unmeasured. History, spender, and script-UTXO
values are versioned/checksummed and key-bound so relocated values fail closed.

## Provider API and browser authority

The provider core and browser adapters parse, classify, permission-gate, and
approval-classify the complete 43-method schema and allowlist 13 events. This
is a protocol surface, not a claim that 43 wallet operations execute in a
browser: the native ABI/application dispatcher is unavailable. The exact
methods are:

- general: `wallet_getCapabilities`, `wallet_getEnabledModules`,
  `wallet_enableModule`, `wallet_disableModule`,
  `wallet_requestPermissions`, `wallet_getPermissions`,
  `wallet_revokePermissions`, `wallet_lock`, `wallet_getStatus`;
- Handshake: `hns_requestAccounts`, `hns_accounts`, `hns_getBalance`,
  `hns_getTransactions`, `hns_getReceiveAddress`, `hns_send`, `hns_getNames`,
  `hns_getName`, `hns_importKnownName`, `hns_transferName`,
  `hns_finalizeName`, `hns_signTypedMessage`;
- external asset: `asset_getAccount`, `asset_getBalance`,
  `asset_getTransactions`, `asset_getReceiveTarget`, `asset_send`;
- name market: `nameMarket_listOffers`,
  `nameMarket_createFixedPriceOffer`, `nameMarket_cancelOffer`,
  `nameMarket_acceptOffer`, `nameMarket_getSession`,
  `nameMarket_finalizePurchase`, `nameMarket_recoverName`;
- cross-chain market: `swap_getSupportedPairs`, `swap_getPriceRound`,
  `swap_listMarketIntents`, `swap_publishMarketIntent`,
  `swap_cancelMarketIntent`, `swap_requestMatch`, `swap_acceptFill`,
  `swap_getSession`, `swap_redeem`, `swap_refund`.

The events are `connect`, `disconnect`, `permissionsChanged`,
`modulesChanged`, `accountsChanged`, `balancesChanged`,
`transactionsChanged`, `namesChanged`, `nameMarketChanged`,
`priceRoundChanged`, `marketIntentChanged`, `swapSessionChanged`, and
`walletLocked`. Discovery uses `hns:requestProvider` and
`hns:announceProvider`.

The API explicitly rejects generic Ethereum calls/signatures/deployment/chain
changes, PSBT and raw-transaction signing, unknown methods, secrets, and
unrestricted native commands. Requests are bounded and bound to exact origin,
namespace, browser-authority session, runtime generation, policy generation,
navigation generation, wallet session, permission generation, and document.
Origin permissions, approvals, replay state, pending counts, read/mutation
rates, expiry, revocation, and stale generations fail closed.

`hns-dane-engine` API version 3 derives the exact logical scheme/host/URL port
from the authoritative namespace decision, binds it to a private
`AuthenticatedOriginContext`, and returns a typed `ProviderInjectionDecision`
for every outcome. Denials distinguish insecure/no-namespace/unauthenticated,
origin/namespace/decision/network mismatch, stale runtime/policy/event,
not-yet-valid/expired evidence, authority lifecycle state, and TLS-policy
mismatch. HNS DANE authorization is also bound to the authenticated TLSA
service port. The authority admits HTTPS document origins only; cleartext,
WSS, and other schemes are denied. For ICANN, the same-process browser adapter
that mints the request-bound opaque authentication token is an explicit
trusted security principal and must use browser-local TLS state, never page
input.

The Chromium adapter installs an isolated document-start bridge but injects
the MAIN-world provider into one exact HTTPS main-frame `documentId` only
after current navigation authority and native ABI-v1 capability pass. It has a
bounded approval window, generation-bound events, and a static no-key/no-
backend demonstration dapp. The currently deployed native host does not yet
provide the wallet ABI, so it returns `walletUnavailable` and no provider is
injected. Wallet database, secret, chain, Shakedex, Denuo, and recovery
integration into the native host remains unavailable. The browser's pinned
engine/native-host boundary also does not yet consume the new Rust facade v3
opaque provider-authority context, so no cross-repository authority/ABI join
is claimed.

Android and iOS contain standalone typed frame validators, fixed command
allowlists, platform secure-key wrappers, authority-binding models, and
wallet-screen state enumerations. These sources deliberately do not alter the
existing browser navigation path without a released wallet ABI. They are not
wired into `MainActivity`/WKWebView, no wallet screens are rendered, and no
signed-device wallet test passed; mobile product integration is incomplete.
The Android scaffold and unit sources compile in the focused Gradle path. The
iOS project contains the expected source/test references, but neither
`swiftc` nor `xcodebuild` was available in this environment, so no Swift,
Xcode, simulator, or signed-device wallet result is claimed.

## Wallet, names, Shakedex, and market board

The wallet store has transactional SQLite schema V1, Argon2id passphrase
derivation, XChaCha20-Poly1305 sensitive-record encryption with associated
data, lock/unlock, secret rows, compare-and-swap workflow journals,
permissions, approvals, and replay protection. The schema includes wallet
accounts/addresses, HNS state, names/transfers, Shakedex, Denuo cache, Kyoto
headers/filter headers/peers/scans, Bitcoin state, Ethereum state, price
rounds, intents, grants, sessions, secrets, and refunds. It is record
encryption, not full-file encryption. Platform wrapping of the database key,
complete entity CRUD/recovery supervision, backup/rollback protection, and
device persistence remain incomplete.

HNS create/restore, encrypted seed storage, deterministic role-separated key
derivation, receive addresses, bounded non-name coin selection, typed node
backend shapes, strict current-name proof import, and persisted name workflow
records exist. Full indexed restoration, mempool/reorg reconciliation, send/
fee transaction construction, transfer/finalize builders and broadcast,
ownership re-verification, and browser UI do not. Name management is therefore
partial. HNS has separate coin, name, Shakedex, atomic-swap, identity, and dapp
session derivation domains, and Ethereum has ordinary/swap branches. The
Bitcoin crate currently derives one ordinary BIP84 descriptor wallet and
accepts caller-supplied HTLC keys; its dedicated atomic-swap derivation branch
is not implemented. A complete, reviewed derivation specification and
cross-module deterministic recovery-vector set are also missing.

Fixed-price Shakedex seller, buyer, and recovery state machines persist before
irreversible steps and consume canonical `hns-swap` proof decoding. Ordering
and recovery negative tests exist. Actual HNS transaction building, node
evidence, live Denuo publication, restart at every state, reorg handling,
regtest, and browser approval are missing, so Shakedex is partial rather than
complete. Reverse Dutch is deferred.

The chain-neutral market engine persists reservations, partial-fill amounts,
expiries, monotonic sequences, frozen terms, refunds, verified evidence, and
success/refund/restart journals. Canonical price-round verification now exists
in `hns-rs`, but reporter/source governance, enrollment, production admission,
live board relay, cooldown/scoring integration, and adversarial end-to-end
qualification do not. Intents carry asset, maximum amount, minimum fill,
partial-fill policy, and expiry—not a user-selected price. A match freezes one
exact rational price-round hash and direction-aware integer amounts. The
verifier requires caller-owned admitted reporter/source sets, freshness and
lifetime policy, duplicate rejection, deterministic outlier/median/movement
rules, and exact-rational fill binding in both directions; it never uses
floating point. No valid quorum means no new match. No pair or board is
advertised.

## Database migrations and restart boundary

`hns-wallet-store` schema V1 is a transactional initial migration from SQLite
`user_version=0`; a database newer than V1 fails closed. It creates the named
wallet, chain, marketplace, approval, replay, secret, refund, and workflow
tables, but there is no historical production-wallet upgrade corpus. Only
generic workflow reopen/CAS evidence exists. Complete entity CRUD, backup and
rollback protection, database-key platform wrapping, and the startup
supervisor that reconciles every chain and workflow remain unavailable.

The node's existing store schemas and the separate checksummed
`wallet-index-profile/v1` record are not silently rewritten into a complete
index. No online backfill or resumable wallet-index migration is claimed.
Neither browser product has a wallet database migration because neither
currently embeds the wallet database. No production user database was
migrated during this update.

## Bitcoin, Ethereum, and bilateral settlement

Bitcoin has one production boundary only: `bip157` 0.6.3, `bdk_kyoto` 0.17.0,
and `bdk_wallet` 3.1.0. Code constructs a direct-P2P Kyoto client and BIP84 BDK
wallet, supports create/load/receive/send building blocks, stores birthday/
reorg metadata, and constructs/verifies native P2WSH SHA-256/CLTV HTLC
funding, unsigned spends, and preimage extraction. No Esplora, Electrum,
hosted indexer, or production Bitcoin Core RPC dependency exists. A dedicated
swap-key branch, continuously persisted supervisor, signed HTLC spends,
broadcast/rebroadcast, complete history runtime, full invalid-PoW/filter/peer
fixtures, regtest settlement, and mobile/resource qualification are missing.

Bitcoin storage and bandwidth benchmark status: **not measured** for fresh
install, new wallet, one-year restore, five-year restore, genesis restore,
time to usable balance, scan completion, persistent disk, bandwidth, and peak
mobile memory. No universal size is claimed.

Ethereum is native-ETH-only. It has separated ordinary/swap derivation,
bounded EIP-1559 native and approved-HTLC signing, chain/code/state/receipt/
event/finality policy, and a hard mainnet guard. Helios is the single selected
model, pinned for evaluation at revision
`43a8c9f3cdda41a6f383c4db41d9a83f102638b1`: a weak-subjectivity checkpoint
and sync-committee/finality path anchors verified execution evidence, while
configured providers remain availability, censorship, omission, privacy, and
startup dependencies. The crate does not embed the Helios runtime that would
produce unforgeable proofs, so ordinary JSON-RPC claims are insufficient and
Ethereum synchronization is incomplete.

Ethereum database size, startup latency, and time to a usable verified balance
were not measured because there is no embedded Helios runtime or persistent
proof database. A future runtime must start from a reviewed weak-subjectivity
checkpoint, remain unavailable until fresh verified evidence is present, and
record those measurements without claiming a universal fixed size.

`NativeEthHtlc.sol` is compiled deterministically with Solidity 0.8.35,
optimizer runs 200, Prague EVM, and metadata CBOR disabled. It has only
`lock`, `redeem`, and `refund`; no administrator, owner, proxy, upgrade,
pause, token, arbitrary call, fee withdrawal, or mutable configuration. No
deployment address is approved. A future manifest must bind chain ID,
contract address/block, exact runtime Keccak-256 hash, compiler artifact, and
qualification evidence. The wallet hard-rejects chain ID 1 until a reviewed
source change follows proof persistence, local-chain tests, bytecode/contract
audit, and finality/reorg qualification.

HNS/BTC and HNS/ETH share a persisted evidence-only state machine and an
asymmetric timeout model: the intent publisher funds its offered-asset chain
first with the later refund deadline; the shorter second lock is funded only
after sufficient first-chain evidence. Neither pair is complete or enabled.
HNS/BTC still lacks signed integrated chain execution; HNS/ETH additionally
lacks embedded Helios evidence and an approved/audited deployment. No success,
refund, restart, or reorg demonstration was run for either pair.

## Qualification results

The standalone wallet gate passed formatting, locked all-target checking,
warning-denied Clippy, 34 Rust unit/negative tests, warning-denied rustdoc,
dependency-boundary checks, deterministic Solidity comparison, and npm audit
with zero reported vulnerabilities. Contract SHA-256 evidence is:

- source: `537c0a4dd05f8128a6fe11046edc825f5a0a6577fc0fe0b61c7b31d5ec00caa7`;
- generated artifact: `ba3bfde0443c13bcdbe287ef292072d1a2a8645fd4efd9bdee2b9dd566f52cec`;
- npm lockfile: `43c5070e3475eb76ea9218bbafbe743307f4e9c7052153f2f53d5c4da3fde8e8`.

The canonical protocol repository's complete `./scripts/check.sh` passed:
locked main/fuzz metadata, both `cargo-deny` policies, V1/V2 registry
reproduction, main/fuzz formatting, fuzz-target checking, warning-denied
all-target/all-feature Clippy, 146 tests with all features, 146 tests without
default features, an optimized all-target release build, deterministic parser
mutation smoke, and dry-run archive verification for all 15 public 0.2.0
packages. Every apparent upload was explicitly aborted by Cargo's dry-run;
no package was published. The node, engine, Chromium, mobile, and ecosystem
gate commands are recorded with the final exact revisions below.

The node's final full gate passed both qualification self-tests, main/fuzz
dependency audits, formatting, fuzz-target checking, warning-denied
all-target/all-feature Clippy, both complete test configurations (1,589
passing results across 54 target summaries and zero failures: 806 passed/3
ignored with all features, 783 passed/3 ignored without defaults), the
optimized all-target release build, the performance gate, and the two-process
regtest.
The engine's full gate passed 13 Python policy tests and 195 Rust tests in each
of three matrices (598 executed tests total), dependency/format/Clippy/release
and C ABI/header checks, plus dry-run archives for all 19 public crates.

Mobile's full source/Rust/ABI/audit/fuzz/exporter gate passed, followed by an
exact focused Android Gradle app/test compilation with the new Kotlin source.
Swift/Xcode remained unavailable. Chromium's complete source/Rust, native-host
release, fuzz, audit, and exporter stages passed before its final extension
policy stage identified one missing `scripting` permission justification.
After that documentation-only amendment, the affected
`npm run check:extension` passed lint, native-host construction, all 113 tests,
and the extension build on the final commit. The unchanged 7.4 GiB Rust build
was not repeated; no claim is made that a single final-commit full-script run
exited zero.

Focused pre-gate evidence also passed: 23 engine facade tests plus its
warning-denied Clippy/dependent-ABI checks; 4 wallet-index and 8 relay tests,
plus the node wallet-backend target (13 node-focused tests total); 25 Chromium
provider/authority/approval tests plus extension lint and embedded-JavaScript
syntax checks; and Android app/test Kotlin compilation with the wallet source
included. These focused results do not substitute for the repository gates,
installed browser, Swift/Xcode, simulator, or signed-device evidence.

Fuzz result: every registered `hns-rs` conformance parser received
deterministic mutation smoke without a panic, and the fuzz target compiled.
This does not fuzz the full wallet/browser/native-host join. No sustained
libFuzzer campaign was run. HNS/Bitcoin regtest demonstrations: not run.
Ethereum local-chain demonstrations: contract compilation only; no Anvil or
equivalent lock/redeem/refund execution was run.

## Security, trust, and release blockers

Security limitations include missing platform-key integration, complete
documented derivation/recovery vectors, a Bitcoin swap-key branch, end-to-end
secret-lifetime review, complete recovery/reorg supervision, installed-browser
and signed-device testing, HTLC/timeout/contract audits, sustained fuzzing, and
real network adversarial tests. Unit tests are not mainnet authorization.

Trust limitations include the first-party HNS node's availability and index
completeness, untrusted Denuo peers/reporters, Bitcoin peer eclipse/omission
risk within Kyoto's validation model, the Helios weak-subjectivity checkpoint,
and Ethereum provider censorship/omission/privacy/availability. Peer status,
relay identity, RPC booleans, and website data are hints, never chain evidence.

Mainnet blockers are the unpublished V2 protocol dependency; absent complete
chain-trait implementations and wallet runtime/native-host/mobile wiring;
incomplete HNS transaction/name and Shakedex flows; missing node mempool/
Shakedex/HTLC/preimage tracking; missing Kyoto swap-key/supervisor/regtest/
resource evidence; absent embedded Helios proof production and approved
contract deployment; no pair success/refund/restart/reorg qualification;
incomplete price governance; and no independent third-party security audit.

Deferred or deliberately unavailable features include auctions/registration,
resource editing, renewal automation, free/donated names, domain-service and
billing features, content aliases, reverse Dutch, Litecoin/additional chains
or pairs, generic Bitcoin signing, generic Ethereum dapps/contracts/tokens/
NFTs/DeFi/staking/WalletConnect/`window.ethereum`, wrapped assets, AMMs,
centralized books, custodial accounts, and server-held user keys.

## Exact revisions and commands

This section is populated only from the final scoped commits and their last
non-redundant repository gates. No listed commit was pushed or published.

| Repository | Branch | Revision | Last non-redundant qualification |
| --- | --- | --- | --- |
| `hns-rs` | `main` | `b66470a6a07f0211e3e7fa9aef7d034c8486e75b` | PASS — `./scripts/check.sh`; full protocol, registry, feature-matrix, release, mutation-smoke, and 15-package dry-run gate |
| `hns-node-rs` | `main` | `96570aa2d0841c5244e464ef46b609e2f6b0a672` | PASS — `CARGO_TARGET_DIR=/home/den/.cache/hns-node-wallet-20260802-target TMPDIR=/home/den/.cache/hns-node-wallet-20260802-tmp.L6x6z3 ./scripts/check.sh`; full matrices, release, performance, and two-node regtest |
| `hns-dane-engine` | `main` | `6ed28559cd32163e3995a944010152d92eabe184` | PASS — `./scripts/check.sh` with disposable NVMe target/temp directories; all matrices, release/ABI, and 19 archive dry-runs |
| `hns-wallet-rs` | `main` | `8aa82dd990d41732874f566a256348b1c325e2a1` | PASS — `./scripts/check.sh`; Rust checks/tests/docs, dependency policy, npm audit, and deterministic Solidity artifact |
| `hns-dane-browser-mobile` | `main` | `58996db0facef1bb6a7cb2876361d13dabc90c75` | PASS — `./scripts/check.sh`; exact focused Android Gradle compilation/tests also passed; Swift/Xcode unavailable |
| `hns-dane-browser-extension` | `main` | `2300ef82a765a6dbd1b99ad537d3d3c2ac312d95` | STAGED PASS — `./scripts/check.sh` stages through Rust/release passed on the source-equivalent predecessor; after the docs-only fix, `npm run check:extension` passed; full script not rerun |
| `ecosystem` | `main` | containing commit; exact hash reported in the handoff | PASS — `./scripts/check.sh`; strict evidence/revision cross-check and diff check |

The ecosystem row necessarily identifies its containing commit here because a
commit cannot embed its own hash. The exact hash is reported in the final
handoff.
