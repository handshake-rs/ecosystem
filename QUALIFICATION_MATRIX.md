# Qualification matrix

> **Audit status (2026-09-02):** This matrix preserves the qualification state
> of its August implementation checkpoint. Several source and publication rows
> have since advanced, notably the published protocol/wallet cohorts and the
> Shakescape `1.0.x` native wallet. Use [`CURRENT_STATE.md`](CURRENT_STATE.md)
> for present status and read each row below only against its cited revision.

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

The authoritative 2026-08-10 remote heads are `hns-rs` `a93ba7a`, node
`063ba6b`, wallet `4cd9a61`, engine `84005f1`, Chromium `bfa0899`, and mobile
`e8d6a0b`. `hns-rs` current-head CI passes, and its source predecessor
`b33b346` passed the full hosted protocol and RustSec gate. Engine and Chromium
current-head CI/CodeQL are green.
Mobile's exact-head documentation/policy gate passes and its source predecessor
`85647ae` passed full hosted CI; full Chromium passed at source predecessor
`08ba480`. Wallet current-head CI failed strict Clippy in HNS workflows. Node
`063ba6b` has a focused exact-head `hns-store` strict-Clippy pass after the
failed predecessor, while its hosted CI/container reruns are pending. None of
those results demonstrates a native wallet
binding, enabled value gate, published wallet ABI, installed provider, or P2P
marketplace lifecycle, so the applicable rows remain `PARTIAL` or `NOT RUN`.
The detailed source and run ledger is in `REFERENCE_COMMITS.md`.

These columns are never collapsed into one “ready” label: implemented source,
exact-head test evidence, product wiring, value enablement, artifact
publication, and installed qualification are separate assertions. A green
browser build or an older public browser artifact does not establish the last
four wallet/marketplace assertions.

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
| 9 | HNSR requester/output inactive until enabled; opaque relay independently opt-out | PARTIAL: exact-head protocol qualification covers independent role defaults, requester transport defaults, bounded reservations, and circuit runtime state; the required product/full-node role topology remains unrun. |
| 10 | HNSR route and relayed inner peer | PARTIAL: exact-head protocol qualification covers HNSA named routes, HNSR route service, bounded circuit runtimes, and non-node chat/web profiles; engine source adds durable authority-bound HNSA admission. No browser-to-live-relay inner peer has been demonstrated. |
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
| 22 | mobile browser builds | PARTIAL: Android release artifacts and store deployment are retained at the documented release sources; iOS 0.5.5 build 57 source/tag `d926561091634cd69fc9b7e79a4b76003fa4ee47` passed exact Apple CI `30454904736`, screenshot run `30454926117`, and protected upload `30456522039`, then became public on 2026-07-31 without TestFlight. Current remote `e8d6a0b` passes its documentation/policy gate, source predecessor `85647ae` passes full hosted CI, and that predecessor's Android debug APK installed and cold-launched. The installed wallet/provider and full resolver-contact matrices remain open. |
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
| 27 | standalone wallet locked build, Clippy, tests, docs, dependency policy, and contract reproducibility | PARTIAL: earlier exact wallet `8aa82dd9` passed local `hns-wallet-rs/scripts/check.sh` with 34 Rust tests, warning-denied Clippy/docs, deterministic solc artifact comparison, and zero npm audit vulnerabilities. Current remote `4cd9a61` failed hosted run `31372389330` on strict Clippy in HNS workflows; a successor fix is in progress and no current consolidated PASS is recorded. |
| 28 | encrypted store, deterministic restore/key separation, lock, migration, workflow CAS, and replay protection | PARTIAL: current source includes schema-v3 encrypted entities, monotonic permission tombstones, approval/workflow/reservation CAS, separate HNS name/Shakedex scans and key allocation, and an account-authenticated encrypted aggregate BDK snapshot. Focused predecessor evidence exists, but current consolidated CI fails strict Clippy; platform key wrapping, populated schema-v1 import, legacy BDK SQLite import, backup/rollback, cross-process/device persistence, and complete recovery qualification remain open. |
| 29 | hostile Provider API origin/permission/navigation/approval/rate/forbidden-method matrix | PARTIAL: current source has the exact 43-method vocabulary, authority/permission/session binding, approval-schema-v3 name disclosures, and library-only exact-account plus synchronized-read compositions including `hns_requestAccounts`/`hns_accounts`. The checked-in executable remains control-only, current consolidated CI does not pass, and no browser dispatches through a released native engine/ABI join; installed hostile-origin/restart matrices remain pending. |
| 30 | complete fixed-price Shakedex seller/buyer/recovery lifecycle over Denuo | PARTIAL: current canonical protocol source has exact listing/cancellation/fulfillment/recovery and TRANSFER/FINALIZE primitives, while wallet source adds an encrypted fixed-price board, canonical transaction plans, key allocation, durable value workflows, and terminal reservation release. All Shakedex canonical-V2, Denuo-V2, and value release gates remain false; product coin selection, live relay, provider/trusted-UI dispatch, restart/reorg, and regtest execution remain unavailable or unrun. |
| 31 | Kyoto direct-P2P restore/send/history/HTLC/reorg qualification | PARTIAL: actual Kyoto/BDK construction, durable supervisor/history/broadcast journals, dedicated swap-key derivation, and encrypted aggregate BDK persistence exist in source. The aggregate is capped at 1 MiB; durable Kyoto header/filter/peer state, a legacy BDK SQLite importer, signed settlement, safe archival, P2P/regtest adversarial cases, and resource suites remain unavailable or unrun. |
| 32 | Helios native-ETH wallet plus immutable contract qualification | PARTIAL: role-separated typed primitives, fail-closed evidence policy, exact contract artifact, and Rust negatives pass only at the earlier exact baseline; current unqualified source advertises offline receive derivation only, keeps synchronization/history/send/value/settlement/mainnet false or unavailable, requires opaque unissued Helios/value/settlement permits, and contains exact-fee/role/address-bound signing plus a zeroizing non-cloneable/non-serializable signed payload with no raw accessor and redacted diagnostics; no current gate, embedded Helios producer, balance/history runtime, controlled broadcast/recovery, local-chain execution, rollback demonstration, approved deployment, or audit exists |
| 33 | HNS/BTC success, restart, reorg, and refund | NOT RUN |
| 34 | HNS/ETH success, restart, finality rollback, and refund | NOT RUN |
| 35 | price quorum, market intent/fill, Denuo board, griefing limits, and browser approval | PARTIAL: canonical market envelopes and a bounded encrypted replay/tombstone-safe fixed-price board with restart watermarks exist, together with durable wallet reservation/session workflows. Reporter governance, live relay/outbox supervision, peer policy, browser approval, and adversarial board qualification remain absent or unrun. |
| 36 | Chromium installed extension/provider/native-host/demo dapp | PARTIAL: current remote `bfa0899` contains signed-wallet artifact admission, approval-schema-v3 source, and consolidated shared-engine dependencies; its exact-head CI/CodeQL are green and full hosted CI also passed at source predecessor `08ba480`. A Chromium extension is installed locally, but no exact wallet artifact launches, the native wallet/provider/value gates remain false, and no installed engine/ABI/provider E2E exists. |
| 37 | Android/iOS signed-device wallet/provider screens and secure storage | PARTIAL: current remote `e8d6a0b` contains approval-schema-v3 and consolidated shared-engine browser source; exact-head documentation/policy CI and predecessor `85647ae` full hosted CI pass. The predecessor Android debug browser installed and launched, but all four wallet release gates remain false, the unavailable adapter is hardwired, and controller, wallet runtime, generated JNI/C binding, native approval UI/event production, and signed-device wallet execution remain absent. |
| 38 | Bitcoin disk/bandwidth/startup/mobile-memory benchmark matrix | NOT RUN: no values estimated |
