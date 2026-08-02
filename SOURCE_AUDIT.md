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

Two additional user-transferred products and the organization profile entered
scope after the initial assignment inventory. The products were cloned only
from their canonical transferred destinations and retained their histories:

| Path | Canonical source | Starting revision |
| --- | --- | --- |
| `work/hns-dane-crawler` | `https://github.com/handshake-rs/hns-dane-crawler.git` | `b1428945ab187eee4c498a6f24e0977b995d596a` |
| `work/hns-dane-bootstrap-generator` | `https://github.com/handshake-rs/hns-dane-bootstrap-generator.git` | `f8ad194609708ba0fdec1f5884ad6871557cdec2` |
| `work/handshake-rs-profile` | `https://github.com/handshake-rs/.github.git` | `534ffce5093363fd722de4de3d8cba9df47e7efd` |

These auxiliary tools remain independent repositories. Their addition does
not rewrite the original supplied-artifact inventory or promote crawler data
or generated instructions to browser trust authority. The `.github`
repository contains organization profile/governance material, not a combined
product package.

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
published only to their matching `handshake-rs` repositories; reference
projects are neither pushed nor rewritten.

## Current local checkpoints

| Path | Current committed checkpoint |
| --- | --- |
| `work/hns-rs` | latest local source-only head `825f212de49d57b0ae7b5bbd0c038ddec5d52ce2`; remote documentation head `f6f46e1ecf9b31ca6592a6350c254a6effb9c9d0`; published `0.1.0` source `0ea5994c336642ea7d01c51c0e22df2008985426`; no `v0.1.0` tag |
| `work/hns-node-rs` | latest local source-only head `74f7ae36ddfd4a396451d33a2bca1c71a04f8a75`; remote/public documentation checkpoint `eba0237dedcbc958a8bc09dd811a4a9eeaa9afe7` |
| `work/hns-wallet-rs` | independently created local `main`; latest source-only head `768850982b37dc84030ab408de0f1f010cf42ed1`; no configured remote or published ABI |
| `work/hns-dane-engine` | latest local source-only head `f76ad37232bcadc85eb9b9bee5f45bff8405b583`; remote `main` `7f7bb8fa100c2393f2cd5a64c64bf5e20a0f3ab5`; older unpublished preparation predecessor `1d0fc9c6ba72f008e60d8c5a98741a32aeea4a75` |
| `work/hns-dane-browser-mobile` | latest local head `58996db0facef1bb6a7cb2876361d13dabc90c75`; Android 0.5.5/version-code-46 source `d24f85158854abb8be4a7bb9e914aebe5e7e4679`; iOS 0.5.5/build-57 source and `v0.5.5` tag `d926561091634cd69fc9b7e79a4b76003fa4ee47`; documentation head `39ea427b744581ccc9a860f5f51f6fc31622d317` |
| `work/hns-dane-browser-extension` | latest local source-only head `6285fda5a7ed61c5ac93f5127de078ce8587da38`; public v0.5.5 source/tag `86b18497285753944ec1b9196ec05ee359c6db11`; documentation head `3495bd1c5e7c26f9486ea81fb21dc1618c9bc2c8` |
| `work/hns-dane-crawler` | `b9e3c406631eb253f26979a0d3d9f794fd9fb11f` |
| `work/hns-dane-bootstrap-generator` | `ff1c709c8584b13bc02654d19ebc00d09025f4c7` |
| `work/MeshMine` | documentation head `9f781a00ee8fc3b7c6773538434235a65f167ca3` |
| `work/handshake-rs-profile` | documentation head `8da203b1359f4c595e0512b4914d1b4f8d497d69` |

Starting revisions above remain unchanged provenance facts. The standalone
node additionally records exact 126-commit subtree equivalence and its
qualification boundary in `work/hns-node-rs/docs/extraction-provenance.md`.
Current publication, release, and hosted-CI distinctions are recorded in
`evidence/non-mobile-publication-release-checkpoint-2026-07-29.md` and
`evidence/mobile-v0.5.5-release-checkpoint-2026-07-29.md`.
