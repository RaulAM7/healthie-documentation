---
title: CallReferenceInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/callreferenceinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/callreferenceinput/index.md
---

Payload for a CallReference

## Fields

[`date_recorded` ](#field-date-recorded)· [`String` ](/reference/2026-01-01/scalars/string)· The date the call was recorded

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the CallReference

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Notes about the call

[`reference_number` ](#field-reference-number)· [`String` ](/reference/2026-01-01/scalars/string)· The reference number for the call

[`time_recorded` ](#field-time-recorded)· [`String` ](/reference/2026-01-01/scalars/string)· The time the call was recorded

## Used By

[`updatePolicyMutationInput.call_reference`](/reference/2026-01-01/input-objects/updatepolicymutationinput)

## Definition

```
"""
Payload for a CallReference
"""
input CallReferenceInput {
  """
  The date the call was recorded
  """
  date_recorded: String


  """
  The ID of the CallReference
  """
  id: ID


  """
  Notes about the call
  """
  notes: String


  """
  The reference number for the call
  """
  reference_number: String


  """
  The time the call was recorded
  """
  time_recorded: String
}
```
