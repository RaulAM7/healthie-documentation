---
title: updateUserAppointmentPricing | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateuserappointmentpricing/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateuserappointmentpricing/index.md
---

Updates the appointment pricing for this user

## Arguments

[`input` ](#argument-input)· [`updateUserAppointmentPricingInput` ](/reference/2026-01-01/input-objects/updateuserappointmentpricinginput)· Parameters for updateUserAppointmentPricing

## Returns

[`updateUserAppointmentPricingPayload`](/reference/2026-01-01/objects/updateuserappointmentpricingpayload)

## Example

```
mutation updateUserAppointmentPricing(
  $input: updateUserAppointmentPricingInput
) {
  updateUserAppointmentPricing(input: $input) {
    advance_appointment_prices
    messages
  }
}
```
