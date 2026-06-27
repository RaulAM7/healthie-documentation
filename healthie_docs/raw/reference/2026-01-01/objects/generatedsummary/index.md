---
title: GeneratedSummary | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/generatedsummary/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/generatedsummary/index.md
---

A generated summary for an associated Healthie object

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The datetime the summary was generated

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the group

[`summary` ](#field-summary)· [`String` ](/reference/2026-01-01/scalars/string)· A summary (most often new-line separated bullet points) of the associated object

## Used By

[`FormAnswerGroup.current_summary`](/reference/2026-01-01/objects/formanswergroup)

[`User.current_summary`](/reference/2026-01-01/objects/user)

## Definition

```
"""
A generated summary for an associated Healthie object
"""
type GeneratedSummary {
  """
  The datetime the summary was generated
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the group
  """
  id: ID!


  """
  A summary (most often new-line separated bullet points) of the associated object
  """
  summary: String
}
```
