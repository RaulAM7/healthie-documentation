---
title: IcdCodesCms1500Input | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/icdcodescms1500input/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/icdcodescms1500input/index.md
---

Payload for ICD code on CMS 1500 form

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the ICD code will be deleted from the join table

[`active` ](#field-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the ICD code is active

[`end_date` ](#field-end-date)· [`String` ](/reference/2026-01-01/scalars/string)· The end date of the ICD code

[`first_symptom_date` ](#field-first-symptom-date)· [`String` ](/reference/2026-01-01/scalars/string)· The first symptom date of the ICD code

[`icd_code_id` ](#field-icd-code-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the ICD code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the ICD code join table

## Used By

[`createCms1500Input.icd_codes_cms1500s`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.icd_codes_cms1500s`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for ICD code on CMS 1500 form
"""
input IcdCodesCms1500Input {
  """
  If true, the ICD code will be deleted from the join table
  """
  _destroy: Boolean


  """
  Whether the ICD code is active
  """
  active: Boolean


  """
  The end date of the ICD code
  """
  end_date: String


  """
  The first symptom date of the ICD code
  """
  first_symptom_date: String


  """
  The ID of the ICD code
  """
  icd_code_id: String


  """
  The ID of the ICD code join table
  """
  id: ID
}
```
