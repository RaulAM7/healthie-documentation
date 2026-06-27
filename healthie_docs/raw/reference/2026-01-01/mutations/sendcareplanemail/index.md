---
title: sendCarePlanEmail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/sendcareplanemail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/sendcareplanemail/index.md
---

Trigger care plan email for given client

## Arguments

[`input` ](#argument-input)· [`sendCarePlanEmailInput` ](/reference/2026-01-01/input-objects/sendcareplanemailinput)· Parameters for sendCarePlanEmail

## Returns

[`sendCarePlanEmailPayload`](/reference/2026-01-01/objects/sendcareplanemailpayload)

## Example

```
mutation sendCarePlanEmail($input: sendCarePlanEmailInput) {
  sendCarePlanEmail(input: $input) {
    carePlan
    messages
  }
}
```
