# Wallet and Marketplace Implementation Report

Snapshot: 2026-08-02

Overall status: **production-completion implementation in progress; not
release-ready and not authorized for mainnet settlement**. Independently
buildable protocol, node, authority, wallet, and browser-adapter foundations
have unqualified source successors, while unavailable value/name/product paths
remain fail closed. This report does not claim a complete wallet product or
bilateral swap because the real multi-process, restart, reorg, device,
benchmark, consolidated-revision, and independent security gates below have
not passed.

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
- `hns-dane-browser-mobile`: dormant source-level Android/iOS wallet-provider
  plus closed public approval/event projections, unconnected secure-key-wrapper,
  and UI-state adapters;
- `ecosystem`: architecture, dependency, registry, qualification, gap,
  revision, and implementation evidence.

New repository: `hns-wallet-rs`, an independent workspace on `main`. It has
its own lockfile, licenses, gate, release boundary, and no committed sibling
path dependency. Its configured `origin` is
`https://github.com/denuoweb/hns-wallet-rs.git` at remote-tracking `main`
`1206a8ab550cf67ff43dc162091e371946278641`; local `main`
`604a35771a9427696b6ecf533368205392e62979` is ahead by seven commits,
and those commits are unpushed with no push authorization. Its twelve crates
are:

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
11. `hns-wallet-service`
12. `hns-wallet-testkit`

Three additional crates were added at their canonical repository boundaries:
`hns-marketplace-protocol` in `hns-rs`, and `hns-wallet-index` plus
`hns-denuo-market-relay` in `hns-node-rs`. In total this update adds fifteen
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
module's full settlement suite passes. HNS now registers source-level
`ChainModule`, `UtxoChainModule`, and `AtomicSettlement` implementations, but
its value permit is hard-disabled and the runtime is unqualified. Bitcoin and
Ethereum still expose incomplete module/settlement boundaries rather than a
complete executable product join.

| Surface | Status at this snapshot |
| --- | --- |
| canonical marketplace/name protocols | feature source at `81f2df26` adds HSD-compatible fee algebra, strict TRANSFER/FINALIZE construction, canonical empty offer inventory, and listing-independent Shakedex recovery; current descendant `4b989aab` adds self-contained public packages and complete listing/cancellation and recovery-FINALIZE vectors; unpublished and unqualified |
| node confirmed indexes/backend | current `main` `3d346e3d` includes authenticated RPC v1 and snapshot-bound exact final-transaction fee quotes; wallet indexes remain disabled by default and the current head is not qualified by this ledger |
| node marketplace relay | implemented and locally tested cache/policy core; live V2 wire unavailable |
| encrypted store/provider policy | schema-v3/runtime hardening, private ABI-v2 binding and typed capability snapshot, strict provider authority lifecycle, concrete HNS node adapter, Kyoto supervisor, false Shakedex/value gates, encrypted same-snapshot `HnsName` discovery, and authoritative-account CAS hardening at `604a3577`; source/static-only, tests unrun, unpushed, and unqualified |
| usable HNS/name wallet | HNS source runtime and concrete node join implemented but value-disabled; bounded name-key discovery exists as unqualified source, but names remain watch-only and the browser product is unavailable |
| fixed-price Shakedex | canonical transaction and listing-independent recovery primitives exist; wallet lifecycle remains disabled and unavailable |
| Kyoto Bitcoin wallet/settlement | durable bounded supervisor and dedicated swap derivation source implemented; value disabled pending Kyoto persistence, signed settlement, archival, and qualification |
| native-ETH wallet/contract | deterministic offline receive derivation plus contained typed source; synchronization/history/send/value/settlement/mainnet false or unavailable; verified synchronization/deployment unavailable |
| HNS/BTC and HNS/ETH | disabled; end-to-end settlement unavailable |
| engine provider/proxy authority | opaque exact-origin proxy admission source at `6eb0174a` retains authority across unrelated work and invalidates on security transitions; product consumption and qualification unavailable |
| Chromium provider | current source `972e63a1` accepts fresh-only generation zero in the private capability input while public website capabilities remain `{providerApiVersion,methods}` and native events retain exact permission-generation/wallet-session matching; source/static-only, tests unrun, unpushed, and disabled by false signed-transport/projection/engine-authority/provider/value gates |
| Android/iOS provider | current `4b684ebb` applies the same private fresh-zero/public-capability/event-binding split to the dormant twelve-approval/thirteen-event projections; source/static-only, tests unrun, unpushed, and unavailable, with four false release gates, a hardwired unavailable adapter, and no controller, wallet runtime/FFI, generated binding, approval UI, or event producer. Earlier `58996db0` Android compile evidence does not transfer |
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

The new, unpublished lockstep `hns-rs` 0.2.0 source and its
runtime-independent `hns-marketplace-protocol` crate own bounded
chain/asset/network bindings, unsigned integer native amounts, reduced
rational prices, signed observations/intents/cancellations/matches/grants,
deterministic quorum/outlier/age/link/movement checks, session terms/status,
and typed Denuo codecs. At source revision `7d3b2604ac572bfea26f8a0518e89c3c8446bdba`,
fill grants delegate to a separate maker settlement key; session hellos bind
both parties, exact native-HNS HTLC descriptors, and ceiling-rounded HSD
refund times. `hns-swap` owns signed fixed-price listings/cancellations,
canonical buyer fulfillment, independently seller-signed explicit-recipient
`0x83` recovery, and SHA-256 HNS HTLC funding/redeem/refund/preimage
primitives. Recovery does not depend on retaining or validating the listing's
`0x84` presign. Feature landing `81f2df2` added canonical HSD-compatible
NameState/resource decoding, sigop-adjusted minimum-fee arithmetic with
explicit units, strict TRANSFER/FINALIZE covenant and transaction helpers,
canonical zero-count offer inventory, and listing-independent Shakedex lock
recovery. Current source head
`4b989aabc132e7e79b8fd57a10f2465073faf588` adds package-local public assets,
complete deterministic listing/cancellation and recovery-FINALIZE vectors,
fail-closed mutation source tests, batching-safe index-zero verifier naming,
and release dependency hygiene. Current-tip ownership, maturity, renewal
ancestry, chain inclusion/unspent status, funding signatures, and wallet fee
selection remain downstream checks. This successor was statically reviewed
only and the shared 0.2 packages remain unpublished and unqualified.

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
`quote_transaction_fee` separately binds an exact final serialized transaction
to an expected chain epoch and mempool process/generation, resolves at most
4,096 inputs from that captured node state, and reports checked actual/minimum
fee evidence using canonical HSD sigop-adjusted policy size. It accepts no
caller-supplied coins, sigops, weight, or rate and does not sign or broadcast.

The Denuo relay core has independently opt-in roles for name listings,
cross-chain intents, observations/rounds, match/fill rendezvous, and bounded
session status. It implements hash-first fetch, object/aggregate limits,
expiry, duplicate and monotonic-sequence checks, peer/signer rates and policy,
timeouts, scoring, malformed penalties, and bounded progressive bans. It does
not sign, choose matches, calculate an authoritative price, store keys, hold
funds, or advance a swap. The current node dependency pin is still Denuo V1,
so live V2 advertisement and typed wire dispatch remain disabled until the new
canonical crate is released and pinned.

The current continuation at
`3d346e3dadc716b5c367eee050308e71a0693a64` includes chain-epoch-bound complete
sorted-script restoration, process-instance/generation/query-bound mempool
pages, and same-block/pre-current-view wallet indexing. It atomically tracks
registered Shakedex-v2 and HNS-HTLC-v1 funding/spends through disconnects,
distinguishes seller `0x84` fulfillment from independently signed `0x83`
recovery, and extracts verified HTLC preimages while redacting incidental
public serialization. Current name state and proof-committed name state remain
separate. It now exposes a conditional authenticated loopback
`POST /api/v1/wallet` v1 contract with bounded strict JSON envelopes, durable
chain epoch/tip binding, process/generation-bound mempool evidence, ordered
spender results, canonical NameState bytes, and exact retained/pruned
transaction semantics. The RPC now also quotes one exact final serialized
transaction against one chain epoch and mempool generation, resolving inputs
itself and returning rate evidence, weight, sigops, HSD policy virtual bytes,
actual/minimum fee, shortfall, and exact bindings without signing or
broadcasting. Relayed status stays an untrusted hint. Tagged v0.3.4 source
`40b456fa` also packages the ordinary DNS resolver as a separate loopback-only
sidecar sharing the node network namespace without publishing RPC; current
`main` adds release-CI port-verification corrections. This externally pushed
source inherits no earlier PASS in this ledger; a released canonical
protocol pin, safe registry retirement/capacity reclamation, exact image and
multi-process qualification, and final release gate remain unavailable. The
concrete wallet adapter now exists as unqualified source at
`5b5409630045b19f81821951da51a9a1f7e1c9e5` and is retained at current
`604a35771a9427696b6ecf533368205392e62979`.

Wallet-index profile V1 is checksummed and fails closed on missing, corrupt,
or partially built components. There is no online backfill: an existing chain
requires a new synchronized data directory or a future version-matched offline
reindex tool. Index rows survive raw block pruning, but historical raw
transaction and owner-transaction retrieval can return `PayloadPruned`; exact
disk and indexing costs remain unmeasured. History, spender, and script-UTXO
values are versioned/checksummed and key-bound so relocated values fail closed.

## Provider API and browser authority

The provider core and browser adapters parse, classify, permission-gate, and
approval-classify one canonical 43-method vocabulary and allowlist 13 events. This
is a protocol surface, not a claim that 43 wallet operations execute in a
browser: private wallet ABI v2 framing and service dispatch foundations now
exist in source, but no released artifact or browser application dispatcher is
available. The exact methods are:

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

The private ABI `providerCapabilities` request produces a typed snapshot with exactly
`providerSchemaVersion`, `approvalSchemaVersion`, `walletSessionId`,
`permissionGeneration`, and `methods`. Those methods describe the current
runtime-supported subset of the canonical vocabulary, not granted permission.
Generation zero is valid only before the exact authority has any grant or
revocation history; an absent permission record after revocation or expiry
retains its nonzero tombstone generation. The website-facing
`wallet_getCapabilities` projection is deliberately different and contains
only `{providerApiVersion,methods}`. No native adapter projects the private
snapshot into either browser today. `hns_requestAccounts` remains a canonical
wire name but is unadvertised and unavailable until an approved Accounts grant
can be atomically joined to a real account result.

The API explicitly rejects generic Ethereum calls/signatures/deployment/chain
changes, PSBT and raw-transaction signing, unknown methods, secrets, and
unrestricted native commands. Requests are bounded and bound to exact origin,
namespace, browser-authority session, runtime generation, policy generation,
navigation generation, wallet session, permission generation, and document.
Origin permissions, approvals, replay state, pending counts, read/mutation
rates, expiry, revocation, and stale generations fail closed. Private provider
results, approval prompts, and events reuse one binding containing the authority
handle/revision, wallet session, and permission generation. Permission-bearing
events require a positive generation matching that binding.

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

At source head `6eb0174ae743e6bd01c516be7a534d94be94b4bd`, the engine consumes
that opaque authority context to publish non-cloneable exact-origin loopback
proxy grants. Admission is bound to authority, runtime, process, listener, and
origin generations; strict CONNECT authentication, pending/publication/grant
lifetimes, and atomic invalid/expired-publication reclamation are bounded and
fail closed. A retained authority survives unrelated admitted work but not
degradation, revocation, stop, policy/runtime invalidation, expiry, navigation,
or same-origin decision replacement. This is an engine boundary, not browser
wiring, and neither browser product consumes or qualifies it yet.

Wallet source `5b5409630045b19f81821951da51a9a1f7e1c9e5` introduced strict private ABI
v2 sessions, opaque authority handles, structured approval prompts, typed
events, and zeroizing secret-bearing frame buffers. Provider persistence is
scoped by exact namespace plus origin;
approval consumption revalidates current unexpired permission, process-local
time rollback fails closed, wallet lock rotates service authority, and
revocation/expiry invalidates event channels. Send prompts bind exact method,
module, chain, amount asset, and fee asset. The checked-in subprocess advertises
framing foundations only—not provider dispatch or value. Current
`604a35771a9427696b6ecf533368205392e62979` adds the shared private binding,
tombstone-preserving permission snapshots, exact typed capability snapshot, and
canonical method-name set described above. It explicitly leaves
`hns_requestAccounts` unavailable and also prevents the legacy Shakedex 0.1
journal from creating, discovering, or advancing sessions until canonical V2,
Denuo V2, and value-runtime release gates are qualified. This source received
static review only; its added tests and consolidated gate remain unrun.

The Chromium adapter at `972e63a14f9067da3608f53b852adc93d8ded2a4`
installs an isolated document-start bridge but injects
the MAIN-world provider into one exact HTTPS main-frame `documentId` only
after current navigation authority and a private-ABI-v2 capability pass. Its
website provider schema remains 1. Its private capability validator accepts
generation zero only for an authority with no permission history; its website
capability projection remains `{providerApiVersion,methods}`, and native events
retain exact wallet-session/permission-generation matching. Source validates a closed 12-kind
browser-owned public approval projection, canonical approval IDs, private
authority containment, native-only events, and exact close/reject context. It
has a bounded approval window, generation-bound events, and a static no-key/no-
backend demonstration dapp. The native host never launches a wallet service
and still returns unavailable because the signed transport, projection adapter,
and engine authority join do not exist. Wallet database, secret, chain,
Shakedex, Denuo, and recovery
integration into the native host remains unavailable. The browser's pinned
engine/native-host boundary also does not yet consume the new Rust facade v3
opaque provider-authority context, so no cross-repository authority/ABI join
is claimed. This unpushed source received static review only; its added tests
remain unrun and every artifact, transport, runtime, authority, provider, and
value gate remains false.

Current mobile head `4b684ebbb576c2b2f8e762c3f81c3ec2fded47f5`
keeps website Provider API schema and `providerApiVersion` 1 separate from the
expected private native wallet ABI 2 and browser-owned public approval schema 2.
Android and iOS close twelve typed approval summaries and thirteen typed event
projections, reject private authority/session/channel/event-sequence material
from page-visible results, and retain standalone secure-key helpers and wallet
UI-state models. Android and iOS accept generation zero only in the fresh
private capability input, keep the website result to
`{providerApiVersion,methods}`, and require positive generation plus exact
wallet session for permission-bearing events. This source deliberately does not alter the existing browser
navigation path: provider-bridge installation, wallet runtime, approval runtime,
and value runtime gates are all false; the unavailable adapter is hardwired;
the bridges are absent from `MainActivity` and WKWebView controller lifecycles;
and no wallet runtime/FFI, generated `hns-wallet-ffi` JNI/C binding, native
approval UI, or typed event producer exists. The successor is unpushed and
received source/static inspection only; its added tests remain unrun, with no
build, Swift/Xcode,
simulator, signed-device, or installed-product result.

At exact predecessor `58996db0facef1bb6a7cb2876361d13dabc90c75`, the
Android scaffold and unit sources compiled in the focused Gradle path and the
iOS project contained the expected source/test references, while neither
`swiftc` nor `xcodebuild` was available. That evidence does not qualify
`4b684ebbb576c2b2f8e762c3f81c3ec2fded47f5`.

## Wallet, names, Shakedex, and market board

The wallet continuation at `604a35771a9427696b6ecf533368205392e62979`
has transactional SQLite schema V3, bounded Argon2id passphrase input,
XChaCha20-Poly1305 typed entity, workflow, permission, approval, and replay
encryption with metadata-bound associated data, monotonic permission
tombstones, and bounded heterogeneous compare-and-swap batches. HNS preparation
authenticates current revisions and atomically commits account change-index
advancement, its prepared workflow, and all input reservations; deterministic
retries return the already-durable artifact. Legacy populated schema-V1 entity
tables fail closed pending an explicit import tool. It remains record encryption
rather than full-file encryption. Platform key wrapping, non-Linux secure
persistent opening, backup/rollback qualification, and device persistence
remain incomplete.

HNS create/restore, encrypted seed storage, deterministic role-separated key
derivation, receive addresses, bounded indexed confirmed/mempool restoration,
history/reorg reconciliation, fee/send construction and signing, durable input
reservations, typed node evidence, and HNS HTLC settlement construction exist in
source. A concrete synchronous adapter consumes authenticated loopback node RPC
v1 contract commit `5ed38d15` with strict bounded HTTP/JSON, exact chain-epoch/
tip and mempool process/generation binding, canonical transaction decoding,
active-block rechecks for inclusions/spenders, and fail-closed coinbase handling.
The ordinary HNS-coin branches and domain-separated `HnsName` branch now run as
separate bounded queries under the same exact chain/mempool snapshot. Their
encrypted address and monotonic scan state are persisted separately by role;
name-role outputs remain in history but are excluded from ordinary balance,
input selection, reservation, and spendability.

Before scanning, reconciliation reloads the full authoritative encrypted account
and CAS revision while holding the store mutex. Account/configuration or
revision inconsistency and receive/change/name derivation-high-water rollback
fail closed; the authoritative revision remains ordered through persistence and
cache installation so a stale scan clone cannot overwrite concurrently prepared
state. This is source-only hardening and has not run the consolidated gate.
Ordinary send and exposed settlement paths still quote the exact final signed
bytes, atomically bind approval/workflow/reservations to the persisted quote,
and durably record `RequiresRebroadcast` plus a current re-quote before
submitting the same bytes. One stale/unavailable quote permits one reconciliation
and one retry, with no polling loop.

HNS value remains hard-disabled because released `hns-script` 0.1 lacks the
canonical sigop-adjusted fee algebra required for an independent wallet minimum
check; the source does not copy the node formula. Name imports preserve separate
exact-tip proof and current-state views and retain exact NameState bytes. The
new scan establishes key discovery only, not ownership: canonical codec and
TRANSFER/FINALIZE helpers exist only in unpublished `hns-rs` `4b989aab`, names
remain watch-only, and transfer/finalize actions and browser UI are unavailable.
HNS has separate coin, name, Shakedex, atomic-swap, identity, and dapp-session
derivation domains, and Ethereum has ordinary/swap branches. The Bitcoin crate
derives a separate deterministic atomic-swap branch with bounded descriptors
and role-aware recovery, but it is unqualified. A complete, reviewed derivation
specification and cross-module deterministic recovery-vector set are still
missing.

Fixed-price Shakedex seller, buyer, and recovery state machines persist before
irreversible steps and consume canonical `hns-swap` proof decoding. Ordering
and recovery negative tests exist at an earlier exact revision. Canonical
strict TRANSFER/FINALIZE construction and listing-independent recovery
transaction construction now exist in unqualified `hns-rs` source, but wallet
adoption, exact
node evidence, live Denuo publication, restart at every state, reorg handling,
regtest, and browser approval are missing. Shakedex is therefore partial rather
than complete. Reverse Dutch is deferred.

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

`hns-wallet-store` schema V3 migrates transactional metadata from SQLite
`user_version=0` and encrypts active typed entity/provider state. Newer schema
versions fail closed; populated legacy entity tables require an explicit
import rather than silent conversion. There is still no historical production-
wallet upgrade corpus. Atomic HNS prepare, exact persisted-artifact retry, and
authoritative-account CAS ordering for the encrypted coin/name-role scan now
exist as unqualified source, and the bounded Kyoto subsystem supervisor has its
own durable journal. Backup/rollback qualification, database-key platform
wrapping, and the complete multi-chain/product startup coordinator remain
unavailable.

The node's existing store schemas and the separate checksummed
`wallet-index-profile/v1` record are not silently rewritten into a complete
index. No online backfill or resumable wallet-index migration is claimed.
Neither browser product has a wallet database migration because neither
currently embeds the wallet database. No production user database was
migrated during this update.

## Bitcoin, Ethereum, and bilateral settlement

Bitcoin has one production boundary only: `bip157` 0.6.3, `bdk_kyoto` 0.17.0,
and `bdk_wallet` 3.1.0. Code constructs a direct-P2P Kyoto client and BIP84 BDK
wallet, supports create/load/receive/send building blocks, and constructs/
verifies native P2WSH SHA-256/CLTV HTLC funding, unsigned spends, and preimage
extraction. The source successor at `3a3323c0` adds a bounded supervisor with
trusted-checkpoint discovery, encrypted CAS scan phases/checkpoints, BDK-first
update persistence, restartable transaction/output reconciliation, bounded
reorg recovery, and fee-bound pre-broadcast/rebroadcast journals. No Esplora,
Electrum, hosted indexer, or production Bitcoin Core RPC dependency exists.
The pinned `bip157` release ignores `data_dir` and does not expose durable
header/filter/peer state, so this is not production persistence. A dedicated
deterministic swap-key branch landed at `5b540963` and remains in current
`604a3577`, but it has not been qualified. Safe record archival, signed HTLC
spends/settlement, full
invalid-PoW/filter/peer fixtures, regtest settlement, trusted-time policy, and
mobile/resource qualification are missing; Bitcoin value paths remain hard-
disabled.

Bitcoin storage and bandwidth benchmark status: **not measured** for fresh
install, new wallet, one-year restore, five-year restore, genesis restore,
time to usable balance, scan completion, persistent disk, bandwidth, and peak
mobile memory. No universal size is claimed.

Ethereum is native-ETH-only. Current `604a3577` capability discovery advertises
deterministic offline account/receive derivation only. The immutable
synchronization, value, settlement, and mainnet qualification constants are
false; history, send, authoritative evidence, and atomic settlement are
therefore unavailable. Separated ordinary/swap accounts, bounded typed
EIP-1559/native-HTLC transactions, structural evidence models, and the contract
remain dormant source boundaries rather than an executable runtime.

Helios is the single selected model, pinned for evaluation at revision
`43a8c9f3cdda41a6f383c4db41d9a83f102638b1`. A future embedded verifier must
start from a reviewed weak-subjectivity checkpoint and bind sync-committee/
finality plus execution proofs. Current serializable execution observations and
their verification booleans are structural data, not proof provenance. A
private-field opaque `HeliosEvidenceRuntimePermit`, with no public acquisition
path or current issuer, is required before those observations may produce an
authoritative verified lock. The crate does not embed that Helios runtime;
configured providers would also remain availability, censorship, omission,
privacy, and startup dependencies.

Native-transfer and HTLC constructors require opaque value/settlement permits
whose public acquisition paths fail closed. Signing additionally requires an
exact immutable transaction to be fee-bound, a permit matching the operation
class, and a secret whose derivation role and address match the required signer.
Chain ID 1 is rejected regardless of the legacy caller policy flag. A resulting
signed payload is zeroized on drop and deliberately has no public raw-byte
accessor, serializer, clone implementation, or byte-revealing `Debug`; only its
type, length, and hash are exposed. Because no permit can currently be issued
and no controlled broadcaster exists, this is an opaque/redacted containment
boundary rather than a raw-signing API or available value path.

Ethereum database size, startup latency, and time to a usable verified balance
were not measured because there is no embedded Helios runtime or persistent
proof database. No synchronization, balance/history, nonce/fee discovery,
broadcast, persistence/recovery, redeem/refund proof verification, or rollback
runtime exists. A future runtime must remain unavailable until fresh verified
evidence is present and record those measurements without claiming a universal
fixed size.

`NativeEthHtlc.sol` is compiled deterministically with Solidity 0.8.35,
optimizer runs 200, Prague EVM, and metadata CBOR disabled. It has only
`lock`, `redeem`, and `refund`; no administrator, owner, proxy, upgrade,
pause, token, arbitrary call, fee withdrawal, or mutable configuration. No
deployment address is approved. A future manifest must bind chain ID,
contract address/block, exact runtime Keccak-256 hash, compiler artifact, and
qualification evidence. The settlement permit has no current issuer, so the
artifact does not expose a wallet lock/redeem/refund path. The wallet
hard-rejects chain ID 1 until a reviewed source change follows proof
persistence, local-chain tests, bytecode/contract audit, and finality/reorg
qualification.

HNS/BTC and HNS/ETH share a persisted evidence-only state machine and an
asymmetric timeout model: the intent publisher funds its offered-asset chain
first with the later refund deadline; the shorter second lock is funded only
after sufficient first-chain evidence. Neither pair is complete or enabled.
HNS/BTC still lacks signed integrated chain execution; HNS/ETH additionally
lacks embedded Helios proof provenance, an available settlement permit,
controlled broadcast/recovery, and an approved/audited deployment. No success,
refund, restart, or reorg demonstration was run for either pair.

## Qualification results

All PASS evidence below belongs to the exact earlier revisions named in the
final table. It did not transfer to feature landing `81f2df26` or current
descendant `4b989aab`, nor to `3d346e3d`, `604a3577`, `6eb0174a`,
`972e63a1`, or `4b684ebb`. This report
records only the per-row provenance and static review stated in the
continuation table; it does not infer a consolidated gate result.

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
documented and qualified derivation/recovery vectors, end-to-end
secret-lifetime review, complete recovery/reorg supervision, installed-browser
and signed-device testing, HTLC/timeout/contract audits, sustained fuzzing, and
real network adversarial tests. Unit tests are not mainnet authorization.

Trust limitations include the first-party HNS node's availability and index
completeness, untrusted Denuo peers/reporters, Bitcoin peer eclipse/omission
risk within Kyoto's validation model, the Helios weak-subjectivity checkpoint,
and Ethereum provider censorship/omission/privacy/availability. Peer status,
relay identity, RPC booleans, and website data are hints, never chain evidence.

Mainnet blockers are the unpublished V2/name/fee-policy dependency; incomplete
Bitcoin/Ethereum chain joins and wallet runtime/native-host/mobile wiring;
hard-disabled HNS value paths pending released canonical fee-algebra adoption
and qualification, and watch-only names; incomplete name and Shakedex product flows;
unqualified node/wallet RPC and tracker integration; unreclaimable node
contract-registry lifetime caps; pinned Kyoto header/filter/peer persistence,
swap-key qualification, archival, signed-settlement, regtest, trusted-time, and resource
gaps; absent embedded Helios proof production and approved contract
deployment; no pair success/refund/restart/reorg qualification; incomplete
price governance; unconsumed engine proxy authority; and no independent
third-party security audit.

Deferred or deliberately unavailable features include auctions/registration,
resource editing, renewal automation, free/donated names, domain-service and
billing features, content aliases, reverse Dutch, Litecoin/additional chains
or pairs, generic Bitcoin signing, generic Ethereum dapps/contracts/tokens/
NFTs/DeFi/staking/WalletConnect/`window.ethereum`, wrapped assets, AMMs,
centralized books, custodial accounts, and server-held user keys.

## Exact revisions and commands

This section separates the last exact non-redundant repository gates from the
current source heads. Publication provenance is stated per row; neither a push
nor a tag authorizes a product or mainnet path.

| Repository | Branch | Revision | Last non-redundant qualification |
| --- | --- | --- | --- |
| `hns-rs` | `main` | `b66470a6a07f0211e3e7fa9aef7d034c8486e75b` | PASS — `./scripts/check.sh`; full protocol, registry, feature-matrix, release, mutation-smoke, and 15-package dry-run gate |
| `hns-node-rs` | `main` | `96570aa2d0841c5244e464ef46b609e2f6b0a672` | PASS — `CARGO_TARGET_DIR=/home/den/.cache/hns-node-wallet-20260802-target TMPDIR=/home/den/.cache/hns-node-wallet-20260802-tmp.L6x6z3 ./scripts/check.sh`; full matrices, release, performance, and two-node regtest |
| `hns-dane-engine` | `main` | `6ed28559cd32163e3995a944010152d92eabe184` | PASS — `./scripts/check.sh` with disposable NVMe target/temp directories; all matrices, release/ABI, and 19 archive dry-runs |
| `hns-wallet-rs` | `main` | `8aa82dd990d41732874f566a256348b1c325e2a1` | PASS — `./scripts/check.sh`; Rust checks/tests/docs, dependency policy, npm audit, and deterministic Solidity artifact |
| `hns-dane-browser-mobile` | `main` | `58996db0facef1bb6a7cb2876361d13dabc90c75` | PASS — `./scripts/check.sh`; exact focused Android Gradle compilation/tests also passed; Swift/Xcode unavailable |
| `hns-dane-browser-extension` | `main` | `2300ef82a765a6dbd1b99ad537d3d3c2ac312d95` | STAGED PASS — `./scripts/check.sh` stages through Rust/release passed on the source-equivalent predecessor; after the docs-only fix, `npm run check:extension` passed; full script not rerun |
| `ecosystem` | `main` | containing commit; exact hash reported in the handoff | PASS — `./scripts/check.sh`; strict evidence/revision cross-check and diff check |

Source-only production-continuation revisions after those exact gates:

| Repository | Revision | Static-only evidence and status |
| --- | --- | --- |
| `hns-rs` | `4b989aabc132e7e79b8fd57a10f2465073faf588` | canonical HSD fee policy and strict Shakedex name transitions/recovery retained from `81f2df2`; self-contained package assets, complete listing/cancellation and recovery-FINALIZE vectors, fail-closed source tests, and release hygiene committed; static/diff review only in this tranche; shared 0.2 packages remain unpublished and unqualified |
| `hns-node-rs` | `3d346e3dadc716b5c367eee050308e71a0693a64` | local and remote-tracking `main`; exact fee quotes and resolver-sidecar source are present, tag `v0.3.4` points to `40b456fa0772729542118a69f27edc37bf42a3d7`, and this ledger records no new consolidated qualification result |
| `hns-wallet-rs` | `604a35771a9427696b6ecf533368205392e62979` | private ABI-v2 results, prompts, and events share the exact authority/wallet/permission binding; the typed private capability snapshot uses the canonical 43-name vocabulary, fresh generation zero cannot erase a nonzero tombstone, and `hns_requestAccounts` is unavailable; prior wallet/name/value containment remains; source/static review only, added tests unrun, unpushed, no qualification inherited |
| `hns-dane-engine` | `6eb0174ae743e6bd01c516be7a534d94be94b4bd` | source/read and diff checks only; retained proxy authority is not consumed or product-qualified |
| `hns-dane-browser-extension` | `972e63a14f9067da3608f53b852adc93d8ded2a4` | source/static checks only; fresh-zero private capability admission is separate from the narrow public website result and exact permission-generation/wallet-session event matching; added tests unrun, unpushed, no service launch, all provider/value joins false or unavailable |
| `hns-dane-browser-mobile` | `4b684ebbb576c2b2f8e762c3f81c3ec2fded47f5` | source/static checks only; dormant adapters apply the same private/public capability split and event binding; added tests unrun, no build/install/push, all four release gates false, unavailable adapter hardwired, and controller/wallet-runtime/FFI/generated-binding/UI/event-producer wiring absent |
| `MeshMine` | `79f3bbc6c24bab80adaef199a9318fd0065113f6` | workspace packages are private; immutable node pin and live parent/job topology status are unchanged |

The ecosystem row necessarily identifies its containing commit here because a
commit cannot embed its own hash. The exact hash is reported in the final
handoff.
