# Cross-project reconciliation

## Authority and dependency direction

```text
hns-rs 0.1 released crates ────────────> hns-wallet-rs foundation
hns-rs exact immutable protocol pin ──> hns-node-rs ──> MeshMine bridge

hns-rs 0.2 marketplace/name-codec release - - -> node / wallet (blocked)
hns-node-rs wallet RPC v1       ═══════> hns-wallet-rs adapter (source-complete; unqualified)
hns-wallet-rs versioned ABI     - - - -> mobile / Chromium (not released/wired)

hns-wallet-rs
  ├──> durable bounded Kyoto direct-P2P Bitcoin supervisor source
  └──> selected Helios Ethereum evidence policy (runtime not embedded)

hns-rs ── exact immutable protocol pin ──> hns-dane-engine
  ├──> hns-icann-dane
  ├──> hns-namespace-resolution
  ├──> hns-resolution-policy
  ├──> hns-browser-runtime
  ├──> hns-browser-observability
  └──> five canonical contracts consumed by:
          ├──> Android/iOS browser adapter
          └──> Chromium extension/native host

hns-dane-engine opaque proxy authority - - -> mobile / Chromium (not consumed)

hns-dane-crawler ── optional observed remediation handoff
                  └──> hns-dane-bootstrap-generator ──> operator-published DNS
```

Solid arrows are current compiled dependencies. The double arrow is a
source-complete versioned process contract without a sibling crate dependency;
it remains unqualified. Dashed arrows are designed or unpublished joins that
remain unavailable; compatible schemas do not constitute product integration.

The encrypted user wallet and atomic-market application belong in standalone
`hns-wallet-rs`; validated Handshake indexes/RPC and bounded untrusted Denuo
relay storage belong in `hns-node-rs`; canonical wire/consensus semantics and
registry assignments belong in `hns-rs`. MeshMine must not become a dependency
of `hns-rs`, `hns-node-rs`, the wallet/market, the DANE engine, or either
browser shell.

## One owner per concern

| Concern | Canonical owner |
| --- | --- |
| semantic consensus/wire/registry types | `hns-rs` |
| chain, P2P runtime, validated indexes/RPC, and bounded Denuo relay | `hns-node-rs` |
| encrypted keys/state, wallet/name workflows, Provider API, Shakedex, external-chain settlement | `hns-wallet-rs` |
| mining application, DAG/settlement, external-node adapter | `MeshMine` |
| DNS wire, DNSSEC, authenticated resolution, TLSA/DANE, policy ABI | `hns-dane-engine` |
| ICANN TLSA-owner derivation and browser trust decision | `hns-dane-engine/crates/hns-icann-dane` |
| full-host HNS/ICANN comparison and namespace precedence | `hns-dane-engine/crates/hns-namespace-resolution` |
| direct-first transport admission and independent requester/provider roles | `hns-dane-engine/crates/hns-resolution-policy` |
| browser authority state, checked runtime sessions, and generation/event admission | `hns-dane-engine/crates/hns-browser-runtime` |
| schema-v2 trusted browser status and evidence/transport topology | `hns-dane-engine/crates/hns-browser-observability` |
| Android/iOS lifecycle and UI | `hns-dane-browser-mobile` |
| native messaging, mandatory PAC/proxy lifecycle, Chromium UI, cross-platform Setup, and release signing | `hns-dane-browser-extension` |
| namespace topology snapshots and observational DANE-readiness reports | `hns-dane-crawler` |
| operator-authored delegation, DNSSEC/DS, TLSA, and appliance material | `hns-dane-bootstrap-generator` |

## Reconciliation rules

The 2026-07-25 user clarification refines the assignment's broad
requester/provider wording: consent follows whether a node is merely an opaque
P2P forwarder or can act as an output, not a blanket “all provider roles
opt-in” rule.

- No protocol number is duplicated as an untyped literal outside a
  compatibility fixture.
- Standard HSD packet types and Denuo assignments occupy separate semantic
  namespaces.
- Opaque P2P forwarding is installed and enabled by default with a durable
  opt-out. A role that can see the plaintext request, originate an external
  request, terminate a circuit, or otherwise act as an output node remains
  explicit opt-in. Relay consent never grants output-node consent.
- Concretely, the HIP 76 DNS relay is an output node and defaults off; the HIP
  77 ODoH proxy is an opaque relay and defaults on with opt-out; the HIP 77
  target defaults off; the HNSR opaque relay defaults on with opt-out; and
  HNSR endpoint/output and rendezvous roles default off. Requester/client
  policy is represented and revoked independently. HIP 76 requester
  eligibility defaults to `Auto` with independent opt-out and never advertises
  output capacity; durable node-policy reload remains a separate gate.
- Direct authoritative DNS remains first. Relay transport never confers
  validation authority; DNSSEC, TLSA, and DANE are local.
- Browser relay controls are requester controls only. New and persisted
  browser profiles start false/off and require explicit user opt-in; false
  maps to `Disabled` and true maps to direct-first `Auto`. Browser P2P
  `VERSION` services and all opaque-relay, output-node, target, market, and
  HNSR provider roles remain zero/disabled rather than inheriting generic
  provider defaults.
- ODoH-required never falls back to a plaintext relay.
- HNSR requester and output roles remain inactive until independently enabled.
  An enabled opaque relay transports an inner Brontide session and never
  becomes chain, DNS, application, or output authority.
- Every DNS-named ICANN HTTPS/WSS origin derives its TLSA owner from the
  effective host, port, and transport. Secure presence enforces DANE; WebPKI
  is allowed only after authenticated absence or a proven insecure
  delegation; bogus and indeterminate DNSSEC fail closed.
- That ICANN decision is made below the browser shells and applies at their
  request boundary to navigations, redirects, subresources, Service Workers,
  downloads, and WebSockets. The accurate transport label is **DANE via ICANN
  DoH**.
- A user-configured recursive HNS DoH recovery endpoint is a separate
  blank-by-default consent boundary. Its ICANN hostname is bootstrapped only
  through validating ICANN DoH, its connection uses exact public addresses
  plus WebPKI for that hostname, and its returned HNS DNS remains untrusted
  until local proof, DNSSEC, TLSA, and DANE validation. It is eligible only
  after admitted direct, owner-authoritative, and requester transports fail
  for a transport reason; it cannot mask bogus DNSSEC or stale/missing proofs.
- Namespace ownership is decided from two independently validated complete
  origin plans, never from an IANA suffix list. The shared classifier retains
  HNS-only, ICANN-only, convergent, divergent, neither, and indeterminate
  states; applies exact-origin pin, successful sticky binding, then ICANN
  first-use precedence; and never combines address, service, or trust records
  across roots.
- Crawler snapshots are observational inputs only. They may identify a
  remediation candidate and populate a generator handoff, but they never
  classify a live browser hostname or authorize TLS.
- Bootstrap-generator output remains an operator-reviewed control-plane
  artifact. A published record becomes security policy only when obtained and
  validated through the applicable live DNSSEC chain.
- Marketplace discovery is best-effort untrusted gossip. Every listing and
  fulfillment is locally verified against chain state and the seller proof.
- Website wallet-provider injection requires the canonical engine's exact
  logical-origin decision. Permission and approval state in `hns-wallet-rs`
  cannot override a denied, stale, insecure, mismatched-port, or degraded
  browser-authority decision.
- Mining authority consumes only a coherent committed node snapshot and is
  rechecked before publication.

## Current unresolved joins

- The node consumes the exact canonical `hns-rs` Denuo/HIP-76 checkpoint and
  now runs bounded live HIP-76 sessions. Its functional readiness matrix is
  complete. The base snapshot's `pre-authority` release stage is replaced in
  live native RPC by a mode-specific diagnostic label; runtime authority
  remains conditional on the synchronized durable canary. A production
  recursive and
  DNSSEC-validating output backend, durable operator-policy restart, HIP 77/78,
  wallets, marketplace messages, and broader shared primitive adoption remain.
- `hns-wallet-rs` now exists as an independent workspace with encrypted secret
  records, origin-bound Provider API policy, persisted Shakedex/market state,
  a source-complete HNS `ChainModule`/`AtomicSettlement` runtime and strict
  node RPC v1 adapter, a durable bounded Kyoto/BDK supervisor, and a narrow
  Ethereum contract/evidence boundary. HNS value remains hard-disabled while
  node policy-vbyte and wallet weight fee units differ; names remain watch-only
  until the unpublished canonical codec is released and a dedicated name-role
  scan exists. Bitcoin still lacks durable Kyoto header/filter/peer state,
  safe archival, dedicated swap-key derivation, and signed settlement;
  Ethereum lacks the Helios evidence producer. Released marketplace protocol
  consumption, live browser ABI integration, real-chain restart/reorg suites,
  resource benchmarks, and independent security review remain blockers.
- The node's confirmed/mempool wallet indexes, Shakedex/HTLC/preimage tracker,
  typed backend, and authenticated loopback RPC v1 are source-complete at
  `74f7ae36`; the strict wallet consumer is source-complete at `76885098`.
  Neither successor was built or tested. The five-role marketplace relay is a
  bounded cache/policy core only, Denuo V2 wire advertisement is disabled
  until canonical V2 adoption, and registry retirement/capacity reclamation
  remains absent.
- MeshMine now consumes an exact immutable `handshake-rs/hns-node-rs` revision
  through its bridge. Its `504d3fed035feb8a637ca09c4e0816b6e1144622`
  pin has complete functional readiness but predates the standalone
  Denuo/HIP-76 session; the coherent parent/job topology has not yet been
  demonstrated end to end.
- Both browser adapters now submit independently resolved complete HNS and
  ICANN plans to the shared full-host policy, consume the same typed transport
  policy and canonical authority/status contracts, and expose the selected
  namespace. One checked nonzero runtime session and active proxy generation
  bind admission; stale generations/events cannot publish responses or trusted
  status after lifecycle invalidation. Installed-browser and signed-device
  matrices still need to prove those semantics through platform network
  processes, restarts, redirects, workers, downloads, and WebSockets.
- Both products now perform long-running header/peer work in private staged
  databases and atomically publish validated header, peer, and readiness
  generations. Chromium additionally retains mandatory PAC control through
  native-host replacement and transient due-but-unexpired maintenance
  failures. The shared engine now contains an opaque-authority-bound loopback
  proxy admission/publication core at source head `f76ad372`; these products
  do not consume it yet.
- Browser adapters still contain platform-owned gateway, resolver, proxy, and
  network code around the five canonical contracts. Proxy-core and live
  resolver/DNSSEC/DANE consumption remain broader shared-engine consolidation.
  The Chromium repository's inactive historical mobile product trees were removed
  in a separate repository-boundary commit after their retained source was
  compared with canonical mobile.
- Wallet-provider source adapters are fail-closed and deliberately inactive:
  Chromium's native host reports `walletUnavailable`, while Android/iOS are
  source-hardwired unavailable and not controller-wired. The engine now mints
  the opaque provider-authority/proxy context, but the browser pins do not yet
  consume it or a released wallet ABI, so no provider method is executable end
  to end.
- Crawler production snapshots/live-directory operation and a deployed,
  hash-pinned bootstrap appliance still need independent release
  qualification; their unit/build gates do not upgrade browser trust rows.
  Bootstrap-generator hosted CI now exists, but run `30401402868` failed at
  `npm ci` because `@emnapi/runtime@1.11.3` is absent from the lockfile.
- Signed-device Android/iOS and installed-browser Chromium matrices remain
  qualification gates. Android 0.5.5 version code 46 is deployed to Google
  Play production; iOS 0.5.5 build 57 has passing exact Apple CI and live
  screenshot evidence, with direct manual App Review and no TestFlight
  (build `57` is `VALID` and its direct App Review submission is
  `WAITING_FOR_REVIEW` after protected upload run `30456522039`). Those
  distribution facts do not constitute installed
  device evidence. Mobile GitHub Release `v0.5.5` publicly retains the verified
  code 46 APK and build 57 IPA. The Chromium v0.5.5 release has 29 assets and
  its macOS artifacts are signed/notarized; Windows artifacts remain unsigned.
- All 14 `hns-rs` `0.1.0` crates are published and non-yanked from embedded
  source `0ea5994c336642ea7d01c51c0e22df2008985426`; no `v0.1.0` Git tag
  exists. The engine remains at remote head
  `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`; its current local source-only
  head `f76ad37232bcadc85eb9b9bee5f45bff8405b583` includes the unpublished
  release preparation, opaque provider authority, and bounded proxy admissions
  and remains unbuilt, untested, unpublished, and unpushed.
- The end-to-end regtest topology and prohibition on public recursive resolver
  contact have not yet been demonstrated.
