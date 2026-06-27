---
title: IndividualClientType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/individualclienttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/individualclienttype/index.md
---

An object containing an individual note for certain patient associated with group charting note

## Fields

[`appointment_inclusion_id` ](#field-appointment-inclusion-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of related appointment\_inclusion

[`attended` ](#field-attended)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if user has attended the appointment

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· The content of the note

[`icd_codes_individual_client_notes` ](#field-icd-codes-individual-client-notes)· [`[IcdCodesIndividualClientNote!]` ](/reference/2026-01-01/objects/icdcodesindividualclientnote)· Diagnoses connected to the individual client attendance

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the note

[`join_time` ](#field-join-time)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The datetime that the attendee joined the appointment (comes from the related appointment inclusion)

[`leave_time` ](#field-leave-time)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The datetime that the attendee left the appointment (comes from the related appointment inclusion)

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time of the last update

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Associated patient

## Used By

[`FormAnswerGroup.individual_client_notes`](/reference/2026-01-01/objects/formanswergroup)

[`FormAnswerGroup.individual_note`](/reference/2026-01-01/objects/formanswergroup)

## Definition

```
"""
An object containing an individual note for certain patient associated with group charting note
"""
type IndividualClientType {
  """
  The ID of related appointment_inclusion
  """
  appointment_inclusion_id: ID


  """
  True if user has attended the appointment
  """
  attended: Boolean


  """
  The content of the note
  """
  content: String


  """
  Diagnoses connected to the individual client attendance
  """
  icd_codes_individual_client_notes: [IcdCodesIndividualClientNote!]


  """
  The unique identifier of the note
  """
  id: ID!


  """
  The datetime that the attendee joined the appointment (comes from the related appointment inclusion)
  """
  join_time: ISO8601DateTime


  """
  The datetime that the attendee left the appointment (comes from the related appointment inclusion)
  """
  leave_time: ISO8601DateTime


  """
  The time of the last update
  """
  updated_at: ISO8601DateTime


  """
  Associated patient
  """
  user: User
}
```
