---
title: Diagnosis | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/diagnosis/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/diagnosis/index.md
---

A diagnosis

## Fields

[`active` ](#field-active)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Active diagnosis

[`custom_module_id` ](#field-custom-module-id)· [`ID` ](/reference/2026-01-01/scalars/id)· custom module id

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· A display name - for use in labels

[`end_date` ](#field-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· End date

[`first_symptom_date` ](#field-first-symptom-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· First symptom date

[`icd_code` ](#field-icd-code)· [`IcdCode` ](/reference/2026-01-01/objects/icdcode)· icd code

[`icd_code_id` ](#field-icd-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· icd code id

[`icd_codes_cms1500s_id` ](#field-icd-codes-cms1500s-id)· [`ID` ](/reference/2026-01-01/scalars/id)· icd codes cms1500s id

[`icd_codes_super_bill_id` ](#field-icd-codes-super-bill-id)· [`ID` ](/reference/2026-01-01/scalars/id)· icd codes super bill id

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the diagnosis

[`primary` ](#field-primary)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Primary diagnosis

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date diagnosis was last updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this diagnosis

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· user id

## Used By

[`EpisodeOfCare.diagnosis`](/reference/2026-01-01/objects/episodeofcare)

[`User.diagnoses`](/reference/2026-01-01/objects/user)

## Definition

```
"""
A diagnosis
"""
type Diagnosis {
  """
  Active diagnosis
  """
  active: Boolean!


  """
  custom module id
  """
  custom_module_id: ID


  """
  A display name - for use in labels
  """
  display_name: String


  """
  End date
  """
  end_date: ISO8601DateTime


  """
  First symptom date
  """
  first_symptom_date: ISO8601Date


  """
  icd code
  """
  icd_code: IcdCode


  """
  icd code id
  """
  icd_code_id: ID


  """
  icd codes cms1500s id
  """
  icd_codes_cms1500s_id: ID


  """
  icd codes super bill id
  """
  icd_codes_super_bill_id: ID


  """
  The unique identifier of the diagnosis
  """
  id: ID!


  """
  Primary diagnosis
  """
  primary: Boolean


  """
  Date diagnosis was last updated
  """
  updated_at: ISO8601DateTime


  """
  Owner of this diagnosis
  """
  user: User


  """
  user id
  """
  user_id: ID
}
```
