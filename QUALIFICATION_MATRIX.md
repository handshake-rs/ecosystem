# Qualification matrix

Status vocabulary:

- `PASS`: directly demonstrated by retained command/output evidence.
- `PARTIAL`: a lower-level prerequisite passes, but the demanded integration
  has not been demonstrated.
- `NOT RUN`: no qualifying execution yet.

The assignment's minimum functioning integration is not complete:

The 2026-07-25 consent clarification refines rows 9–11: the HNSR
requester/client, endpoint/output, and rendezvous roles remain opt-in, while
opaque relay capacity is default-on with a persistent opt-out. The topology
test must demonstrate those independent roles rather than a single HNSR
enable/disable Boolean.

| # | Required demonstration | Status |
| ---: | --- | --- |
| 1 | two Rust full nodes start | NOT RUN |
| 2 | registry fingerprints match | PARTIAL: canonical generator/unit tests pass |
| 3 | standard Handshake P2P continues | PARTIAL: exact frame/packet vectors pass |
| 4 | HIP 76 requester/relay validated exchange | PARTIAL: protocol codec tests pass |
| 5 | HIP 76 opt-out disables requester | PARTIAL: shared policy generation tests pass |
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
| 22 | mobile browser builds | PARTIAL: 469 Git-pinned Rust tests, strict Clippy, cargo-deny, and the C/C++ Apple ABI gate pass; Android SDK/NDK, Xcode, simulator, signed devices, and rebuilt store screenshots remain unrun |
| 23 | Chromium extension builds | PARTIAL: 481 focused Git-pinned Rust tests, strict Clippy, cargo-deny, six Node suites, and the unpacked MV3 build pass; installed-browser/platform matrix not run |
| 24 | direct authoritative DNS remains first | NOT RUN |
| 25 | fallbacks remain locally DNSSEC/DANE validated | PARTIAL: both browser adapters test authenticated absence/proven-insecure WebPKI, secure TLSA enforcement, bogus/indeterminate failure, and immutable selected-root plans; full live browser matrix not run |
| 26 | no public recursive resolver contacted | NOT RUN |

Primitive success never upgrades a topology row to `PASS`. Command transcripts,
ports/process IDs, registry IDs, packet traces with privacy-safe redaction,
wallet/market transaction IDs, browser build artifacts, and resolver-contact
evidence must be retained for the final run.
