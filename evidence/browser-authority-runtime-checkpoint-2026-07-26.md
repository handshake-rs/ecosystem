# Browser authority-runtime checkpoint

Date: 2026-07-26

Status: implementation and portable qualification complete; installed-browser
and signed-device qualification remains open

## Immutable source boundary

| Repository | Commit | Role |
| --- | --- | --- |
| `handshake-rs/hns-dane-engine` | `a03648ec85a115362ebc2ab24bb9ea0f1be127fc` | canonical five-contract engine checkpoint |
| `handshake-rs/hns-dane-browser-mobile` | `00cb9f3e1fdd59bbb3b3f5c8ef371d0f5fecf875` | Android/iOS canonical authority and observability adapter |
| `handshake-rs/hns-dane-browser-mobile` | `140bb77e7b3b363747225b03de705d849768f122` | final mobile main with corrected requester/output consent documentation |
| `handshake-rs/hns-dane-browser-extension` | `a9a7a046c8a8404af5088dd13522bea632126511` | Chromium canonical authority and observability adapter |
| `handshake-rs/hns-dane-browser-extension` | `d6071a5cf969cc5b796b034d460d46ffbfb0a521` | final Chromium-only source boundary |

Both consumers declare exactly these engine packages once at the immutable
engine revision above:

- `hns-browser-runtime`;
- `hns-browser-observability`;
- `hns-icann-dane`;
- `hns-namespace-resolution`; and
- `hns-resolution-policy`.

Their lockfiles, source-policy verifiers, `cargo-deny` policies, and generated
notices accept only that canonical Git URL, exact revision, and reviewed
package set. The local platform runtimes were first renamed at mobile
`5ef5cb9ec66ea460b4168946a7d2d0bba7c2f141` and Chromium
`0334126fa4f5a6d5ae14d15b2584b64e0c8985b3`; no Cargo package alias conceals
the platform/canonical authority boundary.

The generic engine/node policy keeps HIP-76 requester eligibility at `Auto`
with independent opt-out. Both browser products intentionally apply a stricter
product default: their new and persisted requester switch starts false/off and
requires explicit user opt-in. False maps to `Disabled`, true maps to
direct-first `Auto`; browser P2P `VERSION` services and all provider/output
roles remain zero.

## Adopted authority contract

Each portable product adapter:

- creates one checked, nonzero runtime session per process start;
- binds one canonical runtime generation and policy generation to the active
  authenticated proxy generation;
- obtains an engine event stamp before DNS or namespace classification;
- rejects any stale session, generation, event, or proxy binding;
- invalidates earlier admitted work permanently on real policy change,
  degradation, revocation, stop, or restart;
- requires the exact admitted stamp through namespace side effects and
  HTTP/`101` response-head write and flush;
- keeps streamed body and tunnel work revocation-aware after the head permit is
  released; and
- publishes trusted status only from the same request-local decision and exact
  authority stamp.

No stale navigation, redirect, subresource, Service Worker request, download,
WebSocket, direct response, file response, local error, or trusted status can
be published after a degrade/recover or stop/restart ABA cycle. Pre-admission
local errors remain bounded; post-admission failure cannot be converted into a
fresh unstamped response.

The active readiness probe requires a non-genesis header state for every
network, an available proof store, and at least one policy-permitted live
resolution transport/socket. A fresh profile may therefore listen while
remaining degraded and non-admitting. Status never invents a negotiated P2P
peer or registry identity.

## Complete-host namespace and ICANN trust

Every canonical HTTP(S) or WebSocket DNS host reaches the Rust whole-request
boundary. The complete hostname is independently resolved through HNS and
ICANN, producing one of:

- HNS only;
- ICANN only;
- both convergent;
- both divergent with an explicit selected namespace;
- neither; or
- indeterminate failure.

The IANA root-zone snapshot is not namespace authority. It may remain inside a
resolver as a performance hint, but it cannot select a root or bypass the Rust
boundary. A request-local decision retains both complete plans, evidence,
expiry, divergence, selection, and cache identity. A name-free fingerprint
and outcome, including `Neither`, reach schema-v2 status without reconstructing
state from a shared cache.

For every ICANN-selected HTTPS/WSS request, the effective host, port, and
`ServiceTransport` derive the TLSA owner. TCP uses `_port._tcp.host`; QUIC/UDP
uses `_port._udp.host`. Thus the live TCP example derives
`_443._tcp.dane-test.denuoweb.com`. Validating ICANN DoH supplies the
DNSSEC/TLSA decision:

- secure supported TLSA enforces DANE;
- authenticated TLSA denial permits the defined WebPKI fallback;
- a proven insecure delegation permits the defined WebPKI fallback;
- bogus or indeterminate DNSSEC fails closed and is never absence; and
- a real certificate-association mismatch alone becomes typed DANE failure.

The transport preserves that association-mismatch marker without parsing error
strings through HTTP/1.1, controlled HTTP/1.1, HTTP/2, HTTP/3/QUIC, and the
TLS Upgrade/WebSocket tunnel. Generic TLS, QUIC, I/O, framing, invalid-record,
or unrelated validation failures cannot fabricate DANE or SNI evidence.
Because an association mismatch does not prove an SNI mismatch, canonical
status reports DANE `Failed` and origin-SNI evidence `Unavailable`.

HNS root failure retains unavailable transport. ICANN root failure retains
`ValidatingIcannDoh` and an explicit fail-closed action. An ICANN-selected
status clears HNS-only chain and identity claims.

## Sticky namespace publication

Exact pins and successful first-use namespace bindings are durable inputs to
later classification. The binding update and corresponding response head share
one uninterrupted canonical publication permit, so policy invalidation cannot
commit a namespace choice and suppress the matching head. Request-local plans
remain authoritative even if another same-origin request changes the shared
cache.

After a durable sticky update, old-revision cache entries are unreachable.
Their bounded-memory reclamation is best-effort: a poisoned cache lock cannot
turn a successful durable commit into head suppression. Persistence failure
still fails closed before publication.

## Chromium repository boundary

The authority implementation was committed before the source trim so each
milestone is independently reviewable and revertible. The subsequent
Chromium-only commit removed:

- Android and iOS application trees;
- Android JNI and Apple C-ABI crates;
- Play Store and App Store assets and metadata;
- mobile-only branding, release, screenshot, device, and sync documents;
- Android/Apple build, signing, upload, simulator, and path-selection scripts;
  and
- mobile-only Gradle, Cargo, supply-chain, version, and workflow inputs.

Before deletion, all 255 selected tracked files had a corresponding path in
the canonical mobile repository: 163 were byte-identical, 92 had evolved
between the products, and none was absent. The transfer history and the
canonical mobile repository retain every deleted source path. The deletion is
therefore a product-boundary cleanup, not a history rewrite.

The same trim removes the inactive static-IANA browser classifier/PAC,
`HnsOnly`/`WholeBrowser` routing constructors and starters, and the parallel
direct-ICANN forwarding module. The native host starts only `DaneBrowser`, in
which every ordinary DNS host reaches the complete-host canonical decision.
Canonical `NamespaceOutcome::HnsOnly` remains an intentional dual-root result;
it is not a routing-mode shortcut.

The Chromium repository retains only its MV3 extension, native messaging host,
PAC/proxy integration, local-CA lifecycle, desktop installers, the remaining
platform-neutral resolver/proxy implementation awaiting deeper engine
migration, generic fixtures, and Chromium qualification/release material.

## Retained local qualification

### Mobile authority checkpoint

```text
cargo test --workspace                                  PASS
  hns-transport                                         56 tests
  hns-mobile-platform-runtime                          154 tests
  hns-loopback-proxy                                   149 tests
  android-ffi                                           11 tests
  ios-ffi                                               12 tests
cargo clippy --workspace --all-targets -- -D warnings   PASS
cargo fmt --all -- --check                              PASS
iOS C-ABI header/symbol gate                            PASS
exact Git-source policy                                 PASS — 7 tests + verifier
deterministic mobile notices/digest                     PASS
runtime/platform boundary gate                          PASS
git diff --check                                        PASS
```

### Chromium authority checkpoint

```text
cargo test --locked --workspace --all-targets             PASS
  hns-chromium-platform-runtime                           173 tests
  hns-chromium-native-host                                 17 tests
  hns-loopback-proxy                                      154 tests
  hns-transport                                            56 tests
cargo clippy --locked --workspace --all-targets
  -- -D warnings                                          PASS
cargo fmt --all -- --check                                PASS
npm run check:extension                                   PASS — lint, 16 tests, build
source/path policy                                         PASS — 23 tests + verifier
deterministic Chromium notices/digest                     PASS
runtime/platform boundary and version gates               PASS
git diff --check                                          PASS
```

### Chromium-only trim checkpoint

```text
scripts/check.sh                                             PASS
  supply-chain, secret, exact Git-source policy              PASS — 9 tests
  generated Chromium notices/digest                          PASS
  version and Chromium-only runtime boundaries               PASS
  rustfmt and warning-denied all-target Clippy               PASS
  cargo-deny for workspace, fuzz, and exporter               PASS
  locked Rust workspace tests                                PASS — 707 tests
  locked release Chromium native-host build                  PASS
  fuzz smoke and exporter fmt/Clippy/test                     PASS
  extension lint, tests, and unpacked MV3 build               PASS — 16 tests
git diff HEAD --check                                        PASS
final tracked scope                                          32 modified,
                                                             256 deleted,
                                                             0 untracked
exporter lock delta                                          6 insertions,
                                                             required exact
                                                             engine edge only
```

No hosted workflow was polled or counted as passing. Pushing the two local
Chromium commits together intentionally creates one final-main update rather
than treating the intermediate authority commit as a release candidate.

## Qualification boundary

This checkpoint demonstrates portable Rust contracts and repository-local
extension/native-host gates. It does not claim:

- an installed Chrome, Edge, Brave, Vivaldi, Opera, or Chromium matrix;
- Android SDK/NDK, emulator, physical-device, signed APK/AAB, or rebuilt Play
  screenshot qualification for the new commit;
- Xcode, simulator, physical iPhone, signed archive/TestFlight, or rebuilt App
  Store screenshot qualification for the new commit;
- packet-capture proof that no public recursive resolver was contacted;
- a production HIP 77 or HIP 78 browser transport; or
- release signing, artifact provenance, SBOM, package publication, or
  production readiness.

Two portable follow-ups also remain explicit. The Chromium UI should
distinguish a listener/PAC binding from canonical authority that is still
header-syncing and non-admitting on a fresh profile. The production strict
`Neither` regression currently invokes Node and validating DoH; its live
coverage should remain, but a deterministic offline conformance gate should
separate product regressions from external tool/network availability.

The next bounded implementation audit is the engine-owned loopback proxy
admission/publication core recorded in `NEXT_MILESTONE_AUDIT.md`. Live DNS
wire, light-chain/proof, DNSSEC, DANE, resolver, and origin-transport migration
remain later independently qualified slices.
