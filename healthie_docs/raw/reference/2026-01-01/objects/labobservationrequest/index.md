---
title: LabObservationRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/labobservationrequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/labobservationrequest/index.md
---

A lab observation request

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the request

[`lab_analyte` ](#field-lab-analyte)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the lab analyte

[`lab_observation_results` ](#field-lab-observation-results)· [`[LabObservationResult]!` ](/reference/2026-01-01/objects/labobservationresult)· required · Lab observation results for lab request

## Used By

[`LabResult.lab_observation_requests`](/reference/2026-01-01/objects/labresult)

## Definition

```
"""
A lab observation request
"""
type LabObservationRequest {
  """
  The unique identifier of the request
  """
  id: ID!


  """
  The name of the lab analyte
  """
  lab_analyte: String


  """
  Lab observation results for lab request
  """
  lab_observation_results: [LabObservationResult]!
}
```
