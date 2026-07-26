# Standalone `hns-dane-engine` checkpoint

Date: 2026-07-26

Status: committed standalone-source and portable qualification milestone;
release qualification remains open

## Immutable source boundary

| Repository | Commit | Role |
| --- | --- | --- |
| `handshake-rs/hns-dane-engine` | `2850ac1f50e361e2772e18f2e5ecbd7e77085afb` | standalone engine source-policy and qualification checkpoint |
| `handshake-rs/hns-rs` | `dde2da81f29df935f043978a6d517c1d60ceff31` | exact canonical protocol dependency |

The engine root declares nine direct `hns-rs` packages exactly once. The
lockfile contains those packages plus the two required transitive packages,
for an exact eleven-package closure from the same canonical URL and revision.
Seven reviewed consumer manifests contain 24 inherited declarations. No
consumer uses a sibling checkout, mutable branch or tag, alternate URL,
renamed package, unreviewed Git dependency, or path outside the engine
repository.

`scripts/verify_cargo_source_policy.py` enforces those exact package,
manifest, declaration, URL, revision, lockfile, and repository-local path
sets. Its 12 mutation-derived tests pass. `cargo-deny` also passes its
advisory, license, ban, and source checks with `hns-rs` as the sole allowed
Git repository.

## Retained qualification

The complete local gate passed at the engine commit:

```text
source-policy verifier tests                         PASS — 12
exact source-policy verifier                         PASS
cargo-deny                                           PASS
cargo test --workspace --all-targets --all-features  PASS — 144 tests
cargo test --workspace --doc --all-features          PASS — 20 doc targets
cargo test --workspace --all-features                PASS — 144 tests
cargo test --workspace                               PASS — 144 tests
warning-denied all-target/all-feature Clippy          PASS
all-feature release build                            PASS
C11 ABI header syntax smoke                           PASS
formatting                                            PASS
```

Cargo metadata, compilation, tests, lint, and the release build used the
locked dependency graph with `--offline`.

The same checkpoint was then cloned at depth one into an isolated directory
with no sibling `hns-rs` tree and a separate `CARGO_HOME`. After fetching the
locked graph into that isolated Cargo home, the source verifier, locked
metadata check, `cargo-deny`, formatting, all four Rust test forms, Clippy,
release build, and ABI header smoke gate passed there as well. This proves
that the committed engine resolves from its own repository and immutable Git
dependency rather than from the coordination-workspace layout.

Commit `2850ac1f50e361e2772e18f2e5ecbd7e77085afb` also adds a GitHub Actions
workflow that performs source verification before fetching and then runs the
complete locked gate. The workflow was not polled or counted as passing in
this checkpoint.

## Consumer pin follow-up

After engine qualification, both browser products advanced their three exact
engine contracts without changing runtime source:

| Consumer | Commit | Retained qualification |
| --- | --- | --- |
| `handshake-rs/hns-dane-browser-mobile` | `7b826166a2bac3af8d2384dbff9875a992f252ca` | seven exact-source tests, source verifier, root/exporter locked metadata, deterministic notice/digest, and 302 focused offline Rust tests |
| `handshake-rs/hns-dane-browser-extension` | `1fde772006dde8b36c963b3ecc09cc011c542155` | nine exact-source tests, source/supply-chain/notice gates, 233 focused Rust tests, strict Clippy/formatting, lint, 15 extension tests, and extension build |

Each lockfile changes only the three reviewed engine source entries (plus the
mobile snapshot exporter's transitive namespace entry). The current mobile
notice digest is
`9299d5dffbc1bb14accce96293f3b46ebe46f5227649473549858b1af990b463`;
the current Chromium notice digest is
`b8cea340b3709947dcb0d5aa41bab45100fcd437a331ec2e41e886fd732187d7`.
Neither hosted consumer workflow was polled or counted as passing.

## Qualification boundary

A new environment must clone the engine and fetch its exact Git and registry
dependencies before Cargo can operate offline; `--offline` does not make the
initial Git objects appear without a fetch.

This milestone does not publish crates. A crates.io release still requires
compatible published `hns-rs` crates and versioned manifest dependencies.
Release SBOM/provenance, generated third-party notices, checksummed packages,
a fully linked ABI consumer/runtime matrix, retained fuzz qualification, and
production release signing remain later release work.
