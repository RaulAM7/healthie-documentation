---
title: updateSubscription | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesubscription/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesubscription/index.md
---

update Subscription

## Arguments

[`input` ](#argument-input)· [`updateSubscriptionInput` ](/reference/2026-01-01/input-objects/updatesubscriptioninput)· Parameters for updateSubscription

## Returns

[`updateSubscriptionPayload`](/reference/2026-01-01/objects/updatesubscriptionpayload)

## Example

```
mutation updateSubscription($input: updateSubscriptionInput) {
  updateSubscription(input: $input) {
    currentUser
    messages
    subscription
  }
}
```
