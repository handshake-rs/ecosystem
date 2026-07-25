# Remaining gaps

This ledger is deliberately release-blocking.

## Canonical protocol repository

- Finish and gate the complete standalone script VM and `OP_TYPE`.
- Finish/gate shared mining work and dedicated conformance/fuzz packages.
- Add production-parser fuzz targets and retained corpus commands.
- Adopt the canonical crates in every consumer without copying protocol logic.

## Standalone node, wallet, and market

- Complete extraction cleanup and provenance commit.
- Reconcile any HSRD readiness claims with executable gates.
- Add/use canonical `hns-rs` dependencies.
- Demonstrate two-node standard synchronization and all HIP 76/77/78 runtimes.
- Complete wallet persistence, encryption/signing, recovery, coin selection,
  fee handling, and OPEN/BID/REVEAL/REDEEM/REGISTER/UPDATE/RENEW/TRANSFER/
  FINALIZE/REVOKE flows.
- Complete fixed/Dutch listing storage, discovery, preview, fulfillment,
  confirmation, cancellation/expiry, threat controls, and DENUO_EXT board.

## MeshMine

- Adopt the standalone node through a stable external boundary.
- Remove embedded-node coupling without losing the documented RocksDB snapshot,
  batch, cache, segment, undo, pruning, template, and publication fast paths.
- Demonstrate coherent snapshot/job activation, stale-work retirement, solved
  candidate validation, and multi-peer publication.
- Run and record performance/regression gates.

## DANE engine and clients

- Implement `hns-dane-engine`: DNS wire, DNSSEC, authenticated HNS state,
  iterative/direct resolution, TLSA/DANE, cache/provenance, HIP transports,
  HNSR, policy generation, stable C/Android/iOS/native-messaging ABIs.
- Replace duplicated browser crypto/protocol logic with the shared engine.
- Remove third-party public recursive fallback for HNS.
- Implement durable independent requester/provider/transport controls.
- Complete Android/iOS lifecycle/build/ABI tests and Chromium
  native-host/PAC/proxy/restart/uninstall tests.

## Integration and release

- Run adversarial, restart, corruption, fuzz, browser, and performance suites.
- Execute all 26 minimum regtest demonstrations in `QUALIFICATION_MATRIX.md`.
- Produce checksummed binaries/packages, SBOM/license inventory, final commit
  table, environmental limitations, mainnet risks, and rollback plan.

Until every mandatory row is `PASS`, release-readiness remains **NO**.
