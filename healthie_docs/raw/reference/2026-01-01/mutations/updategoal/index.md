---
title: updateGoal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updategoal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updategoal/index.md
---

Update a Goal

## Arguments

[`input` ](#argument-input)· [`updateGoalInput` ](/reference/2026-01-01/input-objects/updategoalinput)· Parameters for updateGoal

## Returns

[`updateGoalPayload`](/reference/2026-01-01/objects/updategoalpayload)

## Example

```
mutation updateGoal($input: updateGoalInput) {
  updateGoal(input: $input) {
    goal
    messages
  }
}
```
