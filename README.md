<p align="center">
  <img src="https://raw.githubusercontent.com/handshake-rs/.github/main/profile/assets/handshake-rs-logo-v1.png" alt="handshake-rs" width="100%">
</p>

<h1 align="center">Handshake Rust Ecosystem</h1>

This repository coordinates architecture, source auditing, integration testing,
qualification, and releases across the `handshake-rs` organization. Product
source code remains in independently versioned repositories.

## Planned work repositories

- `hns-rs`
- `hns-node-rs`
- `MeshMine`
- `hns-dane-engine`
- `hns-dane-browser-mobile`
- `hns-dane-browser-extension`

Repository transfers and creation are intentionally deferred until ownership,
licensing, history, and release boundaries have been reviewed.

## Workspace model

The reproducible local workspace separates maintained work from external
reference material:

```text
hns-rust-ecosystem-YYYY-MM-DD/
├── work/
├── references/
├── source-audit/
└── integration/
```

External implementations are references, not implicitly maintained forks. Each
reference must eventually be pinned by upstream URL and commit, with its license
and audit purpose recorded.

See:

- [Repository map](docs/REPOSITORY-MAP.md)
- [Reference policy](references/README.md)
- [Source-audit workspace](source-audit/README.md)
- [Integration workspace](integration/README.md)
