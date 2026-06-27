---
title: ClientSourceInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/clientsourceinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/clientsourceinput/index.md
---

Payload for a client source

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the client source

[`ref_source` ](#field-ref-source)· [`String` ](/reference/2026-01-01/scalars/string)· The source of the client

[`ref_source_other` ](#field-ref-source-other)· [`String` ](/reference/2026-01-01/scalars/string)· The other source of the client

[`ref_type` ](#field-ref-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of client source

## Used By

[`updateClientInput.client_source`](/reference/2026-01-01/input-objects/updateclientinput)

## Definition

```
"""
Payload for a client source
"""
input ClientSourceInput {
  """
  The ID of the client source
  """
  id: ID


  """
  The source of the client
  """
  ref_source: String


  """
  The other source of the client
  """
  ref_source_other: String


  """
  The type of client source
  """
  ref_type: String
}
```
