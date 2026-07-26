# Integration

This coordination repository records cross-repository tests and evidence
without merging product source into one tree. Current committed state is in
[`../INTEGRATION_STATE.md`](../INTEGRATION_STATE.md), and the required
demonstrations are tracked in
[`../QUALIFICATION_MATRIX.md`](../QUALIFICATION_MATRIX.md).

Integration gates should cover:

- shared protocol and serialization fixtures;
- full-node state and deployment compatibility;
- node-to-miner job and candidate publication paths;
- DANE engine and client conformance;
- crawler snapshot provenance and crawler-to-generator handoff integrity;
- bootstrap-generator record, appliance, and verification-output correctness;
- supported platform and hardware qualification;
- reproducible builds, upgrades, rollback, and release provenance.
