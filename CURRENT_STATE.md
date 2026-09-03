# Ecosystem current state

Snapshot: **2026-09-02**.

This is the current cross-project ledger for source identity, publication, and
product boundaries. Older dated checkpoints and evidence files remain useful
for the exact commits and tests they record, but their candidate versions and
open-gate statements must not be read as present-tense ecosystem status.

## Reviewed source coordinates

| Repository | Reviewed code head | Current version | Current release state |
| --- | --- | --- | --- |
| `hns-rs` | `73611a0d83778e157b35f28ca2197d068e83fc61` | `0.4.1` | 17-crate cohort and `v0.4.1` published |
| `hns-wallet-rs` | `747d550736f10a6b186f0d042b1a53c8bf7a5fba` | `0.2.1` | 14-crate cohort and `v0.2.1` published |
| `hns-node-rs` | `c99dffa9186066ea92aa96ea836fa2d51c2790e1` | `0.3.5` | untagged; `v0.3.4` remains the latest source tag |
| `MeshMine` | `30be371bc6643a358b1ee8c2306378ef4543c4a8` | `0.1.0` | private, non-publishable workspace |
| `hns-dane-engine` | `87d2346c13ade4987801e0f1367bd604fd77c9f0` | root `0.2.2` | exact published component graph spans `0.2.x` and `0.3.0` |
| `hns-dane-browser-mobile` | `7c1e9521fbd6df3c1a29437c6b08e25e13c37e1e` | product `1.0.4`, Rust `1.0.0` | Android code 56 committed to Play production; iOS build 65 waiting for review |
| `hns-dane-browser-extension` | `2b6bf2faf87f7bd14e07db3f21a13423b7d75f39` | `1.0.0` | current extension/Setup source; `v0.5.9` is latest source tag |
| `hns-dane-crawler` | `1a290efa394a2b28e958fb94d556719199bb00dd` | `0.1.0` | untagged `denuo-hns-topology` package candidate |
| `hns-dane-bootstrap-generator` | `65cc8aa1335d7a0e0299c31a96e824a702914869` | `0.2.2` | private application; `v0.2.1` is latest source tag |

Documentation-only successors created by the 2026-09-02 audit do not replace
the code-bearing coordinates above. The organization profile records both
coordinates so a documentation commit is never mistaken for product source.

## Dependency and authority graph

`hns-rs 0.4.1` is the current protocol cohort. `hns-wallet-rs 0.2.1`
consumes that published cohort. The engine and browser products consume exact
published protocol and browser-engine packages; release manifests and
lockfiles, rather than old Git-sibling paths, are the dependency authority.

The architecture remains intentionally one-way:

```text
hns-rs ─┬──> hns-node-rs ──────> MeshMine
        ├──> hns-wallet-rs ─────> Shakescape mobile
        └──> hns-dane-engine ─┬─> Shakescape mobile
                             └─> Shakescape Extension
```

Protocol types do not activate services. Node and relay state do not become
wallet signing authority. Engine APIs do not activate downstream provider or
service roles. Crawler observations and generated DNS records do not become
browser trust evidence.

## Wallet, marketplace, and relay reconciliation

Shakescape mobile `1.0.4` includes the native direct HNS wallet path: wallet
lifecycle, synchronized balance and history, payment and transfer receive
targets, send review/broadcast, tracked names, transfer/finalization, and
closed Shakedex offer exchange. Explicit Shakescape V1 pairing and its
wallet-owned listener are revoked on wallet lock and protected lifecycle exit.
The older scoped-loopback indexed backend remains a compatibility seam rather
than a dependency of the direct wallet.

These native features do not expose a website provider. Active HNSA/HNSR
browser roles and mainnet cross-chain settlement remain disabled, while
physical-iPhone and installed cross-chain-swap qualification remain open.

The Chromium product is separately bounded. It can consume the requester-only
P2P DNS relay after explicit opt-in, but opts out of opaque relay serving and
does not expose wallet, provider, value, market, HNSA/HNSR, or verified
MeshMine-feed authority.

`hns-node-rs` can carry opaque HNSR `0x0004` swap circuits. Enabled relayers
advertise the product profiles the node supports, while requester behavior is
profile-selected. The node does not decode the application payload and does
not thereby acquire discovery, order-book, wallet, approval, funding, or
settlement authority.

## Remaining release and qualification work

- Tag and independently qualify node `0.3.5` before treating it as a release.
- Preserve exact package checksums, VCS provenance, and consumer lock closure
  for the published protocol, wallet, and engine cohorts.
- Complete the remaining signed/installed mobile matrices, especially physical
  iPhone coverage and installed cross-chain swap behavior.
- Keep the website-provider boundary disabled until a product joins a qualified
  wallet service, private transport, engine authority adapter, and trusted
  approval projection.
- Keep HNSA/HNSR product roles disabled until each consumer supplies its own
  authenticated naming, durable authorization, transport, rollback, and
  installed-product evidence.
- Treat crawler, bootstrap, MeshMine, and Namehold releases under their own
  repositories' authority and artifact contracts.

## Reading the older documents

- `evidence/*.md` is immutable, commit-scoped evidence.
- `REFERENCE_COMMITS.md` is a chronological record, not the current ledger.
- Planning, marketplace, source-audit, and qualification documents retain the
  detailed reasoning that led to the current architecture. Their older
  version numbers, heads, and “unavailable” statements are superseded where
  this document or a repository-local current document says otherwise.
- `DUAL_ROOT_NAMESPACE_POLICY.md` and organization-migration records describe
  durable policy/history and remain authoritative within their stated scope.
