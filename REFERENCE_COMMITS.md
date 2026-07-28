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

## Local implementation checkpoints

These commits are canonical source checkpoints on their project `main`
branches, not published package or signed-artifact releases.

| Working repository | Revision | Checkpoint |
| --- | --- | --- |
| `work/hns-rs` | `8c55e8ff1c75c9880dca793a55b02c49d052be87` | canonical protocol/consent checkpoint plus locked production-parser fuzz graph, root/fuzz source/license/advisory gates, deterministic parser smoke, complete check command, CI, and RustSec |
| `work/hns-node-rs` | `eba0237dedcbc958a8bc09dd811a4a9eeaa9afe7` | all-true functional consensus readiness, base `pre-authority` plus mode-specific live release-stage diagnostics, conditional synchronized-canary authority, repaired canonical fuzz lock, complete CI/RustSec qualification, release build, two-full-process matching-registry regtest proof, and current documentation reconciliation |
| `work/hns-dane-engine` | `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5` | standalone exact-revision DNSSEC/DANE graph, canonical browser authority/observability contracts, and recursive-DoH consent binding |
| `work/hns-dane-browser-mobile` | `21719bb9cbe972e11ba1ad285707e6cfa0d629c1` | Android/iOS canonical-engine adoption, atomic staged header maintenance at `14edcaf5f1039e7fd2e6d99c178de927ede5d1b0`, complete localized diagnostics, current Google Play/App Store links, and release-state documentation reconciliation |
| `work/hns-dane-browser-extension` | `9109dc4a9115a8fde8c3026700a104ebf8cdb164` | Chromium canonical-engine/native-host boundary, proxy continuity during staged header maintenance, v0.5.4 cross-platform Setup release, protected Developer ID signing/notarization jobs, default-branch asset replacement, and release-state documentation reconciliation |
| `work/hns-dane-crawler` | `b9e3c406631eb253f26979a0d3d9f794fd9fb11f` | observational authority boundary, exact development lock, clean-environment qualification, pinned CI, and current output/deployment documentation |
| `work/hns-dane-bootstrap-generator` | `ff1c709c8584b13bc02654d19ebc00d09025f4c7` | operator-review boundary, clean dependency audit, complete locked qualification command, pinned CI, and current interface/deployment documentation |
| `work/MeshMine` | `93681bf85b61bcc031ad928321b1bcdb94dfc4bd` | immutable canonical node pin `504d3fed035feb8a637ca09c4e0816b6e1144622`, pre-Denuo/HIP-76 bridge adoption, portable CI correction, consolidated warning-denied HSRD cleanup, and current boundary documentation |
| `work/handshake-rs-profile` | `a87b859e2b1cbd597ff3598862c3d08dd4d1c8c3` | organization repository/authority graph, canonical profile-image checksum/dimension inventory, pinned CI, and current ecosystem profile reconciliation |
