# Experimental assignment registry

Published canonical V1 source:

- [`handshake-rs/hns-rs/registry/denuo-experimental-v1.toml`](https://github.com/handshake-rs/hns-rs/blob/main/registry/denuo-experimental-v1.toml)

Published canonical V1 binary:

- [`handshake-rs/hns-rs/registry/denuo-experimental-v1.bin`](https://github.com/handshake-rs/hns-rs/blob/main/registry/denuo-experimental-v1.bin)

The local, unpublished V2 candidate is generated at
`work/hns-rs/registry/denuo-experimental-v2.toml` and
`work/hns-rs/registry/denuo-experimental-v2.bin`. No remote link is published
for those files until the candidate is pushed and released.

Registry fingerprints:

- V1: `95774db08c569b36fa7b7e4a071930f563b7251fc30934ba986732379a6e542d`
- V2: `734226e866435821e40be7bde85fb19dd6eb867c5620abb8347ac8cd23da4f2c`

The organization migration changed only canonical source-identity URLs encoded
in the registry metadata. Assignments, payload limits, meanings, and consent
defaults are unchanged.

Status: **Denuo Experimental Registry V1 and additive V2; neither is globally
authoritative or an official Handshake assignment registry.** V2 retains
every V1 assignment and adds one separately negotiated cross-chain protocol.
Peers must compare the exact generated fingerprint and may use only the
semantics present in the mutually selected registry version.

V2 is currently a locally qualified, unpublished `hns-rs` release candidate.
No maintained node or wallet release advertises protocol `0x0002`; the node's
five-role relay is a wire-disabled cache/policy core until it pins the
generated V2 types and installs the typed envelope adapter.

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
