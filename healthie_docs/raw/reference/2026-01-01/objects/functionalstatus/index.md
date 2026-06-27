---
title: FunctionalStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/functionalstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/functionalstatus/index.md
---

FunctionalStatus object

## Fields

[`functional_condition` ](#field-functional-condition)· [`String` ](/reference/2026-01-01/scalars/string)· Functional condition

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the functional status

[`start_date` ](#field-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The start date of the functional status

[`user_id` ](#field-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the user who created the functional status

## Used By

[`createFunctionalStatusPayload.functional_status`](/reference/2026-01-01/objects/createfunctionalstatuspayload)

[`deleteFunctionalStatusPayload.functional_status`](/reference/2026-01-01/objects/deletefunctionalstatuspayload)

[`updateFunctionalStatusPayload.functional_status`](/reference/2026-01-01/objects/updatefunctionalstatuspayload)

## Definition

```
"""
FunctionalStatus object
"""
type FunctionalStatus {
  """
  Functional condition
  """
  functional_condition: String


  """
  The unique identifier of the functional status
  """
  id: ID!


  """
  The start date of the functional status
  """
  start_date: ISO8601DateTime


  """
  The ID of the user who created the functional status
  """
  user_id: ID!
}
```
