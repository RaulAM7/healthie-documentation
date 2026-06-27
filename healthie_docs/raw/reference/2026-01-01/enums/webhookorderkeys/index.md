---
title: WebhookOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/webhookorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/webhookorderkeys/index.md
---

Webhook sorting enum

## Used By

[`Query.webhooks`](/reference/2026-01-01/queries/webhooks)

## Definition

```
"""
Webhook sorting enum
"""
enum WebhookOrderKeys {
  CREATED_AT_ASC
  CREATED_AT_DESC
  EVENT_TYPE_ASC
  EVENT_TYPE_DESC
  URL_ASC
  URL_DESC
}
```
