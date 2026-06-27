---
title: updateFamilyHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefamilyhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefamilyhistory/index.md
---

Update Family History

## Arguments

[`input` ](#argument-input)· [`updateFamilyHistoryInput` ](/reference/2026-01-01/input-objects/updatefamilyhistoryinput)· Parameters for updateFamilyHistory

## Returns

[`updateFamilyHistoryPayload`](/reference/2026-01-01/objects/updatefamilyhistorypayload)

## Example

```
mutation updateFamilyHistory($input: updateFamilyHistoryInput) {
  updateFamilyHistory(input: $input) {
    duplicate_family_history_condition
    family_history_condition
    messages
  }
}
```
