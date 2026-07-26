# Browser shared-engine consolidation audit

Date: 2026-07-26

Status: audit and first bounded implementation slice complete; product commits
pushed to canonical `main`

## Scope

This audit follows the automatic ICANN DANE and complete-host dual-root
checkpoint. It does not reopen that trust decision: every DNS hostname still
resolves through both HNS and ICANN, and the selected immutable origin plan
still controls redirects, subresources, Service Workers, downloads, and
WebSockets through each product's whole-request Rust boundary.

The question here is narrower: which browser code is truly shared, which code
is still duplicated, and what can move without changing a qualified trust
decision or a platform ABI?

## Current shared authority

Both browser products pin one immutable `handshake-rs/hns-dane-engine`
revision and consume these standalone engine contracts:

| Engine crate | Canonical responsibility |
| --- | --- |
| `hns-icann-dane` | transport-aware TLSA owner derivation and the typed ICANN DANE/WebPKI decision |
| `hns-namespace-resolution` | complete-host HNS/ICANN comparison, convergence/divergence, precedence, and immutable origin plans |
| `hns-resolution-policy` | typed direct-first transport admission and independent requester, opaque-relayer, provider, and output-node roles |

The first two crates were already active at the start of this audit. The
third is the audit's bounded implementation slice: mobile and Chromium map
their existing requester preference into the same engine `TransportPlan`
before enabling P2P DNS-relay fallback.

The browser mapping is intentionally explicit:

- requester disabled maps to `DnsRelayRequesterPolicy::Disabled`;
- requester enabled maps to `DnsRelayRequesterPolicy::Auto`;
- ODoH and HNSR are disabled because neither browser adapter implements them;
- authenticated authoritative DoH remains enabled after direct UDP/TCP;
- every provider role is disabled in the browser products;
- the Denuo V1 wire profile is selected; and
- legacy regtest compatibility is disabled.

No browser setting is reinterpreted as provider consent. The existing browser
switch controls consumption of relay answers. Opaque relayer participation
remains independently opt-out in the generic engine policy, while every
plaintext/output role remains independently opt-in.

## Remaining duplicate inventory

The same Cargo package names conceal different APIs and cannot be exchanged
as path substitutions.

| Historical browser crate | Active browser responsibility | Engine crate with the same name |
| --- | --- | --- |
| `hns-browser-runtime` | platform storage, sync, sockets, gateway requests, downloads, WebSockets, and proxy lifecycle | deterministic browser authority/session state machine |
| `hns-cache` | browser-specific bounded resource and resolution caches | typed shared cache with generation/evidence invalidation |
| `hns-dane` | live certificate/TLSA matching integrated with the browser crypto stack | canonical DANE evidence and verification core |
| `hns-dnssec` | live browser DNSSEC parsing and validation | canonical DNSSEC validation over `hns-dns-wire` |
| `hns-gateway` | HTTP/TLS origin orchestration and selected-plan execution | direct-first DNS transport-attempt state machine |
| `hns-loopback-proxy` | listener, authentication, local CA, exact-host leaves, HTTP framing, TLS termination, and upgrades | platform-neutral CONNECT/capability admission core |
| `hns-resolver` | live HNS proofs, delegated DNS, validating ICANN DoH, SQLite state, and caches | typed authority/TLSA evidence over the engine light-chain path |
| `hns-transport` | HTTP/1.1, HTTP/2, HTTP/3, TLS, QUIC, and WebSocket origin I/O | authoritative DNS transport |

Mobile additionally owns the intended platform adapters:

- `android-ffi`, Android Kotlin/WebView lifecycle and packaging;
- `ios-ffi`, Swift/WKWebView lifecycle and packaging; and
- platform-specific persistence, UI, proxy-installation, download, and
  Service Worker adapters.

The Chromium repository owns `hns-chromium-native-host`, the MV3 extension,
native messaging, PAC installation, proxy authentication, local-CA
installation, and desktop packaging. Its retained `android/`, `ios/`,
`android-ffi`, and `ios-ffi` trees are historical mobile copies, not Chromium
release authority. PDF section 42 requires their eventual removal.

## Clean-checkout blocker

The three contracts above are the browser dependencies currently consumed and
qualified from clean checkouts. Several additional leaf engine crates are also
standalone, but the complete deeper engine graph contains
coordination-workspace sibling paths into `../../../hns-rs`:

- `hns-light-chain`: `hns-covenants`, `hns-encoding`,
  `hns-header-consensus`, `hns-primitives`, and `hns-urkel-proof`;
- `hns-light-p2p`: `hns-header-consensus`, `hns-p2p-wire`, and
  `hns-primitives`;
- `hns-light-sync`: `hns-header-consensus`, `hns-p2p-wire`, and
  `hns-primitives`;
- `hns-p2p-transport`: `hns-dns-relay-protocol`, `hns-odoh-protocol`,
  `hns-p2p-experimental`, and `hns-primitives`;
- `hns-resolver`: `hns-covenants`, `hns-header-consensus`, and
  `hns-primitives`;
- `hns-transport`: `hns-covenants`, `hns-header-consensus`, and
  `hns-primitives`; and
- `hns-browser-testkit`: `hns-covenants`, `hns-header-consensus`, and
  `hns-primitives`.

A shallow independent clone of `hns-dane-engine` therefore cannot resolve the
full facade, resolver, transport, P2P transport, loopback proxy, or testkit.
Those sibling paths must become centralized immutable Git pins or published
crate dependencies before a browser may consume them. Consumer package-name
collisions and the current OpenSSL-versus-ring/rustls crypto split must then
be migrated explicitly rather than hidden behind Cargo aliases.

## Reversible consolidation sequence

1. **Typed transport policy.** Add exact-pinned `hns-resolution-policy` to
   both products, derive DNS-relay admission from its `TransportPlan`, retain
   current platform persistence and revision ABIs, and prove that unsupported
   roles remain off.
2. **Standalone engine graph.** Replace every sibling `hns-rs` path with one
   reviewed immutable source policy, regenerate locks/notices, and prove the
   complete engine from a shallow clean clone with no coordination workspace.
3. **Names and adapters.** Rename browser-local adapters where package names
   collide, document their I/O boundary, and forbid new protocol/trust logic
   outside the engine.
4. **Authority lifecycle and observability.** Adopt the engine runtime,
   generation admission, stale-completion rejection, evidence states, and
   structured status while keeping platform storage and process lifecycle in
   the products.
5. **Proxy core.** Keep Android/iOS/Chromium listener and certificate-store
   adapters, but move host normalization, CONNECT bounds, capability checks,
   and revocation into the engine proxy core.
6. **Resolution core.** Migrate DNS wire, light chain/proofs, DNSSEC, DANE,
   resolver, DNS transport, and gateway state machines one independently
   qualified boundary at a time. The whole-request selected-plan invariant
   must pass after every step.
7. **Repository trim and device qualification.** Delete the Chromium
   repository's mobile-only trees, then run Android/iOS and the six installed
   Chromium-family browser matrices, including restart, revocation, and
   uninstall.

Each stage must be independently revertible and must leave bogus DNSSEC
distinct from authenticated absence. No stage may restore the IANA suffix
list as namespace authority or add a public-recursive HNS fallback.

## Acceptance gates for the first slice

- exact immutable engine source in every affected manifest and lockfile;
- no unreviewed Git package or moving branch/tag selector;
- requester off excludes `HandshakeP2pDnsRelay`;
- requester on admits it only after direct UDP, direct TCP, and authenticated
  authoritative DoH;
- ODoH, HNSR, provider, output, market, and legacy modes remain disabled;
- rejected Chromium native policy is not persisted;
- existing mobile policy revisions and Android/iOS persisted requester values
  retain their ABI meaning;
- Rust unit tests, warning-denied Clippy, formatting, JavaScript policy tests,
  supply-chain policy, and deterministic notices pass; and
- both consumers pass the focused locked build from independent clean
  checkouts.

## Qualified implementation checkpoint

The exact source boundary is:

| Repository | Commit |
| --- | --- |
| `handshake-rs/hns-dane-engine` | `127b9ad55852df00b4df40826517715048dc3571` |
| `handshake-rs/hns-dane-browser-mobile` | `cde7d6d9d15859ebd5c4169433e72a7e434b2c1b` |
| `handshake-rs/hns-dane-browser-extension` | `13dbb87240807dda0fb6f72c7aaaa7a33d036e70` |

Both browser commits are on canonical `main`. The shared engine repository
was not changed by this slice; its already-committed policy contract was
adopted by both consumers.

The following gates passed in each product worktree:

```sh
cargo +1.92.0 test --locked --manifest-path rust/Cargo.toml --workspace
cargo +1.92.0 clippy --locked --manifest-path rust/Cargo.toml \
  --workspace --all-targets -- -D warnings
cargo +1.92.0 fmt --manifest-path rust/Cargo.toml --all -- --check
python3 scripts/verify_cargo_git_policy.py
python3 scripts/generate-third-party-notices.py --check
git diff --check
```

Mobile additionally passed seven exact-source policy tests. Its changed
runtime/resolver boundary passed 135 and 66 tests respectively. The committed
mobile notice digest is
`b05469ec1f0499363c5dbdd927cacb732b82716671a7a7f8c04ffe78d69275f3`.

Chromium additionally passed:

```sh
python3 -m unittest \
  tests.test_cargo_git_policy tests.test_ci_changed_targets
./scripts/verify-supply-chain.sh
npm run check:extension
```

That retained 23 Python policy/path-classification tests, 154 runtime tests,
65 resolver tests, 14 native-host tests, and 15 extension tests. The unpacked
MV3 build contains the generated desktop notice, and the Linux/macOS and
Windows installers place the same notice beside the native host. Its committed
digest is
`27deb8f955d0054b27df32b889ea28aa29f7f454dc047af880fb79c28be50b4c`.

Finally, both commits were cloned with `git clone --no-local` into separate
temporary directories. From those clean object stores, with no product target
directory and Cargo forced offline, the following passed:

```sh
cargo +1.92.0 metadata --locked --offline \
  --manifest-path rust/Cargo.toml --format-version 1

# Mobile: 201 tests.
cargo +1.92.0 test --locked --offline \
  --manifest-path rust/Cargo.toml \
  -p hns-browser-runtime -p hns-resolver

# Chromium: 233 tests.
cargo +1.92.0 test --locked --offline \
  --manifest-path rust/Cargo.toml \
  -p hns-browser-runtime -p hns-resolver \
  -p hns-chromium-native-host
```

The exact-source and notice verifiers passed again inside each clean clone;
the Chromium clone also passed all 15 extension tests and rebuilt the unpacked
extension with `CARGO_NET_OFFLINE=true`.

This checkpoint proves the first consolidation slice only. It does not upgrade
signed-device, installed-browser, HIP 77/78 runtime, complete engine
consolidation, or release-readiness rows.
