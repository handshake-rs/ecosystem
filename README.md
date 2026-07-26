<p align="center">
  <img src="https://raw.githubusercontent.com/handshake-rs/.github/main/profile/assets/handshake-rs-logo-v1.png" alt="handshake-rs" width="100%">
</p>

<h1 align="center">Handshake Rust Ecosystem</h1>

This repository coordinates architecture, source auditing, integration
testing, qualification, migration, and releases across the
[`handshake-rs`](https://github.com/handshake-rs) organization. Product source
code remains in independently versioned repositories. This is not a Rust
workspace, monorepo, umbrella binary, or combined ecosystem package.

## Canonical repositories

| Repository | Boundary |
| --- | --- |
| [`hns-rs`](https://github.com/handshake-rs/hns-rs) | Canonical runtime-independent protocol, consensus, wire, proof, registry, and consent types |
| [`hns-node-rs`](https://github.com/handshake-rs/hns-node-rs) | Standalone node runtime, storage, P2P, synchronization, mining, and RPC |
| [`MeshMine`](https://github.com/handshake-rs/MeshMine) | Mining overlay and application consuming the external node boundary |
| [`hns-dane-engine`](https://github.com/handshake-rs/hns-dane-engine) | Canonical DNSSEC, TLSA/DANE, resolver, transport, and dual-root browser-policy crates |
| [`hns-dane-browser-mobile`](https://github.com/handshake-rs/hns-dane-browser-mobile) | Android/iOS lifecycle, UI, proxy integration, packaging, and shared-policy adapters |
| [`hns-dane-browser-extension`](https://github.com/handshake-rs/hns-dane-browser-extension) | Chromium extension, PAC/proxy integration, native host, packaging, and shared-policy adapters |
| [`hns-dane-crawler`](https://github.com/handshake-rs/hns-dane-crawler) | Observational HNS topology, stored DNS evidence, DANE-readiness queues, static reports, and optional live-directory output |
| [`hns-dane-bootstrap-generator`](https://github.com/handshake-rs/hns-dane-bootstrap-generator) | Operator-facing HNS/ICANN delegation, DNSSEC/DS, authoritative DoH, and TLSA record/deployment generation |

The dependency direction and authority boundaries are recorded in
[`CROSS_PROJECT_RECONCILIATION.md`](CROSS_PROJECT_RECONCILIATION.md).
The browser-to-engine and MeshMine-to-node boundaries are implemented at the
current audited checkpoints. The node now pins canonical `hns-rs` registry
types and negotiates that exact fingerprint on live peers; HIP runtime
adoption remains tracked work. Browser consumers currently pin the engine's
DANE via ICANN DoH and dual-root policy crates; broader resolver/gateway
consolidation remains tracked work. The crawler may hand an observed
remediation queue to the bootstrap generator, but neither repository is
browser trust authority and no browser request depends on crawler availability
or generated cached evidence.

The consent boundary is role- and protocol-specific: opaque P2P relay capacity
is default-on with a persistent opt-out, every output/provider role requires
an explicit opt-in, HIP-76 requester selection is automatic with a persistent
opt-out, and HNSR client/endpoint participation remains independently opt-in.

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
  repository ownership and migration record; and
- [`evidence/`](evidence/) — retained checkpoint command evidence.

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
