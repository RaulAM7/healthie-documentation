---
title: createFamilyHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfamilyhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfamilyhistory/index.md
---

Create Family History

## Arguments

[`input` ](#argument-input)· [`createFamilyHistoryInput` ](/reference/2026-01-01/input-objects/createfamilyhistoryinput)· Parameters for createFamilyHistory

## Returns

[`createFamilyHistoryPayload`](/reference/2026-01-01/objects/createfamilyhistorypayload)

## Example

```
mutation createFamilyHistory($input: createFamilyHistoryInput) {
  createFamilyHistory(input: $input) {
    duplicate_family_history_condition
    family_history_condition
    messages
  }
}
```
