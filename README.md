<p align="center">
  <img src="https://raw.githubusercontent.com/handshake-rs/.github/main/profile/assets/handshake-rs-logo-v1.png" alt="handshake-rs" width="100%">
</p>

<h1 align="center">Handshake Rust Ecosystem</h1>

This repository coordinates architecture, source auditing, integration
testing, qualification, migration, and releases across the
[`handshake-rs`](https://github.com/handshake-rs) organization. Product source
code remains in independently versioned repositories. This is not a Rust
workspace, monorepo, umbrella binary, or combined ecosystem package.

## Canonical product repositories

| Repository | Boundary |
| --- | --- |
| [`hns-rs`](https://github.com/handshake-rs/hns-rs) | Canonical runtime-independent protocol, consensus, wire, proof, registry, and consent types |
| [`hns-node-rs`](https://github.com/handshake-rs/hns-node-rs) | Standalone node runtime, storage, P2P, synchronization, mining, and RPC |
| [`hns-wallet-rs`](https://github.com/handshake-rs/hns-wallet-rs) | Unpublished production-completion source for the encrypted Handshake-first wallet, Provider API core, Shakedex/market workflows, Kyoto Bitcoin boundary, and offline native-ETH/Helios containment; browser product and value paths remain disabled |
| [`MeshMine`](https://github.com/handshake-rs/MeshMine) | Mining overlay and application consuming the external node boundary |
| [`hns-dane-engine`](https://github.com/handshake-rs/hns-dane-engine) | Canonical DNSSEC, TLSA/DANE, resolver, transport, dual-root and transport/role policy, browser authority lifecycle, and security observability crates |
| [`hns-dane-browser-mobile`](https://github.com/handshake-rs/hns-dane-browser-mobile) | Android/iOS lifecycle, UI, proxy integration, app-store packaging, and canonical-engine adapters |
| [`hns-dane-browser-extension`](https://github.com/handshake-rs/hns-dane-browser-extension) | Chromium extension, PAC/proxy integration, native host, cross-platform Setup, release signing, and canonical-engine adapters |
| [`hns-dane-crawler`](https://github.com/handshake-rs/hns-dane-crawler) | Observational HNS topology, stored DNS evidence, DANE-readiness queues, static reports, and optional live-directory output |
| [`hns-dane-bootstrap-generator`](https://github.com/handshake-rs/hns-dane-bootstrap-generator) | Operator-facing HNS/ICANN delegation, DNSSEC/DS, authoritative DoH, and TLSA record/deployment generation |

These nine products, this `ecosystem` coordination repository, and the
organization `.github` profile are eleven independent repositories. None is a
monorepo subpackage or a fork of another ecosystem product.

`hns-wallet-rs` has an independent Git history and release boundary. Its
canonical `origin` is now `https://github.com/handshake-rs/hns-wallet-rs.git`,
and remote `main` is recorded in the current checkpoint below. No wallet crate
or signed browser ABI artifact has been published merely because the source is
now hosted by the organization.

## Current remote-main checkpoint (2026-08-10)

This is the authoritative current-head summary. Older dated ledgers remain as
evidence, but any statement in them that these heads are local-only, unpushed,
or the current revision is superseded by this section and
[`REFERENCE_COMMITS.md`](REFERENCE_COMMITS.md).

| Repository | Current source head | Exact-head evidence at this checkpoint |
| --- | --- | --- |
| `hns-rs` | remote `main` `a93ba7a806a921a8ce2d13d9c5fc041ff0ecf6e7` | Exact-head CI passed in run `31372546141`; source predecessor `b33b346780c8f6a9bb18a54390019486cdab0221` passed the full hosted protocol qualification and RustSec in run `31369025777`. The source includes HNSA named routes, bounded HNSR circuit/runtime work, HNS chat, marketplace, name, and fee-policy primitives. Version `0.2.0` is still unpublished. |
| `hns-dane-engine` | remote `main` `84005f1df21a30ea9dda7fafb95f9488b8f5da4b` | Exact-head hosted CI and CodeQL passed (`31372280327`, `31372280387`). The preceding HNSA implementation at `3c12ace6daddd0ba555c242b1d893e047827e679` also passed local locked workspace tests, strict Clippy, and release build. No engine crates are published. |
| `hns-wallet-rs` | remote `main` `4cd9a61a8520c4d3bddd15b3fffcad0d02aafd36` | Hosted run `31372389330` failed strict Clippy in HNS workflows after the earlier ceiling-division correction; a successor fix is in progress. RustSec passed at the predecessor. The source has persistent control, HNS account/read composition, name and Shakedex workflows, and encrypted BDK persistence, but no released native browser binding. |
| `hns-node-rs` | remote `main` `063ba6b82b4b34ea0e56992aa0c0d48855e03e71` | Exact-head hosted CI and container runs are pending. Focused Rust 1.97.1 strict Clippy passed for `hns-store` at this head using the mandated prebuilt RocksDB, superseding the `6e3f7a4` hosted Clippy failure. The source is the unpublished `0.3.5` candidate and pins canonical `hns-rs` `b33b346`. |
| `hns-dane-browser-mobile` | remote `main` `e8d6a0baede5e34cfcf0568ffd2187cfd0456815` | Exact-head documentation/policy CI passed in run `31371872754`; the source-equivalent predecessor `85647ae7467daffdc9c80ff91a339a72a2744e98` passed full Android/iOS CI. Its Android debug APK was installed and cold-launched, which qualifies the browser scaffold only. |
| `hns-dane-browser-extension` | remote `main` `bfa089992b427d6b090989b6289dc68ef1e74fee` | Exact-head CI and CodeQL are green; source-equivalent predecessor `08ba480fcbae4144a329c90e478ccae4bcab5000` passed the full hosted gate. A local Chromium installation does not yet supply an exact-artifact wallet/provider end-to-end result. |
| `namehold-wallet` | upstream `main` `e18e38f`; hsrd work branch `pr-21-hsrd` `9d168a6` | The authenticated hsrd/ARM64 work is branch-only and is not reconciled with current upstream `main`; no combined-main or release qualification is claimed. |

The status words are intentionally independent:

- **implemented** means source exists at the cited head;
- **exact-head tested** means a stated gate ran against that exact revision;
- **product-wired** means a shipping browser invokes the wallet/engine through
  its production binding, not merely that schemas and screen enums exist;
- **value-enabled** means spend or marketplace execution gates are enabled;
- **artifact-published** means a versioned registry, GitHub, or store artifact
  exists for that source; and
- **installed-qualified** means that exact artifact passed the stated
  installed-browser or device scenario.

Under those definitions, the mobile and extension sources are **implemented**
browser scaffolds and their engine consolidation is tested at the revisions
stated above. They are not yet **product-wired** to `hns-wallet-rs` or the
engine's new HNSA/HNSR authority path, their wallet/value/market release gates
remain false, no wallet ABI artifact is published, and no installed wallet or
P2P-marketplace flow is qualified. Older public browser/store releases and the
installed Android debug browser do not upgrade those wallet-specific states.

The dependency direction and authority boundaries are recorded in
[`CROSS_PROJECT_RECONCILIATION.md`](CROSS_PROJECT_RECONCILIATION.md).
The browser-to-engine and MeshMine-to-node boundaries are implemented at the
current audited checkpoints. The node now pins canonical `hns-rs` registry
and HIP-76 types, negotiates that exact fingerprint on live peers, and carries
a bounded role-safe HIP-76 requester/output session. Production recursion,
DNSSEC validation, and DANE remain separate resolver boundaries and are not
claimed by the node transport. The engine's complete Cargo graph now pins the
canonical `hns-rs` protocol packages and builds without a sibling workspace.
The standalone node's functional consensus-readiness fields are all true. Its
base snapshot initializes `release_stage` as `pre-authority`, while live
native RPC replaces that value with a configuration-specific diagnostic stage
such as `native-sync-live-p2p`, `mining-engine-observe`, or
`mainnet-canary-gated`. None of those labels grants authority: mainnet mining
still requires the explicit synchronized canary plus a coherent durable
authoritative tip. MeshMine pins node revision
`504d3fed035feb8a637ca09c4e0816b6e1144622`, so its bridge does not yet
consume the later standalone Denuo/HIP-76 session commits.
Browser consumers pin the qualified engine's DANE via ICANN DoH,
complete-host dual-root, direct-first typed transport policy, canonical
authority lifecycle, and schema-v2 observability crates. Their existing relay
controls map only requester consent; browser provider roles stay disabled.
Platform proxy/resolver migration and installed-device qualification remain
tracked work.
The mobile and Chromium runtimes now stage header synchronization away from
live request admission and publish validated header/peer/readiness state
atomically. Chromium additionally keeps a mandatory PAC under explicit
connection/control generations during native-host replacement and transient
header maintenance, while evidence expiry remains independently fail closed.
The crawler may hand an observed
remediation queue to the bootstrap generator, but neither repository is
browser trust authority and no browser request depends on crawler availability
or generated cached evidence.

In the generic node/runtime policy, the consent boundary is role- and
protocol-specific: opaque P2P relay capacity is default-on with an opt-out
policy, every output role—including a HIP-76 provider—requires an explicit
opt-in, HIP-76 requester selection is automatic with an independent opt-out,
and HNSR client/endpoint participation remains independently opt-in. Live
requester revocation is tested; durable node-policy persistence and reload
remain tracked work.
The browser products intentionally apply a stricter product default: a new or
persisted requester switch starts false/off and requires explicit user opt-in.
False maps to `Disabled`, true maps to direct-first `Auto`; the browser P2P
`VERSION` service mask and every provider/output role remain zero.

## Superseded continuation narrative

The paragraphs in this section preserve the earlier production-continuation
audit. They are not the current-head ledger; use the 2026-08-10 checkpoint
above for repository location, push, test, and release status.

The ecosystem is still implementation-in-progress and is not release-ready as
a whole. Current source heads add self-contained canonical HSD fee policy,
Shakedex name transitions, and complete deterministic listing/cancellation and
recovery-FINALIZE vectors (`hns-rs` `4b989aab`), plus snapshot-bound fee
quotes and the v0.3.4 node/resolver sidecar and release-CI corrections
(`hns-node-rs` `3d346e3d`), private ABI v2, dedicated Bitcoin swap derivation,
provider hardening, exact quote adoption, explicit fail-closed Shakedex
V2/Denuo/value gates, an encrypted bounded `HnsName` scan tied to the ordinary
scan's exact chain/mempool snapshot, authoritative-account CAS hardening, and
receive-only Ethereum containment (`hns-wallet-rs` `4935e059`), retained
provider authority across unrelated engine work (`hns-dane-engine`
`6eb0174a`). The wallet now gives every private result, prompt, and event one
authority-handle/revision, wallet-session, and permission-generation binding;
its typed private capability snapshot carries provider/approval schema versions,
wallet session, permission generation, and a runtime-supported subset of the
canonical 43 methods. Fresh generation zero is distinct from a retained nonzero
revocation tombstone. A fail-closed caller host now owns private negotiation,
correlation, approval/authority transitions, and event replay, while checked-in
machine contracts describe private/public/manifest shapes without supplying
artifact trust. `hns_requestAccounts` remains unavailable. Chromium
`972e63a1` and mobile `4b684ebb` accept generation zero only in that never-
authorized private capability input while keeping the public website
`wallet_getCapabilities` result to `{providerApiVersion,methods}`. Chromium
retains exact session/generation matching, while mobile permission-bearing
event payloads remain positive. Both adapters remain
unwired: Chromium's artifact/transport/runtime/authority/provider/value gates
and mobile's four release gates are false, and mobile's unavailable adapter is
hardwired without controller, wallet runtime/FFI, generated binding, approval
UI, or event producer. All three local heads are unpushed and received source/
static review only; their added tests remain unrun and no earlier PASS transfers.
HNS value remains gated on a released canonical
`hns-script` 0.2 fee-algebra helper; the new name scan is source-only key
discovery, not ownership proof, and names remain watch-only. Ethereum
synchronization, history, send, authoritative evidence, settlement, and
mainnet remain disabled or unavailable. Browser provider and bilateral
settlement paths are likewise unavailable. Start with:

- [`INTEGRATION_STATE.md`](INTEGRATION_STATE.md) — committed checkpoints and
  demonstrated gates;
- [`REFERENCE_COMMITS.md`](REFERENCE_COMMITS.md) — exact local and upstream
  revisions;
- [`QUALIFICATION_MATRIX.md`](QUALIFICATION_MATRIX.md) — the retained 26-row
  browser/node topology plus the 12-row wallet/marketplace supplement;
- [`REMAINING_GAPS.md`](REMAINING_GAPS.md) — explicit release blockers;
- [`DEPENDENCY_PUBLICATION.md`](DEPENDENCY_PUBLICATION.md) — crate and
  cross-repository publication policy;
- [`GITHUB_ORGANIZATION_MIGRATION.md`](GITHUB_ORGANIZATION_MIGRATION.md) —
  repository ownership and migration record;
- [`NEXT_MILESTONE_AUDIT.md`](NEXT_MILESTONE_AUDIT.md) — completed node
  checkpoints, completed browser-policy, standalone-engine, and canonical
  authority/observability slices, plus the next bounded consolidation
  milestone;
- [`WALLET_MARKETPLACE_AUDIT.md`](WALLET_MARKETPLACE_AUDIT.md) — wallet,
  Provider API, Shakedex, Denuo, Kyoto, Ethereum, and browser seam audit;
- [`WALLET_MARKETPLACE_IMPLEMENTATION.md`](WALLET_MARKETPLACE_IMPLEMENTATION.md)
  — exact delivered status, qualification evidence, limitations, and
  revisions; and
- [`PRODUCTION_COMPLETION_PLAN.md`](PRODUCTION_COMPLETION_PLAN.md) — ordered
  production tranches, completion evidence, and non-redundant NVMe-only build
  policy; and
- [`evidence/`](evidence/) — retained checkpoint command evidence, including
  the
  [`2026-07-27 software-gate audit`](evidence/software-gate-audit-2026-07-27.md)
  and the
  [`2026-07-28 browser maintenance/release successor`](evidence/browser-maintenance-release-successor-2026-07-28.md),
  followed by the
  [`2026-07-29 non-mobile publication/release checkpoint`](evidence/non-mobile-publication-release-checkpoint-2026-07-29.md)
  and the
  [`2026-07-29 mobile v0.5.5 release checkpoint`](evidence/mobile-v0.5.5-release-checkpoint-2026-07-29.md).

Primitive tests and portable builds do not make unrun full-node, wallet,
marketplace, signed-device, installed-browser, performance, or mainnet rows
pass.

Individual product publication is not ecosystem qualification. All 14
`hns-rs` `0.1.0` crates are published and non-yanked from embedded source
`0ea5994c336642ea7d01c51c0e22df2008985426`. Annotated local and `origin`
`v0.1.0` tag object `354b286ff623424d24376f20885fb05407561d70`
dereferences to the follow-up publication-record commit
`f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`, whose parent is that embedded
release source.
Chromium v0.5.5 is public from source/tag
`86b18497285753944ec1b9196ec05ee359c6db11` with 29 assets: macOS is signed
and notarized, while Windows remains unsigned. Mobile Android 0.5.5 version
code 46 is deployed to Google Play production from source
`d24f85158854abb8be4a7bb9e914aebe5e7e4679`. The iOS 0.5.5 build 57 source
and `v0.5.5` tag are
`d926561091634cd69fc9b7e79a4b76003fa4ee47`; exact Apple CI and live
App Store screenshots pass, while build `57` is `VALID` and its direct App
Review submission is `WAITING_FOR_REVIEW` after protected upload run
`30456522039`. The iOS path is direct
App Review with manual release and no TestFlight distribution. Public mobile
GitHub Release `v0.5.5` retains the verified code 46 APK and build 57 App Store
IPA. These product releases do not upgrade the unrun installed-browser,
signed-device, resolver-contact, or full-topology rows.

Canonical engine remote-tracking `main` remains
`7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`; older local release-preparation
head `1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75` precedes latest local source head
`6eb0174ae743e6bd01c516be7a534d94be94b4bd`. The latest local head is
unqualified, unpublished, and unpushed. MeshMine `main` is
`79f3bbc6c24bab80adaef199a9318fd0065113f6`; its immutable node consumer pin is
unchanged and still predates the current node.
The bootstrap generator does have a hosted run, but
[`30401402868`](https://github.com/handshake-rs/hns-dane-bootstrap-generator/actions/runs/30401402868)
failed at `npm ci` because `@emnapi/runtime@1.11.3` is missing from its lockfile.

Some repositories do not yet have a finalized top-level license. Public source
availability alone does not grant additional rights; consult each repository's
license and notices before reuse.

## Reproducible workspace model

The audit workspace separates maintained work from external reference material:

```text
hns-rust-ecosystem-YYYY-MM-DD/
├── work/          # one independent Git repository per maintained project
├── references/    # pinned read-only upstream implementations
├── SOURCE_AUDIT.md # supplied artifact inventory and provenance
└── integration/   # this repository's coordination/evidence source
```

External implementations are references, not implicitly maintained forks.
Each reference is pinned by upstream URL and commit, with its license and audit
purpose recorded.

Canonical source governance lives in `handshake-rs`. Denuo Web LLC may
separately publish and sign browser, MeshMine, crawler-service, or
bootstrap-appliance artifacts; signing identity does not change the canonical
source repository or review boundary.

> This is an independent project and does not claim to be the official
> Handshake organization.
