# Qualification matrix

Status vocabulary:

- `PASS`: directly demonstrated by retained command/output evidence.
- `PARTIAL`: a lower-level prerequisite passes, but the demanded integration
  has not been demonstrated.
- `NOT RUN`: no qualifying execution yet.

The assignment's minimum functioning integration is not complete:

Rows 1–26 preserve the earlier browser/node topology ledger. Row 13 is a
historical auction demonstration and is explicitly excluded from the current
wallet program; its `NOT RUN` status must not be reinterpreted as permission to
add OPEN/BID/REVEAL/REGISTER flows. Rows 27–38 are the wallet/marketplace
supplement. Only directly demonstrated scope is credited.

The 2026-08-02 production-continuation successors (`hns-rs` `81f2df26`, node
`3d346e3d`, wallet `5c5a13d4`, engine `6eb0174a`, and Chromium
`d58e1473`) do not inherit the earlier exact-revision PASS evidence and
therefore do not upgrade any row. Their fee/name/Shakedex primitives, exact
node fee quotes, private wallet ABI, provider hardening, Kyoto supervisor,
proxy admissions, recovery, and tracking code remain represented by the same
`PARTIAL`/`NOT RUN` topology outcomes until one consolidated gate and the
applicable multi-process or installed-product demonstrations run. Exact node
fee-quote adoption also remains unable to authorize value until released
`hns-script` 0.2 canonical fee algebra is integrated and qualified.

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
| 13 | historical wallet opens/bids/reveals/registers demonstration | NOT RUN: explicitly excluded from this wallet update; retained only for the earlier topology ledger |
| 14 | seller creates fixed listing | PARTIAL: canonical seller proof tested |
| 15 | second market discovers through DENUO_EXT | NOT RUN |
| 16 | buyer previews/verifies | PARTIAL: proof verification tested |
| 17 | buyer fulfills atomic swap | NOT RUN |
| 18 | fulfillment confirms through ordinary relay | NOT RUN |
| 19 | buyer finalizes name | NOT RUN |
| 20 | Dutch lowest price cannot execute early | PASS: permanent primitive regression |
| 21 | MeshMine coherent parent snapshot | PARTIAL: immutable external-node bridge and eight focused snapshot/binding tests pass; live node topology not run |
| 22 | mobile browser builds | PARTIAL: Android 0.5.5 version code 46 from `d24f85158854abb8be4a7bb9e914aebe5e7e4679` is signed, artifact-verified, and deployed to Google Play production; iOS 0.5.5 build 57 source/tag `d926561091634cd69fc9b7e79a4b76003fa4ee47` passed exact Apple CI `30454904736` and live App Store screenshot run `30454926117`; build 57 is `VALID` and its direct App Review submission is `WAITING_FOR_REVIEW` after protected upload run `30456522039`; the review path is manual and uses no TestFlight; installed Android/iOS device behavior and resolver-contact evidence remain open |
| 23 | Chromium extension builds | PARTIAL: public v0.5.5 source/tag `86b18497285753944ec1b9196ec05ee359c6db11` has 29 cross-platform MV3/native-host/Setup assets; macOS artifacts are signed and notarized, Windows artifacts remain unsigned, and documentation head `3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` passed hosted CI `30439859541`; installed catalog/browser proxy/restart/uninstall/policy-revocation matrices remain unrun |
| 24 | direct authoritative DNS remains first | PARTIAL: both five-contract adapters use and test direct UDP/TCP before authenticated authoritative DoH and a policy-admitted relay, with requester consent separate from every disabled browser provider/output role; packet-capture/full-process topology remains unrun |
| 25 | fallbacks remain locally DNSSEC/DANE validated | PARTIAL: the shared engine and both adapters test secure TLSA enforcement, authenticated denial/proven-insecure WebPKI, bogus/indeterminate fail-closed state, transport-aware TLSA owner derivation, and immutable complete-host root plans through canonical authority/status publication; the full live installed-browser/device matrix remains unrun |
| 26 | no public recursive resolver contacted | NOT RUN |

Primitive success never upgrades a topology row to `PASS`. Command transcripts,
ports/process IDs, registry IDs, packet traces with privacy-safe redaction,
wallet/market transaction IDs, browser build artifacts, and resolver-contact
evidence must be retained for the final run.

## Wallet and marketplace supplement

These rows extend the original topology matrix for the standalone wallet
program. They use the same evidence vocabulary.

| # | Required demonstration | Status |
| ---: | --- | --- |
| 27 | standalone wallet locked build, Clippy, tests, docs, dependency policy, and contract reproducibility | PASS at earlier exact wallet `8aa82dd9`: local `hns-wallet-rs/scripts/check.sh`; 34 Rust tests, warning-denied Clippy/docs, deterministic solc artifact comparison, and zero npm audit vulnerabilities. Current `5c5a13d4` has not run this gate |
| 28 | encrypted store, deterministic restore/key separation, lock, migration, workflow CAS, and replay protection | PARTIAL: HNS/ETH separation and focused store units pass at the earlier baseline; current source adds dedicated Bitcoin swap-key derivation, zeroizing private-ABI transport buffers, and atomic approval/workflow/reservation authorization around exact signed bytes, but complete recovery vectors, platform key wrapping, entity-complete migration, backup/rollback, and device persistence remain unavailable or unrun |
| 29 | hostile Provider API origin/permission/navigation/approval/rate/forbidden-method matrix | PARTIAL: Rust core negatives and 25 focused Chromium adapter tests pass at earlier exact revisions; current source adds private ABI v2 and namespace-plus-origin permission scoping, monotonic time checks, exact approval revalidation, lock/session rotation, and permission-bound event invalidation, but this source has not run its gate and no browser dispatches a wallet method through the live engine/ABI join |
| 30 | complete fixed-price Shakedex seller/buyer/recovery lifecycle over Denuo | PARTIAL: earlier canonical proof/state primitives and recovery ordering are tested; current unqualified `hns-rs` source adds strict TRANSFER/FINALIZE construction and listing-independent recovery from an exact FINALIZE coin, while current wallet source rejects every legacy 0.1 session entry/transition and live transaction, relay, restart, reorg, and regtest execution remain unrun |
| 31 | Kyoto direct-P2P restore/send/history/HTLC/reorg qualification | PARTIAL: actual Kyoto/BDK construction and HTLC units pass only at the earlier baseline; durable supervisor/history/broadcast journals and dedicated swap-key derivation now exist as later source, while pinned Kyoto header/filter/peer persistence, signed settlement, safe archival, P2P/regtest adversarial cases, and resource suites remain unavailable or unrun |
| 32 | Helios native-ETH wallet plus immutable contract qualification | PARTIAL: role-separated typed signing, fail-closed evidence policy, exact contract artifact, and Rust negatives pass; no embedded Helios producer, complete balance/history runtime, local-chain execution, rollback demonstration, approved deployment, or audit exists |
| 33 | HNS/BTC success, restart, reorg, and refund | NOT RUN |
| 34 | HNS/ETH success, restart, finality rollback, and refund | NOT RUN |
| 35 | price quorum, market intent/fill, Denuo board, griefing limits, and browser approval | PARTIAL: bounded canonical protocol and local reservation/session units exist; governance, live relay, integration, and adversarial board suite not run |
| 36 | Chromium installed extension/provider/native-host/demo dapp | PARTIAL: the source bridge, approval/event lifecycle, and 25 focused JavaScript tests pass at earlier exact revisions; current `d58e1473` statically aligns discovery to private ABI/service protocol 2 and closes the 12-kind public projection/event boundary, but it ran no gate, the native host still reports unavailable, every launch/provider/value gate is false, and no installed-browser engine/ABI E2E exists |
| 37 | Android/iOS signed-device wallet/provider screens and secure storage | PARTIAL: Android provider/key-store sources and tests compile in the focused Gradle path and iOS project references are present; adapters are source-hardwired unavailable, screens/controller/FFI wiring do not exist, Swift/Xcode was unavailable, and no signed-device run occurred |
| 38 | Bitcoin disk/bandwidth/startup/mobile-memory benchmark matrix | NOT RUN: no values estimated |
