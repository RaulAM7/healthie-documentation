---
title: CallReference | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/callreference/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/callreference/index.md
---

Call reference information associated with a policy

## Fields

[`date_recorded` ](#field-date-recorded)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date call was made

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the reference call

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Notes taken for this reference call

[`reference_number` ](#field-reference-number)· [`String` ](/reference/2026-01-01/scalars/string)· call reference number provided by insurance company

[`time_recorded` ](#field-time-recorded)· [`String` ](/reference/2026-01-01/scalars/string)· Time call was made

[`user_id` ](#field-user-id)· [`Int` ](/reference/2026-01-01/scalars/int)· The ID of the patient who the call reference is for

## Used By

[`Policy.call_reference`](/reference/2026-01-01/objects/policy)

[`User.call_references`](/reference/2026-01-01/objects/user)

## Definition

```
"""
Call reference information associated with a policy
"""
type CallReference {
  """
  Date call was made
  """
  date_recorded: ISO8601DateTime


  """
  The unique identifier of the reference call
  """
  id: ID!


  """
  Notes taken for this reference call
  """
  notes: String


  """
  call reference number provided by insurance company
  """
  reference_number: String


  """
  Time call was made
  """
  time_recorded: String


  """
  The ID of the patient who the call reference is for
  """
  user_id: Int
}
```
