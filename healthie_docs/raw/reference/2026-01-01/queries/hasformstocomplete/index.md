---
title: hasFormsToComplete | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/hasformstocomplete/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/hasformstocomplete/index.md
---

Checks if the specified user has any forms to complete.

## Arguments

[`user_id` ](#argument-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the user.

## Returns

[`Boolean`](/reference/2026-01-01/scalars/boolean)

## Example

```
query hasFormsToComplete($user_id: ID!) {
  hasFormsToComplete(user_id: $user_id)
}
```
