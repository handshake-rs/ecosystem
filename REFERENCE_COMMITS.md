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
| `work/hns-node-rs` | `42c76a622f2600a833835b4ca737d3350f73af52` | standalone node plus repaired canonical fuzz lock, root/fuzz deny/audit gates, complete CI/RustSec qualification, release build, and two-full-process matching-registry regtest proof |
| `work/hns-dane-engine` | `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5` | standalone exact-revision DNSSEC/DANE graph, canonical browser authority/observability contracts, and recursive-DoH consent binding |
| `work/hns-dane-browser-mobile` | `3072c24deef86bc1edd45247ac743251fb3ab598` | Android/iOS canonical-engine adoption plus complete format-safe diagnostic resources across all 20 localized Android sets and an enforced completeness gate |
| `work/hns-dane-browser-extension` | `3d40d164c35e0c462750969f7055d3acdb12398c` | Chromium canonical-engine/native-host boundary, complete portable/packaging qualification, and corrected draft-release lookup |
| `work/hns-dane-crawler` | `26deeb0a7b451922b6a86130c6c0da6d3cbc945a` | observational authority boundary plus exact development lock, clean-environment qualification, and pinned CI |
| `work/hns-dane-bootstrap-generator` | `225182962dfbc7c738312e50f8e6ea7dcc889844` | operator-review boundary plus clean dependency audit, complete locked qualification command, and pinned CI |
| `work/MeshMine` | `bc9cc70de22e455545d44453cec0d6f07ebeaabe` | standalone Rust node adoption, immutable canonical Git dependency, portable CI correction, and consolidated warning-denied HSRD cleanup |
| `work/handshake-rs-profile` | `0b3b703f31a92e2c2795c64b04b409753fba4e6f` | organization repository/authority graph plus canonical profile-image checksum/dimension inventory and pinned CI |
