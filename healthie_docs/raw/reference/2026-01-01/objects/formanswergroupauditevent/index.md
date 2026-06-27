---
title: FormAnswerGroupAuditEvent | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroupauditevent/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroupauditevent/index.md
---

Base class for types

## Fields

[`action` ](#field-action)· [`Action!` ](/reference/2026-01-01/enums/action)· required · Action type

[`committed_at` ](#field-committed-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the action was made

[`committed_by` ](#field-committed-by)· [`User!` ](/reference/2026-01-01/objects/user)· required · Who made the action

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required

[`description` ](#field-description)· [`String`](/reference/2026-01-01/scalars/string)

[`form_answer_group` ](#field-form-answer-group)· [`FormAnswerGroup!` ](/reference/2026-01-01/objects/formanswergroup)· required

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

[`related_object` ](#field-related-object)· [`RelatedObjectUnion`](/reference/2026-01-01/unions/relatedobjectunion)

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required

## Used By

[`FormAnswerGroup.form_answer_group_audit_events`](/reference/2026-01-01/objects/formanswergroup)

## Definition

```
"""
Base class for types
"""
type FormAnswerGroupAuditEvent {
  """
  Action type
  """
  action: Action!


  """
  When the action was made
  """
  committed_at: ISO8601DateTime!


  """
  Who made the action
  """
  committed_by: User!
  created_at: ISO8601DateTime!
  description: String
  form_answer_group: FormAnswerGroup!
  id: ID!
  related_object: RelatedObjectUnion
  updated_at: ISO8601DateTime!
}
```
