---
title: updateWebhook | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatewebhook/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatewebhook/index.md
---

Update Webhook

## Arguments

[`input` ](#argument-input)· [`updateWebhookInput` ](/reference/2026-01-01/input-objects/updatewebhookinput)· Parameters for updateWebhook

## Returns

[`updateWebhookPayload`](/reference/2026-01-01/objects/updatewebhookpayload)

## Example

```
mutation updateWebhook($input: updateWebhookInput) {
  updateWebhook(input: $input) {
    messages
    webhook
  }
}
```
