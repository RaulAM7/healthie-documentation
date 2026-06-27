---
title: startingSuperBillCptCodes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/startingsuperbillcptcodes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/startingsuperbillcptcodes/index.md
---

initial cpt codes for a new super bill

## Arguments

[`form_answer_group_id` ](#argument-form-answer-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`form_answer_group_ids` ](#argument-form-answer-group-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`[CptCodesSuperBill!]`](/reference/2026-01-01/objects/cptcodessuperbill)

## Example

```
query startingSuperBillCptCodes(
  $form_answer_group_id: ID
  $form_answer_group_ids: [ID]
  $user_id: ID
) {
  startingSuperBillCptCodes(
    form_answer_group_id: $form_answer_group_id
    form_answer_group_ids: $form_answer_group_ids
    user_id: $user_id
  ) {
    billing_item_id
    cpt_code
    cpt_code_id
    created_at
    fee
    id
    mod1
    mod2
    mod3
    mod4
    pointers
    service_date
    super_bill_id
    units
    updated_at
  }
}
```
