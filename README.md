# Handshake Rust ecosystem workspace

Canonical source repositories live under `work/`. Their own manifests, operating
rules, and current documentation define build, runtime, and release behavior.

- `hns-rs`: bounded shared Handshake protocol types and codecs.
- `hns-dane-engine`: platform-neutral browser validation and transport policy.
- `hns-wallet-rs`: encrypted wallet state, chain synchronization, and approvals.
- `hns-dane-browser-mobile`: Android and iOS Shakescape applications.
- `hns-dane-browser-extension`: Chromium extension and native host.
- `hns-node-rs`: standalone consensus, state, synchronization, mining, and relay.
- `MeshMine`: external-node mining and operator composition.
- `hns-dane-bootstrap-generator`: authoritative DNS deployment inputs.
- `hns-dane-crawler`: observational topology and endpoint discovery.
- `namehold-wallet`: desktop wallet.
- `DenuoWebSite` and `shakescape-website`: product websites.
- `handshake-rs-profile`: organization profile and contributor guidance.

Use each project's current release guide to qualify selected packages. Wallet
crates are independently versioned; publish only packages whose source changed
or whose required dependency changes need a new release. Publication requires
explicit authorization.

Node builds on this ARM host must use the prebuilt RocksDB archive and the local
Cargo configuration specified by the workspace instructions. Device diagnostics
are read-only evidence.
