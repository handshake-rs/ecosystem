# Mobile v0.5.5 release checkpoint — 2026-07-29

Status: Android production deployment verified; iOS build `57` is `VALID` and
its direct App Review submission is `WAITING_FOR_REVIEW` after protected upload
run `30456522039`; GitHub Release
[`v0.5.5`](https://github.com/handshake-rs/hns-dane-browser-mobile/releases/tag/v0.5.5)
is public with the verified APK and IPA assets.

## Exact checkpoints

| Surface | Source | Version | Verified state |
| --- | --- | --- | --- |
| Android | `d24f85158854abb8be4a7bb9e914aebe5e7e4679` | `0.5.5` / version code `46` | the signed AAB was uploaded to the Google Play production track and edit `17438779769069438085` completed; generated APKs for version code 46 are available |
| iOS | source and annotated `v0.5.5` tag `d926561091634cd69fc9b7e79a4b76003fa4ee47` | `0.5.5` / build `57` | exact-source Apple CI [run `30454904736`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30454904736) passed; build 57 is `VALID` and its direct App Review submission is `WAITING_FOR_REVIEW` after protected upload run `30456522039` |
| App Store screenshots | `d926561091634cd69fc9b7e79a4b76003fa4ee47` | four `1284 × 2778` live captures | [run `30454926117`](https://github.com/handshake-rs/hns-dane-browser-mobile/actions/runs/30454926117) passed provenance, semantic, and visual validation; artifact digest `sha256:8f417552b855cd06a3db3b700de93b33cb8a0133712cd0e1eff8ae50b6f39984` |
| Release documentation | `39ea427b744581ccc9a860f5f51f6fc31622d317` | Android/iOS v0.5.5 | final store, artifact, and review evidence reconciled without retagging the release source; documentation CI run `30460622706` passed |
| GitHub Release | annotated `v0.5.5` tag peels to `d926561091634cd69fc9b7e79a4b76003fa4ee47` | `v0.5.5` | public at the canonical tag URL with verified code 46 APK and build 57 IPA assets |

## Android artifact evidence

The signed APK is 51,326,667 bytes with SHA-256
`b36a4346ffcba14c081500ef3dc7c5012cabd30f42cdaa80a354eefb5da210ba`.
It identifies package `com.denuoweb.hnsdane`, version `0.5.5`, version code
`46`, minimum SDK 34, target SDK 37, and arm64 plus x86_64 native libraries.
APK v2 signing and 16 KiB zip alignment passed.

The uploaded AAB is 60,279,896 bytes with SHA-256
`728d8892e180d954652668a4e53a7e2d6c7542e9d36330f4803cdecdb34598b0`.
Google Play accepted it directly on the production track with completed
status; no testing or staged track was used.

## iOS review boundary

The iOS release target is direct App Store review for app
`6791914326` and bundle `com.denuoweb.hnsdane.ios`. It is not a TestFlight
release and no beta group is part of this checkpoint. Store release is
configured as manual, so approval does not authorize automatic public
availability.

Protected run `30456522039` signed and uploaded the 47,930,601-byte iPhone-only
IPA (SHA-256
`efea01f912035d0e2cde880a59cbe9e5b2e3f546e781fa5d9606942629225345`).
App Store Connect reports build `57` `VALID`; the one-item direct App Review
submission is `WAITING_FOR_REVIEW` with `releaseType=MANUAL` and
`reviewType=APP_STORE`. No TestFlight distribution or beta group was created.

Public GitHub Release `v0.5.5` was published on 2026-07-29 at the annotated tag
source above. APK asset `493959486` is 51,326,667 bytes with SHA-256
`b36a4346ffcba14c081500ef3dc7c5012cabd30f42cdaa80a354eefb5da210ba`;
IPA asset `494101433` is 47,930,601 bytes with SHA-256
`efea01f912035d0e2cde880a59cbe9e5b2e3f546e781fa5d9606942629225345`.

## Qualification boundary

This checkpoint records real build, signing, hosted-CI, screenshot, release,
and store-distribution evidence. It does not demonstrate the signed-device
Android/iOS matrix required by qualification row 22. Redirect, cross-origin
subresource, Service Worker, download, WSS, process-restart, policy-revocation,
and resolver-contact behavior still require retained installed-device
evidence. Qualification therefore remains `PARTIAL`, and ecosystem-wide
release readiness remains **NO**.
