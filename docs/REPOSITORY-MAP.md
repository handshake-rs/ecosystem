# Repository Map

## Maintained products

| Repository | Responsibility |
| --- | --- |
| `hns-rs` | Reusable Handshake protocol, wire, primitive, and consensus libraries |
| `hns-node-rs` | Full-node networking, chain state, storage, RPC, and deployment |
| `MeshMine` | Decentralized mining, hardware backends, work scheduling, and operator UI |
| `hns-dane-engine` | DANE resolution, validation, and policy engine |
| `hns-dane-browser-mobile` | Mobile browser integration |
| `hns-dane-browser-extension` | Desktop browser-extension integration |

## Coordination

This repository owns cross-project architecture decisions, pinned integration
manifests, source-audit reports, compatibility matrices, and release
qualification. It must not become a copy of every product repository.

## External references

`hsd`, `hs-client`, HIPs, Shakedex, Bob Wallet, and Handshake documentation
remain upstream-owned reference inputs. Mirrors or forks require an explicit
maintenance reason and must preserve attribution and licensing.
