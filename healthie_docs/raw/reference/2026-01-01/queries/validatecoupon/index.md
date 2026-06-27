---
title: validateCoupon | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/validatecoupon/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/validatecoupon/index.md
---

Check if a coupon is valid, and return the new price (considered public)

## Arguments

[`coupon_code` ](#argument-coupon-code)· [`String`](/reference/2026-01-01/scalars/string)

[`offering_id` ](#argument-offering-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`requested_payment_id` ](#argument-requested-payment-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`ValidateOfferingCoupon`](/reference/2026-01-01/objects/validateofferingcoupon)

## Example

```
query validateCoupon(
  $coupon_code: String
  $offering_id: ID
  $provider_id: ID
  $requested_payment_id: ID
) {
  validateCoupon(
    coupon_code: $coupon_code
    offering_id: $offering_id
    provider_id: $provider_id
    requested_payment_id: $requested_payment_id
  ) {
    fail_reason
    first_amount
    new_first_price
    new_price
    repeat_times
    still_ask_for_cc
  }
}
```
