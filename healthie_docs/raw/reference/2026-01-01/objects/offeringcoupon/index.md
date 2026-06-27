---
title: OfferingCoupon | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringcoupon/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringcoupon/index.md
---

Offering Coupon

## Fields

[`amount_off` ](#field-amount-off)· [`String` ](/reference/2026-01-01/scalars/string)· The amount off due to this offering coupon

[`amount_off_string` ](#field-amount-off-string)· [`String` ](/reference/2026-01-01/scalars/string)· The amount off due to this offering coupon

[`applies_to_string` ](#field-applies-to-string)· [`String` ](/reference/2026-01-01/scalars/string)· The time this offering coupon is applied

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The code of this offering coupon

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time at which this offering coupon was created

[`deleted_at` ](#field-deleted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time at which this offering coupon was deleted

[`expires_at` ](#field-expires-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date the promo code expires at

[`flat_amount_off` ](#field-flat-amount-off)· [`String` ](/reference/2026-01-01/scalars/string)· The flat amount off due to this offering coupon

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the coupon

[`is_expired` ](#field-is-expired)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The coupon is expired or valid, returns true if coupon is expired

[`is_valid` ](#field-is-valid)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The coupon is expired or valid, returns true if the coupon is valid

[`number_of_times_used` ](#field-number-of-times-used)· [`Int` ](/reference/2026-01-01/scalars/int)· The amount of times the offering coupon has been used

[`offering_coupon_owner` ](#field-offering-coupon-owner)· [`User` ](/reference/2026-01-01/objects/user)· The owner of this Offering Coupon

[`package_connection_names` ](#field-package-connection-names)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Names of offerings this coupon is connected to

[`promo_type` ](#field-promo-type)· [`String` ](/reference/2026-01-01/scalars/string)· The promo type of this offering coupon

[`repeat_times` ](#field-repeat-times)· [`Int` ](/reference/2026-01-01/scalars/int)· The repeat times of this offering coupon

[`to_one_line` ](#field-to-one-line)· [`String` ](/reference/2026-01-01/scalars/string)· concatenated string of amount off string and applies to string

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time at which this offering coupon was last updated at

[`usage_limit` ](#field-usage-limit)· [`Int` ](/reference/2026-01-01/scalars/int)· The amount of times the offering coupon can be used

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The user id who created this offering coupon

## Used By

[`BillingItem.offering_coupon`](/reference/2026-01-01/objects/billingitem)

[`OfferingCouponEdge.node`](/reference/2026-01-01/objects/offeringcouponedge)

[`OfferingCouponPaginationConnection.nodes`](/reference/2026-01-01/objects/offeringcouponpaginationconnection)

[`User.offering_coupons`](/reference/2026-01-01/objects/user)

[`createOfferingCouponPayload.offeringCoupon`](/reference/2026-01-01/objects/createofferingcouponpayload)

[`deleteOfferingCouponPayload.offeringCoupon`](/reference/2026-01-01/objects/deleteofferingcouponpayload)

## Definition

```
"""
Offering Coupon
"""
type OfferingCoupon {
  """
  The amount off due to this offering coupon
  """
  amount_off: String


  """
  The amount off due to this offering coupon
  """
  amount_off_string: String


  """
  The time this offering coupon is applied
  """
  applies_to_string: String


  """
  The code of this offering coupon
  """
  code: String


  """
  The time at which this offering coupon was created
  """
  created_at: ISO8601DateTime!


  """
  The time at which this offering coupon was deleted
  """
  deleted_at: ISO8601DateTime


  """
  The date the promo code expires at
  """
  expires_at: ISO8601DateTime


  """
  The flat amount off due to this offering coupon
  """
  flat_amount_off: String


  """
  The unique identifier of the coupon
  """
  id: ID!


  """
  The coupon is expired or valid, returns true if coupon is expired
  """
  is_expired: Boolean!


  """
  The coupon is expired or valid, returns true if the coupon is valid
  """
  is_valid: Boolean!


  """
  The amount of times the offering coupon has been used
  """
  number_of_times_used: Int


  """
  The owner of this Offering Coupon
  """
  offering_coupon_owner: User


  """
  Names of offerings this coupon is connected to
  """
  package_connection_names: [String!]


  """
  The promo type of this offering coupon
  """
  promo_type: String


  """
  The repeat times of this offering coupon
  """
  repeat_times: Int


  """
  concatenated string of amount off string and applies to string
  """
  to_one_line: String


  """
  The time at which this offering coupon was last updated at
  """
  updated_at: ISO8601DateTime!


  """
  The amount of times the offering coupon can be used
  """
  usage_limit: Int


  """
  The user id who created this offering coupon
  """
  user_id: String
}
```
