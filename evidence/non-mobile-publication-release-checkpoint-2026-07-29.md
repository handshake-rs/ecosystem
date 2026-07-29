# Non-mobile publication and release checkpoint — 2026-07-29

Status: verified registry, source, release, and hosted-CI facts; mobile is
intentionally excluded and has a separate successor checkpoint

## Exact checkpoints

| Repository | Public or remote checkpoint | Follow-up checkpoint | Verified state |
| --- | --- | --- | --- |
| `work/hns-rs` | published source `0ea5994c336642ea7d01c51c0e22df2008985426` | documentation head `f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0` | all 14 allowlisted `0.1.0` crates are published and non-yanked; every package embeds the published source in Cargo VCS metadata; no local or remote `v0.1.0` Git tag exists |
| `work/hns-dane-engine` | remote `main` `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5` | local release-preparation head `1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75` | the local three-commit release-preparation series is unpublished and intentionally remains unpushed |
| `work/hns-dane-browser-extension` | public source and tag `v0.5.5` at `86b18497285753944ec1b9196ec05ee359c6db11` | documentation head `3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` | [CI run `30439859541`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30439859541) passed; the public release has 29 assets, signed and notarized macOS artifacts, and explicitly unsigned Windows artifacts |
| `work/MeshMine` | unchanged implementation and immutable external-node boundary | documentation head `9f781a00ee8fc3b7c6773538434235a65f167ca3` | [CI run `30440116148`](https://github.com/handshake-rs/MeshMine/actions/runs/30440116148) passed its `rustsec`, `verify`, and `hsrd-verify` jobs |
| `work/hns-dane-bootstrap-generator` | remote `main` `ff1c709c8584b13bc02654d19ebc00d09025f4c7` | [CI run `30401402868`](https://github.com/handshake-rs/hns-dane-bootstrap-generator/actions/runs/30401402868) | hosted CI exists but failed in `npm ci`: `package-lock.json` lacks `@emnapi/runtime@1.11.3`; no later generator gate is counted as passing |

## Published `hns-rs` packages

The non-yanked `0.1.0` package set is:

1. `hns-encoding`
2. `hns-primitives`
3. `hns-covenants`
4. `hns-dns-relay-protocol`
5. `hns-header-consensus`
6. `hns-hnsr-protocol`
7. `hns-odoh-protocol`
8. `hns-p2p-experimental`
9. `hns-urkel-proof`
10. `hns-transaction`
11. `hns-script`
12. `hns-mining`
13. `hns-swap`
14. `hns-p2p-wire`

Registry publication does not imply a Git tag. Until a reviewed `v0.1.0` tag
is created and pushed, provenance must identify
`0ea5994c336642ea7d01c51c0e22df2008985426` as the release source.

## Claim boundary

The engine release-preparation work is local evidence only: it is neither the
remote canonical head nor a crates.io release. The generator's hosted run is a
recorded failure, not a passing qualification result. The extension release
and the two successful documentation-head workflows do not complete installed
browser, device, topology, or independent-review qualification.

Mobile was intentionally excluded from this non-mobile checkpoint. Its source,
store, and release evidence is reconciled in the successor below.

Successor: [`mobile-v0.5.5-release-checkpoint-2026-07-29.md`](mobile-v0.5.5-release-checkpoint-2026-07-29.md)
records the Android 0.5.5 production deployment and the independently
versioned iOS 0.5.5 release path.
