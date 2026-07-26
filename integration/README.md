# Integration

This directory will coordinate cross-repository tests without merging all
products into one source tree.

Integration gates should cover:

- shared protocol and serialization fixtures;
- full-node state and deployment compatibility;
- node-to-miner job and candidate publication paths;
- DANE engine and client conformance;
- supported platform and hardware qualification;
- reproducible builds, upgrades, rollback, and release provenance.
