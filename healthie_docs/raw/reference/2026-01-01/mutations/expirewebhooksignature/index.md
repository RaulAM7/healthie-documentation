---
title: expireWebhookSignature | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/expirewebhooksignature/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/expirewebhooksignature/index.md
---

Expires the webhook signature

## Arguments

[`input` ](#argument-input)· [`expireWebhookSignatureInput` ](/reference/2026-01-01/input-objects/expirewebhooksignatureinput)· Parameters for expireWebhookSignature

## Returns

[`expireWebhookSignaturePayload`](/reference/2026-01-01/objects/expirewebhooksignaturepayload)

## Example

```
mutation expireWebhookSignature($input: expireWebhookSignatureInput) {
  expireWebhookSignature(input: $input) {
    messages
    webhook
  }
}
```
