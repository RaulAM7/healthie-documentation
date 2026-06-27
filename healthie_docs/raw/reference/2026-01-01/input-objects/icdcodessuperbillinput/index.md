---
title: IcdCodesSuperBillInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/icdcodessuperbillinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/icdcodessuperbillinput/index.md
---

Payload for an ICD code super bill

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the ICD code super bill will be deleted

[`icd_code_id` ](#field-icd-code-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the ICD code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the ICD code super bill

## Used By

[`createSuperBillInput.icd_codes_super_bills`](/reference/2026-01-01/input-objects/createsuperbillinput)

[`updateSuperBillInput.icd_codes_super_bills`](/reference/2026-01-01/input-objects/updatesuperbillinput)

## Definition

```
"""
Payload for an ICD code super bill
"""
input IcdCodesSuperBillInput {
  """
  If true, the ICD code super bill will be deleted
  """
  _destroy: Boolean


  """
  The ID of the ICD code
  """
  icd_code_id: String


  """
  The ID of the ICD code super bill
  """
  id: ID
}
```
