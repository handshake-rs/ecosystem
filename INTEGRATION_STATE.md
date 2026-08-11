# Integration state

Status: **production-completion implementation in progress; not release-ready
and not authorized for mainnet settlement**

## Authoritative current-head state (2026-08-10)

All coordinated source repositories listed here are now on their stated
remote `main` except the explicitly separate `namehold-wallet` work branch.
This section supersedes later historical statements that a current source head
is local-only, unpushed, or hosted at the old wallet origin. It does not erase
the dated evidence those statements described.

| Repository | Current revision | Current qualification boundary |
| --- | --- | --- |
| `hns-rs` | `a93ba7a806a921a8ce2d13d9c5fc041ff0ecf6e7` | Exact-head CI passed (`31372546141`); source predecessor `b33b346` passed hosted protocol qualification and RustSec (`31369025777`). Current `0.2.0` crates remain unpublished. |
| `hns-dane-engine` | `84005f1df21a30ea9dda7fafb95f9488b8f5da4b` | Exact-head hosted CI and CodeQL passed (`31372280327`, `31372280387`); the HNSA implementation predecessor `3c12ace` also passed local locked workspace tests, warning-denied Clippy, and release build. No crate or browser artifact is published from this head. |
| `hns-wallet-rs` | `4cd9a61a8520c4d3bddd15b3fffcad0d02aafd36` | Hosted run `31372389330` failed strict Clippy in HNS workflows after correcting ceiling division; a successor fix is in progress. No wallet crates or native ABI artifact are published. |
| `hns-node-rs` | `063ba6b82b4b34ea0e56992aa0c0d48855e03e71` | Exact-head hosted CI/container runs are pending. Focused Rust 1.97.1 warning-denied Clippy passed for `hns-store` using the mandated prebuilt RocksDB, superseding the `6e3f7a4` hosted failure. Current source is the unpublished `0.3.5` candidate. |
| `hns-dane-browser-mobile` | `e8d6a0baede5e34cfcf0568ffd2187cfd0456815` | Exact-head documentation/policy CI passed (`31371872754`); source-equivalent `85647ae` passed the full hosted gate and its debug APK installed and cold-launched on Android. This is browser-scaffold evidence, not wallet/provider evidence. |
| `hns-dane-browser-extension` | `bfa089992b427d6b090989b6289dc68ef1e74fee` | Exact-head CI and CodeQL are green; source-equivalent `08ba480` passed full hosted CI. The installed Chromium extension has no exact wallet/provider/native-host end-to-end qualification. |
| `namehold-wallet` | upstream `main` `e18e38f`; `pr-21-hsrd` `9d168a6` | The hsrd/ARM64 integration branch is not yet reconciled with upstream `main`; no combined-main qualification or release claim exists. |

Implementation, testing, wiring, enablement, publication, and installation are
separate states. Current source implements the canonical HNSA/HNSR primitives,
engine authority/admission, wallet lifecycle/read/market components, and
browser-side schemas. The shipping mobile and extension runtimes still do not
invoke `hns-wallet-rs` through a released generated JNI/C/native-host binding;
they do not consume the latest HNSA named-route admission through an
engine-issued product authority; wallet/provider/value/market gates remain
false. Consequently:

| State | Wallet controls | P2P marketplace |
| --- | --- | --- |
| Implemented in source | Partial: persistent wallet control and typed create/restore/read vocabulary exist, but the production executable/controller surface is incomplete | Partial: canonical protocols and durable wallet workflows exist |
| Exact-head tested | Wallet `4cd9a61` failed strict Clippy; browser scaffold evidence is separate | Protocol primitives pass at `hns-rs` `b33b346`; wallet/browser end-to-end remains pending |
| Product-wired | No | No |
| Value-enabled | No | No |
| Current-source artifact published | No wallet ABI artifact | No marketplace-capable browser artifact |
| Installed qualified | No wallet flow | No discovery, approval, fill, settlement, restart, or reorg flow |

The first product milestone remains an app-local wallet slice: app-owned secure
persistence plus generated Android JNI and Apple C bindings for create,
restore, status, unlock, lock, and one configured HNS account identity. Balance,
history, and receive targets require a complete concrete mobile `HnsBackend`
and are not part of that first slice. Origin permission/approval projection
follows independently; HNS value movement, Shakedex/Denuo, HNSA/HNSR
marketplace transport, and bilateral settlement remain later gated slices.

## Production-completion continuation

The narrative below is retained historical evidence. Its old “local,”
“unpushed,” and “current head” statements are superseded by the authoritative
checkpoint above.

Production completion is now the active objective. Work proceeds in the
dependency order and with the evidence rules in
`PRODUCTION_COMPLETION_PLAN.md`; this heading does not upgrade any status on
its own. The current source tranche covers canonical fee/name/Shakedex
primitives, authoritative node wallet/HTLC tracking and fee quotes, the
wallet's encrypted runtime/private ABI/provider/recovery join, and browser
authority and provider-projection boundaries.

Before that tranche, the pre-existing Chromium insecure-delegation correction
was committed on `main` at
`5ffca638481b64172666db482f99f6156a44ccbf`, together with a repository-root
`dist/` ignore rule. No new qualification claim is attached to that follow-up
here. This external-drive checkout is now source-only: any future local gate
must run from an NVMe checkout/worktree, not merely place its final target on
NVMe. Optimized RocksDB must never be rebuilt and may only be supplied from an
existing NVMe prebuilt library. Each coherent source revision receives only
one consolidated qualification layer.

Repository-root `/dist/` is ignored in `hns-rs`, `hns-node-rs`,
`hns-wallet-rs`, `hns-dane-engine`, and Chromium. Mobile is intentionally not
given a global `dist/` ignore because its tracked `dist/` tree contains store
metadata and screenshot source; generated mobile build outputs remain covered
by its narrower ignore rules.

The Chromium half of the source tranche is committed on local `main` at
`972e63a14f9067da3608f53b852adc93d8ded2a4`, three unpushed commits ahead of
remote-tracking `main` and after ABI-v2 documentation commit
`06bea8893ea7e2324d0df7e5b486fb3cf91f9cdd`. It performs bounded same-handle
artifact integrity discovery without treating a digest as publisher
authenticity or executing the artifact, and it invalidates document/approval
authority across asynchronous native results and header maintenance. Private
wallet ABI and service protocol 2 remain distinct from website provider schema
1. A private native capability snapshot may use permission generation zero only
before the origin has any permission history; the public website
`wallet_getCapabilities` result remains `{providerApiVersion,methods}`, and
native events retain exact permission-generation and wallet-session matching.
The browser-owned approval-schema-2 projection closes all 12 summary kinds,
canonical approval IDs, private-authority containment, native-only events, and
exact close/reject context. It still returns unavailable: no signed/pinned
artifact, reviewed private transport/projection adapter, or engine-authority
join is wired; Windows ACL/ownership validation is absent. Artifact
authenticity, transport, runtime, authority, provider, and value gates all stay
false. Source/static review only was performed; the added tests remain unrun,
and no build, push, tag, or publication evidence is attached to this successor.

The mobile half of the source tranche is committed on local `main` at
`4b684ebbb576c2b2f8e762c3f81c3ec2fded47f5`, two unpushed commits ahead of
remote-tracking `main` `58996db0facef1bb6a7cb2876361d13dabc90c75`.
Android and iOS keep website Provider API schema and `providerApiVersion` 1
separate from the expected private native wallet ABI 2 and browser-owned public
approval schema 2. Source closes twelve typed approval summaries and thirteen
typed event projections while excluding private authority, session, channel,
and event-sequence material from page-visible results. Its private capability
input permits generation zero only for a fresh origin, while the website
capability result stays narrow and permission-bearing events retain positive
generation plus exact wallet-session binding. This boundary remains
dormant and unqualified: provider-bridge installation, wallet runtime, approval
runtime, and value runtime release gates are all immutable false; the
unavailable ABI adapter remains hardwired; and no browser controller, wallet
runtime, wallet FFI, generated `hns-wallet-ffi` JNI/C binding, native approval
UI, or typed event producer is wired. Source/static review only was performed;
the added tests remain unrun, and no build, simulator, signed-device,
installed-product, push, tag, or publication evidence is attached to this
source/static-only successor.

The canonical protocol continuation is committed on local `hns-rs` `main` at
`4b989aabc132e7e79b8fd57a10f2465073faf588`. The earlier marketplace
correction binds fill grants to an
independent delegated maker settlement key, joins signed swap-session terms to
the exact native HNS HTLC descriptor, and rounds promised Unix refund times up
to HSD's 512-second encoding rather than shortening them. Fixed-price
Shakedex now has canonical buyer fulfillment plus an explicit-recipient,
independently seller-signed `0x83` recovery TRANSFER; recovery neither retains
nor validates the listing's `0x84` presign. Exact deterministic marketplace,
HNS HTLC, and spend vectors plus registry sidecars are committed. The latest
successor also owns HSD-compatible NameState and resource decode/encode,
canonicality checks, proof-facing exact bytes, and independent fixtures rather
than leaving that protocol to wallet-local projection. Feature landing
`81f2df2` added canonical HSD sigop-adjusted fee arithmetic, strict
TRANSFER/FINALIZE covenant and transaction construction, canonical empty offer
inventory, and listing-independent Shakedex recovery construction. Current
head `4b989aab` makes every public package self-contained with package-local
licenses and fixtures, adds complete deterministic listing/cancellation and
recovery-FINALIZE vectors plus fail-closed source tests, and repairs release-
gate definitions, fixture-mirror enforcement, the fuzz lock, and the publish
dependency map. This tranche received source/static review only; version
`0.2.0` remains unpublished and no
downstream release pin or qualification is implied.

The node continuation is on local and remote-tracking `main` at
`3d346e3dadc716b5c367eee050308e71a0693a64`. Its disabled wallet profile now
provides chain-epoch-bound confirmed restoration for a complete sorted script
set, process-instance/generation/query-bound mempool pages, stable combined
transaction and separately represented current/proof/owner name evidence, and
bounded immutable Shakedex-v2/HNS-HTLC-v1 registrations. Exact funding, spend,
seller-signed `0x83` recovery, refund, and verified revealed-preimage events
enter and leave the canonical block/reorganization batch. Full same-block coin
resolution and pre-current-block overlay ordering keep this optional index
from misreading ordinary children or already-mutated state.
Addresses retain bounded one-to-many descriptor candidates because not every
term is committed by the script; exact output terms select one candidate and
ambiguous matches fail closed. The latest successor exposes this backend as a
strict authenticated `/api/v1/wallet` loopback HTTP contract with durable
epoch/tip and mempool process/generation bindings, exact ordered spender and
transaction evidence, canonical NameState bytes, and nullable transaction
ordinal only when the raw payload is pruned. Contract commit
`df0a47f4118e6d28f0d71eff732345cb0e3795af` adds a snapshot-bound quote for one
exact final transaction, with node-resolved inputs, rate/weight/sigop/policy-
vbyte evidence, actual/minimum fee, shortfall, and exact chain/mempool binding;
the wallet freezes the complete RPC boundary at `5ed38d15d50098191b4473d4dda66a93d4e3e6fc`.
Tagged v0.3.4 source `40b456fa0772729542118a69f27edc37bf42a3d7`
packages the ordinary DNS resolver as a private loopback sidecar, while current
`main` adds later release-CI port-verification corrections. Those external
push/tag facts add no PASS to this ledger. Release remains blocked on a
published canonical protocol boundary, safe registry retirement/reclamation,
multi-process and immutable-image qualification, and the final repository gate.

The engine authority/proxy continuation is committed on local `main` at
`6eb0174ae743e6bd01c516be7a534d94be94b4bd`. It consumes the opaque
`ProviderAuthorityContext` to mint non-cloneable, exact-origin loopback proxy
publications and grants bound to authority/runtime/process/listener
generations. CONNECT parsing, authentication, pending admissions, expiration,
and atomic invalid/expired-record reclamation are bounded and fail closed.
Authority survives unrelated admitted work but not degradation, revocation,
stop, policy/runtime invalidation, expiry, navigation, or same-origin decision
replacement. It does not provide wallet dispatch or prove that Chromium/mobile
consume the authority; installed browser/device and proxy lifecycle
qualification remain open. No new consolidated PASS is recorded.

The encrypted wallet runtime continuation is committed on local `main` at
`4935e059bcde338f4260dd98202ff26ce0f3ca9f`. HNS send and settlement-lock
preparation authenticate and atomically commit the account change index,
prepared workflow, and complete input-reservation set, then recover the exact
durable artifact on an idempotent retry. Confirmed and mempool restoration
retain exact version-zero Address/ScriptId identity plus the node's chain epoch,
tip, mempool instance, and generation through a concrete strict adapter pinned
to node RPC v1 `5ed38d15`. Ordinary HNS-coin branches and the domain-separated
`HnsName` branch now use separate bounded queries that must share that exact
chain/mempool snapshot, including gap expansion. Name-role derivation high-water
state is encrypted and monotonic across restart; derived-address records are
encrypted and restart-durable. Discovered outputs remain visible to history but
are excluded from ordinary balance, input selection, reservation, and
spendability.

Reconciliation now reloads the full authoritative encrypted account and its
CAS revision after taking the store mutex, rejects account/configuration,
revision, or derivation-high-water rollback, saves against that authoritative
revision, and preserves the ordering through cache installation. This source
hardens the stale-reconciliation/concurrent-prepare boundary, but it has not run
the consolidated gate. Name-key discovery is not ownership proof: canonical
NameState/resource decoding is still unpublished/unconsumed, imported names
remain watch-only, and ownership, transfer, and FINALIZE actions remain
unavailable.

The wallet also retains the durable Kyoto/BDK supervisor committed at
`3a3323c0`, private service ABI v2, zeroizing secret-bearing frames, hardened
provider authority, dedicated Bitcoin swap derivation, and exact HNS quote
recovery. Every private provider result, approval prompt, and event now carries
one authority-handle/revision, wallet-session, permission-generation binding.
Its typed private capability snapshot contains provider/approval schema
versions, wallet session, permission generation, and the runtime-supported
subset of the canonical 43 methods; generation zero is fresh-only, a revoked or
expired record retains its nonzero tombstone, and `hns_requestAccounts` remains
unavailable. The new `hns-wallet-host` state machine owns the private hello and
restart generations, clock/entropy, bounded request and approval replay,
authority revisions, mandatory-approval response classes, capability
intersections, exact permission/session transitions, and service-aligned event
replay. Draft 2020-12 contracts and bounded vectors describe private frames,
public approval/event projections, and signed-manifest structure without
claiming a verifier or artifact. No generated browser adapter consumes this
private projection.
`HNS_FEE_QUOTE_ALGEBRA_RELEASE_QUALIFIED` remains false because
released `hns-script` 0.1 lacks canonical fee algebra, so HNS and Bitcoin value
remain hard-disabled. The legacy Shakedex 0.1 journal remains structural-only:
seller/buyer creation, discovery, and every transition—including restored
sessions—fail before decode or mutation behind false canonical-V2, Denuo-V2,
and value-runtime release gates.

Ethereum now advertises deterministic offline receive derivation only. Its
immutable synchronization, value, settlement, and mainnet qualification gates
are false, making history, send, authoritative evidence, and settlement
unavailable; chain ID 1 is rejected independently of caller policy. Public
serializable evidence booleans remain structural data because the private-field
opaque Helios provenance permit has no current issuer. Native/HTLC construction
and exact-fee/role/address-bound signing likewise require opaque value or
settlement permits that cannot be acquired. Any resulting signed bytes are a
zeroizing, non-cloneable, non-serializable object with no raw accessor and
redacted diagnostics, not a public raw-signing API. This successor received
static review only, its added provider/ABI tests remain unrun, and no new
consolidated PASS is recorded.

## 2026-08-02 local wallet and marketplace checkpoint

The coordinated implementation is committed on `main` in six independent
code repositories. It creates the standalone `hns-wallet-rs` workspace, adds
canonical marketplace protocols, adds optional node wallet indexes and a
bounded relay core, and adds fail-closed provider-authority/adaptor slices to
the engine and browser products.

| Repository | Local `main` revision | Delivered boundary |
| --- | --- | --- |
| `work/hns-rs` | `b66470a6a07f0211e3e7fa9aef7d034c8486e75b` | unpublished Denuo V2 marketplace protocol, price/session records, listings, and HNS HTLC primitives |
| `work/hns-node-rs` | `96570aa2d0841c5244e464ef46b609e2f6b0a672` | disabled-by-default confirmed wallet indexes, twelve-call typed backend, and five-role bounded relay policy core |
| `work/hns-dane-engine` | `6ed28559cd32163e3995a944010152d92eabe184` | exact-origin provider-injection decision without wallet or marketplace logic |
| `work/hns-wallet-rs` | `8aa82dd990d41732874f566a256348b1c325e2a1` | eleven-crate encrypted wallet/provider/Shakedex/Kyoto/ETH/settlement foundation |
| `work/hns-dane-browser-mobile` | `58996db0facef1bb6a7cb2876361d13dabc90c75` | deliberately inactive Android/iOS provider, secure-key-wrapper, and UI-state source adapters |
| `work/hns-dane-browser-extension` | `2300ef82a765a6dbd1b99ad537d3d3c2ac312d95` | fail-closed provider bridge, approval/event UI, and no-key demonstration dapp |

The full `./scripts/check.sh` gates passed for `hns-rs`, `hns-node-rs`,
`hns-dane-engine`, `hns-wallet-rs`, and mobile. Chromium's source/Rust,
release, fuzz, audit, and exporter stages passed before a documentation-only
permission-justification amendment; the affected final
`npm run check:extension` then passed 113 tests plus lint/build. No redundant
7.4 GiB Rust rebuild was performed, so this is staged evidence rather than a
claim that one final-commit full-script invocation exited zero. Swift/Xcode,
installed-browser, signed-device, real-chain settlement, sustained fuzz,
resource benchmark, and independent security gates remain open.

Compatible schemas do not create a runtime join. Denuo V2 is unpublished;
the node does not advertise it; the wallet does not have complete registered
chain-module implementations; Chromium returns `walletUnavailable`; mobile
adapters are hardwired unavailable; and HNS/BTC and HNS/ETH remain disabled.
No commit in this checkpoint was pushed, tagged, published, or used with live
mainnet funds. Exact commands and limitations are in
`WALLET_MARKETPLACE_IMPLEMENTATION.md`.

## Earlier checkpoint ledger

Last audited canonical `hns-rs` main:
`f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`

All 14 allowlisted `hns-rs` crates at `0.1.0` are published and non-yanked.
Their Cargo VCS metadata identifies
`0ea5994c336642ea7d01c51c0e22df2008985426` as the release source. Annotated
local and `origin` `v0.1.0` tag object
`354b286ff623424d24376f20885fb05407561d70` dereferences to the follow-up
publication-record commit `f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`,
whose parent is that embedded release source.

Implemented and locally committed there:

- semantic primitives and canonical bounded encoding;
- headers, PoW, targets, chainwork, retargeting, networks, genesis;
- transactions, witnesses, addresses, coins, all covenant encodings/linkage;
- HSD sighash and lock predicates;
- HIP-0001/Shakedex v2 fixed and reverse-Dutch proof primitives;
- standard packet assignments/framing and strict core packet codecs;
- HSD-compatible Urkel proof parsing/verification;
- Denuo Experimental Registry v1 and collision-scoped negotiation;
- exported canonical registry identity/limits and typed Hello/Ack APIs bound to
  the generated TOML/binary/SHA artifacts;
- draft HIP 76, 77, and 78 protocol/cryptographic records;
- HSD-compatible script execution/mining coverage; and
- independent consent for default-on/opt-out opaque relaying, explicit-opt-in
  output-node operation, and independently revocable requester/client
  operation.

Verified checkpoint gates:

- `cargo test --workspace`
- `cargo clippy --workspace --all-targets -- -D warnings`
- `cargo build --workspace --release`

The organization migration changed the Denuo Experimental Registry fingerprint
to
`95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d`
because its canonical encoded source URLs now name `handshake-rs/hns-rs`.
Assignments, payload bounds, meanings, and consent defaults did not change.

Uncommitted work is not counted as a checkpoint until it passes its
repository-specific gate.

The automatic ICANN DANE, full-host dual-root, and typed transport-policy
browser checkpoint is committed and pushed across its shared and
platform-specific boundaries:

- shared DANE engine:
  `2850ac1f50e361e2772e18f2e5ecbd7e77085afb` (policy implementation
  `ab3543ba9b80d23f9fe5a25abf44abd7496a41a2`, standalone dependency
  checkpoint `2850ac1f50e361e2772e18f2e5ecbd7e77085afb`);
- Android/iOS browser:
  `7b826166a2bac3af8d2384dbff9875a992f252ca` (dual-root adapter implementation
  `f25d5fd6dff33a46d5ebd11f73f7f99ec2e3b0b0`, qualified-engine pin
  follow-up `7b826166a2bac3af8d2384dbff9875a992f252ca`); and
- Chromium extension/native host:
  `1fde772006dde8b36c963b3ecc09cc011c542155` (dual-root adapter implementation
  `124190f01c587bce2792a456cb40aab7d0247dfe`, qualified-engine pin
  follow-up `1fde772006dde8b36c963b3ecc09cc011c542155`).

Every canonical DNS host is resolved independently through complete HNS and
ICANN plans. The shared contract reports HNS-only, ICANN-only, convergent,
divergent, neither, or indeterminate state; applies exact pin, successful
persistent binding, then ICANN first-use precedence; retains both roots'
evidence; and derives connection/cache identity without consulting an IANA
suffix list. The selected immutable plan alone supplies endpoints, service
parameters, transport, TLSA owner, trust decision, trace attribution, and cache
partition.

Every DNS-named ICANN HTTPS/WSS request derives its transport-aware TLSA owner.
Secure TLSA presence enforces DANE; authenticated denial or a proven insecure
delegation permits the defined WebPKI fallback; bogus, indeterminate,
malformed, or failed DNSSEC resolution fails closed. HNS address presence
without required TLSA is a root failure, never namespace absence. The shared
decision reaches navigation, redirects, subresources, supported Service Worker
requests, downloads, and WebSockets through each browser's whole-request Rust
proxy boundary.

The browser consumers pin the exact canonical engine Git revision. Their
lockfiles, exact-source policy tests, notices, and `cargo-deny` policies now
bind three shared contracts: `hns-icann-dane`,
`hns-namespace-resolution`, and `hns-resolution-policy`. Both products map the
existing relay-requester control explicitly (`false` to `Disabled`, `true` to
direct-first `Auto`) while disabling every unsupported ODoH, HNSR, provider,
market, output, and legacy role. Direct authoritative UDP/TCP therefore
precedes authenticated authoritative DoH and any admitted P2P relay. The
generic shared policy retains independent default-on/opt-out opaque relaying
and explicit-opt-in output-node operation; browser requester consent does not
grant either provider role.

The browser products intentionally do not inherit the generic node requester
default. A new or persisted browser profile starts with requester relay
false/off and requires explicit user opt-in; false maps to `Disabled`, true
maps to direct-first `Auto`, browser P2P `VERSION` services remain zero, and
all provider/output roles remain disabled.

Current full-workspace tests, warning-denied all-target Clippy, and formatting
pass in both products. Mobile additionally passes seven exact-source policy
tests and 201 focused runtime/resolver tests. Chromium passes 23
source-policy/path tests, its supply-chain gate, 233 focused
runtime/resolver/native-host tests, and all 15 extension tests with a packaged
desktop notice. Separate non-local clones pass locked offline metadata and the
same 201/233 focused tests without a coordination-workspace dependency.
Exact evidence is recorded in
`evidence/browser-engine-consolidation-audit-2026-07-26.md`.

The complete engine graph is now independently cloneable. Its seven deeper
consumer manifests inherit 24 declarations for nine direct canonical
`hns-rs` packages at
`dde2da81f29df935f043978a6d517c1d60ceff31`; the lockfile adds only
`hns-mining` and `hns-transaction` to that exact Git closure. Twelve
source-policy tests, `cargo-deny`, all required 144-test workspace forms, 20
doc-test targets, strict Clippy, release build, formatting, and the C11 header
smoke pass locally and after one verified fetch in a depth-one isolated clone
with no sibling `hns-rs`. Exact evidence is in
`evidence/hns-dane-engine-standalone-checkpoint-2026-07-26.md`.

The two pin-only consumer commits change no runtime source. Mobile passed its
seven source-policy tests, notice/digest checks, locked metadata for both
manifests, and 302 focused offline tests. Chromium passed nine source-policy
tests, the supply-chain and notice gates, 233 focused Rust tests, strict
Clippy/formatting, and its lint, 15-test, and extension-build gate.

Installed-browser, Android SDK/device, Xcode/iOS device, and rebuilt
store-screenshot matrices remain release gates. The initial complete-host
checkpoint remains in
`evidence/browser-dual-root-checkpoint-2026-07-25.md`; the earlier automatic
ICANN milestone remains historical evidence in
`evidence/browser-icann-dane-checkpoint-2026-07-25.md`.

The mobile migration follow-up at
`cb6a5a31c4477fa32bc4d11bd2d935cb3e0c8aa4` reconciles its supply-chain
script with that exact engine pin. Nineteen policy/classifier tests and the
real supply-chain gate pass while alternate URLs, packages, locations,
unpinned sources, and mismatched revisions remain rejected. The later
migration head
`90df79f445f90633cc46a64ce5475bde9879a58b` deterministically regenerates the
third-party notice asset for the same two allowlisted Git crates and their
canonical MIT/Apache license files; notice `--check` passes.
Mobile platform hardening commit
`271044d759b9df3963a934a19cacd47fa8fada12` then binds Android WebView,
Service Worker, download, and security-display WebPKI fallback to a consistent
nested ICANN selection retained by Rust.
Missing, malformed, legacy-top-level, HNS-selected, or contradictory traces
fail closed on both Android and iOS. Android's synthetic WebView asset origin
is local only for canonical HTTPS `/assets/` URLs; alternate schemes, ports,
paths, workers, and downloads cannot escape into DNS or the network proxy.
Runtime/platform boundaries, supply-chain policy, deterministic notices,
version consistency, 20 policy/routing tests, formatting, and focused Rust
namespace-plan tests pass locally. The immediate full-scope hosted run passed
Rust and iOS plus Android assembly/unit tests before Android lint exposed the
two untranslated legacy diagnostics. The final hosted run for that
pre-transport-policy head,
[`CI run 30191799526`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30191799526)
then passed its correctly selected Android assembly, unit, lint, and
release-bundle gates. Installed and signed-device qualification remains a
separate release gate.
CI repair commit `dc3e22483e160d17a75dec39396ede5704d9a06b`
also invalidates queued navigation whenever immutable proxy policy changes,
repairs the standalone snapshot tool lock for the transitive exact engine
revision, and extends the narrow Git-source policy regression suite. The
updated tool lock passes locked offline check, Clippy, tests, `cargo-deny`, and
deterministic-notice regeneration. The pre-transport-policy migration head
`05248d69f52b1963c4b775184fc7b3098fcdcffb` marks both the intentionally
technical unsupported-legacy-HNS-DoH protocol label and its matching
remediation text non-translatable, consistent with the adjacent legacy source
label. XML and the complete 20-locale resource matrix validate without any
missing translatable key.

The standalone node canonical main is
`0e69319d11ca98d788466ed5028d8d897685e9f1`. Its historical live-Denuo
checkpoint is `b2c375e37cac6cfa7a09cfa61113de52ac4f93a1`, layered on the
extraction and qualification implementation checkpoint
`d97aab205ef640008bd61d1b17ba3ef91ee2ac10` and retaining exact 126-commit
subtree provenance from MeshMine. MeshMine implementation checkpoint
`bc9cc70de22e455545d44453cec0d6f07ebeaabe` contains the external-node
adoption and immutable canonical dependency checkpoint
`ca64fc70ca00475318053bf4a4de763d6200f3d6` plus the portable-CI correction.
The 2026-07-28 documentation reconciliation head
`93681bf85b61bcc031ad928321b1bcdb94dfc4bd` additionally marks the embedded
HSRD tree as archival and reconciles the exact standalone-node boundary. The
implementation checkpoint names authenticated Urkel/state record paths, groups node
compaction/commit context, and corrects test scoping so the warning-denied
portable HSRD workspace passes without lint suppression. Focused gates pass 19
Urkel, 46 state, and 116 node tests. The exact local all-features gate was
interrupted after 20 minutes in the known bundled-RocksDB compile; the hosted
CI counterpart completed successfully for that exact implementation head in
[`run 30189487369`](https://github.com/handshake-rs/MeshMine/actions/runs/30189487369).
Details are recorded in
`evidence/standalone-node-checkpoint-2026-07-25.md`.

The later standalone release-qualification implementation head is
`42c76a622f2600a833835b4ca737d3350f73af52`; documentation reconciliation head
`eba0237dedcbc958a8bc09dd811a4a9eeaa9afe7` preserves its claim boundaries.
Every
`RpcConsensusReadiness` field is true there, including the retained historical
replay and independently generated invalid corpus. That is functional source
readiness. `NodeService` initializes its base snapshot with `release_stage:
pre-authority`, but live native RPC replaces that field with
`native-sync-live-p2p`, `mining-engine-observe`, or
`mainnet-canary-gated` according to the active configuration. Those are
diagnostic mode labels, not authority. A mainnet process receives a private
mining permit only when its explicit hardened canary configuration, best
header/active-state synchronization, durable validation/undo state, and
authoritative tip all pass at runtime.

MeshMine still pins standalone node revision
`504d3fed035feb8a637ca09c4e0816b6e1144622`. That revision already has the
promoted functional readiness and conditional canary authority path, but it
predates the later canonical Denuo negotiation and live HIP-76 commits.
MeshMine therefore exposes no substitute relay/provider policy and must
deliberately advance and requalify its immutable pin before claiming those
standalone features.

The historical live-registry checkpoint pins
`hns-p2p-experimental` at exact revision
`5f56e5d381338314e4d7cf1f9e08da7c76d1cf6f`, advertises only ordinary network
plus the extension-envelope service, and exchanges the canonical fingerprint
only after ordinary peer readiness. Exact `0xf4` dispatch is bounded before
generic unknown-packet decoding; mismatch, replay, timeout, malformed input,
and repeated oversize traffic disable only Denuo while ordinary P2P remains
Ready. API-v12 status and native-sync diagnostics expose the same canonical
identity, service mask, live phases, admitted/received/agreement totals, and
fixed rejection taxonomy. Thirty-eight P2P tests, eight RPC tests, 117
no-default-feature node target tests, focused post-hardening status tests,
warning-denied Clippy, formatting, and diff checks pass. Two-full-node and live
Brontide negotiation matrices remain unrun. Exact evidence is in
`evidence/denuo-live-negotiation-checkpoint-2026-07-26.md`.

The role-safe HIP-76 live-session checkpoint pins canonical `hns-rs`
`dde2da81f29df935f043978a6d517c1d60ceff31`. Node implementation commit
`5a35ab9d84da26ce20b8f343efde31e77d6fc898` wires bounded `0xf0`/`0xf1`
sessions into the live manager, and final main
`0e69319d11ca98d788466ed5028d8d897685e9f1` adds a live requester opt-out
regression. Requesting defaults to `Auto` with independent opt-out; operating
a plaintext DNS output remains disabled until the operator opts in and a
backend is ready. Mainnet/testnet plaintext peers are rejected, while Brontide
binds peer provenance to the authenticated remote static key.

Two live regtest TCP peer managers using the explicit plaintext development
transport negotiate the registry and complete a strict, correlated
request/provider-work/response exchange without leaking private frames into
generic packet delivery. The returned DNS bytes remain explicitly untrusted,
ordinary `GetAddr` traffic continues after the exchange and after requester
opt-out, and provider readiness never implies DNSSEC authenticity. The final
portable gates pass 63 P2P, 8 RPC, and 109 no-default-feature node tests plus
warning-denied Clippy, formatting, and diff checks. A
default-feature target was stopped during the known bundled-RocksDB C++
compile and is not counted as passing. A production recursive and
DNSSEC-validating provider backend, durable operator-policy restart, and
two-full-node topology remain open. Exact evidence is in
`evidence/hip76-live-session-checkpoint-2026-07-26.md`.

The DANE operator/data-plane auxiliaries are also migrated independently:

- `hns-dane-crawler` main
  `74546c7e6b0b8a764525a77177a88dc333bf64d8` produces observational
  topology/evidence/report artifacts only; 140 tests, Ruff, shell syntax,
  Node syntax, and dependency checks pass.
- `hns-dane-bootstrap-generator` main
  `f745f122243e5304e6a7ea0e111d47c61d22005e` produces operator-reviewed
  delegation, DNSSEC/DS, DoH, TLSA, and appliance material; 34 web tests, the
  appliance suite, the production build, and a reproducible `npm ci` pass.

All eight product repositories now have their audited checkpoints on canonical
`handshake-rs` `main` branches. The existing `ecosystem` history was preserved
and merged with this audit, and both the ecosystem README and organization
profile now publish the repository/authority map. No package, store binary,
production service, or mainnet state was published or mutated.

## 2026-07-26 browser authority-runtime successor

The browser authority and observability successor advances the shared engine
to `a03648ec85a115362ebc2ab24bb9ea0f1be127fc`. Both browser products now pin
five canonical contracts at that exact Git revision:

- `hns-browser-runtime`;
- `hns-browser-observability`;
- `hns-icann-dane`;
- `hns-namespace-resolution`; and
- `hns-resolution-policy`.

Mobile authority adoption is committed at
`00cb9f3e1fdd59bbb3b3f5c8ef371d0f5fecf875`; final mobile main is
`140bb77e7b3b363747225b03de705d849768f122`, whose follow-up corrects only the
requester/output consent documentation. Chromium authority adoption is
committed at `a9a7a046c8a8404af5088dd13522bea632126511`; its final
Chromium-only source boundary is
`d6071a5cf969cc5b796b034d460d46ffbfb0a521`.

The canonical runtime now issues the checked session, runtime generation,
policy generation, event sequence, and authority state used to admit work.
Each adapter obtains one stamp before namespace or DNS work, retains that
exact request-local snapshot through routing and origin I/O, and requires it
again for response, download, local-error, or `101` publication. Revocation,
degradation, policy change, stop, and restart permanently invalidate earlier
work; later recovery cannot create an ABA publication path.

The canonical observability contract emits name-free schema-v2 authority and
security status from the same retained decision. Chromium's native boundary
serializes that contract as schema v3 for the extension. The production
Chromium regression carries a real strict-`Neither` request through the
loopback backend, metadata observer, native serializer, and the extension's
actual JavaScript validator. Typed DANE association failure survives the
HTTP/1.1, controlled HTTP/1.1, HTTP/2, HTTP/3, Upgrade, and WebSocket paths;
unrelated TLS, QUIC, framing, I/O, or SNI evidence cannot fabricate it.

Full-host dual-root resolution remains authoritative for every canonical DNS
HTTP(S)/WS(S) request. ICANN-selected HTTPS/WSS derives the TLSA owner from the
effective host, port, and service transport; TCP uses `_tcp`, while QUIC/UDP
uses `_udp`. Secure TLSA enforces DANE, authenticated denial or a proven
insecure delegation permits the defined WebPKI fallback, and bogus or
indeterminate DNSSEC fails closed with validating-ICANN-DoH provenance.

Chromium's final source-boundary commit removes the 255 tracked Android/iOS,
FFI, store, branding, and mobile automation paths previously retained from
the shared historical repository. Every selected path was present in the
canonical mobile repository before deletion: 163 were byte-identical, 92 had
since diverged, and none was missing. Git history and the canonical mobile
repository retain the removed source.

Portable workspace tests, warning-denied Clippy, formatting, exact-source,
lock, notice, runtime-boundary, version, native-host, and extension checks are
retained in
`evidence/browser-authority-runtime-checkpoint-2026-07-26.md`. No hosted
workflow was polled or counted as passing for this successor. Installed
Chromium variants, Android/iOS SDK and signed-device matrices, packet-capture
resolver proof, artifact signing/provenance, and the PDF's full topology
qualification remain open release gates.

## 2026-07-27 ecosystem software-gate audit

All nine requested working repositories were reconciled against the PDF's
package and evidence requirements. Existing complete gates passed for the
DANE engine and Chromium extension. The exact MeshMine remote head audited on
July 27 had a successful scheduled hosted workflow. No implementation changes
were needed in those three repositories.

Bounded release-engineering gaps were closed locally in the remaining
repositories:

- the organization profile now verifies a canonical checksum/dimension
  inventory for every published image and has an immutable-action CI gate;
- the bootstrap generator has a clean dependency audit, repaired lockfile, one
  complete check command, and immutable-action CI;
- mobile has all five missing diagnostic resources in every one of 20 locales,
  plus a format-token-safe completeness gate wired into change classification
  and CI;
- the crawler has an exact development lock, clean-environment install gate,
  and immutable-action CI;
- canonical `hns-rs` has a locked production-parser fuzz graph, root/fuzz
  source/license/advisory gates, deterministic parser smoke, a complete check
  command, CI, and RustSec;
- the standalone node has a repaired canonical fuzz lock, root/fuzz
  source/license/advisory gates, a complete check command, CI, RustSec, and a
  two-release-process regtest gate that directly passes matrix rows 1–3; and
- this evidence repository now enforces its required documents, exact 26-row
  matrix, nine-repository checkpoint inventory, and relative-link integrity.

The detailed commands, package results, local/hosted distinction, and read-only
`gh` run audit are retained in
`evidence/software-gate-audit-2026-07-27.md`.

At the close of that July 27 audit, these changes were committed only in the
local working repositories. The PDF forbade pushes, releases, upstream
comments, and publication during that audit, so its newly added workflows did
not yet have protected hosted results. Portable software
and local two-process success also do not satisfy full block synchronization,
production provider/public-service, wallet/market, installed-browser,
signed-device, ASIC, signing/provenance, or independent-review gates. Release
readiness therefore remains **NO**.

## 2026-07-28 browser maintenance and release successor

The browser products advanced after the July 27 software-gate audit.

Mobile implementation commit
`14edcaf5f1039e7fd2e6d99c178de927ede5d1b0` moves network I/O, quorum
collection, snapshot preparation, and peer merging into a private staged
database. Header, peer, and readiness generations publish atomically after
baseline, chain, proof-of-work, chainwork, and canonical-suffix checks.
Unchanged-header peer refreshes do not invalidate admitted requests; process-
wide publication locks, crash-state tokens, conditional deltas, stale-stage
reclamation, and bounded SQLite contention keep concurrent runtimes fail
closed. Exact-head CI run
[`30323566765`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30323566765)
passed. Store-link checkpoint
`153db0306836007b08a9d3bc47c16041b04418d6` then added the live
[Google Play](https://play.google.com/store/apps/details?id=com.denuoweb.hnsdane)
and
[App Store](https://apps.apple.com/us/app/hns-dane-browser/id6791914326)
links; its documentation-only required-CI run
[`30393560141`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30393560141)
passed change classification and repository policy while correctly skipping
unchanged product gates. The July 28 documentation reconciliation head
`21719bb9cbe972e11ba1ad285707e6cfa0d629c1` updates release, store,
qualification, and staged-maintenance guidance without changing product code.

Chromium release/runtime commit
`43819ee3a87e8e400d3b8f3202647f0d4ccc04d8` applies the same staged-chain
model and adds explicit connection/control generations around PAC, native-host
replacement, status adoption, alarms, and header maintenance. The extension
keeps either its live mandatory PAC or a confirmed fixed blocking PAC through
replacement; transient due-but-unexpired synchronization failures retain the
live proxy, while authenticated evidence expiry still blocks. The release also
publishes version-matched graphical Setup applications and native hosts for
Linux, macOS, and Windows on x64 and arm64.

Chromium release-hardening head
`be27931c88929e1e0e7d1504687a5a49a5e86bc3` adds the default-branch Apple
release-replacement workflow and its protected credential-bearing signing
jobs, PKCS#12 normalization, exact certificate fingerprint/SHA-1 identity
selection, concurrent notarization, conservative queue polling, retained
failure evidence, and post-replacement digest checks. The final write-enabled
publisher uses a separate `release` environment that currently has no
environment approval or branch protection rules.
Exact-head CI run
[`30350645836`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30350645836)
passed. Workflow run
[`30350653092`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30350653092)
validated the immutable v0.5.4 source/release, ran the protected signing jobs
for both macOS architectures, stapled Setup, and replaced and reverified the
nine affected
[v0.5.4 release](https://github.com/handshake-rs/hns-dane-browser-extension/releases/tag/v0.5.4)
assets. Windows artifacts remain explicitly unsigned.
The July 28 documentation reconciliation head
`9109dc4a9115a8fde8c3026700a104ebf8cdb164` records those release and
environment-protection boundaries without changing the packaged runtime.

These are real product and release advances, but they do not demonstrate an
installed Chromium catalog/browser matrix, Android/iOS signed-device behavior,
packet-capture proof that no public recursive resolver is contacted, or the
remaining node, wallet, market, ASIC, and multi-operator topology. Ecosystem
release readiness remains **NO**.

## 2026-07-29 non-mobile publication and release reconciliation

The first dependency-publication stage is complete: every one of the 14
allowlisted `hns-rs` `0.1.0` packages is published and non-yanked. Each package
embeds source commit
`0ea5994c336642ea7d01c51c0e22df2008985426`; documentation head
`f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0` records that result. Annotated
local and `origin` `v0.1.0` tag object
`354b286ff623424d24376f20885fb05407561d70` dereferences to that record rather
than its parent release-source commit.

The engine has not advanced remotely or published crates. Remote `main`
remains `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`; the local
release-preparation series ending at
`1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75` is explicitly unpublished and
remains unpushed.

Chromium v0.5.5 is public from source/tag
`86b18497285753944ec1b9196ec05ee359c6db11`. Its 29 release assets include
Developer ID-signed and Apple-notarized macOS artifacts; Windows artifacts
remain unsigned. Documentation head
`3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` passed
[CI run `30439859541`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30439859541).

MeshMine documentation head
`9f781a00ee8fc3b7c6773538434235a65f167ca3` passed all three jobs in
[CI run `30440116148`](https://github.com/handshake-rs/MeshMine/actions/runs/30440116148).
This documentation-only successor does not change its immutable external-node
pin.

The bootstrap generator now has hosted evidence, but it is failing evidence:
[CI run `30401402868`](https://github.com/handshake-rs/hns-dane-bootstrap-generator/actions/runs/30401402868)
stopped at `npm ci` because `@emnapi/runtime@1.11.3` is missing from
`package-lock.json`. It must not be described as having no hosted run or as a
passing current hosted gate.

The exact checkpoint and claim boundaries are retained in
`evidence/non-mobile-publication-release-checkpoint-2026-07-29.md`. Mobile is
intentionally excluded from that checkpoint and reconciled separately below.

## 2026-07-29 mobile v0.5.5 release reconciliation

Mobile Android 0.5.5 version code 46 was built from
`d24f85158854abb8be4a7bb9e914aebe5e7e4679`, signed, structurally verified,
and uploaded directly to the Google Play production track. Play edit
`17438779769069438085` completed and generated APKs for version code 46 are
available. The signed APK SHA-256 is
`b36a4346ffcba14c081500ef3dc7c5012cabd30f42cdaa80a354eefb5da210ba`;
the uploaded AAB SHA-256 is
`728d8892e180d954652668a4e53a7e2d6c7542e9d36330f4803cdecdb34598b0`.

iOS 0.5.5 build 57 uses source and annotated tag
`d926561091634cd69fc9b7e79a4b76003fa4ee47`. Exact-source Apple
[CI run `30454904736`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30454904736)
passed. The four live `1284 × 2778` App Store screenshots from
[run `30454926117`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30454926117)
passed provenance, semantic, and visual validation. Build `57` is `VALID` and
its direct App Review submission is `WAITING_FOR_REVIEW` after protected upload
run `30456522039`. This is a direct App Review path configured for manual store
release, with no
TestFlight build distribution or beta group.

Public GitHub Release
[`v0.5.5`](https://github.com/handshake-rs/hns-dane-browser-mobile/releases/tag/v0.5.5)
retains the verified code 46 APK and build 57 App Store IPA.

Exact artifact and claim boundaries are retained in
`evidence/mobile-v0.5.5-release-checkpoint-2026-07-29.md`. Store build,
signing, screenshot, and publication evidence does not substitute for the
installed signed-device matrix. Qualification row 22 remains `PARTIAL`, and
ecosystem release readiness remains **NO**.
