---
title: startingSuperBillIcd10s | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/startingsuperbillicd10s/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/startingsuperbillicd10s/index.md
---

initial icd10 codes for a new super bill

## Arguments

[`form_answer_group_id` ](#argument-form-answer-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`[IcdCodesSuperBill!]`](/reference/2026-01-01/objects/icdcodessuperbill)

## Example

```
query startingSuperBillIcd10s($form_answer_group_id: ID, $user_id: ID) {
  startingSuperBillIcd10s(
    form_answer_group_id: $form_answer_group_id
    user_id: $user_id
  ) {
    created_at
    icd_code
    icd_code_id
    id
    super_bill_id
    updated_at
  }
}
```
