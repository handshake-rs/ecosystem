# Reference commits

## Repository snapshots

| Repository | URL | Revision |
| --- | --- | --- |
| HSD | `https://github.com/handshake-org/hsd.git` | `698e252ebc7b5c1dd0a9587e342fdd153d020ae4` |
| HIPs | `https://github.com/handshake-org/HIPs.git` | `06f3226a8bf30b9517fe0f85c951d4a090786cd7` |
| Shakedex | `https://github.com/kurumiimari/shakedex.git` | `ab5687b04cb61d2548937b8cee3c056c1c75bbdc` |
| Denuo HSD | `https://github.com/denuoweb/hsd.git` | clone verification pending |
| hs-client | `https://github.com/handshake-org/hs-client.git` | clone verification pending |
| Bob Wallet | `https://github.com/bob-wallet/bob-wallet.git` | clone verification pending |
| Handshake docs | `https://github.com/handshake-org/handshake-org.github.io.git` | clone verification pending |

## Draft pull-request snapshots

These values identify the fetched head commits used by the independent Rust
implementations. Draft assignments are not official Handshake assignments.

| Draft | Commit |
| --- | --- |
| HIP PR 76 | fetch verification pending |
| HSD PR 958 | fetch verification pending |
| HIP PR 77 | `d3ae6be483663ed6cf0ead4f4b4f17a80b1d1162` |
| HSD PR 959 | `909311d97c794eb59ed2eb0b095a122607ae078e` |
| HIP PR 78 | `53b962e901ffa796f4ccf66a5d53956d7421c58c` |
| HSD PR 960 | `2fc40f1c61ff16a2f39d9514cd950d1560430ced` |

Temporary fetch worktrees are evidence only and are never a replacement for
the required read-only reference refs. Pending cells must be resolved before
release qualification.

## Authority order

Consensus behavior follows compatible HSD execution, HSD tests, reproducible
HSD fixtures, compatible protocol documentation, existing Rust differential
tests, and only then architectural inference. Draft behavior follows exact PR
text/commits, deterministic PR fixtures, independent Rust vectors, the Denuo
registry, and documented migration rules.
