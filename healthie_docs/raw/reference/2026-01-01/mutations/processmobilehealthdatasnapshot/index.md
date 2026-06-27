---
title: processMobileHealthDataSnapshot | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/processmobilehealthdatasnapshot/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/processmobilehealthdatasnapshot/index.md
---

Mobile app usage only. Downloads and processes mobile health categories like: 'Heart Rate', 'Steps', etc.

## Arguments

[`input` ](#argument-input)· [`ProcessMobileHealthDataSnapshotInput` ](/reference/2026-01-01/input-objects/processmobilehealthdatasnapshotinput)· Parameters for ProcessMobileHealthDataSnapshot

## Returns

[`ProcessMobileHealthDataSnapshotPayload`](/reference/2026-01-01/objects/processmobilehealthdatasnapshotpayload)

## Example

```
mutation processMobileHealthDataSnapshot(
  $input: ProcessMobileHealthDataSnapshotInput
) {
  processMobileHealthDataSnapshot(input: $input) {
    messages
    snapshot
  }
}
```
