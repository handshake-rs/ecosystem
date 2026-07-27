# Software gate audit — 2026-07-27

## Scope and claim boundary

This audit reconciles the nine working repositories against
`Complete Rust Handshake Ecosystem.pdf`. It executes every portable gate
available on this host, repairs bounded software/CI gaps, and records hosted
GitHub Actions state with read-only `gh` commands.

The audited input is a 57-page PDF with SHA-256
`51dc7363ecc7c597c11de531fbeb1f45f3c6997a4d7b2c5065cd4be9681e7868`.

It does **not** convert primitive, unit, build, or workflow success into a
topology `PASS`. The PDF's public multi-operator deployment, full block-sync
and production recursive/DNSSEC backend, wallet/market, installed Chromium,
Android/iOS SDK and signed-device, ASIC, artifact-signing, and
independent-audit requirements remain external gates. Nothing was pushed,
published, released, or submitted upstream.

## Portable package results

| Repository | Local result | Gate or repair |
| --- | --- | --- |
| `work/handshake-rs-profile` | PASS | Added canonical SHA-256 inventory and PNG dimension/reference validation for all four profile assets; added pinned CI. |
| `work/hns-dane-bootstrap-generator` | PASS | `npm audit` is clean after lock-only `nanoid`/`postcss` remediation; locked install, typecheck, 36 tests, appliance suite, and production build pass; added pinned CI. |
| `work/hns-dane-browser-extension` | PASS | Existing complete gate passes supply-chain, exact-source, notices, versions, runtime boundaries, locked Rust tests/Clippy/release build, ABI/fuzz/deny/tool checks, 75 Node tests, and 19 packaging/workflow tests. |
| `work/hns-dane-browser-mobile` | PASS (portable) | Added all five missing resources to every one of 20 locales and an XML/format-token completeness checker. Complete Rust/ABI/fuzz/deny/tool gate, 14 classifier tests, translation checker, and XML parse pass. Android Gradle lint is not locally executable because the configured SDK path does not exist; installed/signed-device gates remain open. |
| `work/hns-dane-crawler` | PASS | Added an exact development lock and pinned CI. A fresh virtual environment passes exact install, `pip check`, Ruff, all 140 tests, and the fixture/export/validation/archive pipeline. |
| `work/hns-dane-engine` | PASS | Existing complete gate passes 12 source-policy tests, `cargo-deny`, default/all-feature tests and docs, strict Clippy, release build, and C11 ABI smoke. |
| `work/hns-node-rs` | PASS | Repaired the stale fuzz lock and added source/license/advisory policy, a complete root/fuzz check script, pinned CI, RustSec, and a two-process regtest gate. Root/fuzz deny/audit, strict all-feature Clippy/tests, no-default tests, release all-target build, and the full-node topology gate pass. |
| `work/hns-rs` | PASS | Added a locked fuzz graph, source/license/advisory policy, deterministic parser smoke, complete check script, pinned CI, and RustSec. Root/fuzz metadata, deny/audit, formatting, fuzz build, strict all-feature Clippy/tests, no-default tests, and release build pass. |
| `work/MeshMine` | PASS (hosted exact head) | No source repair was needed. The current exact-head scheduled CI passed its Rust, differential, regtest-driver, performance, embedded-HSRD, fuzz, and RustSec jobs. A redundant local RocksDB rebuild was not substituted for this exact-head hosted result. |

The relevant local commands were:

```text
./scripts/check.sh
python3 scripts/verify_android_translations.py
python3 -m unittest -v tests/test_ci_changed_targets.py
python3 -m pytest -q
python3 -m ruff check .
npm ci
npm audit
cargo +1.89.0 deny --locked check
cargo +1.89.0 audit
cargo +1.89.0 clippy --locked --workspace --all-targets --all-features -- -D warnings
cargo +1.89.0 test --locked --workspace --all-targets --all-features
cargo +1.89.0 test --locked --workspace --all-targets --no-default-features
cargo +1.89.0 build --locked --release --workspace --all-targets --all-features
```

Each repository was also checked with `git diff --check`. New workflows use
immutable action revisions, read-only contents permission, concurrency
cancellation, bounded job timeouts, locked installers, and explicit toolchain
versions.

The node's complete all-feature test profile finished successfully after its
native build, including 116 node, 63 P2P, 58 store, 47 state, 30 sync, 20
chain, and 8 RPC tests plus all remaining workspace/bin/example targets. The
isolated no-default profile then passed 109 node, 63 P2P, 53 store, 46 state,
30 sync, 20 chain, and 8 RPC tests plus the remaining targets. The optimized
all-target/all-feature release build completed in 44 minutes 56 seconds.

The release binary then produced this two-process regtest evidence:

```json
{
  "node_a": {
    "bytes_received": 393,
    "bytes_sent": 393,
    "denuo_phase": "negotiated",
    "peer_count": 1,
    "peer_state": "ready",
    "registry_fingerprint": "95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d",
    "registry_negotiated_peers": 1,
    "transport": "plaintext"
  },
  "node_b": {
    "bytes_received": 393,
    "bytes_sent": 393,
    "denuo_phase": "negotiated",
    "peer_count": 1,
    "peer_state": "ready",
    "registry_fingerprint": "95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d",
    "registry_negotiated_peers": 1,
    "transport": "plaintext"
  }
}
```

This directly upgrades qualification rows 1–3. It does not upgrade HIP-76
provider, block synchronization, wallet, market, browser/device, or resolver
contact rows.

## Read-only hosted Actions audit

The following status was queried with `gh run list`, `gh run view`, and
`gh api`:

| Repository | Exact remote head | Hosted evidence |
| --- | --- | --- |
| `hns-dane-browser-extension` | `3d40d164c35e0c462750969f7055d3acdb12398c` | CI run `30259204747`: success |
| `hns-dane-browser-mobile` | `942686612ca2ffcc234834429de5a17f1bf2cf43` | CI run `30234114656`: Android lint failed on five missing translations; Rust and iOS passed. The five resources are repaired locally at `3072c24deef86bc1edd45247ac743251fb3ab598`. |
| `hns-dane-crawler` | `74546c7e6b0b8a764525a77177a88dc333bf64d8` | CI run `30188089994`: success; the dependency-lock/CI hardening is a later local commit. |
| `hns-dane-engine` | `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5` | CI run `30224663683`: success |
| `MeshMine` | `bc9cc70de22e455545d44453cec0d6f07ebeaabe` | Scheduled CI run `30262973337`: success |

At audit start, GitHub reported no hosted workflow definitions for the
profile, bootstrap generator, standalone node, or canonical protocol
repositories. Their new workflows are therefore locally validated
implementation, not hosted results. The evidence repository likewise has no
hosted result for its new structural gate until publication is separately
authorized.

The extension's earlier `v0.5.3` release run failed in historical publish
logic; the current main commit contains the repair and current CI passes.
Release/publish workflows were intentionally not rerun.

## PDF qualification disposition

Rows 1–3 and 20 of the 26-row minimum matrix are topology `PASS`.
Package-level work materially advances prerequisites but cannot demonstrate
wallet/market runtimes that are not present, live public DNS/DANE services,
independent operator separation, production HIP-76 resolution, HIP-77/78
multi-peer paths, installed browsers, signed devices, or absence of recursive
resolver contact. Those rows remain `PARTIAL` or `NOT RUN` in the canonical
matrix.

Release readiness remains **NO** until all mandatory matrix rows have direct
retained execution evidence.
