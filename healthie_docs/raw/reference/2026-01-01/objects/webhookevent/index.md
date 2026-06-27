---
title: WebhookEvent | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/webhookevent/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/webhookevent/index.md
---

The events that the webhook is subscribed to

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time that the webhook was created

[`event_type` ](#field-event-type)· [`WebhookEventType!` ](/reference/2026-01-01/enums/webhookeventtype)· required · The type of webhook

[`first_failed_at` ](#field-first-failed-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date and time that the webhook first failed

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the webhook

[`last_failed_at` ](#field-last-failed-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date and time that the webhook last failed

[`retry_count` ](#field-retry-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · The number of times the webhook has been retried

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time that the webhook was last updated

[`webhook` ](#field-webhook)· [`Webhook!` ](/reference/2026-01-01/objects/webhook)· required · The webhook that the event is associated with

## Used By

[`Webhook.webhook_events`](/reference/2026-01-01/objects/webhook)

## Definition

```
"""
The events that the webhook is subscribed to
"""
type WebhookEvent {
  """
  The date and time that the webhook was created
  """
  created_at: ISO8601DateTime!


  """
  The type of webhook
  """
  event_type: WebhookEventType!


  """
  The date and time that the webhook first failed
  """
  first_failed_at: ISO8601DateTime


  """
  The unique identifier of the webhook
  """
  id: ID!


  """
  The date and time that the webhook last failed
  """
  last_failed_at: ISO8601DateTime


  """
  The number of times the webhook has been retried
  """
  retry_count: Int!


  """
  The date and time that the webhook was last updated
  """
  updated_at: ISO8601DateTime!


  """
  The webhook that the event is associated with
  """
  webhook: Webhook!
}
```
