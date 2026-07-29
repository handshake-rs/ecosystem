# Reference commits

## Repository snapshots

| Repository | URL | Revision |
| --- | --- | --- |
| HSD | `https://github.com/handshake-org/hsd.git` | `698e252ebc7b5c1dd0a9587e342fdd153d020ae4` |
| Denuo HSD | `https://github.com/denuoweb/hsd.git` | `698e252ebc7b5c1dd0a9587e342fdd153d020ae4` |
| hs-client | `https://github.com/handshake-org/hs-client.git` | `03a243a7fc38e2032950e6bec32d9137d2f74355` |
| HIPs | `https://github.com/handshake-org/HIPs.git` | `06f3226a8bf30b9517fe0f85c951d4a090786cd7` |
| Shakedex | `https://github.com/kurumiimari/shakedex.git` | `ab5687b04cb61d2548937b8cee3c056c1c75bbdc` |
| Bob Wallet | `https://github.com/bob-wallet/bob-wallet.git` | `0432158e5bc55c9d5aa24e0f256e468c44459d15` |
| Handshake docs | `https://github.com/handshake-org/handshake-org.github.io.git` | `b8611a6bd4e9208ec0561f0a5042c6bbc532e3a1` |

## Draft pull-request snapshots

These values identify the fetched head commits used by the independent Rust
implementations. Draft assignments are not official Handshake assignments.

| Draft | Commit |
| --- | --- |
| HIP PR 76 | `25f6d99cdd2b766f9eb6bb3b72d9dc804efd6131` |
| HSD PR 958 | `ea31be1554f3235bfa96bdd394e6d33e7dda8080` |
| HIP PR 77 | `d3ae6be483663ed6cf0ead4f4b4f17a80b1d1162` |
| HSD PR 959 | `909311d97c794eb59ed2eb0b095a122607ae078e` |
| HIP PR 78 | `53b962e901ffa796f4ccf66a5d53956d7421c58c` |
| HSD PR 960 | `2fc40f1c61ff16a2f39d9514cd950d1560430ced` |

The six PR heads are retained under `refs/remotes/origin/pr-*` in their
read-only reference repositories. Temporary fetch worktrees are evidence only
and are never a replacement for those refs.

## Authority order

Consensus behavior follows compatible HSD execution, HSD tests, reproducible
HSD fixtures, compatible protocol documentation, existing Rust differential
tests, and only then architectural inference. Draft behavior follows exact PR
text/commits, deterministic PR fixtures, independent Rust vectors, the Denuo
registry, and documented migration rules.

## Current implementation and release checkpoints

The table distinguishes remote or public source from later documentation
heads. A documentation head does not retag a release, and an unpushed local
head is not a canonical remote checkpoint.

| Working repository | Revision | Checkpoint |
| --- | --- | --- |
| `work/hns-rs` | `f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0` | current documentation head; all 14 non-yanked `0.1.0` crates embed published source `0ea5994c336642ea7d01c51c0e22df2008985426`; no local or remote `v0.1.0` tag exists |
| `work/hns-node-rs` | `eba0237dedcbc958a8bc09dd811a4a9eeaa9afe7` | all-true functional consensus readiness, base `pre-authority` plus mode-specific live release-stage diagnostics, conditional synchronized-canary authority, repaired canonical fuzz lock, complete CI/RustSec qualification, release build, two-full-process matching-registry regtest proof, and current documentation reconciliation |
| `work/hns-dane-engine` | `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5` | current remote `main`; standalone exact-revision DNSSEC/DANE graph, canonical browser authority/observability contracts, and recursive-DoH consent binding; local unpublished release preparation ends at `1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75` and remains unpushed |
| `work/hns-dane-browser-mobile` | Android `d24f85158854abb8be4a7bb9e914aebe5e7e4679`; iOS/tag `d926561091634cd69fc9b7e79a4b76003fa4ee47`; documentation `39ea427b744581ccc9a860f5f51f6fc31622d317` | Android 0.5.5 version code 46 is in Google Play production; iOS 0.5.5 build 57 passed exact Apple CI `30454904736` and live-screenshot run `30454926117`; build 57 is `VALID` and its direct App Review submission is `WAITING_FOR_REVIEW` after protected upload run `30456522039`, with manual release and no TestFlight; documentation CI `30460622706` passed |
| `work/hns-dane-browser-extension` | `3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` | current documentation head with green CI `30439859541`; public v0.5.5 source/tag is `86b18497285753944ec1b9196ec05ee359c6db11`, with 29 assets, signed/notarized macOS artifacts, and unsigned Windows artifacts |
| `work/hns-dane-crawler` | `b9e3c406631eb253f26979a0d3d9f794fd9fb11f` | observational authority boundary, exact development lock, clean-environment qualification, pinned CI, and current output/deployment documentation |
| `work/hns-dane-bootstrap-generator` | `ff1c709c8584b13bc02654d19ebc00d09025f4c7` | operator-review boundary and current documentation; hosted CI `30401402868` exists but fails at `npm ci` because `@emnapi/runtime@1.11.3` is missing from the lockfile |
| `work/MeshMine` | `9f781a00ee8fc3b7c6773538434235a65f167ca3` | current documentation head with green CI `30440116148`; immutable canonical node pin `504d3fed035feb8a637ca09c4e0816b6e1144622` still predates the later standalone Denuo/HIP-76 implementation |
| `work/handshake-rs-profile` | `8da203b1359f4c595e0512b4914d1b4f8d497d69` | organization repository/authority graph, canonical profile-image checksum/dimension inventory, pinned CI, and current mobile-distribution reconciliation; CI `30460714542` passed |
