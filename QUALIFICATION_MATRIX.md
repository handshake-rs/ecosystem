# Qualification matrix

Status vocabulary:

- `PASS`: directly demonstrated by retained command/output evidence.
- `PARTIAL`: a lower-level prerequisite passes, but the demanded integration
  has not been demonstrated.
- `NOT RUN`: no qualifying execution yet.

The assignment's minimum functioning integration is not complete:

The 2026-07-25 consent clarification separates transport from output
authority: opaque P2P relay capacity is default-on with an opt-out policy,
while any endpoint/output role remains explicit opt-in. HIP-76 requester
eligibility defaults to `Auto` with an independent opt-out and never
advertises provider capacity. Live revocation is tested, while durable
operator-policy persistence and reload are still open. HNSR client,
endpoint/output, and rendezvous are distinct roles and currently remain
independently opt-in. The topology test must demonstrate these independent
roles rather than a single enable/disable Boolean.
The browser products intentionally use a stricter product default: new and
persisted profiles keep requester relay off until explicit opt-in, mapping
false to `Disabled` and true to direct-first `Auto`, while P2P services and all
provider/output roles remain zero.

| # | Required demonstration | Status |
| ---: | --- | --- |
| 1 | two Rust full nodes start | PASS: two isolated release-mode `hsrd` processes start on regtest with distinct durable state, RPC, and P2P listeners and shut down cleanly after retained diagnostics |
| 2 | registry fingerprints match | PASS: both full-node processes report fingerprint `95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d`, phase `negotiated`, and exactly one negotiated registry peer |
| 3 | standard Handshake P2P continues | PASS: both full-node peers remain ordinary `ready` plaintext peers after registry negotiation and report 393 bytes sent and received in each direction; the separate in-process regression also exchanges `GetAddr` after negotiation and scoped extension failure |
| 4 | HIP 76 requester/relay validated exchange | PARTIAL: two live TCP peer managers complete strict DNSSEC-shaped f0/provider-work/f1 exchange with correlated per-admission provenance and no generic-packet leak; a production recursive/DNSSEC-validating backend and full-node process topology have not run |
| 5 | HIP 76 opt-out disables requester | PARTIAL: the live requester policy is replaced with disabled, new HIP work fails closed, and ordinary P2P continues; durable operator-policy restart has not been demonstrated |
| 6 | HIP 77 through distinct proxy/target peers | PARTIAL: requester/target crypto round trip only |
| 7 | proxy observes no plaintext qname | PARTIAL: HPKE boundary tested, topology not run |
| 8 | ODoH opt-out disables path | PARTIAL: shared policy types tested |
| 9 | HNSR requester/output inactive until enabled; opaque relay independently opt-out | PARTIAL: independent role defaults and migration tested |
| 10 | HNSR route and relayed inner peer | PARTIAL: records/store/envelopes tested |
| 11 | disabling an HNSR role withdraws/closes only that role's state | NOT RUN |
| 12 | block traverses HNSR inner connection | NOT RUN |
| 13 | wallet opens/bids/reveals/registers | NOT RUN |
| 14 | seller creates fixed listing | PARTIAL: canonical seller proof tested |
| 15 | second market discovers through DENUO_EXT | NOT RUN |
| 16 | buyer previews/verifies | PARTIAL: proof verification tested |
| 17 | buyer fulfills atomic swap | NOT RUN |
| 18 | fulfillment confirms through ordinary relay | NOT RUN |
| 19 | buyer finalizes name | NOT RUN |
| 20 | Dutch lowest price cannot execute early | PASS: permanent primitive regression |
| 21 | MeshMine coherent parent snapshot | PARTIAL: immutable external-node bridge and eight focused snapshot/binding tests pass; live node topology not run |
| 22 | mobile browser builds | PARTIAL: exact implementation-head CI passes the complete Rust/supply-chain gate, Android build/tests/lint and unsigned-bundle structure, and Apple ABI/XCFramework/XCTest/simulator/device-link jobs; atomic staged header maintenance and all five format-safe diagnostics are covered, and current main links live Google Play/App Store listings; signed 0.5.3 candidate verification, installed Android/iOS device behavior, and rebuilt store-screenshot evidence remain open |
| 23 | Chromium extension builds | PARTIAL: public v0.5.5 source/tag `86b18497285753944ec1b9196ec05ee359c6db11` has 29 cross-platform MV3/native-host/Setup assets; macOS artifacts are signed and notarized, Windows artifacts remain unsigned, and documentation head `3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` passed hosted CI `30439859541`; installed catalog/browser proxy/restart/uninstall/policy-revocation matrices remain unrun |
| 24 | direct authoritative DNS remains first | PARTIAL: both five-contract adapters use and test direct UDP/TCP before authenticated authoritative DoH and a policy-admitted relay, with requester consent separate from every disabled browser provider/output role; packet-capture/full-process topology remains unrun |
| 25 | fallbacks remain locally DNSSEC/DANE validated | PARTIAL: the shared engine and both adapters test secure TLSA enforcement, authenticated denial/proven-insecure WebPKI, bogus/indeterminate fail-closed state, transport-aware TLSA owner derivation, and immutable complete-host root plans through canonical authority/status publication; the full live installed-browser/device matrix remains unrun |
| 26 | no public recursive resolver contacted | NOT RUN |

Primitive success never upgrades a topology row to `PASS`. Command transcripts,
ports/process IDs, registry IDs, packet traces with privacy-safe redaction,
wallet/market transaction IDs, browser build artifacts, and resolver-contact
evidence must be retained for the final run.
