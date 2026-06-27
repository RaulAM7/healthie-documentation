---
title: HttpHeader | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/httpheader/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/httpheader/index.md
---

An HTTP header (case-insensitive name; duplicates allowed).

## Fields

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required

[`value` ](#field-value)· [`String!` ](/reference/2026-01-01/scalars/string)· required

## Used By

[`CreateCustomModuleFileAttachmentUploadUrlPayload.headers`](/reference/2026-01-01/objects/createcustommodulefileattachmentuploadurlpayload)

[`createFormAnswerFileAttachmentUploadUrlPayload.headers`](/reference/2026-01-01/objects/createformanswerfileattachmentuploadurlpayload)

## Definition

```
"""
An HTTP header (case-insensitive name; duplicates allowed).
"""
type HttpHeader {
  name: String!
  value: String!
}
```
