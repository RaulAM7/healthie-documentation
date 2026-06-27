---
title: WebhookEventInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/webhookeventinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/webhookeventinput/index.md
---

Payload for a webhook event

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the webhook event

[`event_type` ](#field-event-type)· [`WebhookEventType!` ](/reference/2026-01-01/enums/webhookeventtype)· required · The type of webhook event

## Used By

[`createWebhookInput.webhook_events`](/reference/2026-01-01/input-objects/createwebhookinput)

[`updateWebhookInput.webhook_events`](/reference/2026-01-01/input-objects/updatewebhookinput)

## Definition

```
"""
Payload for a webhook event
"""
input WebhookEventInput {
  """
  The ID of the webhook event
  """
  id: ID


  """
  The type of webhook event
  """
  event_type: WebhookEventType!
}
```
