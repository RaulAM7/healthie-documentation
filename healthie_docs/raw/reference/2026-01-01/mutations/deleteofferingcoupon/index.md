---
title: deleteOfferingCoupon | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteofferingcoupon/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteofferingcoupon/index.md
---

Destroy an Offering Coupon

## Arguments

[`input` ](#argument-input)· [`deleteOfferingCouponInput` ](/reference/2026-01-01/input-objects/deleteofferingcouponinput)· Parameters for deleteOfferingCoupon

## Returns

[`deleteOfferingCouponPayload`](/reference/2026-01-01/objects/deleteofferingcouponpayload)

## Example

```
mutation deleteOfferingCoupon($input: deleteOfferingCouponInput) {
  deleteOfferingCoupon(input: $input) {
    messages
    offeringCoupon
  }
}
```
