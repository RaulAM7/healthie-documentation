---
title: RequestedFormStatusType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedformstatustype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedformstatustype/index.md
---

The status of the requested form

## Fields

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· Used to return something after request if the job has been triggered

## Used By

[`createRequestedFormPayload.requestedFormCompletionStatus`](/reference/2026-01-01/objects/createrequestedformpayload)

## Definition

```
"""
The status of the requested form
"""
type RequestedFormStatusType {
  """
  Used to return something after request if the job has been triggered
  """
  status: String
}
```
