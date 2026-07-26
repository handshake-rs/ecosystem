# GitHub organization migration evidence

Date: 2026-07-25

Target organization: `handshake-rs`

Status: canonical product source migration complete; organization administration
and signed-release configuration remain open

## Canonical product mains

| Repository | Canonical `main` | Migration |
| --- | --- | --- |
| `handshake-rs/hns-rs` | `8543f317a0ac23e40b6a79ea0cdc957dd01a04d9` | new independent repository |
| `handshake-rs/hns-node-rs` | `504d3fed035feb8a637ca09c4e0816b6e1144622` | new independent repository retaining the documented 126-commit MeshMine subtree extraction |
| `handshake-rs/hns-dane-engine` | `127b9ad55852df00b4df40826517715048dc3571` | new independent repository |
| `handshake-rs/hns-dane-browser-mobile` | `05248d69f52b1963c4b775184fc7b3098fcdcffb` | existing Denuo Web repository transferred and renamed by the user, then fast-forwarded, migrated, given an exact-source CI policy and deterministic notices, hardened so platform WebPKI paths require the retained Rust ICANN decision, supplied a consistent standalone-tool lock, and cleared the complete Android localization matrix |
| `handshake-rs/hns-dane-browser-extension` | `bcf587a6cc06c9c07c1f713eef108d317fcadfc7` | new independent repository retaining common historical browser ancestry and the Chromium-only release boundary |
| `handshake-rs/hns-dane-crawler` | `74546c7e6b0b8a764525a77177a88dc333bf64d8` | existing repository transferred by the user, migrated to canonical source links, and bounded as observational output |
| `handshake-rs/hns-dane-bootstrap-generator` | `f745f122243e5304e6a7ea0e111d47c61d22005e` | existing repository transferred by the user, migrated to canonical source/release URLs, given a reproducible npm lock, and documented with a separate publisher boundary |
| `handshake-rs/MeshMine` | `bc9cc70de22e455545d44453cec0d6f07ebeaabe` | existing repository transferred by the user and fast-forwarded to the audited external-node boundary plus consolidated warning-denied HSRD cleanup |

Each local product `main` was clean and equal to its matching remote-tracking
`origin/main` after push. No product branch was merged into a different
project, no unreviewed mirror push was used, and no canonical product was
created as a GitHub fork.

## Hosted current-main verification

- Chromium extension/native-host main `bcf587a6cc06c9c07c1f713eef108d317fcadfc7`:
  [`CI run 30187225880`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30187225880)
  succeeded.
- Crawler main `74546c7e6b0b8a764525a77177a88dc333bf64d8`:
  [`CI run 30188089994`](https://github.com/handshake-rs/hns-dane-crawler/actions/runs/30188089994)
  succeeded.
- MeshMine main `bc9cc70de22e455545d44453cec0d6f07ebeaabe`:
  [`CI run 30189487369`](https://github.com/handshake-rs/MeshMine/actions/runs/30189487369)
  succeeded.
- Mobile browser main `05248d69f52b1963c4b775184fc7b3098fcdcffb`:
  [`CI run 30191799526`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30191799526)
  succeeded for its Android-only final diff. Its immediate full-scope ancestor
  passed Rust and iOS plus Android assembly/unit tests before the subsequently
  repaired localization-lint finding.

The primitives, standalone-node, engine, bootstrap-generator, ecosystem, and
organization-profile repositories have no checked-in hosted workflows at this
checkpoint; their evidence is local or comes from exact-revision consumer
gates. The bootstrap generator's locked install, tests, appliance suite, and
production build passed locally, and its missing required workflow remains an
explicit release blocker.

## Coordination and organization profile

- Existing `handshake-rs/ecosystem` commit
  `000d0bab5782a6a74a861847cc23121f30ec3db0` and the local audit lineage were
  preserved through merge commit
  `b7a3dabebf3faaa3f83c75fe3e96dd205fef3578`.
- Ecosystem repository map/README commit
  `16b21e4200f3a5f82ffc76871bb026b5ee4c646a` documents every product boundary,
  dependency direction, consent role, source/release distinction, and
  qualification entrypoint.
- Expanded ecosystem map/evidence commit
  `c71f13d9e3851799e913d5dfdd91048398f473ce` adds the transferred crawler and
  bootstrap generator, their optional handoff, current product checkpoints,
  and their remaining release gates.
- Organization profile commit
  `534ffce5093363fd722de4de3d8cba9df47e7efd` publishes the expanded map and
  authority model from `handshake-rs/.github`, including the crawler-to-
  generator operator workflow and verified root-level ecosystem links.

The existing ecosystem ruleset reported that `main` normally must not contain
merge commits. GitHub accepted the user-authorized push through the caller's
ruleset bypass for the single unrelated-history preservation merge. Product
repositories did not receive cross-project merge commits.

## Immutable source boundaries

- Mobile and Chromium both pin `hns-icann-dane` and
  `hns-namespace-resolution` to exact
  `handshake-rs/hns-dane-engine` revision
  `127b9ad55852df00b4df40826517715048dc3571`.
- Both browser lockfiles contain the full Git source and commit, and
  `cargo-deny` rejects unknown Git sources while allowlisting only the
  canonical engine URL.
- MeshMine pins exact `handshake-rs/hns-node-rs` revision
  `504d3fed035feb8a637ca09c4e0816b6e1144622` and its validators reject path,
  embedded, unpinned, or alternate-source fallbacks.
- A clean shallow MeshMine clone resolved that node revision without a sibling
  checkout. The browser post-pin Rust/extension/ABI gates likewise resolved
  the engine through the canonical Git source.
- Crawler and bootstrap-generator package, application, production-clone, and
  release-source links name their matching canonical repositories. Denuo
  authorship, deployment, publishing, and release-signing identity remain a
  separate boundary.

## History and repository boundaries

GitHub transfer was used only where one existing repository had one canonical
successor: MeshMine, the mobile browser, the crawler, and the bootstrap
generator. This preserves their hosted history and old-URL redirects. The
node, engine, primitives, and extension are independent repositories rather
than organization forks.

`hns-node-rs` retains the history-filtered `hsrd/` lineage as provenance; that
lineage was not merged back into MeshMine. The extension retains historical
mobile source directories for traceable ancestry, but its active Cargo
workspace, workflows, README, package metadata, and manifest define only the
Chromium/native-host release. Current Android/iOS authority lives in the one
canonical `hns-dane-browser-mobile` repository.

`handshake-rs/ecosystem` coordinates audits, policies, compatibility, and
evidence. It is not a Rust monorepo, umbrella package, or replacement for any
product repository.

## Publisher and signer boundary

Canonical source governance belongs to `handshake-rs`. Denuo Web LLC may keep
browser-store publisher identities, Apple/Android release credentials,
extension distribution accounts, MeshMine signing keys, crawler deployments,
and bootstrap-generator service/appliance publishing. Those credentials
should be scoped to protected release environments and exact canonical source
tags; publishing or signing an artifact does not change repository authority.

## Open administrative and release work

- Establish least-privilege Owners, Maintainers, Security, and Denuo Web
  Release teams and require organization 2FA.
- Configure organization rulesets for protected `main` and release tags,
  required checks/reviews, stale-approval dismissal, conversation resolution,
  and force-push/deletion restrictions.
- Audit transferred environments, Actions secrets, deploy keys, webhooks,
  releases, packages, Pages, LFS, and old-URL redirects.
- Finalize missing top-level license decisions for `hns-node-rs` and MeshMine;
  public source availability alone grants no additional rights.
- Run fresh installed-browser, Android SDK/device, Xcode/signed-device, node,
  wallet, market, crawler-production, bootstrap-appliance, and full 26-row
  integration qualification before release.

No crate, package, browser/store artifact, production service, or mainnet state
was published or mutated by this migration.
