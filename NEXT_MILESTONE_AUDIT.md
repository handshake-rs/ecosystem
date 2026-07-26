# Next ecosystem milestone audit

Date: 2026-07-26

Status: successive milestones completed and pushed; next bounded audit identified

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

The next milestone identified at that checkpoint was:

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

## Completed browser audit and next bounded milestone

The browser shared-engine inventory and first implementation slice are complete
at:

- mobile `cde7d6d9d15859ebd5c4169433e72a7e434b2c1b`;
- Chromium `13dbb87240807dda0fb6f72c7aaaa7a33d036e70`; and
- unchanged shared engine `127b9ad55852df00b4df40826517715048dc3571`.

Both products now derive relay-requester admission from the shared
`hns-resolution-policy` transport plan without changing platform persistence
or ABI meaning. Requester off maps to `Disabled`, requester on maps to `Auto`,
all browser provider roles remain off, and live HNS resolution is direct
authoritative UDP/TCP before authenticated authoritative DoH and any admitted
relay. Separate offline clean-clone gates passed. The exact duplicate map,
staged migration, commands, and limitations are retained in
`evidence/browser-engine-consolidation-audit-2026-07-26.md`.

The next independently committable milestone is:

> Make the complete `hns-dane-engine` dependency graph build from a shallow
> standalone clone before migrating another browser trust boundary.

At that checkpoint, seven deeper engine crates reached `hns-rs` through
coordination-workspace `../../../hns-rs` paths. That prevented independent
consumption of the full facade, resolver, transport, P2P transport, loopback
proxy, and testkit. Its acceptance scope was:

- choose and enforce one reviewed immutable `handshake-rs/hns-rs` source
  revision for every engine dependency, with no branch, tag, sibling path, or
  duplicated protocol implementation;
- regenerate and audit all locks, source-policy tests, and `cargo-deny` rules;
  determine the SBOM/license/notice impact and retain any missing release
  artifact generator as an explicit blocker;
- prove `cargo metadata --locked`, formatting, warning-denied all-target
  Clippy, both workspace test forms, all-feature release build, ABI smoke, and
  every implemented fuzz smoke from a shallow engine clone with no
  coordination siblings, without treating the current lack of executable fuzz
  targets as a pass;
- document the package-name collisions and OpenSSL-versus-ring/rustls adapter
  boundary that consumers must address next; and
- leave both browser pins unchanged until the standalone engine commit is
  qualified and independently revertible.

After that gate, the next browser slice can rename local adapters, adopt one
deeper canonical engine boundary at a time, and finally remove the Chromium
repository's historical mobile-only trees. The IANA suffix list must not
return as classification authority, and bogus DNSSEC must remain distinct from
authenticated absence throughout. This work does not itself upgrade
installed-browser or signed-device qualification.

## Completed standalone-engine successor

The standalone-engine milestone is committed and pushed on
`handshake-rs/hns-dane-engine` main at
`2850ac1f50e361e2772e18f2e5ecbd7e77085afb`. All 24 declarations in the seven
consumer manifests now inherit one reviewed canonical `hns-rs` source at
`dde2da81f29df935f043978a6d517c1d60ceff31`. The lockfile binds the nine
direct packages and two transitive packages to that same revision.

Twelve source-policy tests, the exact source verifier, `cargo-deny`, 144
workspace tests in every required form, 20 doc-test targets, warning-denied
all-target/all-feature Clippy, the all-feature release build, formatting, and
the C11 ABI header smoke pass. The complete gate also passes offline after one
locked fetch in a depth-one clone with an isolated Cargo home and no sibling
`hns-rs` tree. The new hosted workflow was added but was not polled or counted
as passing. Exact evidence is in
`evidence/hns-dane-engine-standalone-checkpoint-2026-07-26.md`.

The three browser contracts were then advanced without runtime-source changes
to that qualified revision on mobile
`7b826166a2bac3af8d2384dbff9875a992f252ca` and Chromium
`1fde772006dde8b36c963b3ecc09cc011c542155`. Their exact-source policies,
lockfiles, deterministic notices, focused Rust gates, and Chromium extension
gate pass.

## Next bounded browser consolidation milestone

The next independently committable browser milestone is:

> Resolve the browser/engine Cargo name collisions, then adopt the canonical
> engine authority lifecycle and observability contracts in both products.

The slice should start with the duplicated browser-local
`hns-browser-runtime` name. Rename the platform-owned socket, storage, proxy,
download, WebSocket, and lifecycle adapter without changing its persisted
settings or public ABI. Both products can then consume canonical
`hns-browser-runtime` and `hns-browser-observability` from the same exact
engine revision.

Acceptance requires:

- one documented owner for the authority state graph, runtime session,
  generation/event admission, evidence-state taxonomy, and status schema;
- stale session, generation, event, redirect, subresource, Service Worker,
  download, and WebSocket work rejected before origin connection;
- platform adapters retaining sockets, secure storage, process lifecycle, UI,
  native messaging, and packaging without reimplementing trust decisions;
- exact Git/lock/source-policy and deterministic notice checks remaining green
  in both standalone browser clones;
- no persisted-setting, Android/iOS ABI, native-message, PAC, or proxy policy
  reinterpretation; and
- the Chromium repository's inactive mobile trees retained only until their
  history/evidence comparison is complete, then removed in a separate
  reviewable trim.

This slice does not yet migrate the complete live resolver/DNSSEC/DANE/proxy
implementation and does not upgrade installed-browser or signed-device
qualification.

## Completed authority and observability successor

The shared engine successor is committed on `handshake-rs/hns-dane-engine`
main at `a03648ec85a115362ebc2ab24bb9ea0f1be127fc`. It makes five canonical
contracts independently consumable:

- `hns-browser-runtime`;
- `hns-browser-observability`;
- `hns-icann-dane`;
- `hns-namespace-resolution`; and
- `hns-resolution-policy`.

The platform-owned runtime packages were first renamed at mobile
`5ef5cb9ec66ea460b4168946a7d2d0bba7c2f141` and Chromium
`0334126fa4f5a6d5ae14d15b2584b64e0c8985b3`, so the products can consume the
canonical authority crate without a Cargo package collision. Their final
consumer revisions are retained in `REFERENCE_COMMITS.md`.

Both portable adapters bind one checked nonzero runtime session to the active
proxy generation, mint an engine event stamp before DNS/classification work,
and require that exact stamp through response or tunnel-head publication.
Policy change and degraded, revoked, or stopped lifecycle transitions
permanently invalidate earlier work; recovery cannot resurrect it. The
adapters retain typed request-local root failures and namespace decisions,
including `Neither`, and emit schema-v2 name-free status without parsing
diagnostic JSON or inventing negotiated P2P identity. ICANN bogus or
indeterminate DNSSEC keeps validating-DoH provenance and fails closed; HNS
failure remains unavailable transport; unrelated post-selection errors cannot
be mislabeled as DANE or SNI evidence.

The final Chromium repository boundary also removes the historical
Android/iOS product trees after their retained history was compared with the
canonical mobile repository. That is a source-boundary cleanup, not installed
Chromium qualification. It safely advances only the repository-boundary half
of the historical later trim stage; it does not skip or complete the earlier
installed-device and installed-browser qualification stages.

Exact source/lock/notice checks, stale-work regressions, test counts, final
consumer and trim revisions, and environmental limitations are retained in
`evidence/browser-authority-runtime-checkpoint-2026-07-26.md`.

## Next bounded browser proxy-core milestone

The next independently committable browser milestone is:

> Make `hns-dane-engine` own the platform-neutral loopback proxy admission and
> publication core, while Android, iOS, and Chromium keep their native
> listener, certificate-store, TLS-I/O, and lifecycle adapters.

This is stage 5 of the previously recorded reversible consolidation sequence.
It precedes the larger live resolution-core migration. The current same-name
`hns-loopback-proxy` packages conceal materially different APIs: browser-local
crates own complete socket/TLS servers, while the engine crate owns only an
older CONNECT/capability admission gate. A path substitution would therefore
be unsafe.

### Engine checkpoint

- Rebase the engine proxy contract on the canonical checked runtime
  session/generation/event types rather than a parallel bridge clock.
- Own strict host/port normalization, numeric-loopback admission,
  per-instance capability validation, HTTP head/header bounds, pending-request
  capacity, exact-origin binding, and lifecycle revocation.
- Represent response, local-error, download, and `101` publication as typed
  capabilities that carry the exact admitted stamp.
- Require one atomic publication boundary for any durable namespace choice or
  cache-visible side effect and the corresponding HTTP/`101` head write and
  flush.
- Hold the authority permit only through head publication. Response bodies and
  tunnel I/O must own revocation-aware guards without blocking policy changes
  indefinitely.
- Signal cancellation before any lifecycle operation waits for an in-flight
  permit, and bound every listener/worker join.
- Keep platform CA keys, exact-host leaf issuance, socket accept loops, TLS
  termination, browser authentication callbacks, and native packaging outside
  the engine crate.

### Consumer checkpoints

- Rename the platform-local complete-server adapters before adding the exact
  engine dependency; do not hide the collision behind a Cargo alias.
- Adopt mobile and Chromium separately so each consumer revision is
  independently revertible.
- Preserve Android/iOS ABIs, native-messaging schema, PAC behavior, persisted
  policy meaning, local-CA identity, and current listener endpoints.
- Prove that navigation, redirect, subresource, Service Worker, download,
  WebSocket, generated-error, and upgrade paths cannot publish or persist
  routing state from stale work.
- Keep all five current engine contracts and add the proxy-core contract from
  one immutable engine revision, with matching locks, source policy,
  `cargo-deny`, notices, and shallow standalone builds.

### Focused qualification

- wrong endpoint, realm, capability, method, host syntax, port, header count,
  head size, session, generation, event, or proxy instance fails closed;
- same-generation degrade/recover and listener replacement cannot publish an
  old success, error, download, sticky binding, or `101` head;
- cancellation/revocation completes under a deliberately blocked head writer,
  and the authority permit is released before a deliberately blocked response
  body or tunnel read;
- ordinary Chromium and mobile proxy behavior remains green under their
  existing portable suites; and
- engine full checks plus both consumer format, warning-denied Clippy,
  test/source/notice, and platform-neutral packaging gates pass.

This checkpoint will not yet replace the browser-local DNS wire, light-chain,
DNSSEC, DANE, resolver, origin transport, or gateway implementations. It also
will not upgrade installed-browser, Android device, iOS device, store-signing,
or the PDF's 26-row topology qualification.
