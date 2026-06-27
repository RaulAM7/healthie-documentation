---
title: ClaimDiagnosis | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimdiagnosis/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimdiagnosis/index.md
---

Frozen diagnosis data from a submitted claim snapshot

## Fields

[`active` ](#field-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the diagnosis is active

[`end_date` ](#field-end-date)· [`String` ](/reference/2026-01-01/scalars/string)· Diagnosis end date

[`first_symptom_date` ](#field-first-symptom-date)· [`String` ](/reference/2026-01-01/scalars/string)· First symptom date

[`icd_code` ](#field-icd-code)· [`ClaimIcdCode` ](/reference/2026-01-01/objects/claimicdcode)· ICD code data

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Diagnosis join record ID

## Used By

[`Claim.diagnoses`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
Frozen diagnosis data from a submitted claim snapshot
"""
type ClaimDiagnosis {
  """
  Whether the diagnosis is active
  """
  active: Boolean


  """
  Diagnosis end date
  """
  end_date: String


  """
  First symptom date
  """
  first_symptom_date: String


  """
  ICD code data
  """
  icd_code: ClaimIcdCode


  """
  Diagnosis join record ID
  """
  id: ID
}
```
