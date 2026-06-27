---
title: DiagnosesInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/diagnosesinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/diagnosesinput/index.md
---

Payload for a diagnosis

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the diagnosis will be deleted upon saving

[`active` ](#field-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the diagnosis is active or not

[`primary` ](#field-primary)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the diagnosis is the primary diagnosis

[`end_date` ](#field-end-date)· [`String` ](/reference/2026-01-01/scalars/string)· The date of the end of the diagnosis

[`first_symptom_date` ](#field-first-symptom-date)· [`String` ](/reference/2026-01-01/scalars/string)· The date of the first symptom

[`icd_code_id` ](#field-icd-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the ICD code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the diagnosis

## Used By

[`updateClientInput.diagnoses`](/reference/2026-01-01/input-objects/updateclientinput)

## Definition

```
"""
Payload for a diagnosis
"""
input DiagnosesInput {
  """
  If true, the diagnosis will be deleted upon saving
  """
  _destroy: Boolean


  """
  Whether the diagnosis is active or not
  """
  active: Boolean


  """
  Whether the diagnosis is the primary diagnosis
  """
  primary: Boolean


  """
  The date of the end of the diagnosis
  """
  end_date: String


  """
  The date of the first symptom
  """
  first_symptom_date: String


  """
  The ID of the ICD code
  """
  icd_code_id: ID


  """
  The ID of the diagnosis
  """
  id: ID
}
```
