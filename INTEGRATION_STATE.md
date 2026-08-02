# Integration state

Status: **experimental wallet/marketplace foundation delivered; not
release-ready and not authorized for mainnet settlement**

## 2026-08-02 local wallet and marketplace checkpoint

The coordinated implementation is committed on `main` in six independent
code repositories. It creates the standalone `hns-wallet-rs` workspace, adds
canonical marketplace protocols, adds optional node wallet indexes and a
bounded relay core, and adds fail-closed provider-authority/adaptor slices to
the engine and browser products.

| Repository | Local `main` revision | Delivered boundary |
| --- | --- | --- |
| `work/hns-rs` | `b66470a6a07f0211e3e7fa9aef7d034c8486e75b` | unpublished Denuo V2 marketplace protocol, price/session records, listings, and HNS HTLC primitives |
| `work/hns-node-rs` | `96570aa2d0841c5244e464ef46b609e2f6b0a672` | disabled-by-default confirmed wallet indexes, twelve-call typed backend, and five-role bounded relay policy core |
| `work/hns-dane-engine` | `6ed28559cd32163e3995a944010152d92eabe184` | exact-origin provider-injection decision without wallet or marketplace logic |
| `work/hns-wallet-rs` | `8aa82dd990d41732874f566a256348b1c325e2a1` | eleven-crate encrypted wallet/provider/Shakedex/Kyoto/ETH/settlement foundation |
| `work/hns-dane-browser-mobile` | `58996db0facef1bb6a7cb2876361d13dabc90c75` | deliberately inactive Android/iOS provider, secure-key-wrapper, and UI-state source adapters |
| `work/hns-dane-browser-extension` | `2300ef82a765a6dbd1b99ad537d3d3c2ac312d95` | fail-closed provider bridge, approval/event UI, and no-key demonstration dapp |

The full `./scripts/check.sh` gates passed for `hns-rs`, `hns-node-rs`,
`hns-dane-engine`, `hns-wallet-rs`, and mobile. Chromium's source/Rust,
release, fuzz, audit, and exporter stages passed before a documentation-only
permission-justification amendment; the affected final
`npm run check:extension` then passed 113 tests plus lint/build. No redundant
7.4 GiB Rust rebuild was performed, so this is staged evidence rather than a
claim that one final-commit full-script invocation exited zero. Swift/Xcode,
installed-browser, signed-device, real-chain settlement, sustained fuzz,
resource benchmark, and independent security gates remain open.

Compatible schemas do not create a runtime join. Denuo V2 is unpublished;
the node does not advertise it; the wallet does not have complete registered
chain-module implementations; Chromium returns `walletUnavailable`; mobile
adapters are hardwired unavailable; and HNS/BTC and HNS/ETH remain disabled.
No commit in this checkpoint was pushed, tagged, published, or used with live
mainnet funds. Exact commands and limitations are in
`WALLET_MARKETPLACE_IMPLEMENTATION.md`.

## Earlier checkpoint ledger

Last audited canonical `hns-rs` main:
`f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`

All 14 allowlisted `hns-rs` crates at `0.1.0` are published and non-yanked.
Their Cargo VCS metadata identifies
`0ea5994c336642ea7d01c51c0e22df2008985426` as the release source. No local
or remote `v0.1.0` Git tag exists.

Implemented and locally committed there:

- semantic primitives and canonical bounded encoding;
- headers, PoW, targets, chainwork, retargeting, networks, genesis;
- transactions, witnesses, addresses, coins, all covenant encodings/linkage;
- HSD sighash and lock predicates;
- HIP-0001/Shakedex v2 fixed and reverse-Dutch proof primitives;
- standard packet assignments/framing and strict core packet codecs;
- HSD-compatible Urkel proof parsing/verification;
- Denuo Experimental Registry v1 and collision-scoped negotiation;
- exported canonical registry identity/limits and typed Hello/Ack APIs bound to
  the generated TOML/binary/SHA artifacts;
- draft HIP 76, 77, and 78 protocol/cryptographic records;
- HSD-compatible script execution/mining coverage; and
- independent consent for default-on/opt-out opaque relaying, explicit-opt-in
  output-node operation, and independently revocable requester/client
  operation.

Verified checkpoint gates:

- `cargo test --workspace`
- `cargo clippy --workspace --all-targets -- -D warnings`
- `cargo build --workspace --release`

The organization migration changed the Denuo Experimental Registry fingerprint
to
`95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d`
because its canonical encoded source URLs now name `handshake-rs/hns-rs`.
Assignments, payload bounds, meanings, and consent defaults did not change.

Uncommitted work is not counted as a checkpoint until it passes its
repository-specific gate.

The automatic ICANN DANE, full-host dual-root, and typed transport-policy
browser checkpoint is committed and pushed across its shared and
platform-specific boundaries:

- shared DANE engine:
  `2850ac1f50e361e2772e18f2e5ecbd7e77085afb` (policy implementation
  `ab3543ba9b80d23f9fe5a25abf44abd7496a41a2`, standalone dependency
  checkpoint `2850ac1f50e361e2772e18f2e5ecbd7e77085afb`);
- Android/iOS browser:
  `7b826166a2bac3af8d2384dbff9875a992f252ca` (dual-root adapter implementation
  `f25d5fd6dff33a46d5ebd11f73f7f99ec2e3b0b0`, qualified-engine pin
  follow-up `7b826166a2bac3af8d2384dbff9875a992f252ca`); and
- Chromium extension/native host:
  `1fde772006dde8b36c963b3ecc09cc011c542155` (dual-root adapter implementation
  `124190f01c587bce2792a456cb40aab7d0247dfe`, qualified-engine pin
  follow-up `1fde772006dde8b36c963b3ecc09cc011c542155`).

Every canonical DNS host is resolved independently through complete HNS and
ICANN plans. The shared contract reports HNS-only, ICANN-only, convergent,
divergent, neither, or indeterminate state; applies exact pin, successful
persistent binding, then ICANN first-use precedence; retains both roots'
evidence; and derives connection/cache identity without consulting an IANA
suffix list. The selected immutable plan alone supplies endpoints, service
parameters, transport, TLSA owner, trust decision, trace attribution, and cache
partition.

Every DNS-named ICANN HTTPS/WSS request derives its transport-aware TLSA owner.
Secure TLSA presence enforces DANE; authenticated denial or a proven insecure
delegation permits the defined WebPKI fallback; bogus, indeterminate,
malformed, or failed DNSSEC resolution fails closed. HNS address presence
without required TLSA is a root failure, never namespace absence. The shared
decision reaches navigation, redirects, subresources, supported Service Worker
requests, downloads, and WebSockets through each browser's whole-request Rust
proxy boundary.

The browser consumers pin the exact canonical engine Git revision. Their
lockfiles, exact-source policy tests, notices, and `cargo-deny` policies now
bind three shared contracts: `hns-icann-dane`,
`hns-namespace-resolution`, and `hns-resolution-policy`. Both products map the
existing relay-requester control explicitly (`false` to `Disabled`, `true` to
direct-first `Auto`) while disabling every unsupported ODoH, HNSR, provider,
market, output, and legacy role. Direct authoritative UDP/TCP therefore
precedes authenticated authoritative DoH and any admitted P2P relay. The
generic shared policy retains independent default-on/opt-out opaque relaying
and explicit-opt-in output-node operation; browser requester consent does not
grant either provider role.

The browser products intentionally do not inherit the generic node requester
default. A new or persisted browser profile starts with requester relay
false/off and requires explicit user opt-in; false maps to `Disabled`, true
maps to direct-first `Auto`, browser P2P `VERSION` services remain zero, and
all provider/output roles remain disabled.

Current full-workspace tests, warning-denied all-target Clippy, and formatting
pass in both products. Mobile additionally passes seven exact-source policy
tests and 201 focused runtime/resolver tests. Chromium passes 23
source-policy/path tests, its supply-chain gate, 233 focused
runtime/resolver/native-host tests, and all 15 extension tests with a packaged
desktop notice. Separate non-local clones pass locked offline metadata and the
same 201/233 focused tests without a coordination-workspace dependency.
Exact evidence is recorded in
`evidence/browser-engine-consolidation-audit-2026-07-26.md`.

The complete engine graph is now independently cloneable. Its seven deeper
consumer manifests inherit 24 declarations for nine direct canonical
`hns-rs` packages at
`dde2da81f29df935f043978a6d517c1d60ceff31`; the lockfile adds only
`hns-mining` and `hns-transaction` to that exact Git closure. Twelve
source-policy tests, `cargo-deny`, all required 144-test workspace forms, 20
doc-test targets, strict Clippy, release build, formatting, and the C11 header
smoke pass locally and after one verified fetch in a depth-one isolated clone
with no sibling `hns-rs`. Exact evidence is in
`evidence/hns-dane-engine-standalone-checkpoint-2026-07-26.md`.

The two pin-only consumer commits change no runtime source. Mobile passed its
seven source-policy tests, notice/digest checks, locked metadata for both
manifests, and 302 focused offline tests. Chromium passed nine source-policy
tests, the supply-chain and notice gates, 233 focused Rust tests, strict
Clippy/formatting, and its lint, 15-test, and extension-build gate.

Installed-browser, Android SDK/device, Xcode/iOS device, and rebuilt
store-screenshot matrices remain release gates. The initial complete-host
checkpoint remains in
`evidence/browser-dual-root-checkpoint-2026-07-25.md`; the earlier automatic
ICANN milestone remains historical evidence in
`evidence/browser-icann-dane-checkpoint-2026-07-25.md`.

The mobile migration follow-up at
`cb6a5a31c4477fa32bc4d11bd2d935cb3e0c8aa4` reconciles its supply-chain
script with that exact engine pin. Nineteen policy/classifier tests and the
real supply-chain gate pass while alternate URLs, packages, locations,
unpinned sources, and mismatched revisions remain rejected. The later
migration head
`90df79f445f90633cc46a64ce5475bde9879a58b` deterministically regenerates the
third-party notice asset for the same two allowlisted Git crates and their
canonical MIT/Apache license files; notice `--check` passes.
Mobile platform hardening commit
`271044d759b9df3963a934a19cacd47fa8fada12` then binds Android WebView,
Service Worker, download, and security-display WebPKI fallback to a consistent
nested ICANN selection retained by Rust.
Missing, malformed, legacy-top-level, HNS-selected, or contradictory traces
fail closed on both Android and iOS. Android's synthetic WebView asset origin
is local only for canonical HTTPS `/assets/` URLs; alternate schemes, ports,
paths, workers, and downloads cannot escape into DNS or the network proxy.
Runtime/platform boundaries, supply-chain policy, deterministic notices,
version consistency, 20 policy/routing tests, formatting, and focused Rust
namespace-plan tests pass locally. The immediate full-scope hosted run passed
Rust and iOS plus Android assembly/unit tests before Android lint exposed the
two untranslated legacy diagnostics. The final hosted run for that
pre-transport-policy head,
[`CI run 30191799526`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30191799526)
then passed its correctly selected Android assembly, unit, lint, and
release-bundle gates. Installed and signed-device qualification remains a
separate release gate.
CI repair commit `dc3e22483e160d17a75dec39396ede5704d9a06b`
also invalidates queued navigation whenever immutable proxy policy changes,
repairs the standalone snapshot tool lock for the transitive exact engine
revision, and extends the narrow Git-source policy regression suite. The
updated tool lock passes locked offline check, Clippy, tests, `cargo-deny`, and
deterministic-notice regeneration. The pre-transport-policy migration head
`05248d69f52b1963c4b775184fc7b3098fcdcffb` marks both the intentionally
technical unsupported-legacy-HNS-DoH protocol label and its matching
remediation text non-translatable, consistent with the adjacent legacy source
label. XML and the complete 20-locale resource matrix validate without any
missing translatable key.

The standalone node canonical main is
`0e69319d11ca98d788466ed5028d8d897685e9f1`. Its historical live-Denuo
checkpoint is `b2c375e37cac6cfa7a09cfa61113de52ac4f93a1`, layered on the
extraction and qualification implementation checkpoint
`d97aab205ef640008bd61d1b17ba3ef91ee2ac10` and retaining exact 126-commit
subtree provenance from MeshMine. MeshMine implementation checkpoint
`bc9cc70de22e455545d44453cec0d6f07ebeaabe` contains the external-node
adoption and immutable canonical dependency checkpoint
`ca64fc70ca00475318053bf4a4de763d6200f3d6` plus the portable-CI correction.
The 2026-07-28 documentation reconciliation head
`93681bf85b61bcc031ad928321b1bcdb94dfc4bd` additionally marks the embedded
HSRD tree as archival and reconciles the exact standalone-node boundary. The
implementation checkpoint names authenticated Urkel/state record paths, groups node
compaction/commit context, and corrects test scoping so the warning-denied
portable HSRD workspace passes without lint suppression. Focused gates pass 19
Urkel, 46 state, and 116 node tests. The exact local all-features gate was
interrupted after 20 minutes in the known bundled-RocksDB compile; the hosted
CI counterpart completed successfully for that exact implementation head in
[`run 30189487369`](https://github.com/handshake-rs/MeshMine/actions/runs/30189487369).
Details are recorded in
`evidence/standalone-node-checkpoint-2026-07-25.md`.

The later standalone release-qualification implementation head is
`42c76a622f2600a833835b4ca737d3350f73af52`; documentation reconciliation head
`eba0237dedcbc958a8bc09dd811a4a9eeaa9afe7` preserves its claim boundaries.
Every
`RpcConsensusReadiness` field is true there, including the retained historical
replay and independently generated invalid corpus. That is functional source
readiness. `NodeService` initializes its base snapshot with `release_stage:
pre-authority`, but live native RPC replaces that field with
`native-sync-live-p2p`, `mining-engine-observe`, or
`mainnet-canary-gated` according to the active configuration. Those are
diagnostic mode labels, not authority. A mainnet process receives a private
mining permit only when its explicit hardened canary configuration, best
header/active-state synchronization, durable validation/undo state, and
authoritative tip all pass at runtime.

MeshMine still pins standalone node revision
`504d3fed035feb8a637ca09c4e0816b6e1144622`. That revision already has the
promoted functional readiness and conditional canary authority path, but it
predates the later canonical Denuo negotiation and live HIP-76 commits.
MeshMine therefore exposes no substitute relay/provider policy and must
deliberately advance and requalify its immutable pin before claiming those
standalone features.

The historical live-registry checkpoint pins
`hns-p2p-experimental` at exact revision
`5f56e5d381338314e4d7cf1f9e08da7c76d1cf6f`, advertises only ordinary network
plus the extension-envelope service, and exchanges the canonical fingerprint
only after ordinary peer readiness. Exact `0xf4` dispatch is bounded before
generic unknown-packet decoding; mismatch, replay, timeout, malformed input,
and repeated oversize traffic disable only Denuo while ordinary P2P remains
Ready. API-v12 status and native-sync diagnostics expose the same canonical
identity, service mask, live phases, admitted/received/agreement totals, and
fixed rejection taxonomy. Thirty-eight P2P tests, eight RPC tests, 117
no-default-feature node target tests, focused post-hardening status tests,
warning-denied Clippy, formatting, and diff checks pass. Two-full-node and live
Brontide negotiation matrices remain unrun. Exact evidence is in
`evidence/denuo-live-negotiation-checkpoint-2026-07-26.md`.

The role-safe HIP-76 live-session checkpoint pins canonical `hns-rs`
`dde2da81f29df935f043978a6d517c1d60ceff31`. Node implementation commit
`5a35ab9d84da26ce20b8f343efde31e77d6fc898` wires bounded `0xf0`/`0xf1`
sessions into the live manager, and final main
`0e69319d11ca98d788466ed5028d8d897685e9f1` adds a live requester opt-out
regression. Requesting defaults to `Auto` with independent opt-out; operating
a plaintext DNS output remains disabled until the operator opts in and a
backend is ready. Mainnet/testnet plaintext peers are rejected, while Brontide
binds peer provenance to the authenticated remote static key.

Two live regtest TCP peer managers using the explicit plaintext development
transport negotiate the registry and complete a strict, correlated
request/provider-work/response exchange without leaking private frames into
generic packet delivery. The returned DNS bytes remain explicitly untrusted,
ordinary `GetAddr` traffic continues after the exchange and after requester
opt-out, and provider readiness never implies DNSSEC authenticity. The final
portable gates pass 63 P2P, 8 RPC, and 109 no-default-feature node tests plus
warning-denied Clippy, formatting, and diff checks. A
default-feature target was stopped during the known bundled-RocksDB C++
compile and is not counted as passing. A production recursive and
DNSSEC-validating provider backend, durable operator-policy restart, and
two-full-node topology remain open. Exact evidence is in
`evidence/hip76-live-session-checkpoint-2026-07-26.md`.

The DANE operator/data-plane auxiliaries are also migrated independently:

- `hns-dane-crawler` main
  `74546c7e6b0b8a764525a77177a88dc333bf64d8` produces observational
  topology/evidence/report artifacts only; 140 tests, Ruff, shell syntax,
  Node syntax, and dependency checks pass.
- `hns-dane-bootstrap-generator` main
  `f745f122243e5304e6a7ea0e111d47c61d22005e` produces operator-reviewed
  delegation, DNSSEC/DS, DoH, TLSA, and appliance material; 34 web tests, the
  appliance suite, the production build, and a reproducible `npm ci` pass.

All eight product repositories now have their audited checkpoints on canonical
`handshake-rs` `main` branches. The existing `ecosystem` history was preserved
and merged with this audit, and both the ecosystem README and organization
profile now publish the repository/authority map. No package, store binary,
production service, or mainnet state was published or mutated.

## 2026-07-26 browser authority-runtime successor

The browser authority and observability successor advances the shared engine
to `a03648ec85a115362ebc2ab24bb9ea0f1be127fc`. Both browser products now pin
five canonical contracts at that exact Git revision:

- `hns-browser-runtime`;
- `hns-browser-observability`;
- `hns-icann-dane`;
- `hns-namespace-resolution`; and
- `hns-resolution-policy`.

Mobile authority adoption is committed at
`00cb9f3e1fdd59bbb3b3f5c8ef371d0f5fecf875`; final mobile main is
`140bb77e7b3b363747225b03de705d849768f122`, whose follow-up corrects only the
requester/output consent documentation. Chromium authority adoption is
committed at `a9a7a046c8a8404af5088dd13522bea632126511`; its final
Chromium-only source boundary is
`d6071a5cf969cc5b796b034d460d46ffbfb0a521`.

The canonical runtime now issues the checked session, runtime generation,
policy generation, event sequence, and authority state used to admit work.
Each adapter obtains one stamp before namespace or DNS work, retains that
exact request-local snapshot through routing and origin I/O, and requires it
again for response, download, local-error, or `101` publication. Revocation,
degradation, policy change, stop, and restart permanently invalidate earlier
work; later recovery cannot create an ABA publication path.

The canonical observability contract emits name-free schema-v2 authority and
security status from the same retained decision. Chromium's native boundary
serializes that contract as schema v3 for the extension. The production
Chromium regression carries a real strict-`Neither` request through the
loopback backend, metadata observer, native serializer, and the extension's
actual JavaScript validator. Typed DANE association failure survives the
HTTP/1.1, controlled HTTP/1.1, HTTP/2, HTTP/3, Upgrade, and WebSocket paths;
unrelated TLS, QUIC, framing, I/O, or SNI evidence cannot fabricate it.

Full-host dual-root resolution remains authoritative for every canonical DNS
HTTP(S)/WS(S) request. ICANN-selected HTTPS/WSS derives the TLSA owner from the
effective host, port, and service transport; TCP uses `_tcp`, while QUIC/UDP
uses `_udp`. Secure TLSA enforces DANE, authenticated denial or a proven
insecure delegation permits the defined WebPKI fallback, and bogus or
indeterminate DNSSEC fails closed with validating-ICANN-DoH provenance.

Chromium's final source-boundary commit removes the 255 tracked Android/iOS,
FFI, store, branding, and mobile automation paths previously retained from
the shared historical repository. Every selected path was present in the
canonical mobile repository before deletion: 163 were byte-identical, 92 had
since diverged, and none was missing. Git history and the canonical mobile
repository retain the removed source.

Portable workspace tests, warning-denied Clippy, formatting, exact-source,
lock, notice, runtime-boundary, version, native-host, and extension checks are
retained in
`evidence/browser-authority-runtime-checkpoint-2026-07-26.md`. No hosted
workflow was polled or counted as passing for this successor. Installed
Chromium variants, Android/iOS SDK and signed-device matrices, packet-capture
resolver proof, artifact signing/provenance, and the PDF's full topology
qualification remain open release gates.

## 2026-07-27 ecosystem software-gate audit

All nine requested working repositories were reconciled against the PDF's
package and evidence requirements. Existing complete gates passed for the
DANE engine and Chromium extension. The exact MeshMine remote head audited on
July 27 had a successful scheduled hosted workflow. No implementation changes
were needed in those three repositories.

Bounded release-engineering gaps were closed locally in the remaining
repositories:

- the organization profile now verifies a canonical checksum/dimension
  inventory for every published image and has an immutable-action CI gate;
- the bootstrap generator has a clean dependency audit, repaired lockfile, one
  complete check command, and immutable-action CI;
- mobile has all five missing diagnostic resources in every one of 20 locales,
  plus a format-token-safe completeness gate wired into change classification
  and CI;
- the crawler has an exact development lock, clean-environment install gate,
  and immutable-action CI;
- canonical `hns-rs` has a locked production-parser fuzz graph, root/fuzz
  source/license/advisory gates, deterministic parser smoke, a complete check
  command, CI, and RustSec;
- the standalone node has a repaired canonical fuzz lock, root/fuzz
  source/license/advisory gates, a complete check command, CI, RustSec, and a
  two-release-process regtest gate that directly passes matrix rows 1–3; and
- this evidence repository now enforces its required documents, exact 26-row
  matrix, nine-repository checkpoint inventory, and relative-link integrity.

The detailed commands, package results, local/hosted distinction, and read-only
`gh` run audit are retained in
`evidence/software-gate-audit-2026-07-27.md`.

At the close of that July 27 audit, these changes were committed only in the
local working repositories. The PDF forbade pushes, releases, upstream
comments, and publication during that audit, so its newly added workflows did
not yet have protected hosted results. Portable software
and local two-process success also do not satisfy full block synchronization,
production provider/public-service, wallet/market, installed-browser,
signed-device, ASIC, signing/provenance, or independent-review gates. Release
readiness therefore remains **NO**.

## 2026-07-28 browser maintenance and release successor

The browser products advanced after the July 27 software-gate audit.

Mobile implementation commit
`14edcaf5f1039e7fd2e6d99c178de927ede5d1b0` moves network I/O, quorum
collection, snapshot preparation, and peer merging into a private staged
database. Header, peer, and readiness generations publish atomically after
baseline, chain, proof-of-work, chainwork, and canonical-suffix checks.
Unchanged-header peer refreshes do not invalidate admitted requests; process-
wide publication locks, crash-state tokens, conditional deltas, stale-stage
reclamation, and bounded SQLite contention keep concurrent runtimes fail
closed. Exact-head CI run
[`30323566765`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30323566765)
passed. Store-link checkpoint
`153db0306836007b08a9d3bc47c16041b04418d6` then added the live
[Google Play](https://play.google.com/store/apps/details?id=com.denuoweb.hnsdane)
and
[App Store](https://apps.apple.com/us/app/hns-dane-browser/id6791914326)
links; its documentation-only required-CI run
[`30393560141`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30393560141)
passed change classification and repository policy while correctly skipping
unchanged product gates. The July 28 documentation reconciliation head
`21719bb9cbe972e11ba1ad285707e6cfa0d629c1` updates release, store,
qualification, and staged-maintenance guidance without changing product code.

Chromium release/runtime commit
`43819ee3a87e8e400d3b8f3202647f0d4ccc04d8` applies the same staged-chain
model and adds explicit connection/control generations around PAC, native-host
replacement, status adoption, alarms, and header maintenance. The extension
keeps either its live mandatory PAC or a confirmed fixed blocking PAC through
replacement; transient due-but-unexpired synchronization failures retain the
live proxy, while authenticated evidence expiry still blocks. The release also
publishes version-matched graphical Setup applications and native hosts for
Linux, macOS, and Windows on x64 and arm64.

Chromium release-hardening head
`be27931c88929e1e0e7d1504687a5a49a5e86bc3` adds the default-branch Apple
release-replacement workflow and its protected credential-bearing signing
jobs, PKCS#12 normalization, exact certificate fingerprint/SHA-1 identity
selection, concurrent notarization, conservative queue polling, retained
failure evidence, and post-replacement digest checks. The final write-enabled
publisher uses a separate `release` environment that currently has no
environment approval or branch protection rules.
Exact-head CI run
[`30350645836`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30350645836)
passed. Workflow run
[`30350653092`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30350653092)
validated the immutable v0.5.4 source/release, ran the protected signing jobs
for both macOS architectures, stapled Setup, and replaced and reverified the
nine affected
[v0.5.4 release](https://github.com/handshake-rs/hns-dane-browser-extension/releases/tag/v0.5.4)
assets. Windows artifacts remain explicitly unsigned.
The July 28 documentation reconciliation head
`9109dc4a9115a8fde8c3026700a104ebf8cdb164` records those release and
environment-protection boundaries without changing the packaged runtime.

These are real product and release advances, but they do not demonstrate an
installed Chromium catalog/browser matrix, Android/iOS signed-device behavior,
packet-capture proof that no public recursive resolver is contacted, or the
remaining node, wallet, market, ASIC, and multi-operator topology. Ecosystem
release readiness remains **NO**.

## 2026-07-29 non-mobile publication and release reconciliation

The first dependency-publication stage is complete: every one of the 14
allowlisted `hns-rs` `0.1.0` packages is published and non-yanked. Each package
embeds source commit
`0ea5994c336642ea7d01c51c0e22df2008985426`; documentation head
`f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0` records that result. A
`v0.1.0` Git tag does not exist locally or on `origin`.

The engine has not advanced remotely or published crates. Remote `main`
remains `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`; the local
release-preparation series ending at
`1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75` is explicitly unpublished and
remains unpushed.

Chromium v0.5.5 is public from source/tag
`86b18497285753944ec1b9196ec05ee359c6db11`. Its 29 release assets include
Developer ID-signed and Apple-notarized macOS artifacts; Windows artifacts
remain unsigned. Documentation head
`3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` passed
[CI run `30439859541`](https://github.com/handshake-rs/hns-dane-browser-extension/actions/runs/30439859541).

MeshMine documentation head
`9f781a00ee8fc3b7c6773538434235a65f167ca3` passed all three jobs in
[CI run `30440116148`](https://github.com/handshake-rs/MeshMine/actions/runs/30440116148).
This documentation-only successor does not change its immutable external-node
pin.

The bootstrap generator now has hosted evidence, but it is failing evidence:
[CI run `30401402868`](https://github.com/handshake-rs/hns-dane-bootstrap-generator/actions/runs/30401402868)
stopped at `npm ci` because `@emnapi/runtime@1.11.3` is missing from
`package-lock.json`. It must not be described as having no hosted run or as a
passing current hosted gate.

The exact checkpoint and claim boundaries are retained in
`evidence/non-mobile-publication-release-checkpoint-2026-07-29.md`. Mobile is
intentionally excluded from that checkpoint and reconciled separately below.

## 2026-07-29 mobile v0.5.5 release reconciliation

Mobile Android 0.5.5 version code 46 was built from
`d24f85158854abb8be4a7bb9e914aebe5e7e4679`, signed, structurally verified,
and uploaded directly to the Google Play production track. Play edit
`17438779769069438085` completed and generated APKs for version code 46 are
available. The signed APK SHA-256 is
`b36a4346ffcba14c081500ef3dc7c5012cabd30f42cdaa80a354eefb5da210ba`;
the uploaded AAB SHA-256 is
`728d8892e180d954652668a4e53a7e2d6c7542e9d36330f4803cdecdb34598b0`.

iOS 0.5.5 build 57 uses source and annotated tag
`d926561091634cd69fc9b7e79a4b76003fa4ee47`. Exact-source Apple
[CI run `30454904736`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30454904736)
passed. The four live `1284 × 2778` App Store screenshots from
[run `30454926117`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30454926117)
passed provenance, semantic, and visual validation. Build `57` is `VALID` and
its direct App Review submission is `WAITING_FOR_REVIEW` after protected upload
run `30456522039`. This is a direct App Review path configured for manual store
release, with no
TestFlight build distribution or beta group.

Public GitHub Release
[`v0.5.5`](https://github.com/handshake-rs/hns-dane-browser-mobile/releases/tag/v0.5.5)
retains the verified code 46 APK and build 57 App Store IPA.

Exact artifact and claim boundaries are retained in
`evidence/mobile-v0.5.5-release-checkpoint-2026-07-29.md`. Store build,
signing, screenshot, and publication evidence does not substitute for the
installed signed-device matrix. Qualification row 22 remains `PARTIAL`, and
ecosystem release readiness remains **NO**.
