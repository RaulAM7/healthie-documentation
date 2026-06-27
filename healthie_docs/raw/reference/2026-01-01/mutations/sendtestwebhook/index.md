---
title: sendTestWebhook | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/sendtestwebhook/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/sendtestwebhook/index.md
---

Sends a test webhook to the specified URL

## Arguments

[`input` ](#argument-input)· [`sendTestWebhookInput` ](/reference/2026-01-01/input-objects/sendtestwebhookinput)· Parameters for sendTestWebhook

## Returns

[`sendTestWebhookPayload`](/reference/2026-01-01/objects/sendtestwebhookpayload)

## Example

```
mutation sendTestWebhook($input: sendTestWebhookInput) {
  sendTestWebhook(input: $input) {
    messages
    sent
  }
}
```
