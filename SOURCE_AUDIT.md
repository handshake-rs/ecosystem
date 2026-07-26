# Source audit

Audit root:
`/media/den/DEN_DATA_128/Organized_Backup/Personal/Documents/Projects/Crypto-and-Blockchain/handshake/hns-rust-ecosystem-2026-07-24`

Assignment document:

- file: `Complete Rust Handshake Ecosystem.pdf`
- size: 232,862 bytes
- SHA-256:
  `51dc7363ecc7c597c11de531fbeb1f45f3c6997a4d7b2c5065cd4be9681e7868`
- pages: 57

## Supplied snapshots

The three artifacts named by the assignment were not present in the
coordination root or `source-audit/` at audit time:

- `Browser-source-2026-07-24.zip`
- `MeshMine-source-2026-07-24(1).zip`
- `Pasted markdown(7).md`

No archive was invented, substituted, or extracted over a fresh clone.
Consequently there are no archive digests, embedded Git states, modified-file
comparisons, or archive-only implementations to report. If those exact files
become available, they must be hashed and extracted under `source-audit/`, and
this report must be extended without rewriting the working clones.

## Working repositories

| Path | Creation/source | Starting revision | Assigned branch |
| --- | --- | --- | --- |
| `work/hns-rs` | new Git repository | initial repository commit | `main` |
| `work/hns-node-rs` | history-preserving extraction from MeshMine `hsrd/` | subtree tip `a99f58ca66fc0288526a3af7aae448e7af9bfbd1` | `main` |
| `work/MeshMine` | `https://github.com/denuoweb/MeshMine.git` | `67a11290d410dc88113c4c3516ce9d22e8640a49` | `codex/external-rust-node-and-experimental-p2p` |
| `work/hns-dane-engine` | new Git repository | unborn | `main` |
| `work/hns-dane-browser-mobile` | `https://github.com/Denuo-Web/hns-dane-browser.git` | `a71f9ea8dd2e697df6059e8840907f96e6eea2c9` | `codex/shared-engine-p2p-privacy-transports` |
| `work/hns-dane-browser-extension` | same upstream, independent clone | `a71f9ea8dd2e697df6059e8840907f96e6eea2c9` | `codex/chromium-p2p-privacy-transports` |
| `integration` | new Git repository | unborn | `main` |

The HSRD extraction preserves source history while removing MeshMine as an
upstream dependency. Its exact extraction command and file-boundary report are
recorded in `work/hns-node-rs/docs/extraction-provenance.md`.

## Repositories added during organization migration

Two additional user-transferred products entered scope after the initial
assignment inventory. They were cloned only from their canonical transferred
destinations and retained their histories:

| Path | Canonical source | Starting revision |
| --- | --- | --- |
| `work/hns-dane-crawler` | `https://github.com/handshake-rs/hns-dane-crawler.git` | `b1428945ab187eee4c498a6f24e0977b995d596a` |
| `work/hns-dane-bootstrap-generator` | `https://github.com/handshake-rs/hns-dane-bootstrap-generator.git` | `f8ad194609708ba0fdec1f5884ad6871557cdec2` |

These auxiliary tools remain independent repositories. Their addition does
not rewrite the original supplied-artifact inventory or promote crawler data
or generated instructions to browser trust authority.

## Read-only authority

| Reference | Revision/status |
| --- | --- |
| `references/hsd` | `698e252ebc7b5c1dd0a9587e342fdd153d020ae4` |
| `references/HIPs` | `06f3226a8bf30b9517fe0f85c951d4a090786cd7` |
| `references/denuoweb-hsd` | `698e252ebc7b5c1dd0a9587e342fdd153d020ae4` |
| `references/hs-client` | `03a243a7fc38e2032950e6bec32d9137d2f74355` |
| `references/shakedex` | `ab5687b04cb61d2548937b8cee3c056c1c75bbdc` |
| `references/bob-wallet` | `0432158e5bc55c9d5aa24e0f256e468c44459d15` |
| `references/handshake-docs` | `b8611a6bd4e9208ec0561f0a5042c6bbc532e3a1` |

Reference repositories remain read-only. Canonical working checkpoints are
being published only to their matching `handshake-rs` repositories; reference
projects are neither pushed nor rewritten.

## Current local checkpoints

| Path | Current committed checkpoint |
| --- | --- |
| `work/hns-rs` | `dde2da81f29df935f043978a6d517c1d60ceff31` |
| `work/hns-node-rs` | `0e69319d11ca98d788466ed5028d8d897685e9f1` |
| `work/hns-dane-engine` | `127b9ad55852df00b4df40826517715048dc3571` |
| `work/hns-dane-browser-mobile` | `cde7d6d9d15859ebd5c4169433e72a7e434b2c1b` |
| `work/hns-dane-browser-extension` | `13dbb87240807dda0fb6f72c7aaaa7a33d036e70` |
| `work/hns-dane-crawler` | `74546c7e6b0b8a764525a77177a88dc333bf64d8` |
| `work/hns-dane-bootstrap-generator` | `f745f122243e5304e6a7ea0e111d47c61d22005e` |
| `work/MeshMine` | `bc9cc70de22e455545d44453cec0d6f07ebeaabe` |

Starting revisions above remain unchanged provenance facts. The standalone
node additionally records exact 126-commit subtree equivalence and its
qualification boundary in `work/hns-node-rs/docs/extraction-provenance.md`.
