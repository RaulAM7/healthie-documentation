---
title: RecurringPayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringpayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringpayment/index.md
---

Recurring Payment

## Fields

[`amount_paid` ](#field-amount-paid)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of recurring payment

[`amount_to_pay` ](#field-amount-to-pay)· [`String` ](/reference/2026-01-01/scalars/string)· The amount to be paid for the next payment

[`appointment_id` ](#field-appointment-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment associated with this recurring payment

[`billing_frequency` ](#field-billing-frequency)· [`String` ](/reference/2026-01-01/scalars/string)· The frequency the payment should be made

[`billing_items_count` ](#field-billing-items-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of billing items

[`canceled_at` ](#field-canceled-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date on which the recurring payment is canceled

[`canceled_by` ](#field-canceled-by)· [`User` ](/reference/2026-01-01/objects/user)· The provider who canceled the recurring payment

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date on which the recurring payment is created

[`has_next_payment_date` ](#field-has-next-payment-date)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Includes the next payment date, returns true if next payment date is set and payments remaining is greater than zero

[`has_scheduled_billing_item` ](#field-has-scheduled-billing-item)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not this recurring payment has scheduled billing item

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the recurring payment

[`is_canceled` ](#field-is-canceled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If the recurring payment has been canceled

[`is_paused` ](#field-is-paused)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not the recurring payments has been paused

[`last_billing_item` ](#field-last-billing-item)· [`BillingItem` ](/reference/2026-01-01/objects/billingitem)· The last billing item for this recurring payment

[`next_payment_date` ](#field-next-payment-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date of the next payment

[`next_restart_payment_date` ](#field-next-restart-payment-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The next payment date if the recurring payment is restarted

[`offering_coupon_id` ](#field-offering-coupon-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the coupon

[`offering_id` ](#field-offering-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The offering ID

[`offering_name` ](#field-offering-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the offering associated with recurring payment

[`original_price` ](#field-original-price)· [`String` ](/reference/2026-01-01/scalars/string)· The original price

[`paused_at` ](#field-paused-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date on which the recurring payment is paused

[`paused_by` ](#field-paused-by)· [`User` ](/reference/2026-01-01/objects/user)· The provider who paused the recurring payment

[`payments_remaining` ](#field-payments-remaining)· [`String` ](/reference/2026-01-01/scalars/string)· Count remaining payments or returns Until Canceled

[`recipient_id` ](#field-recipient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the receiver

[`repeat_tiems` ](#field-repeat-tiems)· [`String` ](/reference/2026-01-01/scalars/string)· The number of times the payment should repeat

deprecated

Use \`repeat\_times\` instead

[`repeat_times` ](#field-repeat-times)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of times the payment should repeat

[`sender_id` ](#field-sender-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID oft the sender

[`start_at` ](#field-start-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date payments should begin

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The updated at date

## Used By

[`BillingItem.recurring_payment`](/reference/2026-01-01/objects/billingitem)

[`RecurringPaymentEdge.node`](/reference/2026-01-01/objects/recurringpaymentedge)

[`RecurringPaymentPaginationConnection.nodes`](/reference/2026-01-01/objects/recurringpaymentpaginationconnection)

[`ScheduledUserPackageSelection.recurring_payment`](/reference/2026-01-01/objects/scheduleduserpackageselection)

[`User.next_recurring_payment`](/reference/2026-01-01/objects/user)

[`User.upcoming_payments`](/reference/2026-01-01/objects/user)

[`UserPackageSelection.recurring_payment`](/reference/2026-01-01/objects/userpackageselection)

[`Query.recurringPayment`](/reference/2026-01-01/queries/recurringpayment)

## Definition

```
"""
Recurring Payment
"""
type RecurringPayment {
  """
  The amount of recurring payment
  """
  amount_paid: String


  """
  The amount to be paid for the next payment
  """
  amount_to_pay: String


  """
  The ID of the appointment associated with this recurring payment
  """
  appointment_id: ID


  """
  The frequency the payment should be made
  """
  billing_frequency: String


  """
  The number of billing items
  """
  billing_items_count: Int


  """
  The date on which the recurring payment is canceled
  """
  canceled_at: ISO8601DateTime


  """
  The provider who canceled the recurring payment
  """
  canceled_by: User


  """
  The date on which the recurring payment is created
  """
  created_at: ISO8601DateTime!


  """
  Includes the next payment date, returns true if next payment date is set and payments remaining is greater than zero
  """
  has_next_payment_date: Boolean


  """
  Whether or not this recurring payment has scheduled billing item
  """
  has_scheduled_billing_item: Boolean


  """
  The unique identifier of the recurring payment
  """
  id: ID!


  """
  If the recurring payment has been canceled
  """
  is_canceled: Boolean!


  """
  Whether or not the recurring payments has been paused
  """
  is_paused: Boolean!


  """
  The last billing item for this recurring payment
  """
  last_billing_item: BillingItem


  """
  The date of the next payment
  """
  next_payment_date: ISO8601DateTime


  """
  The next payment date if the recurring payment is restarted
  """
  next_restart_payment_date: ISO8601DateTime


  """
  The ID of the coupon
  """
  offering_coupon_id: ID


  """
  The offering ID
  """
  offering_id: ID


  """
  The name of the offering associated with recurring payment
  """
  offering_name: String


  """
  The original price
  """
  original_price: String


  """
  The date on which the recurring payment is paused
  """
  paused_at: ISO8601DateTime


  """
  The provider who paused the recurring payment
  """
  paused_by: User


  """
  Count remaining payments or returns Until Canceled
  """
  payments_remaining: String


  """
  The ID of the receiver
  """
  recipient_id: ID


  """
  The number of times the payment should repeat
  """
  repeat_tiems: String @deprecated(reason: "Use `repeat_times` instead")


  """
  The number of times the payment should repeat
  """
  repeat_times: Int


  """
  The ID oft the sender
  """
  sender_id: ID


  """
  The date payments should begin
  """
  start_at: ISO8601DateTime


  """
  The updated at date
  """
  updated_at: ISO8601DateTime
}
```
