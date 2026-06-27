---
title: deleteWebhook | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletewebhook/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletewebhook/index.md
---

Destroy Webhook

## Arguments

[`input` ](#argument-input)· [`deleteWebhookInput` ](/reference/2026-01-01/input-objects/deletewebhookinput)· Parameters for deleteWebhook

## Returns

[`deleteWebhookPayload`](/reference/2026-01-01/objects/deletewebhookpayload)

## Example

```
mutation deleteWebhook($input: deleteWebhookInput) {
  deleteWebhook(input: $input) {
    messages
    webhook
  }
}
```
