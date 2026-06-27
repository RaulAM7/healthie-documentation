---
title: Webhook | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/webhook/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/webhook/index.md
---

A configured webhook

## Fields

[`event_type` ](#field-event-type)· [`WebhookEventType` ](/reference/2026-01-01/enums/webhookeventtype)· The type of webhook

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the webhook

[`is_enabled` ](#field-is-enabled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the webhook is enabled or not

[`should_retry` ](#field-should-retry)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the webhook should retry on failure

[`signature_secret` ](#field-signature-secret)· [`String` ](/reference/2026-01-01/scalars/string)· The secret key used to sign the webhook

[`url` ](#field-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL that the webhook will be sent to

[`warned_at` ](#field-warned-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date and time that the customer was wamed about the webhook failing

[`webhook_events` ](#field-webhook-events)· [`[WebhookEvent!]` ](/reference/2026-01-01/objects/webhookevent)· The events that the webhook is subscribed to

## Used By

[`WebhookEdge.node`](/reference/2026-01-01/objects/webhookedge)

[`WebhookEvent.webhook`](/reference/2026-01-01/objects/webhookevent)

[`WebhookPaginationConnection.nodes`](/reference/2026-01-01/objects/webhookpaginationconnection)

[`createWebhookPayload.webhook`](/reference/2026-01-01/objects/createwebhookpayload)

[`deleteWebhookPayload.webhook`](/reference/2026-01-01/objects/deletewebhookpayload)

[`expireWebhookSignaturePayload.webhook`](/reference/2026-01-01/objects/expirewebhooksignaturepayload)

[`updateWebhookPayload.webhook`](/reference/2026-01-01/objects/updatewebhookpayload)

## Definition

```
"""
A configured webhook
"""
type Webhook {
  """
  The type of webhook
  """
  event_type: WebhookEventType


  """
  The unique identifier of the webhook
  """
  id: ID!


  """
  Whether the webhook is enabled or not
  """
  is_enabled: Boolean!


  """
  Whether the webhook should retry on failure
  """
  should_retry: Boolean!


  """
  The secret key used to sign the webhook
  """
  signature_secret: String


  """
  The URL that the webhook will be sent to
  """
  url: String


  """
  The date and time that the customer was wamed about the webhook failing
  """
  warned_at: ISO8601DateTime


  """
  The events that the webhook is subscribed to
  """
  webhook_events: [WebhookEvent!]
}
```
