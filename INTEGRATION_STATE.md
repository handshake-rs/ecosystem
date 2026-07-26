# Integration state

Status: **implementation in progress; not release-ready**

Last audited canonical `hns-rs` checkpoint:
`6bd4a23c4ec0f89dace34da58f07809a2a08d522`

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

Uncommitted work is not counted as a checkpoint until it passes its
repository-specific gate.

The automatic ICANN DANE browser checkpoint is locally committed across its
shared and platform-specific boundaries:

- shared DANE engine:
  `f8e8d7709f93490595e02b0bd48d484ea2421ab8`;
- Android/iOS browser:
  `75b5108ea9080ca3b1d9c74127e24e30d848b843`;
- Chromium extension/native host:
  `3347d7fbd214d771e0571dcb5749990137e4bc77`.

Every DNS-named ICANN HTTPS/WSS request admitted by the current namespace
classifier derives its transport-aware TLSA owner. Secure TLSA presence
enforces DANE; authenticated denial or a proven insecure delegation permits
the defined WebPKI fallback; bogus, indeterminate, malformed, or failed DNSSEC
resolution fails closed. The shared decision reaches navigation, redirects,
subresources, supported Service Worker requests, downloads, and WebSockets
through each browser's whole-request proxy boundary. Portable Rust, ABI, and
extension gates pass; installed-browser, Android SDK/device, and Xcode/iOS
device matrices remain release gates. Exact evidence is recorded in
`evidence/browser-icann-dane-checkpoint-2026-07-25.md`.

The current IANA-suffix check is an interim routing shortcut, not the intended
authoritative namespace classifier. Full-host resolution through both HNS and
ICANN, typed convergence/divergence, explicit precedence, and visible
namespace choice remain release-blocking.

The standalone node extraction and qualification checkpoint is
`d97aab205ef640008bd61d1b17ba3ef91ee2ac10`, retaining exact 126-commit subtree
provenance from MeshMine. MeshMine's external-node adoption is committed at
`c8bd975fc80d0037772160018ecdaf35d5dd7d1d`. Its completed portable gates and
the interrupted all-features RocksDB build are recorded in
`evidence/standalone-node-checkpoint-2026-07-25.md`.

No push, public deployment, package publication, or mainnet state mutation has
occurred.
