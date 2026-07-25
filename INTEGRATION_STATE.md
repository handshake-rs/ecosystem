# Integration state

Status: **implementation in progress; not release-ready**

Last audited canonical `hns-rs` checkpoint:
`a5a2084f7cb1a878f4672b8c9ab6eeaedc1681fb`

Implemented and locally committed there:

- semantic primitives and canonical bounded encoding;
- headers, PoW, targets, chainwork, retargeting, networks, genesis;
- transactions, witnesses, addresses, coins, all covenant encodings/linkage;
- HSD sighash and lock predicates;
- HIP-0001/Shakedex v2 fixed and reverse-Dutch proof primitives;
- standard packet assignments/framing and strict core packet codecs;
- HSD-compatible Urkel proof parsing/verification;
- Denuo Experimental Registry v1 and collision-scoped negotiation;
- draft HIP 76, 77, and 78 protocol/cryptographic records.

Verified checkpoint gates:

- `cargo test --workspace`
- `cargo clippy --workspace --all-targets -- -D warnings`
- `cargo build --workspace --release`

Uncommitted work is not counted as a checkpoint until it passes the same gate.

The standalone node extraction currently points at history-preserving tip
`a99f58ca66fc0288526a3af7aae448e7af9bfbd1`; extraction cleanup/audit is in
progress. MeshMine and both browser clones remain at their starting commits.
The DANE engine is not implemented.

No push, public deployment, package publication, or mainnet state mutation has
occurred.
