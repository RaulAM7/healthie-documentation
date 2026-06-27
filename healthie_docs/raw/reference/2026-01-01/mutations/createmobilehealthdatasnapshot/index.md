---
title: createMobileHealthDataSnapshot | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmobilehealthdatasnapshot/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmobilehealthdatasnapshot/index.md
---

Creates mobile health data snapshot record

## Arguments

[`input` ](#argument-input)· [`CreateMobileHealthDataSnapshotInput` ](/reference/2026-01-01/input-objects/createmobilehealthdatasnapshotinput)· Parameters for CreateMobileHealthDataSnapshot

## Returns

[`CreateMobileHealthDataSnapshotPayload`](/reference/2026-01-01/objects/createmobilehealthdatasnapshotpayload)

## Example

```
mutation createMobileHealthDataSnapshot(
  $input: CreateMobileHealthDataSnapshotInput
) {
  createMobileHealthDataSnapshot(input: $input) {
    messages
    snapshot
  }
}
```
