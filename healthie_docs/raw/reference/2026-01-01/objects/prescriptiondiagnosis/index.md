---
title: PrescriptionDiagnosis | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/prescriptiondiagnosis/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/prescriptiondiagnosis/index.md
---

Prescription Diagnosis created in Dosespot

## Fields

[`diagnosis_code` ](#field-diagnosis-code)· [`String` ](/reference/2026-01-01/scalars/string)· ICD10 Code in Dosespot for the diagnosis

[`diagnosis_description` ](#field-diagnosis-description)· [`String` ](/reference/2026-01-01/scalars/string)· Dosespot description of the diagnosis

[`diagnosis_id` ](#field-diagnosis-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Dosespot ID of the diagnosis

[`is_primary` ](#field-is-primary)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Primary diagnosis

## Used By

[`Prescription.first_prescription_diagnosis`](/reference/2026-01-01/objects/prescription)

[`Prescription.second_prescription_diagnosis`](/reference/2026-01-01/objects/prescription)

## Definition

```
"""
Prescription Diagnosis created in Dosespot
"""
type PrescriptionDiagnosis {
  """
  ICD10 Code in Dosespot for the diagnosis
  """
  diagnosis_code: String


  """
  Dosespot description of the diagnosis
  """
  diagnosis_description: String


  """
  Dosespot ID of the diagnosis
  """
  diagnosis_id: ID


  """
  Primary diagnosis
  """
  is_primary: Boolean
}
```
