---
title: FormHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formhistory/index.md
---

A form history object

## Fields

[`action` ](#field-action)· [`FormHistoryAction` ](/reference/2026-01-01/enums/formhistoryaction)· Action of the form history object

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date/Time created

[`creator` ](#field-creator)· [`User` ](/reference/2026-01-01/objects/user)· The User who created form history object or dietitian of the patient

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the form history object

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· The patient who owns the form history object

[`title` ](#field-title)· [`String` ](/reference/2026-01-01/scalars/string)· The title describing form history creation

## Used By

[`FormHistoryEdge.node`](/reference/2026-01-01/objects/formhistoryedge)

[`FormHistoryPaginationConnection.nodes`](/reference/2026-01-01/objects/formhistorypaginationconnection)

## Definition

```
"""
A form history object
"""
type FormHistory {
  """
  Action of the form history object
  """
  action: FormHistoryAction


  """
  Date/Time created
  """
  created_at: ISO8601DateTime


  """
  The User who created form history object or dietitian of the patient
  """
  creator: User


  """
  The unique identifier of the form history object
  """
  id: ID!


  """
  The patient who owns the form history object
  """
  patient: User


  """
  The title describing form history creation
  """
  title: String
}
```
