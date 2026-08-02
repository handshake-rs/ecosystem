# Production completion plan

Status date: 2026-08-02

Target state: a production-complete, independently qualified Handshake wallet,
Provider API, fixed-price Shakedex/Denuo market, Kyoto Bitcoin module, narrow
Helios-backed native-ETH module, and HNS/BTC plus HNS/ETH settlement system.
The target is not satisfied by compatible schemas, compiled scaffolds, unit
state machines, or a green repository build in isolation.

## Completion rule

A product surface loses its experimental, disabled, or unavailable status
only after all of the following evidence exists at one exact revision:

1. Executable code is wired through the real product boundary.
2. Safety-critical state is durably persisted before irreversible actions.
3. Restart, retry, rollback, corruption, and chain-reorganization recovery are
   deterministic and fail closed.
4. Negative and adversarial tests cover hostile sites, peers, providers,
   malformed evidence, stale generations, replay, and authorization failures.
5. The applicable full process, installed-browser, device, local-chain, or
   regtest topology passes—not only a unit test.
6. Resource, privacy, trust, migration, backup, and rollback behavior is
   measured and documented.
7. The repository's one consolidated qualification gate and independent
   security review pass.

Mainnet settlement remains disabled until every requirement above is true for
the complete pair and both refund paths.

## Dependency order

```text
hns-rs canonical protocols and release
  -> hns-node-rs authoritative indexes/backend/relay
  -> hns-wallet-rs encrypted runtime and recovery
  -> versioned wallet ABI artifact
  -> Chromium and Android/iOS product wiring

Kyoto HNS/BTC adapter ----\
                          +-> price board/fill grants -> bilateral settlement
Helios HNS/ETH adapter ---/
```

No maintained repository may gain a sibling-checkout dependency. Until an
upstream artifact is released, downstream code may implement and test the
versioned boundary but must remain fail closed rather than copy canonical
types or silently substitute a backend.

## Active production tranche

The first tranche is being implemented in parallel on `main`:

| Repository | Cohesive result |
| --- | --- |
| `hns-node-rs` | mempool-aware wallet restoration plus persisted Shakedex/HTLC funding, spend, refund, and verified-preimage tracking |
| `hns-wallet-rs` | entity-complete encrypted CRUD, restart/reorg supervisor, and registered HNS chain/settlement runtime |
| `hns-dane-browser-extension` | independently released wallet ABI discovery, version/capability negotiation, typed provider dispatch, and lifecycle recovery |

The pre-existing Chromium insecure-delegation correction and the repository-
root `dist/` ignore rule are committed separately at
`5ffca638481b64172666db482f99f6156a44ccbf` before this tranche.

## Qualification efficiency policy

- Source, tests, and Markdown are changed as one coherent tranche and
  committed once on `main`.
- Local agents do not run focused builds followed by the same full build.
- One consolidated repository gate is selected after the source converges;
  hosted CI may be the qualification layer when a push is separately
  authorized.
- Any necessary local Cargo target, temporary directory, Gradle state, or npm
  cache lives on NVMe, never in the external workspace.
- RocksDB is never rebuilt. Node qualification must use an existing prebuilt
  library through `ROCKSDB_LIB_DIR` and `ROCKSDB_STATIC=1`.
- A failed gate is followed only by the smallest affected rerun needed to
  prove the fix; unchanged heavyweight stages are not repeated.

Repository scripts remain portable; these storage and cache choices are local
orchestration policy rather than committed absolute paths.

## Remaining production sequence

After the active tranche:

1. Complete fixed-price Shakedex construction, Denuo discovery, purchase,
   finalization, cancellation, recovery, restart, and reorg topology.
2. Complete Kyoto direct-P2P persistence, dedicated swap derivation, birthday
   restore, signed HTLC spends, adversarial peer/reorg cases, and the full
   disk/bandwidth/startup/mobile-memory benchmark matrix.
3. Embed the selected Helios verifier/persistence runtime, qualify native ETH
   receive/send/history, execute and audit the immutable HTLC contract on a
   local chain, and bind any deployment to chain ID and runtime code hash.
4. Complete reporter governance, deterministic price rounds, Denuo board
   resistance, bilateral reservation/fill, and browser approval.
5. Demonstrate both directions of HNS/BTC and HNS/ETH success, abort, refund,
   restart, fee-spike, timeout, preimage, and reorganization behavior.
6. Run installed Chromium, signed Android/iOS, backup/migration, corruption,
   privacy, sustained fuzz, performance, and independent security gates.
7. Reconcile exact revisions, release artifacts, rollback plans, and every
   row of `QUALIFICATION_MATRIX.md` before enabling mainnet.

## Evidence ledger

`INTEGRATION_STATE.md`, `REFERENCE_COMMITS.md`,
`QUALIFICATION_MATRIX.md`, `REMAINING_GAPS.md`, and
`WALLET_MARKETPLACE_IMPLEMENTATION.md` remain authoritative for demonstrated
status. This plan records ordering and proof requirements; it does not upgrade
any qualification row by itself.
