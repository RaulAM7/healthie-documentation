---
title: deleteFamilyHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefamilyhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefamilyhistory/index.md
---

Delete a Family History Condition

## Arguments

[`input` ](#argument-input)· [`deleteFamilyHistoryInput` ](/reference/2026-01-01/input-objects/deletefamilyhistoryinput)· Parameters for deleteFamilyHistory

## Returns

[`deleteFamilyHistoryPayload`](/reference/2026-01-01/objects/deletefamilyhistorypayload)

## Example

```
mutation deleteFamilyHistory($input: deleteFamilyHistoryInput) {
  deleteFamilyHistory(input: $input) {
    family_history_condition
    messages
  }
}
```
