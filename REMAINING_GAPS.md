# Remaining gaps

This ledger is deliberately release-blocking.

## Canonical protocol repository

- Retain the production-parser fuzz target, locked fuzz dependency graph, and
  deterministic parser-smoke command in hosted qualification.
- Adopt the canonical crates in every consumer without copying protocol logic.

## Standalone node, wallet, and market

- Keep HSRD readiness claims bound to the implemented executable package and
  two-process regtest gates; do not generalize them to synchronization,
  consensus completeness, provider readiness, or mining authority.
- Extend exact-revision canonical `hns-rs` adoption beyond the completed live
  registry and HIP-76 session boundaries; do not copy protocol semantics into
  the node.
- Connect HIP-76 provider work to an explicitly opted-in production recursive
  and DNSSEC-validating backend, persist/reload operator role policy, and
  demonstrate it through two full-node processes.
- Demonstrate two-node standard synchronization, live Brontide Denuo/HIP-76
  negotiation, and HIP 77/78 runtimes.
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

- Continue replacing the browser products' historical platform-neutral copies
  with the shared engine. TLSA-owner/ICANN trust, full-host root comparison,
  direct-first transport/role policy, canonical authority lifecycle, and
  schema-v2 observability are now shared through five exact-pinned contracts.
  The next bounded slice is the loopback proxy admission/publication core;
  live DNS wire, light-chain, DNSSEC, DANE, resolver, origin transport, and
  gateway migration follow independently.
- The complete engine graph is now standalone at exact canonical `hns-rs`
  revision `dde2da81f29df935f043978a6d517c1d60ceff31`; retain its exact-source,
  shallow-clone, cargo-deny, and offline gates while adopting deeper engine
  crates in each browser.
- The platform runtime versus canonical `hns-browser-runtime` collision is
  resolved with explicit mobile and Chromium adapter package names. Resolve
  each remaining same-name package collision the same way; in particular, do
  not alias the browser-local complete TLS proxy server to the engine's
  narrower `hns-loopback-proxy` admission crate.
- Keep Chromium free of the historical Android/iOS product trees now retained
  in the canonical mobile repository; prevent mobile packaging, FFI, and
  store-only paths from returning through copied release automation.
- Exercise the implemented explicit-pin, sticky-binding, divergent-root,
  persistence-failure, cache-partition, and selected-namespace UI semantics in
  installed Chromium and signed Android/iOS network processes.
- Make Chromium's initial-sync UI distinguish a bound/listening native host
  from canonical authority that is still header-syncing, degraded, and
  non-admitting; expose bounded progress or an explicit sync trigger without
  weakening the authority gate.
- Keep the strict `Neither` end-to-end Chromium regression, but separate its
  optional live validating-DoH/Node dependency from the deterministic offline
  conformance gate so external tool or network availability cannot obscure a
  product regression.
- Complete Android/iOS lifecycle/build/ABI tests and Chromium
  native-host/PAC/proxy/restart/uninstall tests.
- Run signed-device Android/iOS and installed-browser Chromium matrices for
  redirects, cross-origin subresources, Service Workers, downloads, WSS,
  process restarts, and policy revocation.

## DANE observational and operator tools

- Qualify crawler production snapshot provenance, incremental/reorg handling,
  stored DNS evidence expiry, static publication, and the optional live
  directory without promoting observed data to trust authority.
- Retain the crawler's exact development lock, clean-environment install, Ruff,
  140-test, and full fixture/export/validation/archive pipeline gates.
- Qualify a hash-pinned bootstrap-generator release archive and appliance on
  supported operating systems, including DNSSEC rollover, authoritative DoH,
  TLSA rollover, backup/restore, uninstall, and failure recovery.
- Publish and protect the bootstrap-generator CI workflow now implemented
  locally for its locked install, dependency audit, web tests, appliance
  tests, and production build; no hosted run exists until that local commit is
  deliberately pushed.
- Retain a versioned crawler-to-generator handoff fixture and prove that every
  generated record still requires operator review and independent live
  DNSSEC/DANE validation.

## Integration and release

- Deliberately publish and protect the locally implemented workflows for
  `handshake-rs-profile`, `hns-dane-bootstrap-generator`, `hns-rs`,
  `hns-node-rs`, and the ecosystem evidence repository. The engine already has
  a successful exact-head hosted workflow; local gates and exact-revision
  consumer evidence do not substitute for protected current-main checks.
- Run adversarial, restart, corruption, fuzz, browser, and performance suites.
- Execute all 26 minimum regtest demonstrations in `QUALIFICATION_MATRIX.md`.
- Produce checksummed binaries/packages, SBOM/license inventory, final commit
  table, environmental limitations, mainnet risks, and rollback plan.

Until every mandatory row is `PASS`, release-readiness remains **NO**.
