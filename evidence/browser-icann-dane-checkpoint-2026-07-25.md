# Automatic ICANN DANE browser checkpoint

Date: 2026-07-25
Status: locally committed portable checkpoint; not a signed release

## Commit boundary

| Component | Commit |
| --- | --- |
| Shared `hns-icann-dane` policy | `f8e8d7709f93490595e02b0bd48d484ea2421ab8` |
| Android and iOS browser | `75b5108ea9080ca3b1d9c74127e24e30d848b843` |
| Chromium extension and native host | `3347d7fbd214d771e0571dcb5749990137e4bc77` |

All three worktrees were clean after these commits. Nothing was pushed.

## Shared trust contract

For every DNS-named HTTPS/WSS request admitted as ICANN, Rust derives
`_<effective-port>._<transport>.<host>.` after HTTPS/SVCB transport selection.
HTTP/1.1, HTTP/2, and WSS use TCP; HTTP/3 uses UDP.

| Authenticated validating-DoH evidence | Required result |
| --- | --- |
| Secure, supported TLSA RRset | Enforce DANE; mismatch is fatal |
| Secure authenticated denial | Explicit WebPKI fallback |
| Proven insecure/unsigned delegation | Ignore unsigned TLSA and use explicit WebPKI fallback |
| Bogus, indeterminate, malformed, timeout, resolver/HTTP/rcode error, or invalid owner | Fail closed |

The decision is retained into TLS verification and bound into connection,
verifier, resumption, and HTTP-pool identity where those caches exist. A
bounded secure CNAME chain may reach the terminal TLSA owner. Loops, multiple
aliases, CNAME/TLSA conflicts, malformed targets, excess depth, and aliases
without retained authenticated terminal evidence fail closed.

The precise user-facing name for this path is **DANE via ICANN DoH**.

## Browser request boundaries

| Browser | Lower-level enforcement boundary | Covered request classes |
| --- | --- | --- |
| Chromium | authenticated loopback proxy plus Rust native host | main-frame navigation, redirects, subresources, Service Workers, downloads, WSS |
| Android | whole-WebView authenticated proxy with bounded fail-closed interceptors | navigation, same/cross-origin proxy redirects, subresources, bodyless Service Worker GET/HEAD, native downloads, WSS |
| iOS | authenticated no-failover whole-WKWebView proxy | navigation, redirects, subresources, Service Workers at the WebKit proxy boundary, downloads, WSS |

The former exact-host `NativeGateway` exception is removed. Named ICANN
CONNECT requests are rejected for unsafe ports before any target TLS
connection. Public IP literals have no TLSA owner and retain only the
documented bounded opaque/WebPKI compatibility path.

## Portable validation completed

Shared engine:

- full workspace tests: 122 passed;
- strict all-target Clippy, release build, documentation tests, formatting,
  and C ABI smoke gate passed.

Android/iOS checkout:

- locked/offline Rust suites passed: `hns-icann-dane` 7,
  `hns-transport` 50, `android-ffi` 11, `hns-browser-runtime` 119,
  `hns-gateway` 48, `hns-loopback-proxy` 148, and `ios-ffi` 11;
- full locked/offline warning-denied workspace Clippy, formatting, optimized
  release build, portable C/C++ iOS ABI and exact-symbol checks, runtime and
  version boundary checks, notice verification, and 19 screenshot-tool tests
  passed.

Chromium checkout:

- automatic-DANE gateway suite: 47 passed;
- the named-ICANN unsafe-port and transport decision/cache regressions passed;
- focused strict Clippy, runtime/native checks, formatting, and diff audit
  passed;
- the preceding checkpoint retained 129 browser-runtime tests, 11 native-host
  tests, six Node/extension suites, isolated installer coverage, PAC parity,
  and the unpacked MV3 build.

## Qualification still open

- Android Gradle could not start because this host has no configured Android
  SDK (`SDK location not found`).
- This Linux host has no Xcode, Swift/XCTest, simulator, or physical iOS
  device.
- Signed Android/iOS device matrices and installed Chromium-family browser
  matrices remain required for network-process, lifecycle, restart, update,
  and uninstall behavior.
- The browser workspaces use a coordination-root path dependency on the shared
  policy crate. Release artifacts must pin or publish an immutable engine
  revision.

## Architectural follow-up

This checkpoint still inherits the static IANA-suffix namespace shortcut. That
list may be a cache or performance hint, but it is not sufficient authority
for a dual-root browser. The next classifier must resolve the complete
hostname independently through HNS and ICANN and report:

- HNS only;
- ICANN only;
- convergent answers;
- divergent answers with an explicit precedence decision and visible namespace
  choice; or
- neither.

An error, timeout, bogus proof, or indeterminate result from either root must
not be converted into authenticated absence. Live TLSA and negative-state
evidence for the current trust contract is retained in
`icann-dane-live-2026-07-25.md`.
