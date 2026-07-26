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

The worktree was clean at handoff. Nothing was pushed.
