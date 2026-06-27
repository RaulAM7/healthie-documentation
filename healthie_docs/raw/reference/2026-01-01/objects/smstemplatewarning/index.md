---
title: SmsTemplateWarning | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/smstemplatewarning/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/smstemplatewarning/index.md
---

Warning about SMS template length and multi-message costs

## Fields

[`estimated_length` ](#field-estimated-length)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Estimated character length after template variable expansion

[`estimated_message_count` ](#field-estimated-message-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Estimated number of SMS messages that will be sent

[`message` ](#field-message)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Warning message to display to the user

## Used By

[`createAppointmentTypePayload.sms_template_warning`](/reference/2026-01-01/objects/createappointmenttypepayload)

[`updateAppointmentTypePayload.sms_template_warning`](/reference/2026-01-01/objects/updateappointmenttypepayload)

## Definition

```
"""
Warning about SMS template length and multi-message costs
"""
type SmsTemplateWarning {
  """
  Estimated character length after template variable expansion
  """
  estimated_length: Int!


  """
  Estimated number of SMS messages that will be sent
  """
  estimated_message_count: Int!


  """
  Warning message to display to the user
  """
  message: String!
}
```
