---
title: PatientEncounter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/patientencounter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/patientencounter/index.md
---

The details for a patient encounter

## Fields

[`appointment` ](#field-appointment)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· The appointment associated with the patient encounter

[`charting_notes` ](#field-charting-notes)· [`[FormAnswerGroup!]` ](/reference/2026-01-01/objects/formanswergroup)· The charting notes for the patient encounter

[`cms1500` ](#field-cms1500)· [`Cms1500` ](/reference/2026-01-01/objects/cms1500)· The CMS1500 for the patient encounter

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the patient encounter

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· The patient associated with this patient encounter

[`requested_payments` ](#field-requested-payments)· [`[RequestedPayment!]` ](/reference/2026-01-01/objects/requestedpayment)· The invoices for the patient encounter

## Used By

[`EpisodeOfCare.patient_encounters`](/reference/2026-01-01/objects/episodeofcare)

[`Query.patientEncounter`](/reference/2026-01-01/queries/patientencounter)

## Definition

```
"""
The details for a patient encounter
"""
type PatientEncounter {
  """
  The appointment associated with the patient encounter
  """
  appointment: Appointment


  """
  The charting notes for the patient encounter
  """
  charting_notes: [FormAnswerGroup!]


  """
  The CMS1500 for the patient encounter
  """
  cms1500: Cms1500


  """
  The unique identifier of the patient encounter
  """
  id: ID!


  """
  The patient associated with this patient encounter
  """
  patient: User


  """
  The invoices for the patient encounter
  """
  requested_payments: [RequestedPayment!]
}
```
