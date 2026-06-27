---
title: CognitiveStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cognitivestatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cognitivestatus/index.md
---

CognitiveStatus object

## Fields

[`cognitive_status` ](#field-cognitive-status)· [`String` ](/reference/2026-01-01/scalars/string)· Cognitive status

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the status

[`start_date` ](#field-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Start date

[`user_id` ](#field-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · User id

## Used By

[`createCognitiveStatusPayload.cognitive_status`](/reference/2026-01-01/objects/createcognitivestatuspayload)

[`deleteCognitiveStatusPayload.cognitive_status`](/reference/2026-01-01/objects/deletecognitivestatuspayload)

[`updateCognitiveStatusPayload.cognitive_status`](/reference/2026-01-01/objects/updatecognitivestatuspayload)

## Definition

```
"""
CognitiveStatus object
"""
type CognitiveStatus {
  """
  Cognitive status
  """
  cognitive_status: String


  """
  The unique identifier of the status
  """
  id: ID!


  """
  Start date
  """
  start_date: ISO8601DateTime


  """
  User id
  """
  user_id: ID!
}
```
