# Integration state

Status: **implementation in progress; not release-ready**

Last audited canonical `hns-rs` main:
`dde2da81f29df935f043978a6d517c1d60ceff31`

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

The automatic ICANN DANE and full-host dual-root browser checkpoint is
committed and pushed across its shared and platform-specific boundaries:

- shared DANE engine:
  `127b9ad55852df00b4df40826517715048dc3571` (policy implementation
  `ab3543ba9b80d23f9fe5a25abf44abd7496a41a2`);
- Android/iOS browser:
  `05248d69f52b1963c4b775184fc7b3098fcdcffb` (adapter implementation
  `f25d5fd6dff33a46d5ebd11f73f7f99ec2e3b0b0`); and
- Chromium extension/native host:
  `bcf587a6cc06c9c07c1f713eef108d317fcadfc7` (adapter implementation
  `124190f01c587bce2792a456cb40aab7d0247dfe`).

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

The browser consumers pin the exact canonical engine Git revision, and their
lockfiles and `cargo-deny` policies bind that source. Post-pin gates passed 469
mobile Rust tests plus Apple ABI/header/export checks, and 481 focused Chromium
Rust tests plus all six extension suites and the MV3 build. Installed-browser,
Android SDK/device, Xcode/iOS device, and rebuilt store-screenshot matrices
remain release gates. Exact evidence is recorded in
`evidence/browser-dual-root-checkpoint-2026-07-25.md`; the earlier automatic
ICANN milestone remains historical evidence in
`evidence/browser-icann-dane-checkpoint-2026-07-25.md`.

The mobile migration follow-up at
`cb6a5a31c4477fa32bc4d11bd2d935cb3e0c8aa4` reconciles its supply-chain
script with that exact engine pin. Nineteen policy/classifier tests and the
real supply-chain gate pass while alternate URLs, packages, locations,
unpinned sources, and mismatched revisions remain rejected. Final main
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
two untranslated legacy diagnostics. Final current-main
[`CI run 30191799526`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30191799526)
then passed its correctly selected Android assembly, unit, lint, and
release-bundle gates. Installed and signed-device qualification remains a
separate release gate.
CI repair commit `dc3e22483e160d17a75dec39396ede5704d9a06b`
also invalidates queued navigation whenever immutable proxy policy changes,
repairs the standalone snapshot tool lock for the transitive exact engine
revision, and extends the narrow Git-source policy regression suite. The
updated tool lock passes locked offline check, Clippy, tests, `cargo-deny`, and
deterministic-notice regeneration. Final current main
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
subtree provenance from MeshMine. MeshMine's canonical main is
`bc9cc70de22e455545d44453cec0d6f07ebeaabe`, containing the external-node
adoption and immutable canonical dependency checkpoint
`ca64fc70ca00475318053bf4a4de763d6200f3d6` plus the portable-CI correction.
The current main names authenticated Urkel/state record paths, groups node
compaction/commit context, and corrects test scoping so the warning-denied
portable HSRD workspace passes without lint suppression. Focused gates pass 19
Urkel, 46 state, and 116 node tests. The exact local all-features gate was
interrupted after 20 minutes in the known bundled-RocksDB compile; the hosted
CI counterpart completed successfully for the exact final main in
[`run 30189487369`](https://github.com/handshake-rs/MeshMine/actions/runs/30189487369).
Details are recorded in
`evidence/standalone-node-checkpoint-2026-07-25.md`.

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
