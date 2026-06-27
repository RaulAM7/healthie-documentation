---
title: SmokingStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/smokingstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/smokingstatus/index.md
---

Smoking Status object

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the status

[`smoking_status_code` ](#field-smoking-status-code)· [`String` ](/reference/2026-01-01/scalars/string)· The smoking status code

[`status_end_datetime` ](#field-status-end-datetime)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The end date of the status

[`status_start_datetime` ](#field-status-start-datetime)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The start date of the status

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the user the status belongs to

## Used By

[`createSmokingStatusPayload.smokingStatus`](/reference/2026-01-01/objects/createsmokingstatuspayload)

[`deleteSmokingStatusPayload.smokingStatus`](/reference/2026-01-01/objects/deletesmokingstatuspayload)

[`updateSmokingStatusPayload.smokingStatus`](/reference/2026-01-01/objects/updatesmokingstatuspayload)

## Definition

```
"""
Smoking Status object
"""
type SmokingStatus {
  """
  The unique identifier of the status
  """
  id: ID!


  """
  The smoking status code
  """
  smoking_status_code: String


  """
  The end date of the status
  """
  status_end_datetime: ISO8601DateTime


  """
  The start date of the status
  """
  status_start_datetime: ISO8601DateTime


  """
  The id of the user the status belongs to
  """
  user_id: ID
}
```
