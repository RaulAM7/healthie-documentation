---
title: LabResult | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/labresult/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/labresult/index.md
---

Lab Result

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the lab result record was created

[`document` ](#field-document)· [`Document` ](/reference/2026-01-01/objects/document)· Document for lab result

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the result

[`interpretation` ](#field-interpretation)· [`LabOrderInterpretation!` ](/reference/2026-01-01/enums/laborderinterpretation)· required · The interpretation of the lab result

[`lab_observation_requests` ](#field-lab-observation-requests)· [`[LabObservationRequest]` ](/reference/2026-01-01/objects/labobservationrequest)· Lab observation requests for lab result

[`lab_order_id` ](#field-lab-order-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the corresponding lab order

[`ordering_physician` ](#field-ordering-physician)· [`User` ](/reference/2026-01-01/objects/user)· Ordering Physician for lab result

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· Patient for lab result

[`result_type` ](#field-result-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the lab result

[`status_flag` ](#field-status-flag)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the result

## Used By

[`LabOrder.lab_results`](/reference/2026-01-01/objects/laborder)

[`Query.labResult`](/reference/2026-01-01/queries/labresult)

## Definition

```
"""
Lab Result
"""
type LabResult {
  """
  The time the lab result record was created
  """
  created_at: ISO8601DateTime!


  """
  Document for lab result
  """
  document: Document


  """
  The unique identifier of the result
  """
  id: ID!


  """
  The interpretation of the lab result
  """
  interpretation: LabOrderInterpretation!


  """
  Lab observation requests for lab result
  """
  lab_observation_requests: [LabObservationRequest]


  """
  The ID of the corresponding lab order
  """
  lab_order_id: ID!


  """
  Ordering Physician for lab result
  """
  ordering_physician: User


  """
  Patient for lab result
  """
  patient: User


  """
  The type of the lab result
  """
  result_type: String


  """
  The status of the result
  """
  status_flag: String
}
```
