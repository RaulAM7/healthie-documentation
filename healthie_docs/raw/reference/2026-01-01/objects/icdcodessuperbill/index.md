---
title: IcdCodesSuperBill | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodessuperbill/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodessuperbill/index.md
---

icd codes super bills join table

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date the join was created

[`icd_code` ](#field-icd-code)· [`IcdCode` ](/reference/2026-01-01/objects/icdcode)· The joined ICD code object

[`icd_code_id` ](#field-icd-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the ICD code

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the join

[`super_bill_id` ](#field-super-bill-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the super bill

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last date when the join was updated

## Used By

[`Query.startingSuperBillIcd10s`](/reference/2026-01-01/queries/startingsuperbillicd10s)

[`SuperBill.icd_codes_super_bills`](/reference/2026-01-01/objects/superbill)

## Definition

```
"""
icd codes super bills join table
"""
type IcdCodesSuperBill {
  """
  The date the join was created
  """
  created_at: ISO8601DateTime


  """
  The joined ICD code object
  """
  icd_code: IcdCode


  """
  The ID of the ICD code
  """
  icd_code_id: ID


  """
  The unique identifier of the join
  """
  id: ID!


  """
  The ID of the super bill
  """
  super_bill_id: ID


  """
  The last date when the join was updated
  """
  updated_at: ISO8601DateTime
}
```
