---
title: deleteGoalHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletegoalhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletegoalhistory/index.md
---

Destroy a Goal GoalHistory

## Arguments

[`input` ](#argument-input)· [`deleteGoalHistoryInput` ](/reference/2026-01-01/input-objects/deletegoalhistoryinput)· Parameters for deleteGoalHistory

## Returns

[`deleteGoalHistoryPayload`](/reference/2026-01-01/objects/deletegoalhistorypayload)

## Example

```
mutation deleteGoalHistory($input: deleteGoalHistoryInput) {
  deleteGoalHistory(input: $input) {
    goal_history
    messages
  }
}
```
