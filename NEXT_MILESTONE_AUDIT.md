# Next ecosystem milestone audit

Date: 2026-07-26

Status: two milestones completed and pushed; next bounded audit identified

## Completed recommendation

The next independently committable milestone after the browser dual-root
checkpoint is:

> Adopt the canonical Denuo registry and live collision-safe `DENUO_EXT`
> negotiation in `hns-node-rs`.

This must precede wallet and marketplace construction. The standalone node
had no `hns-rs` dependency at the start of this milestone, advertised only the
ordinary network service, and discarded decoded unknown packets—including
packet `0xf4`. There were not yet wallet, wallet-service, market, or node-client
crates on which to build a correct live marketplace.

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

The prerequisite is committed on `handshake-rs/hns-rs` main at
`5f56e5d381338314e4d7cf1f9e08da7c76d1cf6f`. The live-node checkpoint is
committed on `handshake-rs/hns-node-rs` main at
`b2c375e37cac6cfa7a09cfa61113de52ac4f93a1`. Every focused requirement above
is implemented and green at those revisions. Exact retained evidence is in
`evidence/denuo-live-negotiation-checkpoint-2026-07-26.md`.

This completion does not upgrade the unrun two-full-node, Brontide transport,
HIP runtime, wallet, marketplace, or 26-point topology rows.

## Completed successor

The next independently committable milestone is:

> Add a role-safe HIP-76 live session layer without yet claiming a production
> DNS output service.

This follows the PDF's ordered `hns-node-rs` workstream after Denuo registry
negotiation. It should add real bounded `0xf0`/`0xf1` session admission,
correlation, deadlines, revocation, and diagnostics over already negotiated
Denuo peers, using an in-process qualification backend. Production recursion
and acceptance of DNS answers remain a later, separately qualified boundary.

### Consent and trust boundary

- HIP-76's so-called relay sees the plaintext qname and performs DNS egress.
  It is an output/provider role, not an opaque intermediary, and must remain
  explicit opt-in.
- Opaque relay defaults apply to protocols that forward opaque material, such
  as the ODoH proxy and HNSR relay. They must not silently enable a HIP-76
  output node.
- Request generation is a third, independent role. The current canonical
  HIP-76 policy is `Auto` with independent opt-out; that eligibility must
  never advertise the provider bit or perform unsolicited work. Durable
  operator-policy reload remains a separate gate. Any future change to an
  opt-in requester default requires an explicit policy decision rather than
  being smuggled into output-role implementation.
- An untrusted DNS reply received over Brontide is not authenticated merely
  because its peer or transport was authenticated. Local DNS message
  correlation and DNSSEC/TLSA/DANE validation remain mandatory before a
  higher-level consumer accepts it.

### Canonical prerequisite

In `hns-rs`:

- add direction-aware HIP-76 admission APIs; remote service advertisement
  authorizes outbound requester selection, while local advertisement and
  backend readiness authorize inbound requests;
- keep opaque-relay roles separate from output/provider roles;
- expose the HIP-76 semantic version and distinguish the 4,096/65,535-byte DNS
  body limits from the 4,106/65,546-byte complete request/response payload
  limits; and
- retain strict query/response codecs and current-generation request tracking.

### Node checkpoint

In `hns-node-rs`:

- add a bounded per-peer HIP-76 session coordinator after ordinary readiness
  and successful canonical Denuo negotiation;
- advertise service `0x40000000` only when an explicitly enabled output
  backend is synchronized, ready, and able to accept work;
- keep requester eligibility independent from local service advertisement;
- track peer, request ID, policy generation, DNS transaction/question,
  absolute deadline, capacity, and disconnect cleanup;
- never run recursive/output work on the peer reader;
- use typed backend and response-authenticator boundaries so test responses,
  untrusted wire responses, and locally authenticated answers cannot be
  confused;
- replace policy generations live, cancel or drain work on revocation,
  withdraw future advertisements, and reconnect affected peers when a
  connection's service mask changes; and
- add qname-free structured HIP-76 status to native diagnostics and RPC.

Malformed, oversized, duplicate, unsolicited, wrong-peer, stale-generation,
late, or policy-incompatible HIP-76 traffic must disable only HIP-76 for that
session. Ordinary Handshake and Denuo registry traffic must continue.

### Focused qualification

- Defaults advertise only ordinary network plus Denuo; no HIP-76 provider bit
  is present and no request is sent without an actual requester operation.
- Requester eligibility alone never advertises the provider service.
- Output opt-in with an unready backend advertises nothing.
- A ready test backend completes a live two-manager correlated request/response
  after Denuo negotiation.
- Exact PR fixtures, complete-payload maxima, duplicate/stale IDs, malformed
  DNS/EDNS, prohibited query types, queue pressure, timeout, disconnect, and
  policy revocation fail closed.
- Ordinary ping, headers, blocks, and unknown packets continue after each
  scoped HIP-76 failure.
- Native and RPC status agree and contain no qname or raw DNS body.

This milestone does not claim production recursion, a trusted DNS answer,
durable policy reload, signed-service discovery, ODoH, HNSR, wallet, or market
completion.

### Completion record

The canonical prerequisite is committed on `handshake-rs/hns-rs` main at
`dde2da81f29df935f043978a6d517c1d60ceff31`. The live-session implementation
is `5a35ab9d84da26ce20b8f343efde31e77d6fc898`; the final requester-opt-out
regression and canonical `handshake-rs/hns-node-rs` main are
`0e69319d11ca98d788466ed5028d8d897685e9f1`.

The focused checkpoint passes 63 `hns-p2p` library tests, 8 `hns-rpc` library
tests, 109 portable `hns-node` library tests, warning-denied Clippy for the
affected targets, formatting, and diff checks. The live plaintext regtest TCP
topology includes canonical Denuo negotiation, bounded `0xf0`/`0xf1` exchange,
no generic-packet leak, ordinary traffic after HIP activity, and a live
requester opt-out. The Brontide implementation carries the authenticated
remote static key into peer provenance; separate frame tests prove
authentication/decryption precedes typed frame classification, but do not
assert that provenance end to end. Exact limitations and retained commands are
in
`evidence/hip76-live-session-checkpoint-2026-07-26.md`.

## Next bounded ecosystem audit

The next independently committable audit is:

> Inventory and plan the remaining browser shared-engine consolidation from
> clean checkouts, without changing the already-qualified dual-root policy.

Automatic ICANN DANE and complete-host HNS/ICANN comparison already live in the
shared engine and are pinned by both mobile and Chromium consumers. The
remaining browser shells still contain historical gateway/runtime copies.
Before moving code, the audit should:

- map every remaining copied gateway/runtime crate and its active mobile,
  extension, or shared-engine consumers;
- identify the one canonical owner for DNS wire, DNSSEC, DANE, namespace
  selection, proxying, and platform-only adapters;
- prove from clean locked checkouts that both products consume the same exact
  engine revision and whole-request decision for navigation, redirects,
  subresources, Service Workers, downloads, and WebSockets;
- classify each copy as removable, platform-specific, or retained only for
  historical migration compatibility; and
- produce a staged, independently reversible consolidation sequence with
  platform gates and no path dependency on this coordination workspace.

The IANA suffix list must not return as classification authority during this
work. The audit is complete only when it leaves an exact file/dependency map,
fresh-checkout command evidence, and a minimal first consolidation
implementation slice with explicit acceptance gates. It does not itself
upgrade installed-browser or signed-device qualification.
