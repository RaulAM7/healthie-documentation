---
title: completeCheckout | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/completecheckout/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/completecheckout/index.md
---

Complete the checkout for booking or buying

## Arguments

[`input` ](#argument-input)· [`completeCheckoutInput` ](/reference/2026-01-01/input-objects/completecheckoutinput)· Parameters for completeCheckout

## Returns

[`completeCheckoutPayload`](/reference/2026-01-01/objects/completecheckoutpayload)

## Example

```
mutation completeCheckout($input: completeCheckoutInput) {
  completeCheckout(input: $input) {
    appointment
    appointments
    billingItem
    formAnswerGroupSaved
    messages
    patientEmail
    reassignClientProvider
    userPackageSelection
    widgetCompletedSubheaderHtml
  }
}
```
