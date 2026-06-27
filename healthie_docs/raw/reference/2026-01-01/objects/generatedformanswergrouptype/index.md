---
title: GeneratedFormAnswerGroupType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/generatedformanswergrouptype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/generatedformanswergrouptype/index.md
---

AI-Generated Form Answer Group

## Fields

[`appointment` ](#field-appointment)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· The appointment the note is connected to

[`appointment_id` ](#field-appointment-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment the note is connected to

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date of the item' creation

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm!` ](/reference/2026-01-01/objects/custommoduleform)· required · The form AI Scribe used to structure the proposed chart note

[`feedback` ](#field-feedback)· [`String` ](/reference/2026-01-01/scalars/string)· Feedback for the generated form answer group

[`form_answer_group` ](#field-form-answer-group)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· The chart note created from this proposed note, if it has been converted

[`generated_form_answers` ](#field-generated-form-answers)· [`[GeneratedFormAnswerType!]!` ](/reference/2026-01-01/objects/generatedformanswertype)· required · The visible answers for the filled form

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

[`kind` ](#field-kind)· [`String` ](/reference/2026-01-01/scalars/string)· The AI Scribe kind (ambient or video\_call)

[`rejection_reason` ](#field-rejection-reason)· [`[String!]` ](/reference/2026-01-01/scalars/string)· The reasons the provider selected when rejecting this proposed note. Null if the note has not been rejected, empty array if rejected without selecting specific reasons.

## Used By

[`Appointment.generated_form_answer_group`](/reference/2026-01-01/objects/appointment)

[`ChartingItemType.generated_form_answer_group`](/reference/2026-01-01/objects/chartingitemtype)

[`convertGeneratedFormAnswerGroupPayload.generated_form_answer_group`](/reference/2026-01-01/objects/convertgeneratedformanswergrouppayload)

[`rejectGeneratedFormAnswerGroupPayload.generated_form_answer_group`](/reference/2026-01-01/objects/rejectgeneratedformanswergrouppayload)

[`updateGeneratedFormAnswerGroupFeedbackPayload.generated_form_answer_group`](/reference/2026-01-01/objects/updategeneratedformanswergroupfeedbackpayload)

## Definition

```
"""
AI-Generated Form Answer Group
"""
type GeneratedFormAnswerGroupType {
  """
  The appointment the note is connected to
  """
  appointment: Appointment


  """
  The ID of the appointment the note is connected to
  """
  appointment_id: ID


  """
  The date of the item' creation
  """
  created_at: ISO8601DateTime!


  """
  The form AI Scribe used to structure the proposed chart note
  """
  custom_module_form: CustomModuleForm!


  """
  Feedback for the generated form answer group
  """
  feedback: String


  """
  The chart note created from this proposed note, if it has been converted
  """
  form_answer_group: FormAnswerGroup


  """
  The visible answers for the filled form
  """
  generated_form_answers: [GeneratedFormAnswerType!]!
  id: ID!


  """
  The AI Scribe kind (ambient or video_call)
  """
  kind: String


  """
  The reasons the provider selected when rejecting this proposed note. Null if the note has not been rejected, empty array if rejected without selecting specific reasons.
  """
  rejection_reason: [String!]
}
```
