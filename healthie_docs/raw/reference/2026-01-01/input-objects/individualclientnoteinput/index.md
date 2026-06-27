---
title: IndividualClientNoteInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/individualclientnoteinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/individualclientnoteinput/index.md
---

Payload for an individual client note

## Fields

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· The content of the individual client note

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the individual client note

[`attended` ](#field-attended)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The client's attendance status. This gets applied to the AppointmentInclusion object

[`icd_codes_individual_client_notes_attributes` ](#field-icd-codes-individual-client-notes-attributes)· [`[IcdCodesIndividualClientNoteInput]` ](/reference/2026-01-01/input-objects/icdcodesindividualclientnoteinput)· Diagnoses connected to the individual client attendance

[`join_time` ](#field-join-time)· [`String` ](/reference/2026-01-01/scalars/string)· The datetime (ISO 8601) that the attendee joined the appointment

[`leave_time` ](#field-leave-time)· [`String` ](/reference/2026-01-01/scalars/string)· The datetime (ISO 8601) that the attendee left the appointment

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user who created the individual client note

## Used By

[`createFormAnswerGroupInput.individual_client_notes`](/reference/2026-01-01/input-objects/createformanswergroupinput)

[`updateFormAnswerGroupInput.individual_client_notes`](/reference/2026-01-01/input-objects/updateformanswergroupinput)

## Definition

```
"""
Payload for an individual client note
"""
input IndividualClientNoteInput {
  """
  The content of the individual client note
  """
  content: String


  """
  The ID of the individual client note
  """
  id: ID


  """
  The client's attendance status. This gets applied to the AppointmentInclusion object
  """
  attended: Boolean


  """
  Diagnoses connected to the individual client attendance
  """
  icd_codes_individual_client_notes_attributes: [IcdCodesIndividualClientNoteInput]


  """
  The datetime (ISO 8601) that the attendee joined the appointment
  """
  join_time: String


  """
  The datetime (ISO 8601) that the attendee left the appointment
  """
  leave_time: String


  """
  The ID of the user who created the individual client note
  """
  user_id: ID
}
```
