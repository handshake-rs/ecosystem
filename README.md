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
| [`MeshMine`](https://github.com/handshake-rs/MeshMine) | Mining overlay and application consuming the external node boundary |
| [`hns-dane-engine`](https://github.com/handshake-rs/hns-dane-engine) | Canonical DNSSEC, TLSA/DANE, resolver, transport, dual-root and transport/role policy, browser authority lifecycle, and security observability crates |
| [`hns-dane-browser-mobile`](https://github.com/handshake-rs/hns-dane-browser-mobile) | Android/iOS lifecycle, UI, proxy integration, packaging, and canonical-engine adapters |
| [`hns-dane-browser-extension`](https://github.com/handshake-rs/hns-dane-browser-extension) | Chromium extension, PAC/proxy integration, native host, packaging, and canonical-engine adapters |
| [`hns-dane-crawler`](https://github.com/handshake-rs/hns-dane-crawler) | Observational HNS topology, stored DNS evidence, DANE-readiness queues, static reports, and optional live-directory output |
| [`hns-dane-bootstrap-generator`](https://github.com/handshake-rs/hns-dane-bootstrap-generator) | Operator-facing HNS/ICANN delegation, DNSSEC/DS, authoritative DoH, and TLSA record/deployment generation |

These eight products, this `ecosystem` coordination repository, and the
organization `.github` profile are ten independent repositories. None is a
monorepo subpackage or a fork of another ecosystem product.

The dependency direction and authority boundaries are recorded in
[`CROSS_PROJECT_RECONCILIATION.md`](CROSS_PROJECT_RECONCILIATION.md).
The browser-to-engine and MeshMine-to-node boundaries are implemented at the
current audited checkpoints. The node now pins canonical `hns-rs` registry
and HIP-76 types, negotiates that exact fingerprint on live peers, and carries
a bounded role-safe HIP-76 requester/output session. Production recursion,
DNSSEC validation, and DANE remain separate resolver boundaries and are not
claimed by the node transport. The engine's complete Cargo graph now pins the
canonical `hns-rs` protocol packages and builds without a sibling workspace.
Browser consumers pin the qualified engine's DANE via ICANN DoH,
complete-host dual-root, direct-first typed transport policy, canonical
authority lifecycle, and schema-v2 observability crates. Their existing relay
controls map only requester consent; browser provider roles stay disabled.
Platform proxy/resolver migration and installed-device qualification remain
tracked work.
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

## Current audit

The ecosystem is still implementation-in-progress and is not release-ready as
a whole. Start with:

- [`INTEGRATION_STATE.md`](INTEGRATION_STATE.md) — committed checkpoints and
  demonstrated gates;
- [`REFERENCE_COMMITS.md`](REFERENCE_COMMITS.md) — exact local and upstream
  revisions;
- [`QUALIFICATION_MATRIX.md`](QUALIFICATION_MATRIX.md) — the required 26-point
  integration demonstration;
- [`REMAINING_GAPS.md`](REMAINING_GAPS.md) — explicit release blockers;
- [`DEPENDENCY_PUBLICATION.md`](DEPENDENCY_PUBLICATION.md) — crate and
  cross-repository publication policy;
- [`GITHUB_ORGANIZATION_MIGRATION.md`](GITHUB_ORGANIZATION_MIGRATION.md) —
  repository ownership and migration record;
- [`NEXT_MILESTONE_AUDIT.md`](NEXT_MILESTONE_AUDIT.md) — completed node
  checkpoints, completed browser-policy, standalone-engine, and canonical
  authority/observability slices, plus the next bounded consolidation
  milestone; and
- [`evidence/`](evidence/) — retained checkpoint command evidence, including
  the
  [`2026-07-27 software-gate audit`](evidence/software-gate-audit-2026-07-27.md).

Primitive tests and portable builds do not make unrun full-node, wallet,
marketplace, signed-device, installed-browser, performance, or mainnet rows
pass.

Some repositories do not yet have a finalized top-level license. Public source
availability alone does not grant additional rights; consult each repository's
license and notices before reuse.

## Reproducible workspace model

The audit workspace separates maintained work from external reference material:

```text
hns-rust-ecosystem-YYYY-MM-DD/
├── work/          # one independent Git repository per maintained project
├── references/    # pinned read-only upstream implementations
├── source-audit/  # supplied artifact inventory and provenance
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
