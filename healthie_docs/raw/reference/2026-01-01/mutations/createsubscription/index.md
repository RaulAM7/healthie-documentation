---
title: createSubscription | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsubscription/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsubscription/index.md
---

create Subscription

## Arguments

[`input` ](#argument-input)· [`createSubscriptionInput` ](/reference/2026-01-01/input-objects/createsubscriptioninput)· Parameters for createSubscription

## Returns

[`createSubscriptionPayload`](/reference/2026-01-01/objects/createsubscriptionpayload)

## Example

```
mutation createSubscription($input: createSubscriptionInput) {
  createSubscription(input: $input) {
    messages
    subscription
  }
}
```
