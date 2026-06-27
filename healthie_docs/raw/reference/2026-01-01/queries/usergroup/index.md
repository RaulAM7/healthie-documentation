---
title: userGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/usergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/usergroup/index.md
---

fetch a user group by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`UserGroup`](/reference/2026-01-01/objects/usergroup)

## Example

```
query userGroup($id: ID) {
  userGroup(id: $id) {
    created_at
    doc_share_id
    id
    invite_code
    name
    onboarding_flow
    onboarding_flow_id
    recurring_forms
    recurring_forms_count
    user
    user_ids
    users
    users_count
    users_with_membership
  }
}
```
