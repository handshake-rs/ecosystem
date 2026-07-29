# GitHub organization migration

Status: **canonical source migration complete**; organization teams/rulesets,
remaining signing platforms, and installed-platform qualification remain
separate administrative/release work

Target organization: `handshake-rs`

## Ownership model

The GitHub organization, release publisher, and code-signing identity are
separate authorities:

- `handshake-rs` owns the canonical source repositories and review policy.
- Denuo Web LLC may continue to own browser-store listings, mobile publisher
  accounts, release certificates, MeshMine signing keys, crawler deployments,
  and bootstrap-generator service/appliance publishing.
- A dedicated Denuo Web release team receives only the repository/environment
  permissions needed to build and sign those products.
- Moving a repository does not transfer copyright or trademark ownership.
  Each repository must retain its license, notices, provenance, and explicit
  independent-project disclaimer.

`handshake-rs/ecosystem` remains a coordination, qualification, and evidence
repository. It is not a Rust workspace, umbrella binary, or combined ecosystem
package.

## One repository per working project

| Local project | Canonical GitHub destination | Migration type |
| --- | --- | --- |
| `work/hns-rs` | `handshake-rs/hns-rs` | independent repository; audited `main` pushed |
| `work/hns-node-rs` | `handshake-rs/hns-node-rs` | independent repository with retained extraction history; audited `main` pushed |
| `work/hns-dane-engine` | `handshake-rs/hns-dane-engine` | independent repository; audited `main` pushed |
| `work/hns-dane-browser-mobile` | `handshake-rs/hns-dane-browser-mobile` | user-completed transfer/rename; audited `main` pushed |
| `work/hns-dane-browser-extension` | `handshake-rs/hns-dane-browser-extension` | independent historical split; audited Chromium `main` pushed |
| `work/hns-dane-crawler` | `handshake-rs/hns-dane-crawler` | user-completed transfer; canonical identity and role boundary audited on `main` |
| `work/hns-dane-bootstrap-generator` | `handshake-rs/hns-dane-bootstrap-generator` | user-completed transfer; canonical identity, release URLs, and role boundary audited on `main` |
| `work/MeshMine` | `handshake-rs/MeshMine` | user-completed transfer; audited `main` pushed |
| `integration` | `handshake-rs/ecosystem` | existing coordination history merged with the local audit history and pushed |
| `work/handshake-rs-profile` | `handshake-rs/.github` | organization profile and public repository/authority map pushed |

The workspace represents eight product repositories plus `ecosystem` and
`.github`: ten independent repositories under `handshake-rs`. The product
repositories are not GitHub forks of one another. Each local `origin` names
only its matching canonical repository.

The initial ecosystem map was published at
`16b21e4200f3a5f82ffc76871bb026b5ee4c646a`; its expanded migration/evidence
update is `c71f13d9e3851799e913d5dfdd91048398f473ce`. The organization profile,
including the observational crawler, operator generator, and
source-versus-release boundary, was corrected at
`534ffce5093363fd722de4de3d8cba9df47e7efd`. A later intermediate
organization-profile checkpoint is
`864357ba3badd2b5baf45a0791f9d7d4781da021`, adding the exact
`hns-rs`-to-node relationship, live HIP-76 trust/consent boundary, shared
mobile/Chromium whole-request policy, and the durable-policy limitation. The
next organization-profile checkpoint,
`e6739420fa5152d0907bfe9690318a4b6d740079`, records the exact
`hns-rs`-to-engine dependency and standalone engine boundary. The next
organization-profile checkpoint,
`4fbfbc2df1c9d67ae0b7dff434b9e31a0ccc29d8`, publishes the complete
repository/authority graph, five browser-engine contracts, crawler/generator
handoff boundary, role-specific consent, and source-versus-signing ownership.
The next organization-profile checkpoint,
`fcbeae9874c4eaa62ce5fc52d4cbc499dae94be1`, makes the browser-specific
requester opt-in exception explicit. Organization-profile implementation
checkpoint `0b3b703f31a92e2c2795c64b04b409753fba4e6f` adds the
checksum/dimension inventory and immutable-action asset gate; documentation
reconciliation head `a87b859e2b1cbd597ff3598862c3d08dd4d1c8c3` records the
current repository and distribution boundaries. The current
ecosystem coordination checkpoint before this documentation reconciliation is
`cba166bd8ab7049a1972d6821b0cafe084c50746`; current product and
coordination revisions are maintained in `REFERENCE_COMMITS.md`.

## Transfer, import, and fork policy

A local `git clone` is not automatically a GitHub fork. Pushing that history to
a newly created organization repository produces an independent repository
unless the destination was explicitly created through GitHub's fork workflow.

Use a GitHub repository transfer when one existing repository maps to one
canonical destination. The user completed that operation for
`denuoweb/MeshMine`, `Denuo-Web/hns-dane-browser`,
`denuoweb/HNScrawler`, and
`denuoweb/hns-dane-bootstrap-generator`; none is a fork. A transfer preserves
Git history, issues, pull requests, releases, settings, stars/watchers,
secrets, deploy keys, webhooks, and its fork network, while old repository and
Git URLs redirect.

Create independent repositories for the three new Rust workspaces because
they have no upstream GitHub repository. `hns-node-rs` retains its documented
history-preserving extraction from MeshMine without making the new node a
MeshMine fork.

The two browser worktrees descend from the same historical
`Denuo-Web/hns-dane-browser` repository but now have distinct package and
release boundaries. The transferred repository is the canonical
`hns-dane-browser-mobile` repository. The extension is an independent
repository that retains the common ancestry and exact source checkpoint; it is
not a GitHub fork of mobile. Its historical Android/iOS source, FFI, store, and
packaging trees were removed only after comparison with the canonical mobile
repository and in a separate reviewed commit. No history was rewritten merely
to make the products look separate.

Forks are appropriate only for contributing back to external reference
projects such as HSD or HIPs. They are not appropriate for the canonical
`work/*` projects: a fork remains in the upstream repository network, shares
visibility constraints, and can inherit root-network push rules.

## Branch and merge policy

Repositories do not need every historical, release, extraction, or abandoned
branch merged into `main` before migration:

- a GitHub transfer moves every branch and tag as-is;
- a new repository may receive an explicitly selected audited `main` without
  importing unrelated local branches or duplicated legacy release tags;
- no branch from one working repository is ever merged into another
  repository's `main`; and
- only reviewed, qualified milestones should reach each repository's protected
  `main` before its first release.

The user explicitly directed the current audited updates to project-local
`main`. The new Rust repositories published their exact clean checkpoints.
Mobile and Chromium local `main` branches were fast-forwarded to their reviewed
feature checkpoints before their canonical migration commits; MeshMine's
reviewed checkpoint was likewise promoted only inside MeshMine. The
history-filtered node extraction remains in `hns-node-rs` and was not merged
back into MeshMine.

Never use a working clone's unreviewed `git push --mirror` as the migration
mechanism. Push an explicit audited set of branches and tags. A temporary bare
mirror or `git bundle --all` may be used for backup and object verification.

## Completion record and administrative follow-up

Completed in this source migration:

- every milestone included in this source-migration/browser-authority
  checkpoint was committed, qualified proportionately, promoted to its
  project-local `main`, and pushed explicitly;
- transferred repositories were reused instead of recreated;
- new destinations were initialized without unrelated generated source
  commits;
- Cargo repository identities, immutable cross-repository pins, lockfiles,
  source links, mobile release commands, and browser-extension metadata were
  migrated;
- crawler and bootstrap-generator source/release links now name their
  canonical repositories, while preserving their separate observational and
  operator-control boundaries;
- the unrelated existing `ecosystem` history was merged, not discarded; and
- the organization and ecosystem READMEs now describe repository authority,
  dependencies, consent roles, release ownership, and remaining gates.

Organization administrators still need to inventory and configure teams, 2FA,
rulesets, protected release tags, environments, Actions secrets, deploy keys,
webhooks, Pages, packages, LFS, security contacts, and Denuo Web release-team
access. Before a signed release, verify fresh-clone builds, remote tags,
artifacts, SBOM/provenance, and old-URL redirects. Never recreate a repository
at a transferred old path because doing so destroys GitHub's redirect.

## Cross-repository Rust dependencies

The browser migrations replaced coordination-root path dependencies with exact
`handshake-rs/hns-dane-engine` revision
`7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`. Both now consume
`hns-browser-runtime`, `hns-browser-observability`, `hns-icann-dane`,
`hns-namespace-resolution`, and `hns-resolution-policy`;
their lockfiles record the complete Git source and their exact-source policies
and `cargo-deny` configurations allowlist only the canonical engine URL.
The mobile and Chromium platform-owned runtimes were first separated from the
canonical package name at `5ef5cb9ec66ea460b4168946a7d2d0bba7c2f141`
and `0334126fa4f5a6d5ae14d15b2584b64e0c8985b3`, respectively. The final
consumer heads and their exact source, lock, notice, authority, stale-work,
and focused product gates are recorded in `REFERENCE_COMMITS.md` and
`INTEGRATION_STATE.md`. MeshMine uses the same immutable-boundary rule for
exact
`handshake-rs/hns-node-rs` revision
`504d3fed035feb8a637ca09c4e0816b6e1144622`.

`hns-node-rs` now follows the same rule for exact
`handshake-rs/hns-rs` revision
`dde2da81f29df935f043978a6d517c1d60ceff31`. Lockfiles and SBOM/provenance
evidence must identify the same immutable source revision in every consumer.
The complete engine graph now follows that rule too: nine direct and two
transitive `hns-rs` packages resolve from the one exact canonical revision,
with no coordination-workspace sibling dependency.

Do not copy shared crates into browser or node repositories to avoid this
dependency boundary.

## Denuo Web release boundary

Denuo Web LLC can remain the named publisher and signer even though source
lives under `handshake-rs`. Signing keys should be environment-scoped,
unavailable to ordinary pull requests, and usable only by the Denuo Web Release
team after protected-tag approval. Store listings should link to the canonical
`handshake-rs` source and the exact signed source tag.

That separation is now exercised for the public Chromium v0.5.5 release.
Canonical source/tag `86b18497285753944ec1b9196ec05ee359c6db11` and release
automation live under `handshake-rs`; the 29-asset release contains
Developer ID-signed and Apple-notarized macOS artifacts. Windows artifacts
remain unsigned. Documentation head
`3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` passed exact-head CI
`30439859541`. This proves a bounded source/signing path, not
organization-wide credential governance or installed-browser qualification.

The MeshMine transfer is complete, but its visibility, licensing, and any
affected protected-branch or Pages behavior still require a release audit.
GitHub Packages likewise require a registry-specific ownership/link audit.

## Source-migration acceptance

- every local project maps to exactly one canonical repository;
- each audited project-local `main` has the exact expected remote object ID;
- no uncommitted or untracked source was omitted from the promoted
  checkpoints;
- repository-local source, lock, policy, and portable qualification checks
  pass for each promoted checkpoint;
- dependency metadata names immutable canonical sources;
- no reference-project fork is mistaken for a canonical implementation; and
- every write stays within the user-authorized migration: project-local audited
  mains, the ecosystem coordination history, and the organization profile
  README.

## Open administrative and release acceptance

- configure organization teams, 2FA, repository rulesets, protected release
  tags, and environment-scoped release credentials;
- protect and default-branch-restrict the Chromium write-enabled `release`
  environment, then generalize the bounded model without granting
  organization-wide owner access;
- verify transferred old-URL redirects and any changed Pages, package, webhook,
  deploy-key, or Actions behavior;
- run fresh standalone release-checkout gates and installed/signed platform
  matrices; and
- make every release artifact identify its exact canonical source tag, SBOM,
  provenance, checksums, publisher, and rollback path.

## GitHub references

- <https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository>
- <https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository>
- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks>
- <https://docs.github.com/en/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization>
