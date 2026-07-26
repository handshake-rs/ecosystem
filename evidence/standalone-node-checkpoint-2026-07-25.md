# Standalone Rust node extraction checkpoint

Date: 2026-07-25
Status: locally committed portable checkpoint; not a release qualification

## Provenance

- MeshMine source:
  `67a11290d410dc88113c4c3516ce9d22e8640a49:hsrd`
- history-preserving subtree split:
  `a99f58ca66fc0288526a3af7aae448e7af9bfbd1`
- source-prefix and split-root tree:
  `cf8a5fb2f133bbfac1df038dc4598c7015fd8fa3`
- preserved history: 126 commits
- standalone normalization:
  `7e5c5d96fb8fd2430a141284ed0c13aafe2e8d34`
- qualification cleanup:
  `d97aab205ef640008bd61d1b17ba3ef91ee2ac10`
- canonical `handshake-rs/hns-node-rs` main:
  `504d3fed035feb8a637ca09c4e0816b6e1144622`
- MeshMine immutable external-node consumer:
  `f0f25aacdc5eb05ba41d3bd81e4d22680fa70fb9`

The split tree was compared exactly with the source prefix. The normalization
removed the MeshMine-only miner binary/service, corrected root-relative
operational paths, and added explicit extraction provenance. It did not change
schema version 19, storage profile `hsrd-mining-v15`, RocksDB snapshot/multi-get
paths, append-only authenticated name pages, block/undo segment locators,
pruning checkpoints, or one-batch reorganization behavior.

## Portable gates passed

- locked/offline metadata for the root and fuzz workspaces;
- formatting for both workspaces;
- strict all-target, all-feature Clippy;
- the complete no-default-features workspace test matrix, including loopback
  tests with local socket permission; and
- locked/offline checks for every fuzz target.

## Explicit limitations

The all-features test command spent more than one hour compiling/archiving
bundled RocksDB on the external ARM-host work disk and was interrupted before
test execution. No source or test failure occurred, but this is not a pass.
The release rebuild was not started. Existing readiness-document
inconsistencies also require a dedicated evidence reconciliation before any
production-readiness claim.

## Migration-specific external boundary

MeshMine now resolves `hns-consensus`, `hns-mining`, `hns-node`, and
`hns-primitives` from the exact canonical node Git revision above. The locked
metadata validator rejects a sibling path override, unpinned branch, different
URL/revision, or embedded `MeshMine/hsrd` runtime source.

Migration gates passed:

- exact locked/offline Cargo metadata and source-boundary validation;
- live-parent/source validation against the resolved Git checkout;
- 8 focused `meshmine-hsrd-bridge` tests;
- strict focused Clippy;
- formatting, shell syntax, Python compilation, and diff checks; and
- a shallow fresh clone of `handshake-rs/MeshMine` resolved locked metadata and
  passed the external-node validator without a sibling node checkout.

The node and MeshMine worktrees were clean and their exact mains were pushed to
their matching canonical repositories. This does not upgrade the unrun live
node/MeshMine topology to release-ready.

The first hosted post-migration MeshMine run passed the complete primary
workspace, RustSec, fixtures, external-node boundary, differential, regtest,
simulation, and performance jobs. Its only failure was the warning-denied HSRD
lint job, where two authenticated Urkel record-path return signatures exceeded
Clippy's type-complexity threshold. Commit
`f0f25aacdc5eb05ba41d3bd81e4d22680fa70fb9` introduces documented semantic
aliases without lint suppression; the exact Clippy command, formatting, and 19
focused Urkel tests pass.
