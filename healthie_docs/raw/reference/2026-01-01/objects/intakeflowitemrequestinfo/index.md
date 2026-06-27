---
title: IntakeFlowItemRequestInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/intakeflowitemrequestinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/intakeflowitemrequestinfo/index.md
---

The intake flow item request details

## Fields

[`complete_date` ](#field-complete-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Completion date of the form

[`completed_by` ](#field-completed-by)· [`User` ](/reference/2026-01-01/objects/user)· User who completed the form

[`details` ](#field-details)· [`String` ](/reference/2026-01-01/scalars/string)· Info how client received the form

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· Requested / Auto-Requested

[`request_date` ](#field-request-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Request date of the form

[`requested_by` ](#field-requested-by)· [`User` ](/reference/2026-01-01/objects/user)· User who requested the form

## Used By

[`IntakeFlowItem.request_info`](/reference/2026-01-01/objects/intakeflowitem)

## Definition

```
"""
The intake flow item request details
"""
type IntakeFlowItemRequestInfo {
  """
  Completion date of the form
  """
  complete_date: ISO8601DateTime


  """
  User who completed the form
  """
  completed_by: User


  """
  Info how client received the form
  """
  details: String


  """
  Requested / Auto-Requested
  """
  label: String


  """
  Request date of the form
  """
  request_date: ISO8601DateTime


  """
  User who requested the form
  """
  requested_by: User
}
```
