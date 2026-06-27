---
title: ValidateOfferingCoupon | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/validateofferingcoupon/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/validateofferingcoupon/index.md
---

Information based on if an offering coupon is valid

## Fields

[`fail_reason` ](#field-fail-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The reason why the promo code was not successfully applied

[`first_amount` ](#field-first-amount)· [`String` ](/reference/2026-01-01/scalars/string)· Discount amount for first payment

[`new_first_price` ](#field-new-first-price)· [`String` ](/reference/2026-01-01/scalars/string)· The size of the discount with the promo code applied to the first payment (in case offering has a different first payment amount)

[`new_price` ](#field-new-price)· [`String` ](/reference/2026-01-01/scalars/string)· The new price with a promo code applied

[`repeat_times` ](#field-repeat-times)· [`String` ](/reference/2026-01-01/scalars/string)· Indicates number of discount periods

[`still_ask_for_cc` ](#field-still-ask-for-cc)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicates necessary of displaying CC form

## Used By

[`Query.validateCoupon`](/reference/2026-01-01/queries/validatecoupon)

## Definition

```
"""
Information based on if an offering coupon is valid
"""
type ValidateOfferingCoupon {
  """
  The reason why the promo code was not successfully applied
  """
  fail_reason: String


  """
  Discount amount for first payment
  """
  first_amount: String


  """
  The size of the discount with the promo code applied to the first payment (in case offering has a different first payment amount)
  """
  new_first_price: String


  """
  The new price with a promo code applied
  """
  new_price: String


  """
  Indicates number of discount periods
  """
  repeat_times: String


  """
  Indicates necessary of displaying CC form
  """
  still_ask_for_cc: Boolean
}
```
