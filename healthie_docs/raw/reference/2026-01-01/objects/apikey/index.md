---
title: ApiKey | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/apikey/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/apikey/index.md
---

A created API Key

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The datetime the API Key was created

[`displayable_key` ](#field-displayable-key)· [`String` ](/reference/2026-01-01/scalars/string)· Upon the initial creation of the key, this field displays the actual key to be used to authenticate.

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique identifier of the key

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· A user-chosen name for the API key.

## Used By

[`ApiKeyEdge.node`](/reference/2026-01-01/objects/apikeyedge)

[`ApiKeyPaginationConnection.nodes`](/reference/2026-01-01/objects/apikeypaginationconnection)

[`createApiKeyPayload.api_key_object`](/reference/2026-01-01/objects/createapikeypayload)

[`deleteApiKeyPayload.api_key`](/reference/2026-01-01/objects/deleteapikeypayload)

## Definition

```
"""
A created API Key
"""
type ApiKey {
  """
  The datetime the API Key was created
  """
  created_at: ISO8601DateTime!


  """
  Upon the initial creation of the key, this field displays the actual key to be used to authenticate.
  """
  displayable_key: String


  """
  Unique identifier of the key
  """
  id: ID!


  """
  A user-chosen name for the API key.
  """
  name: String
}
```
