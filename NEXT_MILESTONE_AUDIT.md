# Next ecosystem milestone audit

Date: 2026-07-25

Status: identified; implementation not started

## Recommendation

The next independently committable milestone after the browser dual-root
checkpoint is:

> Adopt the canonical Denuo registry and live collision-safe `DENUO_EXT`
> negotiation in `hns-node-rs`.

This must precede wallet and marketplace construction. The standalone node
currently has no `hns-rs` dependency, advertises only the ordinary network
service, and discards decoded unknown packets—including packet `0xf4`. There
are not yet wallet, wallet-service, market, or node-client crates on which to
build a correct live marketplace.

The canonical `hns-rs` implementation already owns the bounded Denuo envelope,
registry hello/negotiation state, replay tracking, service assignments,
resource limits, and collision-isolating peer state. The node should consume
that authority rather than duplicate constants or registry hashes.
The organization-migrated registry fingerprint is
`95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d`.

## Prerequisite `hns-rs` checkpoint

- export the canonical registry name, version, fingerprint, and payload limits;
- add typed RegistryHello/Ack constructors so consumers never repeat private
  message numbers;
- require registry protocol `0x0000`, version 1 before negotiation is complete;
  and
- test the exported identity against the canonical TOML, generated binary, and
  SHA-256 registry artifact.

## Standalone-node checkpoint

- add an immutable dependency on the exact canonical
  `handshake-rs/hns-rs` revision (or its later published
  `hns-p2p-experimental` crate);
- add a bounded per-peer negotiation coordinator to `crates/hns-p2p`;
- have the outbound peer initiate the first extension exchange only after the
  ordinary compatible peer handshake;
- bind negotiation to the exact network and network genesis hash;
- route only canonical packet `0xf4` from the unknown-packet branch;
- enforce the 16 KiB registry-message bound, correlation IDs, replay
  rejection, and negotiated resource limits;
- isolate fingerprint/network/genesis/version mismatch to experimental
  traffic—ordinary Handshake peers must not be banned or disconnected solely
  for that mismatch;
- continue ordinary header, block, ping, transaction, and synchronization
  behavior before, during, and after negotiation;
- advertise only the Denuo extension service until real HIP requester/relay/
  output runtimes exist; and
- expose registry name/version/fingerprint/profile plus bounded negotiation
  counts/reasons through node status and native-sync diagnostics.

## Focused qualification

- two local live peer managers negotiate the exact canonical fingerprint;
- ordinary P2P succeeds before and after negotiation;
- fingerprint, network, and genesis mismatches disable only Denuo traffic;
- a peer without the Denuo service receives no private packet;
- oversized, malformed, duplicate, and replayed messages fail closed;
- RPC status reports the exact canonical registry fingerprint; and
- focused offline `hns-p2p`, `hns-rpc`, no-default-feature node, Clippy, and
  formatting gates pass.

This advances the assignment's registry, extension-envelope, compatibility,
and full-node requirements and creates the required transport boundary for the
later `DENUO_EXT` market board. It does not make the two-full-node topology,
wallet, HIP runtime, market, or 26-point qualification rows pass.

No source file in `hns-rs` or `hns-node-rs` was changed during this audit, and
no build was run for it.
