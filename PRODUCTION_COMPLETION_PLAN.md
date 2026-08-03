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

The current source tranche has committed the canonical fee/name/Shakedex
boundary, authenticated node/wallet quote join, durable Kyoto supervisor,
private wallet ABI, engine authority/proxy admission, and Chromium boundary on
`main` without upgrading release status:

| Repository | Cohesive result |
| --- | --- |
| `hns-rs` | committed at `81f2df2651e8ea81be33e33a3438c4c9e0348f93`: canonical HSD fee-policy arithmetic, strict TRANSFER/FINALIZE construction, canonical empty offer inventory, and listing-independent Shakedex recovery extend the prior settlement/session/name-codec source; shared 0.2 packages remain unpublished and unqualified |
| `hns-node-rs` | local and remote-tracking `main` at `3d346e3dadc716b5c367eee050308e71a0693a64`: exact snapshot-bound final-transaction fee quotes plus the v0.3.4 private resolver-sidecar/container source and later release-CI port fixes; tag `v0.3.4` remains at `40b456fa0772729542118a69f27edc37bf42a3d7`, and the separate external push/tag does not upgrade this ledger's qualification status |
| `hns-wallet-rs` | committed at `5b5409630045b19f81821951da51a9a1f7e1c9e5`: private service ABI v2 with zeroizing frames, dedicated Bitcoin swap derivation, hardened namespace/origin permission and approval/event authority, and exact signed-byte quote persistence/rebroadcast; HNS value remains gated on released canonical fee algebra and product qualification |
| `hns-dane-engine` | committed at `6eb0174ae743e6bd01c516be7a534d94be94b4bd`: opaque exact-origin proxy authority survives unrelated admitted work while security-invalidating transitions revoke it; product consumption and qualification remain unavailable |
| `hns-dane-browser-extension` | committed through `6285fda5a7ed61c5ac93f5127de078ce8587da38`: fail-closed ABI discovery and authority invalidation; provider remains unavailable |

The pre-existing Chromium insecure-delegation correction and the repository-
root `dist/` ignore rule are committed separately at
`5ffca638481b64172666db482f99f6156a44ccbf` before this tranche.

## Qualification efficiency policy

- Source, tests, and Markdown are grouped into the fewest cohesive repository
  commits on `main`, avoiding fixup churn while preserving real dependency and
  review boundaries.
- Local agents do not run focused builds followed by the same full build.
- One consolidated repository gate is selected after the source converges;
  hosted CI may be the qualification layer when a push is separately
  authorized.
- The external-drive checkout is source-only. Any necessary local build or
  qualification runs from a disposable NVMe checkout/worktree so source-
  adjacent Cargo, Gradle, npm, compiler, and temporary state cannot return to
  the external workspace; pointing only a final target directory at NVMe is
  insufficient.
- Optimized RocksDB is never rebuilt under any circumstance. Node
  qualification must reuse one of the existing NVMe prebuilt libraries through
  `ROCKSDB_LIB_DIR` and `ROCKSDB_STATIC=1`; a missing or incompatible artifact
  blocks that gate rather than authorizing another RocksDB compile.
- Repository-root `/dist/` is ignored in the Rust protocol, node, wallet,
  engine, and Chromium source repositories. Mobile's tracked store metadata and
  screenshots deliberately remain under `dist/`, so it uses narrower generated-
  output ignores rather than a destructive global rule.
- A failed gate is followed only by the smallest affected rerun needed to
  prove the fix; unchanged heavyweight stages are not repeated.

Repository scripts remain portable; these storage and cache choices are local
orchestration policy rather than committed absolute paths.

## Remaining production sequence

After the active tranche:

1. Adopt the canonical Shakedex TRANSFER/FINALIZE and recovery primitives in the
   wallet, then complete Denuo discovery, purchase, signed transaction flow,
   cancellation, recovery, restart, and reorg topology.
2. Replace or extend the pinned Kyoto boundary with durable header/filter/peer
   state, qualify the dedicated swap derivation, add signed HTLC supervision,
   safe record archival, adversarial peer/reorg cases, and the full disk/
   bandwidth/startup/mobile-memory benchmark matrix.
3. Embed the selected Helios verifier/persistence runtime, qualify native ETH
   receive/send/history, execute and audit the immutable HTLC contract on a
   local chain, and bind any deployment to chain ID and runtime code hash.
4. Complete reporter governance, deterministic price rounds, Denuo board
   resistance, bilateral reservation/fill, and browser approval.
5. Demonstrate both directions of HNS/BTC and HNS/ETH success, abort, refund,
   restart, fee-spike, timeout, preimage, and reorganization behavior.
6. Release and consume the engine-minted opaque proxy authority and private
   wallet ABI v2 in Chromium/mobile, then run installed Chromium, signed Android/iOS, backup/
   migration, corruption, privacy, sustained fuzz, performance, and independent
   security gates.
7. Reconcile exact revisions, release artifacts, rollback plans, and every
   row of `QUALIFICATION_MATRIX.md` before enabling mainnet.

## Evidence ledger

`INTEGRATION_STATE.md`, `REFERENCE_COMMITS.md`,
`QUALIFICATION_MATRIX.md`, `REMAINING_GAPS.md`, and
`WALLET_MARKETPLACE_IMPLEMENTATION.md` remain authoritative for demonstrated
status. This plan records ordering and proof requirements; it does not upgrade
any qualification row by itself.
