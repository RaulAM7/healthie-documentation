---
title: createOfferingCoupon | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createofferingcoupon/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createofferingcoupon/index.md
---

Create an Offering Coupon

## Arguments

[`input` ](#argument-input)· [`createOfferingCouponInput` ](/reference/2026-01-01/input-objects/createofferingcouponinput)· Parameters for createOfferingCoupon

## Returns

[`createOfferingCouponPayload`](/reference/2026-01-01/objects/createofferingcouponpayload)

## Example

```
mutation createOfferingCoupon($input: createOfferingCouponInput) {
  createOfferingCoupon(input: $input) {
    messages
    offeringCoupon
  }
}
```
