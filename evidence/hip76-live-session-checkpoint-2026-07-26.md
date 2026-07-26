# HIP-76 live-session checkpoint

Date: 2026-07-26

Status: **implemented, qualified at the portable live-manager boundary, and
pushed; production DNS output and two-full-node qualification remain open**

## Exact revisions

- canonical protocol and role-policy source:
  `handshake-rs/hns-rs`
  `dde2da81f29df935f043978a6d517c1d60ceff31`;
- live-session implementation:
  `handshake-rs/hns-node-rs`
  `5a35ab9d84da26ce20b8f343efde31e77d6fc898`; and
- requester-opt-out regression and final canonical node main:
  `handshake-rs/hns-node-rs`
  `0e69319d11ca98d788466ed5028d8d897685e9f1`.

The node's lockfile pins the exact canonical `hns-rs` revision. No sibling
workspace path or copied protocol implementation is accepted as the
dependency boundary.

## Consent and authority boundary

- Requester eligibility defaults to `Auto` and has an independent opt-out.
  Requesting never advertises provider capacity. Live policy replacement and
  revocation are implemented; durable reload across process restart is not.
- HIP-76's so-called relay sees the plaintext qname and performs DNS egress,
  so it is an output/provider role. It defaults off and requires explicit
  operator opt-in plus a ready backend before the service bit is advertised.
- Default-on, opt-out opaque P2P relay policy remains a separate capability and
  cannot grant DNS output authority.
- A correlated response received over an authenticated peer is exposed only as
  `Hip76UntrustedDnsResponse`. Brontide authenticates peer provenance, not the
  DNS answer. Local DNSSEC, TLSA, DANE, namespace, and caching policy remain
  mandatory consuming-resolver work.

## Implemented live boundary

The live manager intercepts private `0xf0` and `0xf1` frames before generic
packet publication. It enforces packet-specific bounds before large plaintext
allocation and applies the same typed limits after Brontide authentication and
decryption. Public-network plaintext peer configuration is rejected; regtest
and simnet retain explicit plaintext development support.

Every admitted request carries peer provenance, a current policy generation,
DNS transaction/question correlation, absolute deadline, capacity accounting,
and a unique opaque socket-write receipt. Requester outcomes and provider work
capabilities are non-cloneable. Queue admission and completed socket writes
are separate phases, and stale capabilities cannot complete later work that
reuses a peer-supplied request ID.

The provider accepts one-question, non-recursive DNSSEC-shaped queries only:
`RD=0`, otherwise clear request flags, EDNS DO present, no ECS, an allowed
qtype, and a bounded canonical name. It can return correlated `InvalidQuery`,
`Busy`, or `ResolverUnavailable` statuses without treating them as
authenticated DNS answers.

## Live topology evidence

A real loopback TCP test joins two live peer managers, completes ordinary
Handshake readiness and canonical Denuo registry negotiation, then:

1. admits a requester operation only against the peer advertising an
   explicitly enabled and ready HIP-76 output;
2. carries the bounded `0xf0` request to a non-reader-thread provider work
   capability;
3. commits a fully correlated `0xf1` response only after writer-queue
   admission;
4. returns the response with the exact live peer/direction/transport
   provenance;
5. confirms neither private packet enters the generic packet stream;
6. exchanges ordinary `GetAddr` traffic afterwards; and
7. disables the requester policy, confirms new HIP-76 work fails
   `RequesterDisabled`, and again confirms ordinary P2P remains available.

The loopback topology intentionally uses regtest plaintext and therefore has
no authenticated remote static key. The Brontide runtime implementation copies
the authenticated session remote static key into peer provenance. Separate
frame tests prove authentication/decryption occurs before typed packet
classification, but do not assert that provenance end to end. Other tests
cover mainnet/testnet plaintext rejection, pre-allocation frame bounds,
malformed DNS, duplicate and unsolicited IDs, wrong-peer and stale-generation
work, timeouts, disconnects, revocation, bounded queues, failed writes, stale
queued frames, and qname-free native/RPC projection.

## Retained gates

The final source passed:

```text
cargo test -p hns-p2p --lib
63 passed

cargo test -p hns-rpc --lib
8 passed

cargo test -p hns-node --no-default-features --lib
109 passed

cargo clippy -p hns-p2p --all-targets -- -D warnings
passed

cargo clippy -p hns-rpc -p hns-node --all-targets --no-default-features -- -D warnings
passed

cargo fmt --all -- --check
passed

git diff --check
passed
```

The focused wire subset passed 17 tests and the Brontide subset passed 8
tests. They are included in the 63-test P2P total rather than counted twice.

A default-feature `hns-node` target was stopped after about 16 minutes while
the bundled RocksDB C++ dependency was still compiling. It did not report a
Rust test failure, but it is not recorded as a passing gate. The complete
portable no-default-feature node library suite above passed on final source.

## Remaining production gates

This checkpoint deliberately does not provide or claim:

- a production recursive and DNSSEC-validating provider backend;
- authenticated acceptance of remote DNS answers;
- durable operator-policy checksum/reload across process restart;
- a two-full-node public-network topology;
- installed service configuration, rate economics, or abuse qualification; or
- HIP-77, HIP-78, wallet, marketplace, or browser integration.

Those limits keep the role-safe transport milestone distinct from production
resolver and release readiness.
