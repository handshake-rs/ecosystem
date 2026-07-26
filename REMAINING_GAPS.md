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

- Retire the historical embedded `hsrd` qualification tree only after its
  remaining fixtures/provenance are retained independently; runtime and build
  authority now use the immutable canonical external-node revision.
- Demonstrate coherent snapshot/job activation, stale-work retirement, solved
  candidate validation, and multi-peer publication.
- Run and record performance/regression gates.

## DANE engine and clients

- Replace the browser clones' remaining historical gateway/runtime copies with
  the shared engine. TLSA owner derivation and the ICANN trust decision are
  shared through `hns-icann-dane`, and full-host root comparison is shared
  through `hns-namespace-resolution`, but this is not yet full engine
  consolidation.
- Exercise the implemented explicit-pin, sticky-binding, divergent-root,
  persistence-failure, cache-partition, and selected-namespace UI semantics in
  installed Chromium and signed Android/iOS network processes.
- Complete Android/iOS lifecycle/build/ABI tests and Chromium
  native-host/PAC/proxy/restart/uninstall tests.
- Run signed-device Android/iOS and installed-browser Chromium matrices for
  redirects, cross-origin subresources, Service Workers, downloads, WSS,
  process restarts, and policy revocation.

## DANE observational and operator tools

- Qualify crawler production snapshot provenance, incremental/reorg handling,
  stored DNS evidence expiry, static publication, and the optional live
  directory without promoting observed data to trust authority.
- Qualify a hash-pinned bootstrap-generator release archive and appliance on
  supported operating systems, including DNSSEC rollover, authoritative DoH,
  TLSA rollover, backup/restore, uninstall, and failure recovery.
- Add a required bootstrap-generator CI workflow for its locked install, web
  tests, appliance tests, and production build; those gates pass locally, but
  the transferred repository currently has no hosted Actions workflow.
- Retain a versioned crawler-to-generator handoff fixture and prove that every
  generated record still requires operator review and independent live
  DNSSEC/DANE validation.

## Integration and release

- Run adversarial, restart, corruption, fuzz, browser, and performance suites.
- Execute all 26 minimum regtest demonstrations in `QUALIFICATION_MATRIX.md`.
- Produce checksummed binaries/packages, SBOM/license inventory, final commit
  table, environmental limitations, mainnet risks, and rollback plan.

Until every mandatory row is `PASS`, release-readiness remains **NO**.
