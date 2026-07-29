# Browser maintenance and release successor — 2026-07-28

Status: source and hosted workflow reconciliation complete; installed-platform
qualification remains open

## Exact source

| Repository | Revision | Role |
| --- | --- | --- |
| `work/hns-dane-browser-mobile` | `21719bb9cbe972e11ba1ad285707e6cfa0d629c1` | July 28 documentation head; store-link checkpoint `153db0306836007b08a9d3bc47c16041b04418d6` follows atomic header-maintenance implementation `14edcaf5f1039e7fd2e6d99c178de927ede5d1b0` |
| `work/hns-dane-browser-extension` | `9109dc4a9115a8fde8c3026700a104ebf8cdb164` | July 28 documentation head; protected signing/notarization jobs and default-branch asset-replacement head `be27931c88929e1e0e7d1504687a5a49a5e86bc3` follows v0.5.4 proxy/header-maintenance source `43819ee3a87e8e400d3b8f3202647f0d4ccc04d8` |

Both repositories continue to pin the five canonical
`handshake-rs/hns-dane-engine` contracts at exact revision
`7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`.

## Runtime successor

Both products stage long-running header synchronization outside live request
admission, validate conditional deltas against immutable baseline state, and
publish header, peer, and readiness generations atomically. Process-wide
publication locks, crash-state tokens, stale-stage reclamation, exact peer
merging, and bounded SQLite contention protect concurrent runtimes.

Chromium additionally owns explicit connection and control generations around
PAC writes, native callbacks, alarms, header maintenance, and host
replacement. It never clears mandatory proxy control to system/direct routing:
replacement first confirms a fixed blocking PAC, disconnects the captured
generation, then publishes the replacement PAC. Due-but-unexpired maintenance
failure keeps the live proxy; authenticated evidence expiry independently
fails closed.

## Hosted evidence

| Evidence | Exact head | Result |
| --- | --- | --- |
| [Mobile CI 30323566765](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30323566765) | `14edcaf5f1039e7fd2e6d99c178de927ede5d1b0` | PASS: implementation CI |
| [Mobile CI 30393560141](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30393560141) | `153db0306836007b08a9d3bc47c16041b04418d6` | PASS: documentation-only change classification/repository policy; product jobs correctly skipped |
| [Chromium CI 30350645836](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30350645836) | `be27931c88929e1e0e7d1504687a5a49a5e86bc3` | PASS: repository/supply-chain, extension, Rust/native-host, and required-CI jobs |
| [macOS replacement 30350653092](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30350653092) | `be27931c88929e1e0e7d1504687a5a49a5e86bc3` | PASS: immutable release validation, tooling validation, x64/arm64 signing and notarization, asset replacement and verification |

The
[Chromium v0.5.4 release](https://github.com/handshake-rs/hns-dane-browser-extension/releases/tag/v0.5.4)
contains the MV3 packages and native-host/Setup archives for Linux, macOS, and
Windows on x64 and arm64. The successor's protected credential-bearing jobs
signed and notarized both macOS architectures. Its default-branch publisher
replaced only the two macOS native-host archives, two macOS Setup archives,
their four sidecar digests, and `SHA256SUMS`. The write-enabled publisher's
separate `release` environment currently has no approval or branch rules.
macOS native hosts and Setup applications are Developer ID signed and
notarized; Setup carries stapled tickets. Windows artifacts remain unsigned.

The mobile repository now links the live
[Google Play listing](https://play.google.com/store/apps/details?id=com.denuoweb.hnsdane)
and
[App Store listing](https://apps.apple.com/us/app/hns-dane-browser/id6791914326).

## Claim boundary

Published packages and successful hosted workflows do not prove behavior after
installation in each supported Chromium catalog/browser, Android/iOS signed
device, or platform network process. They also do not prove resolver-contact
privacy, full ecosystem topology, wallet/market operation, ASIC behavior, or
independent review. Qualification rows 22 and 23 therefore remain `PARTIAL`,
and release readiness remains **NO**.

## 2026-07-29 Chromium successor

The July 28 v0.5.4 evidence above remains the historical predecessor. Public
v0.5.5 source/tag
`86b18497285753944ec1b9196ec05ee359c6db11` supersedes it with 29 release
assets. macOS artifacts are Developer ID signed and Apple notarized; Windows
artifacts remain unsigned. Documentation head
`3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` records that state, and
[CI run `30439859541`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30439859541)
passed all four jobs. The installed-browser and wider qualification boundaries
above remain unchanged.
