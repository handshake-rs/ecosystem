# Denuo live registry-negotiation checkpoint

Date: 2026-07-26

Status: implemented, committed, and pushed; full-node topology qualification
remains open

## Canonical checkpoints

- `handshake-rs/hns-rs`:
  `5f56e5d381338314e4d7cf1f9e08da7c76d1cf6f`
- `handshake-rs/hns-node-rs`:
  `b2c375e37cac6cfa7a09cfa61113de52ac4f93a1`

The node pins that exact `hns-rs` revision in `Cargo.toml` and `Cargo.lock`.
No registry digest, service bit, packet number, Hello/Ack message number, or
payload limit is copied into the live implementation.

## Shared registry authority

The `hns-rs` checkpoint exports:

- canonical registry name, ID, version, protocol version, fingerprint, wire
  profile, and experimental-status label;
- the exact complete-packet, nested-payload, and registry-negotiation limits;
- canonical typed RegistryHello and RegistryHelloAck constructors/decoders;
- protocol `0x0000`, version `1` as a mandatory negotiated protocol; and
- artifact tests binding the public identity to the canonical TOML, generated
  binary, and SHA-256 file.

Canonical fingerprint:

`95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d`

## Live node behavior

`hns-node-rs` now:

- advertises only ordinary `SERVICE_NETWORK` plus the Denuo extension service;
- completes ordinary VERSION/VERACK readiness before an outbound peer may
  initiate the private exchange;
- sends no Denuo Hello to a peer that did not advertise the extension service;
- binds the correlated Hello/Ack exchange to the canonical fingerprint,
  registry/protocol versions, exact Handshake network, exact genesis hash,
  receive-size limit, live-request limit, and feature flags;
- intercepts only packet `0xf4`; every other unknown packet retains the
  ordinary opaque P2P path;
- enforces the 1,048,576-byte complete-packet limit before generic unknown
  packet decoding, the 1,048,550-byte nested limit, and the 16,384-byte
  registry-negotiation limit;
- avoids an extra owned copy of rejected `0xf4` payloads;
- counts repeated oversized attempts even after Denuo is disabled while
  preserving the first scoped disable reason;
- rejects malformed, incompatible, uncorrelated, duplicate, replayed, and
  late messages without banning or disconnecting the ordinary peer;
- drops a stale queued Hello after its admission-based negotiation deadline
  while retaining the required mismatch Ack path; and
- rejects bounded unknown subprotocols without destroying an already
  successful registry agreement.

Two live local peer managers negotiate protocol `0x0000` version `1`, a
maximum of 64 live requests, zero feature flags, and the canonical payload
limit. Ordinary `GetAddr` traffic continues after negotiation. Process
agreement and admission totals survive peer retirement while live-peer counts
return to zero.

## Truthful diagnostics

Diagnostic API version 12 exposes one fixed `experimental_registry` object
through node status and native-sync diagnostics. It includes:

- canonical identity, fingerprint, profile, assignment warning, service bit,
  packet type, and all three payload limits;
- the complete local service mask and whether the extension is advertised;
- awaiting-version, locally disabled, eligible, Hello-admitted, negotiated,
  not-advertised, and disabled live-peer counts;
- outbound queue admissions, inbound wire receipts, compatible agreement
  computations, rejections, disabled sessions, and the fixed ordered rejection
  taxonomy; and
- per-peer phase, disable reason, request correlation, and negotiated limits.

Outbound admission totals deliberately do not claim socket-write completion.
The existing per-peer byte counters remain the transport-write evidence.
Bare, non-live node status reports the canonical identity with
`advertised=false` and zero counts instead of empty identity strings.

## Retained gates

Canonical `hns-rs` delta:

- `cargo test -p hns-p2p-experimental`: 30 passed
- `cargo test -p hns-conformance`: 3 passed
- `cargo run -p hns-registry-gen -- --check`: passed
- focused warning-denied Clippy, formatting, and diff checks: passed

Standalone node:

- `cargo test --locked -p hns-p2p`: 38 passed
- `cargo test --locked -p hns-rpc`: 8 passed
- `cargo test --locked -p hns-node --all-targets --no-default-features`:
  117 passed across the library and binary targets
- focused API-v12 projection and native/status parity tests after the final
  terminology/resource hardening: passed
- `cargo clippy --locked -p hns-p2p --all-targets -- -D warnings`: passed
- `cargo clippy --locked -p hns-node -p hns-rpc --all-targets
  --no-default-features -- -D warnings`: passed
- `cargo fmt --all -- --check` and `git diff --check`: passed

An independent adversarial review found no P0 defect. Its oversized-disabled
session finding was fixed before commit by moving exact `0xf4` dispatch ahead
of generic packet decoding and keeping the Denuo cap authoritative after
disable. Its diagnostic and stale-queue P2 findings were addressed with
admission/computation terminology, admission-based timeout state, and stale
Hello suppression.

## Not claimed

This checkpoint does not claim:

- two complete `hsrd` processes synchronizing over a retained regtest
  topology;
- live Denuo negotiation over the Brontide mainnet/testnet transport matrix;
- HIP 76, 77, or 78 runtime support;
- requester, opaque-relayer, output/provider, HNSR, or market-role enablement;
- wallet or marketplace implementation; or
- release readiness.

Those remain explicit qualification or implementation gaps.
