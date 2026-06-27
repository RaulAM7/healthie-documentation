---
title: DirectMessageAttachment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/directmessageattachment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/directmessageattachment/index.md
---

Information on the direct message attachment

## Fields

[`attachment_name` ](#field-attachment-name)· [`String` ](/reference/2026-01-01/scalars/string)· The file name of the attachment

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique ID of the direct message attachment

## Used By

[`ReceivedDirectMessage.direct_message_attachments`](/reference/2026-01-01/objects/receiveddirectmessage)

## Definition

```
"""
Information on the direct message attachment
"""
type DirectMessageAttachment {
  """
  The file name of the attachment
  """
  attachment_name: String


  """
  The unique ID of the direct message attachment
  """
  id: ID
}
```
