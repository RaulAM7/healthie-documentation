---
title: createGoal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/creategoal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/creategoal/index.md
---

create Goal

## Arguments

[`input` ](#argument-input)· [`createGoalInput` ](/reference/2026-01-01/input-objects/creategoalinput)· Parameters for createGoal

## Returns

[`createGoalPayload`](/reference/2026-01-01/objects/creategoalpayload)

## Example

```
mutation createGoal($input: createGoalInput) {
  createGoal(input: $input) {
    goal
    messages
  }
}
```
