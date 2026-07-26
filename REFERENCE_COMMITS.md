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
| `work/hns-rs` | `dde2da81f29df935f043978a6d517c1d60ceff31` | canonical protocol/consent checkpoint plus direction-safe HIP-76 requester/output policy APIs, exported registry identity, typed negotiation, exact bounds, and artifact-bound fingerprint |
| `work/hns-node-rs` | `0e69319d11ca98d788466ed5028d8d897685e9f1` | history-preserving standalone extraction plus exact-revision live Denuo negotiation, bounded role-safe HIP-76 sessions, API-v13 qname-free diagnostics, and portable qualification |
| `work/hns-dane-engine` | `a03648ec85a115362ebc2ab24bb9ea0f1be127fc` | standalone exact-revision DNSSEC/DANE and dual-root graph plus the canonical schema-v2 browser authority lifecycle, checked runtime session/generation/event admission, typed ICANN failure semantics, and security observability contract |
| `work/hns-dane-browser-mobile` | `140bb77e7b3b363747225b03de705d849768f122` | Android/iOS five-contract canonical authority/observability adoption, exact engine pin, stale-work and status enforcement, complete portable qualification, and corrected requester/output consent documentation |
| `work/hns-dane-browser-extension` | `d6071a5cf969cc5b796b034d460d46ffbfb0a521` | Chromium five-contract canonical authority/observability adoption, exact engine pin, typed DANE and schema-v3 native security publication, stale-work qualification, and final Chromium-only source boundary |
| `work/hns-dane-crawler` | `74546c7e6b0b8a764525a77177a88dc333bf64d8` | canonical migration, observational authority boundary, and date-stable qualification |
| `work/hns-dane-bootstrap-generator` | `f745f122243e5304e6a7ea0e111d47c61d22005e` | canonical migration, release-source URL update, reproducible npm lock repair, and publisher-boundary documentation |
| `work/MeshMine` | `bc9cc70de22e455545d44453cec0d6f07ebeaabe` | standalone Rust node adoption, immutable canonical Git dependency, portable CI correction, and consolidated warning-denied HSRD cleanup |
| `work/handshake-rs-profile` | `fcbeae9874c4eaa62ce5fc52d4cbc499dae94be1` | organization repository/authority graph, role consent, product-specific browser requester opt-in, and source-versus-release boundary |
