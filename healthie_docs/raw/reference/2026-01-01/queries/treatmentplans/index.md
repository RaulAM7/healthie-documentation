---
title: treatmentPlans | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/treatmentplans/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/treatmentplans/index.md
---

Fetch an array of treatment plans and recommended products from Fullscript given a user id

## Arguments

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`[FullscriptTreatmentPlanType!]`](/reference/2026-01-01/objects/fullscripttreatmentplantype)

## Example

```
query treatmentPlans($user_id: ID) {
  treatmentPlans(user_id: $user_id) {
    activation_date
    id
    ordered_count
    personal_message
    practitioner_name
    recommendations
  }
}
```
