# Remaining gaps

This ledger is deliberately release-blocking.

## Canonical protocol repository

- Add production-parser fuzz targets and retained corpus commands.
- Adopt the canonical crates in every consumer without copying protocol logic.

## Standalone node, wallet, and market

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

- Replace the current IANA-suffix namespace shortcut with full-host,
  independently authenticated HNS and ICANN resolution. Classify HNS-only,
  ICANN-only, convergent, divergent, and neither results; apply a documented
  precedence policy to divergence and expose the chosen namespace. The IANA
  snapshot may remain only as a cache/performance hint.
- Replace the browser clones' remaining historical gateway/runtime copies with
  the shared engine. TLSA owner derivation and the ICANN trust decision are
  already shared through `hns-icann-dane`, but this is not yet full engine
  consolidation.
- Pin or publish the shared engine dependency for release instead of using the
  coordination-root path dependency.
- Complete Android/iOS lifecycle/build/ABI tests and Chromium
  native-host/PAC/proxy/restart/uninstall tests.
- Run signed-device Android/iOS and installed-browser Chromium matrices for
  redirects, cross-origin subresources, Service Workers, downloads, WSS,
  process restarts, and policy revocation.

## Integration and release

- Run adversarial, restart, corruption, fuzz, browser, and performance suites.
- Execute all 26 minimum regtest demonstrations in `QUALIFICATION_MATRIX.md`.
- Produce checksummed binaries/packages, SBOM/license inventory, final commit
  table, environmental limitations, mainnet risks, and rollback plan.

Until every mandatory row is `PASS`, release-readiness remains **NO**.
