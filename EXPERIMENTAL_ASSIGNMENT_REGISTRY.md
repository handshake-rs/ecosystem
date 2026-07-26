# Experimental assignment registry

Canonical source:
`work/hns-rs/registry/denuo-experimental-v1.toml`

Canonical binary:
`work/hns-rs/registry/denuo-experimental-v1.bin`

Registry fingerprint:
`c6f99e2403d5a9a2b257b995eca35082b51c75fa903a7fd3e354a1567529f1ff`

Status: **Denuo Experimental Registry v1; not globally authoritative and not
an official Handshake assignment registry.**

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

Wire assignments do not imply consent. The runtime distinguishes opaque relay
capacity from output-node capacity and persists each role independently:

| Runtime role | Default | Consent boundary |
| --- | --- | --- |
| HIP 76 DNS relay/output | Off | Explicit operator opt-in; sees the plaintext qname and originates DNS |
| HIP 77 ODoH proxy/opaque relay | On | Persistent operator opt-out |
| HIP 77 ODoH target/output | Off | Explicit operator opt-in |
| HNSR opaque relay | On | Persistent operator opt-out |
| HNSR endpoint/output | Off | Explicit operator opt-in |
| HNSR rendezvous | Off | Explicit operator opt-in |
| HNSR requester/client | Off | Independent client opt-in |

Requester policy for HIP 76/77 is separate from every provider role. Enabling
opaque relay capacity never enables an output role, and enabling requester
traffic never advertises provider capacity.

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
| reserved | `0x0002..=0xffff` | no semantics |

The fingerprint is SHA-256 of the generated canonical binary, not ordinary
TOML or JSON serialization. Mainnet/testnet experimental traffic requires the
service bit, established ordinary peer connection, `DENUO_EXT`, compatible
registry negotiation, semantic version agreement, and matching
network/genesis identity. A collision disables only the affected experimental
protocol; it does not by itself ban the peer or stop safe ordinary P2P.

Legacy PR behavior is confined to the explicit `LegacyDraftRegtest` profile.
Application code uses semantic assignments so future official mappings can be
added without rewriting stored domain objects.
