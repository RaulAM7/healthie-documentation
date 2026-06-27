---
title: LabObservationResultInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/labobservationresultinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/labobservationresultinput/index.md
---

Payload for a client portal setting

## Fields

[`units` ](#field-units)· [`String` ](/reference/2026-01-01/scalars/string)· The units of the measurement e.g "x10E3/uL^x10E3/uL"

[`reference_range` ](#field-reference-range)· [`String` ](/reference/2026-01-01/scalars/string)· The reference range e.g "3.4-10.8"

[`qualitative_result` ](#field-qualitative-result)· [`String` ](/reference/2026-01-01/scalars/string)· The qualitative result e.g "005025^WBC^L^6690-2^Leukocytes^LN"

[`quantitative_result` ](#field-quantitative-result)· [`String` ](/reference/2026-01-01/scalars/string)· The quantitative result e.g "9.6"

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Extra description or context on the result

[`abnormal_flag` ](#field-abnormal-flag)· [`String` ](/reference/2026-01-01/scalars/string)· A flag on any abnormality (e.g L for low or H for high)

## Used By

[`LabObservationRequestInput.lab_observation_result`](/reference/2026-01-01/input-objects/labobservationrequestinput)

## Definition

```
"""
Payload for a client portal setting
"""
input LabObservationResultInput {
  """
  The units of the measurement e.g "x10E3/uL^x10E3/uL"
  """
  units: String


  """
  The reference range e.g "3.4-10.8"
  """
  reference_range: String


  """
  The qualitative result e.g "005025^WBC^L^6690-2^Leukocytes^LN"
  """
  qualitative_result: String


  """
  The quantitative result e.g "9.6"
  """
  quantitative_result: String


  """
  Extra description or context on the result
  """
  notes: String


  """
  A flag on any abnormality (e.g L for low or H for high)
  """
  abnormal_flag: String
}
```
