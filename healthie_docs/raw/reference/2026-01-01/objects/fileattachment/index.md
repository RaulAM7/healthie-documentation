---
title: FileAttachment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/fileattachment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/fileattachment/index.md
---

A file attachment representing an uploaded file

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the file attachment

[`url` ](#field-url)· [`String` ](/reference/2026-01-01/scalars/string)· The pre-signed expiring URL to access the file

## Used By

[`CreateCustomModuleFileAttachmentPayload.file_attachment`](/reference/2026-01-01/objects/createcustommodulefileattachmentpayload)

[`CustomModule.file_attachment`](/reference/2026-01-01/objects/custommodule)

[`DeleteCustomModuleFileAttachmentPayload.file_attachment`](/reference/2026-01-01/objects/deletecustommodulefileattachmentpayload)

[`FormAnswer.file_attachments`](/reference/2026-01-01/objects/formanswer)

[`createFormAnswerFileAttachmentPayload.file_attachment`](/reference/2026-01-01/objects/createformanswerfileattachmentpayload)

[`deleteFormAnswerFileAttachmentPayload.file_attachment`](/reference/2026-01-01/objects/deleteformanswerfileattachmentpayload)

## Definition

```
"""
A file attachment representing an uploaded file
"""
type FileAttachment {
  """
  The ID of the file attachment
  """
  id: ID!


  """
  The pre-signed expiring URL to access the file
  """
  url: String
}
```
