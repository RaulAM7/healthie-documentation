---
title: carePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/careplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/careplan/index.md
---

fetch a single care plan

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`is_managing_templates` ](#argument-is-managing-templates)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Deprecated. Does nothing

## Returns

[`CarePlan`](/reference/2026-01-01/objects/careplan)

## Example

```
query carePlan($id: ID, $is_managing_templates: Boolean) {
  carePlan(id: $id, is_managing_templates: $is_managing_templates) {
    assigned_to
    created_at
    creator
    description
    documents
    feature_toggle
    goals
    group_plan_is_active_for_given_user
    has_users_with_real_emails
    id
    is_active
    is_group
    is_hidden
    is_template
    name
    patient
    recommendations
    updated_at
    user_group
  }
}
```
