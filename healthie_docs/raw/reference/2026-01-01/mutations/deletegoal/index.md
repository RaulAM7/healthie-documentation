---
title: deleteGoal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletegoal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletegoal/index.md
---

Destroy a Goal

## Arguments

[`input` ](#argument-input)· [`deleteGoalInput` ](/reference/2026-01-01/input-objects/deletegoalinput)· Parameters for deleteGoal

## Returns

[`deleteGoalPayload`](/reference/2026-01-01/objects/deletegoalpayload)

## Example

```
mutation deleteGoal($input: deleteGoalInput) {
  deleteGoal(input: $input) {
    goal
    messages
  }
}
```
