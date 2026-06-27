---
title: SentWebhook | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentwebhook/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentwebhook/index.md
---

The record of a sent webhook

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The datetime that the webhook was sent

[`event_type` ](#field-event-type)· [`WebhookEventType` ](/reference/2026-01-01/enums/webhookeventtype)· The type of webhook

[`http_response_status` ](#field-http-response-status)· [`String` ](/reference/2026-01-01/scalars/string)· Whether the webhook is enabled or not

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the webhook

[`resource_id` ](#field-resource-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the resource the sent webhook related to

[`resource_id_type` ](#field-resource-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of resource the sent webhook related to

[`url` ](#field-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL that the webhook was sent to

[`webhook_id` ](#field-webhook-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The configured webhook thst was sent

## Used By

[`SentWebhookEdge.node`](/reference/2026-01-01/objects/sentwebhookedge)

[`SentWebhookPaginationConnection.nodes`](/reference/2026-01-01/objects/sentwebhookpaginationconnection)

## Definition

```
"""
The record of a sent webhook
"""
type SentWebhook {
  """
  The datetime that the webhook was sent
  """
  created_at: ISO8601DateTime!


  """
  The type of webhook
  """
  event_type: WebhookEventType


  """
  Whether the webhook is enabled or not
  """
  http_response_status: String


  """
  The unique identifier of the webhook
  """
  id: ID!


  """
  The id of the resource the sent webhook related to
  """
  resource_id: ID


  """
  The type of resource the sent webhook related to
  """
  resource_id_type: String


  """
  The URL that the webhook was sent to
  """
  url: String


  """
  The configured webhook thst was sent
  """
  webhook_id: ID
}
```
