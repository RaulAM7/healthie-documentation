---
title: goalHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/goalhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/goalhistory/index.md
---

Fetch goal history

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`GoalHistory`](/reference/2026-01-01/objects/goalhistory)

## Example

```
query goalHistory($id: ID) {
  goalHistory(id: $id) {
    action
    completed_on
    created_at
    description
    goal
    goal_id
    id
    is_subgoal
    name
    repeat
    user
    user_id
  }
}
```
