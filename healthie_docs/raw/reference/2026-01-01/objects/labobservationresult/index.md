---
title: LabObservationResult | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/labobservationresult/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/labobservationresult/index.md
---

A lab observation result

## Fields

[`abnormal_flag` ](#field-abnormal-flag)· [`String` ](/reference/2026-01-01/scalars/string)· The flag of abnormality in the observation

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the result

[`interpretation` ](#field-interpretation)· [`LabOrderInterpretation!` ](/reference/2026-01-01/enums/laborderinterpretation)· required · The interpretation of the lab observation result

[`is_abnormal` ](#field-is-abnormal)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True indicates the result is abnormal

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· The notes of the lab observation

[`qualitative_result` ](#field-qualitative-result)· [`String` ](/reference/2026-01-01/scalars/string)· The qualitative result of the lab observation

[`quantitative_result` ](#field-quantitative-result)· [`String` ](/reference/2026-01-01/scalars/string)· The quantitative result of the lab observation

[`reference_range` ](#field-reference-range)· [`String` ](/reference/2026-01-01/scalars/string)· The reference range of the lab observation

[`units` ](#field-units)· [`String` ](/reference/2026-01-01/scalars/string)· The units of the lab observation measurement

## Used By

[`LabObservationRequest.lab_observation_results`](/reference/2026-01-01/objects/labobservationrequest)

## Definition

```
"""
A lab observation result
"""
type LabObservationResult {
  """
  The flag of abnormality in the observation
  """
  abnormal_flag: String


  """
  The unique identifier of the result
  """
  id: ID!


  """
  The interpretation of the lab observation result
  """
  interpretation: LabOrderInterpretation!


  """
  True indicates the result is abnormal
  """
  is_abnormal: Boolean


  """
  The notes of the lab observation
  """
  notes: String


  """
  The qualitative result of the lab observation
  """
  qualitative_result: String


  """
  The quantitative result of the lab observation
  """
  quantitative_result: String


  """
  The reference range of the lab observation
  """
  reference_range: String


  """
  The units of the lab observation measurement
  """
  units: String
}
```
