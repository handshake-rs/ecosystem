# Reference Policy

Reference repositories provide protocol history, fixtures, interoperability
targets, and behavioral evidence. They are not automatically part of the
maintained Rust product surface.

A reference lock entry must record:

- canonical upstream URL;
- immutable commit identifier;
- license and attribution requirements;
- audit purpose;
- any patches applied locally;
- the date the reference was reviewed.

Prefer a bootstrap manifest or pinned Git submodule over copied source trees.
Never silently replace an upstream reference with a locally modified checkout.
