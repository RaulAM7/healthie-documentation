---
title: ChartingNoteAddendumType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chartingnoteaddendumtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chartingnoteaddendumtype/index.md
---

A charting note addendum

## Fields

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· The content of the addendum

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the addendum was created

[`form_answer_group` ](#field-form-answer-group)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· The form answer group the addendum belongs to

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the addendum

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· A provider who created the addendum

## Used By

[`FormAnswerGroup.charting_note_addendums`](/reference/2026-01-01/objects/formanswergroup)

[`createAddendumPayload.addendum`](/reference/2026-01-01/objects/createaddendumpayload)

[`updateAddendumPayload.addendum`](/reference/2026-01-01/objects/updateaddendumpayload)

[`Query.chartingNoteAddendum`](/reference/2026-01-01/queries/chartingnoteaddendum)

## Definition

```
"""
A charting note addendum
"""
type ChartingNoteAddendumType {
  """
  The content of the addendum
  """
  content: String


  """
  The date the addendum was created
  """
  created_at: ISO8601DateTime!


  """
  The form answer group the addendum belongs to
  """
  form_answer_group: FormAnswerGroup


  """
  The unique identifier of the addendum
  """
  id: ID!


  """
  A provider who created the addendum
  """
  user: User
}
```
