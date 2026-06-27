---
title: createGoalHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/creategoalhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/creategoalhistory/index.md
---

create Goal History

## Arguments

[`input` ](#argument-input)· [`createGoalHistoryInput` ](/reference/2026-01-01/input-objects/creategoalhistoryinput)· Parameters for createGoalHistory

## Returns

[`createGoalHistoryPayload`](/reference/2026-01-01/objects/creategoalhistorypayload)

## Example

```
mutation createGoalHistory($input: createGoalHistoryInput) {
  createGoalHistory(input: $input) {
    goalHistory
    messages
  }
}
```
