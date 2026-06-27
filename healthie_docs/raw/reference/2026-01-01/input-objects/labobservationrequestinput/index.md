---
title: LabObservationRequestInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/labobservationrequestinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/labobservationrequestinput/index.md
---

Payload for a client portal setting

## Fields

[`lab_analyte` ](#field-lab-analyte)· [`String` ](/reference/2026-01-01/scalars/string)· The substance being measured and test code. e.g 005009^CBC With Differential/Platelet^RN

[`lab_observation_result` ](#field-lab-observation-result)· [`LabObservationResultInput` ](/reference/2026-01-01/input-objects/labobservationresultinput)· the analyte result

## Used By

[`createLabOrderInput.lab_observation_requests`](/reference/2026-01-01/input-objects/createlaborderinput)

## Definition

```
"""
Payload for a client portal setting
"""
input LabObservationRequestInput {
  """
  The substance being measured and test code. e.g 005009^CBC With Differential/Platelet^RN
  """
  lab_analyte: String


  """
  the analyte result
  """
  lab_observation_result: LabObservationResultInput
}
```
