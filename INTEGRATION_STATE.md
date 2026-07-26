# Integration state

Status: **implementation in progress; not release-ready**

Last audited canonical `hns-rs` main:
`8543f317a0ac23e40b6a79ea0cdc957dd01a04d9`

Implemented and locally committed there:

- semantic primitives and canonical bounded encoding;
- headers, PoW, targets, chainwork, retargeting, networks, genesis;
- transactions, witnesses, addresses, coins, all covenant encodings/linkage;
- HSD sighash and lock predicates;
- HIP-0001/Shakedex v2 fixed and reverse-Dutch proof primitives;
- standard packet assignments/framing and strict core packet codecs;
- HSD-compatible Urkel proof parsing/verification;
- Denuo Experimental Registry v1 and collision-scoped negotiation;
- draft HIP 76, 77, and 78 protocol/cryptographic records;
- HSD-compatible script execution/mining coverage; and
- independent consent for opaque relaying, output-node operation, and
  requester/client operation.

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
  `90df79f445f90633cc46a64ce5475bde9879a58b` (adapter implementation
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

The standalone node canonical main is
`504d3fed035feb8a637ca09c4e0816b6e1144622`, containing the extraction and
qualification implementation checkpoint
`d97aab205ef640008bd61d1b17ba3ef91ee2ac10` and retaining exact 126-commit
subtree provenance from MeshMine. MeshMine's canonical main is
`f0f25aacdc5eb05ba41d3bd81e4d22680fa70fb9`, containing the external-node
adoption and immutable canonical dependency checkpoint
`ca64fc70ca00475318053bf4a4de763d6200f3d6` plus the portable-CI correction.
The current main also names authenticated Urkel record-path types so the exact
warning-denied HSRD Clippy gate passes without lint suppression; 19 focused
Urkel tests pass. Its completed portable gates and the interrupted
all-features RocksDB build are recorded in
`evidence/standalone-node-checkpoint-2026-07-25.md`.

The DANE operator/data-plane auxiliaries are also migrated independently:

- `hns-dane-crawler` main
  `74546c7e6b0b8a764525a77177a88dc333bf64d8` produces observational
  topology/evidence/report artifacts only; 140 tests, Ruff, shell syntax,
  Node syntax, and dependency checks pass.
- `hns-dane-bootstrap-generator` main
  `63548ff6ae76fb175fce2d118f5ddee6910e7c96` produces operator-reviewed
  delegation, DNSSEC/DS, DoH, TLSA, and appliance material; 34 web tests, the
  appliance suite, the production build, and a reproducible `npm ci` pass.

All eight product repositories now have their audited checkpoints on canonical
`handshake-rs` `main` branches. The existing `ecosystem` history was preserved
and merged with this audit, and both the ecosystem README and organization
profile now publish the repository/authority map. No package, store binary,
production service, or mainnet state was published or mutated.
