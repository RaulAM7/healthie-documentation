---
title: UserPackageSelection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/userpackageselection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/userpackageselection/index.md
---

A user package selection

## Fields

[`billing_item` ](#field-billing-item)· [`BillingItem` ](/reference/2026-01-01/objects/billingitem)· The related billing item

[`billing_item_id` ](#field-billing-item-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the related billing item

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time when the user package selection was created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the user package selection

[`initial_price_with_offering_coupon` ](#field-initial-price-with-offering-coupon)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of the first payment for a package, including promo discounts

[`offering` ](#field-offering)· [`Offering` ](/reference/2026-01-01/objects/offering)· The related offering

[`offering_coupon_id` ](#field-offering-coupon-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the related offering coupon

[`recurring_payment` ](#field-recurring-payment)· [`RecurringPayment` ](/reference/2026-01-01/objects/recurringpayment)· The related recurring payment

[`requested_payment` ](#field-requested-payment)· [`RequestedPayment` ](/reference/2026-01-01/objects/requestedpayment)· The related requested payment

[`requested_payment_id` ](#field-requested-payment-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the related requested payment

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The related user

## Used By

[`BillingItem.user_package_selection`](/reference/2026-01-01/objects/billingitem)

[`RequestedPayment.user_package_selection`](/reference/2026-01-01/objects/requestedpayment)

[`UserPackageSelectionEdge.node`](/reference/2026-01-01/objects/userpackageselectionedge)

[`UserPackageSelectionPaginationConnection.nodes`](/reference/2026-01-01/objects/userpackageselectionpaginationconnection)

[`completeCheckoutPayload.userPackageSelection`](/reference/2026-01-01/objects/completecheckoutpayload)

## Definition

```
"""
A user package selection
"""
type UserPackageSelection {
  """
  The related billing item
  """
  billing_item: BillingItem


  """
  The id of the related billing item
  """
  billing_item_id: ID


  """
  The time when the user package selection was created
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the user package selection
  """
  id: ID!


  """
  The amount of the first payment for a package, including promo discounts
  """
  initial_price_with_offering_coupon: String


  """
  The related offering
  """
  offering: Offering


  """
  The id of the related offering coupon
  """
  offering_coupon_id: ID


  """
  The related recurring payment
  """
  recurring_payment: RecurringPayment


  """
  The related requested payment
  """
  requested_payment: RequestedPayment


  """
  The id of the related requested payment
  """
  requested_payment_id: ID


  """
  The related user
  """
  user: User
}
```
