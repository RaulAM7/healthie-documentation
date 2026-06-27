---
title: intakeFlow | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/intakeflow/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/intakeflow/index.md
---

Fetch intake flow

## Arguments

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`sort_by` ](#argument-sort-by)· [`String` ](/reference/2026-01-01/scalars/string)· possible values: request\_date\_asc, request\_date\_desc, complete\_date\_asc, complete\_date\_desc, ​date\_asc, date\_desc, name\_asc, name\_desc, status\_asc, status\_desc, type\_asc, type\_desc

[`order_by` ](#argument-order-by)· [`IntakeFlowOrderKeys`](/reference/2026-01-01/enums/intakefloworderkeys)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`statuses` ](#argument-statuses)· [`[FormStatus]` ](/reference/2026-01-01/enums/formstatus)· Filter records by list of statuses

[`form_types` ](#argument-form-types)· [`[FormType]` ](/reference/2026-01-01/enums/formtype)· Filter records by list of form types

## Returns

[`IntakeFlowType`](/reference/2026-01-01/objects/intakeflowtype)

## Example

```
query intakeFlow(
  $keywords: String
  $sort_by: String
  $order_by: IntakeFlowOrderKeys
  $user_id: ID
  $statuses: [FormStatus]
  $form_types: [FormType]
) {
  intakeFlow(
    keywords: $keywords
    sort_by: $sort_by
    order_by: $order_by
    user_id: $user_id
    statuses: $statuses
    form_types: $form_types
  ) {
    all_forms
    completed_skipped
    forms
    intake_flows
    not_started_incomplete
    requested
  }
}
```
