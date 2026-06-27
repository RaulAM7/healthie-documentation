---
title: IcdCodesCms1500 | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodescms1500/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodescms1500/index.md
---

icd codes cms 1500s join table

## Fields

[`active` ](#field-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Active IcdCodesCms1500

[`cms1500_id` ](#field-cms1500-id)· [`ID` ](/reference/2026-01-01/scalars/id)· cms 1500 id

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date created

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· display name

[`end_date` ](#field-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· End date

[`first_symptom_date` ](#field-first-symptom-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· ICD codes in use for this claim

[`icd_code` ](#field-icd-code)· [`IcdCode` ](/reference/2026-01-01/objects/icdcode)· ICD code

[`icd_code_id` ](#field-icd-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· icd code id

deprecated

Use icd\_code instead

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the CMS 1500 ICD code

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date updated

## Used By

[`Cms1500.icd_codes_cms1500s`](/reference/2026-01-01/objects/cms1500)

## Definition

```
"""
icd codes cms 1500s join table
"""
type IcdCodesCms1500 {
  """
  Active IcdCodesCms1500
  """
  active: Boolean


  """
  cms 1500 id
  """
  cms1500_id: ID


  """
  date created
  """
  created_at: ISO8601DateTime


  """
  display name
  """
  display_name: String


  """
  End date
  """
  end_date: ISO8601DateTime


  """
  ICD codes in use for this claim
  """
  first_symptom_date: ISO8601DateTime


  """
  ICD code
  """
  icd_code: IcdCode


  """
  icd code id
  """
  icd_code_id: ID @deprecated(reason: "Use icd_code instead")


  """
  The unique identifier of the CMS 1500 ICD code
  """
  id: ID


  """
  date updated
  """
  updated_at: ISO8601DateTime
}
```
