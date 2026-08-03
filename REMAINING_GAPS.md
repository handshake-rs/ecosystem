# Remaining gaps

This ledger is deliberately release-blocking.

## Canonical protocol repository

- Retain the production-parser fuzz target, locked fuzz dependency graph, and
  deterministic parser-smoke command in hosted qualification.
- Qualify and publish the canonical marketplace/session/HNS-HTLC/Shakedex,
  NameState/resource, HSD fee-policy, and TRANSFER/FINALIZE boundary at
  `4b989aabc132e7e79b8fd57a10f2465073faf588`; until separately authorized,
  its `0.2.0` source and vectors are not a consumable release.
- Adopt the canonical crates in every consumer without copying protocol logic.

## Standalone node, wallet, and market

- Keep the all-true HSRD functional-readiness matrix bound to its retained
  stopped-state, rollback, invalid-corpus, and executable evidence. Do not
  conflate it with either the base snapshot's `pre-authority` label or live
  native RPC's mode-specific release-stage diagnostics, a synchronized durable
  runtime tip, production provider readiness, operational endorsement, or
  independent review.
- Extend exact-revision canonical `hns-rs` adoption beyond the completed live
  registry and HIP-76 session boundaries; do not copy protocol semantics into
  the node.
- Connect HIP-76 provider work to an explicitly opted-in production recursive
  and DNSSEC-validating backend, persist/reload operator role policy, and
  demonstrate it through two full-node processes.
- Demonstrate two-node standard synchronization, live Brontide Denuo/HIP-76
  negotiation, and HIP 77/78 runtimes.
- Publish the new canonical marketplace protocol/Denuo V2 crate boundary and
  adopt it by immutable release in node/wallet/browser consumers; do not use a
  sibling path or copied wire types.
- Qualify the source-complete HNS transaction/reconciliation runtime and
  concrete authenticated node adapter at
  `4935e059bcde338f4260dd98202ff26ce0f3ca9f`, including the separate encrypted
  bounded HNS-coin/name-role scans under one exact chain/mempool snapshot, the
  authoritative-account revision/CAS ordering and derivation-high-water
  rollback rejection, plus
  atomic prepared-workflow recovery and hostile HTTP/JSON, stale epoch/mempool,
  pruned payload, coinbase, fee-quote, restart, and reorg cases. Exact
  final-signed node quotes are now adopted in source, but value must remain
  disabled until the wallet consumes the released `hns-script` 0.2 canonical
  sigop-adjusted fee algebra and independently validates the quoted minimum.
- Publish and consume the canonical NameState/resource codec, qualify the
  separately persisted bounded `HnsName` scan, add platform-backed database-key
  wrapping, and complete transfer/finalize/reorg integration before enabling
  ownership actions. The scan is source-only key discovery; the current name
  path remains watch-only.
- Complete and register the remaining Bitcoin and Ethereum runtime/settlement
  adapters. HNS now has a source-level `ChainModule`/`AtomicSettlement` join,
  but its value permit remains unavailable; the Bitcoin supervisor is not yet
  signed-settlement complete. Ethereum advertises offline receive derivation
  only: synchronization/history/send/value/settlement/mainnet remain false or
  unavailable, and the opaque Helios provenance/value/settlement permits have
  no current issuer.
- Complete and independently review the derivation/recovery specification:
  qualify the new HNS name scan and its role/identifier separation, retain
  Ethereum role separation, qualify the dedicated Bitcoin atomic-swap branch,
  bind metadata-encryption key recovery, and publish deterministic vectors for
  every required role.
- Adopt the canonical strict TRANSFER/FINALIZE and listing-independent recovery
  primitives from `hns-rs` in the wallet, then complete fixed-price Shakedex
  discovery, preview, signed funding/fulfillment/finalization, recovery,
  restart-at-every-state, reorg, and Denuo relay integration. Reverse Dutch
  remains deferred until fixed price passes.
  Current wallet source correctly blocks every legacy 0.1 seller/buyer entry
  and transition, including restored sessions; those false release gates must
  not be changed before published canonical V2/Denuo consumption and the full
  lifecycle evidence exist.
- Replace or extend the pinned Kyoto boundary so headers, compact-filter
  headers/filters, and peer/address state are durably exposed and restored;
  add safe archival beyond the bounded transaction/output lifetime caps.
  Then run direct-P2P/regtest birthday, invalid-PoW, filter mismatch,
  inconsistent-peer, false-positive, spend, signed HTLC, reorg, restart,
  broadcast-retry, trusted-time, and resource suites. No Esplora/Electrum/RPC
  fallback may be added.
- Embed and audit the selected Helios proof/persistence adapter and the private
  issuer for its opaque evidence-provenance permit; add synchronization,
  history, nonce/fee discovery, controlled broadcast/recovery for the opaque
  redacted signed-payload boundary, and restart/reorg handling. Run the
  deterministic native-ETH contract on a local development chain through
  lock/redeem/refund/replay/authorization/reentrancy/event/rollback cases, and
  bind any approved address to exact chain ID and deployed runtime hash.
- Demonstrate HNS/BTC and HNS/ETH success/refund/restart/reorg flows before
  advertising either pair. Mainnet settlement remains disabled.
- Complete reporter governance, quorum/outlier/circuit-breaker policy,
  malicious-board controls, fill-grant expiration, peer cooldown/scoring, and
  end-to-end browser approval for the market-price board.
- Adopt and qualify the source-complete authenticated RPC, exact transaction
  fee quotes, confirmed/mempool Shakedex, and HTLC tracker at
  `3d346e3dadc716b5c367eee050308e71a0693a64` through the released canonical
  protocol dependency and the source-complete wallet adapter. Its chain
  evidence and verified revealed-preimage events—not Denuo status relay
  objects—must remain settlement authority. Add safe registry retirement and
  capacity reclamation; the current 16,384-global and 256-per-address limits
  are unreclaimable lifetime caps and remain a production-availability block.
- Qualify the `v0.3.4` node plus private loopback resolver-sidecar/container
  topology at tagged source `40b456fa0772729542118a69f27edc37bf42a3d7`
  and reconcile the later release-CI-only `main` corrections. Retain RPC
  authentication, avoid sharing a wallet-enabled credential with the resolver,
  keep DNS off public interfaces, and record immutable image digests before
  product consumption.
- Qualify wallet schema upgrades from every supported prior version, offline
  backup/restore, rollback detection, and corruption recovery. Qualify the
  node's offline wallet-index reindex path and measure index disk/build cost;
  do not claim an online backfill that does not exist.

## MeshMine

- Deliberately advance and requalify MeshMine's immutable node pin before
  attributing the standalone node's later Denuo/HIP-76 session features to the
  bridge.
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
  The engine's loopback proxy admission/publication core now exists at
  `6eb0174ae743e6bd01c516be7a534d94be94b4bd`, including retention across
  unrelated admitted work and fail-closed security-epoch invalidation; the next
  bounded slice is exact Chromium/mobile consumption of that opaque authority. Live DNS wire,
  light-chain, DNSSEC, DANE, resolver, origin transport, and gateway migration
  follow independently.
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
- Retain atomic staged header/peer/readiness publication and Chromium's
  generation-bound mandatory PAC during native-host replacement. Exercise
  crash recovery, concurrent runtimes, evidence expiry, and replacement races
  in installed processes rather than treating portable lifecycle tests as the
  installed-browser result.
- Retain the completed Android/iOS portable lifecycle, build, ABI, signed
  artifact, store-upload, and live-screenshot gates while keeping them
  distinct from installed-device qualification; complete Chromium
  native-host/PAC/proxy/restart/uninstall tests.
- Run signed-device Android/iOS and installed-browser Chromium matrices for
  redirects, cross-origin subresources, Service Workers, downloads, WSS,
  process restarts, and policy revocation.
- Publish the private wallet ABI v2 as a signed, pinned artifact and consume it
  in each browser. Preserve its typed private capability snapshot
  (`providerSchemaVersion`, `approvalSchemaVersion`, `walletSessionId`,
  `permissionGeneration`, and `methods`) and four-field result/prompt/event
  binding without widening the public website `wallet_getCapabilities` result
  beyond `{providerApiVersion,methods}`. Keep generation zero exclusive to an
  origin with no permission history, retain nonzero tombstones, and implement
  an atomic approved-Accounts-to-real-result join before advertising
  `hns_requestAccounts`. Bind the checked-in manifest structure to verifier-
  owned trust roots, artifact hashes, durable anti-rollback state, and actual
  process launch; schema validity alone must not affect availability. For
  mobile, connect the dormant projections at
  `4b684ebbb576c2b2f8e762c3f81c3ec2fded47f5` only through reviewed generated
  `hns-wallet-ffi` JNI/C bindings, the canonical typed engine authority result,
  controller lifecycle wiring, permission persistence, native approval UI, and
  a typed event producer. Then qualify permission, approval, lock/session,
  event, installed-device, and value behavior and implement the actual wallet
  screens, notification, backup, migration, and removal paths.
  The current wallet, Chromium, and mobile successors are source/static-only,
  unrun, and unpushed; Chromium's provider/value gates and all four mobile
  release gates are false, and the mobile unavailable adapter is hardwired.
  Until reviewed native projection exists, the Chromium host and both mobile
  scaffolds must continue to report unavailable and avoid announcing a provider.
- Retain the protected Developer ID identity checks, notarization evidence,
  stapling, and digest-verified release path proven for Chromium v0.5.5.
  Add equivalent authorized signing/provenance for Windows and qualify all
  published artifacts after installation.

## DANE observational and operator tools

- Qualify crawler production snapshot provenance, incremental/reorg handling,
  stored DNS evidence expiry, static publication, and the optional live
  directory without promoting observed data to trust authority.
- Retain the crawler's exact development lock, clean-environment install, Ruff,
  140-test, and full fixture/export/validation/archive pipeline gates.
- Qualify a hash-pinned bootstrap-generator release archive and appliance on
  supported operating systems, including DNSSEC rollover, authoritative DoH,
  TLSA rollover, backup/restore, uninstall, and failure recovery.
- Repair and rerun the published bootstrap-generator CI workflow. Hosted run
  `30401402868` failed before qualification at `npm ci` because
  `package-lock.json` lacks `@emnapi/runtime@1.11.3`; do not count downstream
  audit, web, appliance, or production-build steps until the locked install
  passes.
- Retain a versioned crawler-to-generator handoff fixture and prove that every
  generated record still requires operator review and independent live
  DNSSEC/DANE validation.

## Integration and release

- Retain protected, exact-head hosted evidence for published checkpoints and
  close any current hosted failures. The engine's latest local source head
  `6eb0174ae743e6bd01c516be7a534d94be94b4bd` (with older release-preparation
  predecessor `1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75`) must remain unpushed,
  unpublished, and unqualified until its separate release is authorized;
  local gates and exact-revision consumer evidence do not substitute for
  protected current-main checks.
- Mobile distribution readback: iOS 0.5.5 build 57 is `VALID` and its direct
  App Review submission is `WAITING_FOR_REVIEW` after protected upload run
  `30456522039`; GitHub
  `v0.5.5` is public with the verified code 46 APK and build 57 App Store IPA.
  Keep App Store release manual and do not add
  a TestFlight or beta-group path. Android 0.5.5 version code 46 is already on
  the Google Play production track.
- Run adversarial, restart, corruption, fuzz, browser, and performance suites.
- Complete every applicable open demonstration in the 38-row
  `QUALIFICATION_MATRIX.md`. Historical row 13 remains explicitly excluded by
  the current wallet scope and must not be implemented as a shortcut to a
  green matrix.
- Produce checksummed binaries/packages, SBOM/license inventory, final commit
  table, environmental limitations, mainnet risks, and rollback plan.

Until every mandatory row is `PASS`, release-readiness remains **NO**.
