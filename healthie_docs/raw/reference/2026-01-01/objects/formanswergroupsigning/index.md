---
title: FormAnswerGroupSigning | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroupsigning/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroupsigning/index.md
---

An instance representing connection between a charting note(form\_answer\_group) and a user signing the note

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time the form was signed

[`form_answer_group_id` ](#field-form-answer-group-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the form that was signed

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the signing

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· A provider who signed the form

[`user_avatar_url` ](#field-user-avatar-url)· [`String` ](/reference/2026-01-01/scalars/string)· The avatar URL of the user who signed the form

[`user_full_legal_name` ](#field-user-full-legal-name)· [`String` ](/reference/2026-01-01/scalars/string)· The full legal name of the user who signed the form

[`user_qualifications` ](#field-user-qualifications)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifications of the user who signed the form

## Used By

[`FormAnswerGroup.form_answer_group_signings`](/reference/2026-01-01/objects/formanswergroup)

[`SignPayload.form_answer_group_signing`](/reference/2026-01-01/objects/signpayload)

[`createFormAnswerGroupSigningPayload.formAnswerGroupSigning`](/reference/2026-01-01/objects/createformanswergroupsigningpayload)

[`deleteFormAnswerGroupSigningPayload.formAnswerGroupSigning`](/reference/2026-01-01/objects/deleteformanswergroupsigningpayload)

## Definition

```
"""
An instance representing connection between a charting note(form_answer_group) and a user signing the note
"""
type FormAnswerGroupSigning {
  """
  The date and time the form was signed
  """
  created_at: ISO8601DateTime!


  """
  The id of the form that was signed
  """
  form_answer_group_id: String


  """
  The unique identifier of the signing
  """
  id: ID!


  """
  A provider who signed the form
  """
  user: User


  """
  The avatar URL of the user who signed the form
  """
  user_avatar_url: String


  """
  The full legal name of the user who signed the form
  """
  user_full_legal_name: String


  """
  The qualifications of the user who signed the form
  """
  user_qualifications: String
}
```
