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
| `handshake-rs/hns-dane-browser-mobile` | `0d069d102c0bf8fe9975798faf6864193fe20bf3` | existing Denuo Web repository transferred and renamed by the user, then fast-forwarded and migrated |
| `handshake-rs/hns-dane-browser-extension` | `bcf587a6cc06c9c07c1f713eef108d317fcadfc7` | new independent repository retaining common historical browser ancestry and the Chromium-only release boundary |
| `handshake-rs/MeshMine` | `a8ce46e276ec27749afe578484e65b3df3546515` | existing repository transferred by the user and fast-forwarded to the audited external-node boundary |

Each local product `main` was clean and equal to its matching remote-tracking
`origin/main` after push. No product branch was merged into a different
project, no unreviewed mirror push was used, and no canonical product was
created as a GitHub fork.

## Coordination and organization profile

- Existing `handshake-rs/ecosystem` commit
  `000d0bab5782a6a74a861847cc23121f30ec3db0` and the local audit lineage were
  preserved through merge commit
  `b7a3dabebf3faaa3f83c75fe3e96dd205fef3578`.
- Ecosystem repository map/README commit
  `16b21e4200f3a5f82ffc76871bb026b5ee4c646a` documents every product boundary,
  dependency direction, consent role, source/release distinction, and
  qualification entrypoint.
- Organization profile commit
  `084fb2f0f120e085a363934d055e46146434c15d` publishes the same map and
  authority model from `handshake-rs/.github`.

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

## History and repository boundaries

GitHub transfer was used only where one existing repository had one canonical
successor: MeshMine and the mobile browser. This preserves their hosted
history and old-URL redirects. The node, engine, primitives, and extension are
independent repositories rather than organization forks.

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
extension distribution accounts, and MeshMine signing keys. Those credentials
should be scoped to protected release environments and exact canonical source
tags; signing an artifact does not change repository authority.

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
  wallet, market, and full 26-row integration qualification before release.

No crate, package, browser/store artifact, production service, or mainnet state
was published or mutated by this migration.
