---
title: cancelMobileHealthDataSnapshot | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/cancelmobilehealthdatasnapshot/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/cancelmobilehealthdatasnapshot/index.md
---

Cancels a mobile health data snapshot that encountered an error during upload or was abandoned by the mobile app

## Arguments

[`input` ](#argument-input)· [`CancelMobileHealthDataSnapshotInput` ](/reference/2026-01-01/input-objects/cancelmobilehealthdatasnapshotinput)· Parameters for CancelMobileHealthDataSnapshot

## Returns

[`CancelMobileHealthDataSnapshotPayload`](/reference/2026-01-01/objects/cancelmobilehealthdatasnapshotpayload)

## Example

```
mutation cancelMobileHealthDataSnapshot(
  $input: CancelMobileHealthDataSnapshotInput
) {
  cancelMobileHealthDataSnapshot(input: $input) {
    messages
    snapshot
  }
}
```
