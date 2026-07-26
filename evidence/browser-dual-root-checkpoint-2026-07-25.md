# Browser dual-root namespace checkpoint

Date: 2026-07-25

Status: shared and portable browser-adapter checkpoint complete; installed
browser/device qualification remains open

## Immutable shared authority

| Repository | Commit | Scope |
| --- | --- | --- |
| `work/hns-dane-engine` | `127b9ad55852df00b4df40826517715048dc3571` | canonical repository checkpoint containing shared full-origin HNS/ICANN policy commit `ab3543ba9b80d23f9fe5a25abf44abd7496a41a2` |

The shared `hns-namespace-resolution` crate contains no IANA root-zone list.
Platform adapters must independently submit a complete HNS result and a
complete ICANN result for the same scheme, host, effective origin port, and
protocol-capability query. Each result is exactly one of a validated whole
origin plan, typed authenticated absence, or typed failure.

## Retained decision

The contract produces only these authoritative outcomes:

| HNS | ICANN | Result |
| --- | --- | --- |
| present | absent | HNS only |
| absent | present | ICANN only |
| present | equivalent present | both convergent |
| present | different present | both divergent |
| absent | absent | neither |
| failure | any | indeterminate error |
| any | failure | indeterminate error |

Every valid plan retains the complete origin alias path, terminal HTTPS/SVCB
owner, normalized ServiceMode target, separate endpoint CNAME path, final
A/AAAA owner and endpoints, selected service parameters, effective
port/transport/protocol, TLS action, and canonical supported TLSA records.
Plans are independently constructed and never merge records between roots.

HNS evidence retains the exact network, Urkel tree root, and height carried by
the lookup proof. ICANN evidence retains the authenticated validating-DoH
secure or proven-insecure chain state. Positive and negative evidence carries
absolute observation and expiry times; loading a cached result cannot restart
its TTL. Unsupported secure TLSA, terminal AliasMode, unsupported mandatory
SVCB keys, cycles, mismatched endpoints/hints, bogus or indeterminate DNSSEC,
stale evidence, missing provenance, and either root's failure remain terminal.

The precedence order is exact-origin explicit pin, successful persistent
binding, then ICANN on first use. A stricter require-explicit-selection mode is
available; there is no unpinned HNS-first mode. An absent pinned or bound root
cannot silently switch to the other root.

The decision fingerprint binds the complete query, exact policy, HNS network,
outcome, selected root, and both retained plans/absence evidence while
intentionally ignoring refreshed TTLs and volatile proof bytes. The decision
cache key is derived from that actual decision and additionally binds resolver
configuration and trust-anchor generation.

## Shared-engine qualification

All commands used the locked dependency graph with no dependency download:

```text
cargo +1.89.0 test --workspace --all-targets --all-features --locked --offline
  PASS — 144 unit tests

cargo +1.89.0 test --workspace --doc --all-features --locked --offline
  PASS — 20 doc-test targets, 0 doctests

cargo +1.89.0 clippy --workspace --all-targets --all-features --locked --offline -- -D warnings
  PASS

cargo +1.89.0 build --workspace --all-features --release --locked --offline
  PASS

cc -std=c11 -Wall -Wextra -Werror -fsyntax-only tests/abi_header_smoke.c
  PASS

cargo +1.89.0 fmt --all -- --check
  PASS

git diff --cached --check
  PASS before commit
```

The full test command ran with permission for its local-only UDP/TCP regtest
sockets. It made no public resolver or dependency-network contact.

## Browser adapter evidence

| Adapter | Implementation | Canonical `main` |
| --- | --- | --- |
| Android/iOS mobile | `f25d5fd6dff33a46d5ebd11f73f7f99ec2e3b0b0` | `0d069d102c0bf8fe9975798faf6864193fe20bf3` |
| Chromium extension/native host | `124190f01c587bce2792a456cb40aab7d0247dfe` | `bcf587a6cc06c9c07c1f713eef108d317fcadfc7` |

Both canonical browser lockfiles resolve `hns-icann-dane` and
`hns-namespace-resolution` from exact
`handshake-rs/hns-dane-engine` revision
`127b9ad55852df00b4df40826517715048dc3571`. Their `cargo-deny` policies reject
unknown Git sources and allowlist only that canonical URL.

The adapters independently prepare complete A and AAAA endpoint observations,
HTTPS/SVCB service policy, CNAME paths, and transport-aware TLSA evidence
through both roots. They consume only the selected immutable plan: later DNS,
cross-root address/trust mixing, missing-HNS-TLSA downgrades, contradictory
NXDOMAIN answers, repeated-alias ambiguity, stale denial signatures, unsigned
TLSA under a secure chain, and binding-persistence failure are all covered by
fail-closed regressions. HNS, ICANN, and diagnostic trace events remain
partitioned even when ICANN is selected.

The same lower Rust request boundary covers main-frame navigation, redirects,
subresources, supported Service Worker requests, downloads, and WebSocket
tunnels. Android and Swift parse/admit URLs and present settings/status, but do
not make the namespace or trust decision. Mobile requester relay consumption
is independently off by default; that does not alter the separate
default-on/persistent-opt-out opaque relayer role or grant output-node
authority.

Post-migration browser gates:

```text
Android/iOS:
  469 focused mobile-workspace Rust tests              PASS
    browser-runtime 134; loopback 147; resolver 65;
    transport 51; gateway 50; android-ffi 11; ios-ffi 11
  warning-denied workspace Clippy and rustfmt          PASS
  cargo-deny advisories/bans/licenses/sources           PASS
  Apple ABI: ios-ffi, C/C++ headers, archive symbols    PASS
  ios-ffi exact ABI suite, 50 repeated rounds           PASS
  Android Gradle unit/lint/instrumentation               NOT RUN — no SDK/NDK
  App Store metadata validator                           BLOCKED — screenshots
    still carry a pre-checkpoint WebPKI security label

Chromium:
  481 focused Rust tests                                 PASS
    browser-runtime 154; gateway 48; loopback 152;
    resolver 64; transport 51; native host 12
  doc tests, warning-denied Clippy, rustfmt               PASS
  cargo-deny advisories/bans/licenses/sources             PASS
  six Node extension suites and unpacked MV3 build        PASS
  independent final P0/P1 diff audit                      PASS
  installed six-browser OS matrix                         NOT RUN
```

The apparent Apple ABI failure seen once under the restricted command sandbox
was reproduced as denied loopback binding, not a runtime race. The exact same
binary passed when permitted to bind only its ephemeral local proxy sockets,
and the 50-round stress run passed.

Both adapter checkpoints and the engine authority were pushed to their
canonical `handshake-rs` `main` branches. No package, store artifact,
production service, or mainnet state was published or changed.

## Live ICANN DANE evidence

One external audit query checked the exact service owner independently of the
browser fixtures:

```text
delv _443._tcp.dane-test.denuoweb.com. TLSA
  fully validated
  TLSA 3 1 1
  369E0DBBA20489BDEE1A963239716DD16C6FECC6EFC30116889AB6AD6DC18BAE
  accompanying RRSIG TLSA present
```

This confirms that the live origin supplies ordinary DNSSEC-authenticated
authoritative TLSA data; it does not rely on a proprietary discovery record.
The command was external audit evidence, not browser-runtime resolver traffic,
and does not substitute for the still-required installed-browser/device
matrix.
