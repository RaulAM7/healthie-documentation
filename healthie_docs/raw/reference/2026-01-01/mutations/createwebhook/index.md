---
title: createWebhook | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createwebhook/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createwebhook/index.md
---

Create Webhook

## Arguments

[`input` ](#argument-input)· [`createWebhookInput` ](/reference/2026-01-01/input-objects/createwebhookinput)· Parameters for createWebhook

## Returns

[`createWebhookPayload`](/reference/2026-01-01/objects/createwebhookpayload)

## Example

```
mutation createWebhook($input: createWebhookInput) {
  createWebhook(input: $input) {
    messages
    webhook
  }
}
```
