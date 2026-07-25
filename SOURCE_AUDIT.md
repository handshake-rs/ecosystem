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

## Read-only authority

| Reference | Revision/status |
| --- | --- |
| `references/hsd` | `698e252ebc7b5c1dd0a9587e342fdd153d020ae4` |
| `references/HIPs` | `06f3226a8bf30b9517fe0f85c951d4a090786cd7` |
| remaining reference clones | tracked in `REFERENCE_COMMITS.md`; incomplete clones are not treated as authority |

Reference repositories are read-only. No working repository has been pushed.
