# Experimental assignment registry

Published Shakescape Experimental V1 source:

- [`handshake-rs/hns-rs/registry/shakescape-experimental-v1.toml`](https://github.com/handshake-rs/hns-rs/blob/main/registry/shakescape-experimental-v1.toml)

Published canonical binary:

- [`handshake-rs/hns-rs/registry/shakescape-experimental-v1.bin`](https://github.com/handshake-rs/hns-rs/blob/main/registry/shakescape-experimental-v1.bin)

The separate HNSR service-profile source and binary are
[`hnsr-service-profiles-v1.toml`](https://github.com/handshake-rs/hns-rs/blob/main/registry/hnsr-service-profiles-v1.toml)
and
[`hnsr-service-profiles-v1.bin`](https://github.com/handshake-rs/hns-rs/blob/main/registry/hnsr-service-profiles-v1.bin).
Adding a named route does not reinterpret or change the packet-registry
fingerprint.

Registry fingerprints:

- Shakescape V1: `04fce3f12b717c4254bb66ac07474a6c9f61bd2916efc18ebfc79df82a89a66b`
- HNSR service profiles V1: `59f47afa6e536afe784ba65823eb1a028fa0ace72d7e721888b4be586a687ad2`

The organization migration changed only canonical source-identity URLs encoded
in the registry metadata. Assignments, payload limits, meanings, and consent
defaults are unchanged.

Status: **Production-supported Shakescape Experimental V1; not globally
authoritative and not an official Handshake assignment registry.**
“Experimental” names the private assignment namespace and does not make the
published parsers or compatibility commitments prototypes. Peers compare the
exact generated fingerprints and use only mutually selected semantics.

The `hns-rs 0.4.1` publication contains the current registry and protocol
types. HNSR `0x0004` is an opaque swap-circuit protocol with independent
named requester profiles; it does not replace the atomic (`0x0001`) or
cross-chain (`0x0002`) marketplace assignments. See
[`CURRENT_STATE.md`](CURRENT_STATE.md) for current consumers and product gates.

## Service bits

| Semantic capability | Value | Status |
| --- | ---: | --- |
| HNSR rendezvous | `0x04000000` | stable-experimental |
| HNSR relay | `0x08000000` | stable-experimental |
| Denuo extension envelope | `0x10000000` | stable-experimental |
| P2P ODoH | `0x20000000` | stable-experimental |
| P2P DNS relay | `0x40000000` | stable-experimental |
| reserved | `0x80000000` | reserved; no v1 semantics |

Service masks remain unsigned 64-bit values internally.

## Runtime consent defaults

Wire assignments do not imply consent. The canonical policy distinguishes
opaque relay capacity from output-node capacity and represents each role
independently:

| Runtime role | Default | Consent boundary |
| --- | --- | --- |
| HIP 76 requester | Auto | Independent operator opt-out; live revocation implemented; never advertises provider capacity |
| HIP 76 DNS relay/output | Off | Explicit operator opt-in; sees the plaintext qname and originates DNS |
| HIP 77 ODoH proxy/opaque relay | On | Persistent operator opt-out |
| HIP 77 ODoH target/output | Off | Explicit operator opt-in |
| HNSR opaque relay | On | Persistent operator opt-out |
| HNSR endpoint/output | Off | Explicit operator opt-in |
| HNSR rendezvous | Off | Explicit operator opt-in |
| HNSR requester/client | Off | Independent HNSR client opt-in |

Requester policy is separate from every provider role. Enabling opaque relay
capacity never enables an output role, and enabling requester traffic never
advertises provider capacity. “Persistent” in this table is the required
operator-policy behavior for opaque relays; the current node enforces live
HIP-76 requester revocation but does not yet persist and reload that decision
across process restart.

Browser products deliberately do not inherit the generic HIP-76 requester
default. Their new and persisted requester switch starts false/off and
requires explicit user opt-in; false maps to `Disabled`, true maps to
direct-first `Auto`, browser P2P services remain zero, and every provider or
output role remains disabled.

## Packet types

| Semantic packet | Value | Maximum payload |
| --- | ---: | ---: |
| `GETDNSRELAY` | `0xf0` | 4,096 |
| `DNSRELAY` | `0xf1` | 65,535 |
| `ODNS` | `0xf2` | 65,535 |
| `HNSR` | `0xf3` | 262,144 |
| `DENUO_EXT` | `0xf4` | 1,048,576 |
| reserved | `0xf5..=0xff` | no semantics |

## Denuo extension protocols

| Protocol | ID | Maximum payload |
| --- | ---: | ---: |
| registry negotiation | `0x0000` | 16,384 |
| atomic name marketplace | `0x0001` | 1,048,576 |
| cross-chain marketplace (V2 only) | `0x0002` | 524,288 |
| reserved in V1 | `0x0002..=0xffff` | no semantics |
| reserved in V2 | `0x0003..=0xffff` | no semantics |

The atomic-name protocol defines eight typed message kinds: `HELLO`,
`GET_OFFER_INVENTORY`, `OFFER_INVENTORY`, `GET_OFFERS`, `OFFERS`, `GET_OFFER`,
`OFFER`, and `CANCEL`. The V2 cross-chain protocol defines fifteen typed kinds:
intent inventory/get/object/cancel, price-observation inventory/get/object and
price round, match request/fill grant/reject, session hello, and funding,
redeem, and refund status. All are nested in the existing bounded
`DENUO_EXT` envelope; V1 peers reject protocol `0x0002` rather than
reinterpreting it.

The fingerprint is SHA-256 of the generated canonical binary, not ordinary
TOML or JSON serialization. Mainnet/testnet experimental traffic requires the
service bit, established ordinary peer connection, `DENUO_EXT`, compatible
registry negotiation, semantic version agreement, and matching
network/genesis identity. A collision disables only the affected experimental
protocol; it does not by itself ban the peer or stop safe ordinary P2P.

Legacy PR behavior is confined to the explicit `LegacyDraftRegtest` profile.
Application code uses semantic assignments so future official mappings can be
added without rewriting stored domain objects.
