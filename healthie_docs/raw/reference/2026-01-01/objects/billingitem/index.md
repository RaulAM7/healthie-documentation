---
title: BillingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/billingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/billingitem/index.md
---

Billing

## Fields

[`amount_paid` ](#field-amount-paid)· [`String` ](/reference/2026-01-01/scalars/string)· Raw amount value (use amount\_paid\_string for displaying money amounts)

[`amount_paid_string` ](#field-amount-paid-string)· [`String` ](/reference/2026-01-01/scalars/string)· Formatted money amount with 2 decimal places - use this field for displaying payment amounts

[`application_fee_amount` ](#field-application-fee-amount)· [`String` ](/reference/2026-01-01/scalars/string)· Fee charged by stripe in cents

[`card_brand` ](#field-card-brand)· [`String` ](/reference/2026-01-01/scalars/string)· card brand used for this charge (e.g. visa, mastercard) for succeeded payments

[`card_last4` ](#field-card-last4)· [`String` ](/reference/2026-01-01/scalars/string)· last 4 digits of the card used for this specific charge for succeeded payments

[`card_source` ](#field-card-source)· [`String` ](/reference/2026-01-01/scalars/string)· card brand and last4 digits in the event of a failed charge

[`charge_backs` ](#field-charge-backs)· [`[ChargeBack!]` ](/reference/2026-01-01/objects/chargeback)· the related charge backs

[`coupon_code` ](#field-coupon-code)· [`String` ](/reference/2026-01-01/scalars/string)· coupon code

[`cpt_codes_super_bills_id` ](#field-cpt-codes-super-bills-id)· [`ID` ](/reference/2026-01-01/scalars/id)· cpt codes super bills id

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at date

[`currency` ](#field-currency)· [`String` ](/reference/2026-01-01/scalars/string)· type of currency

[`deleted_at` ](#field-deleted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date payment was deleted

[`failure_reason` ](#field-failure-reason)· [`String` ](/reference/2026-01-01/scalars/string)· Error message returned when payment failed

[`gifted_by` ](#field-gifted-by)· [`String` ](/reference/2026-01-01/scalars/string)· Name of person who gifted this package(if applicable). Returns nil if not an offering or if not a gift

[`gifted_to` ](#field-gifted-to)· [`String` ](/reference/2026-01-01/scalars/string)· Name of person who received this package as a gift. Returns nil if not an offering or if not a gift

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the billing item

[`invoice_id` ](#field-invoice-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of invoice

deprecated

Use requested\_payment\_id instead. This will return the same data as that

[`is_canceled` ](#field-is-canceled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· canceled indicator

[`is_outside_payment` ](#field-is-outside-payment)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether this payment was made outside of Healthie

[`is_recurring` ](#field-is-recurring)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether this payment is recurring

[`item_position_number` ](#field-item-position-number)· [`Int` ](/reference/2026-01-01/scalars/int)· The index number of partial payment

[`net_payment` ](#field-net-payment)· [`String` ](/reference/2026-01-01/scalars/string)· The payment, after refunds are taken out

[`next_scheduled_payment_amount` ](#field-next-scheduled-payment-amount)· [`String` ](/reference/2026-01-01/scalars/string)· Nil unless the payment is an uncharged upcoming scheduled payment. Otherwise, is the payment amount that is scheduled to be charged

[`note` ](#field-note)· [`String` ](/reference/2026-01-01/scalars/string)· payment note

[`offering` ](#field-offering)· [`Offering` ](/reference/2026-01-01/objects/offering)· offering connected to the payment

[`offering_coupon` ](#field-offering-coupon)· [`OfferingCoupon` ](/reference/2026-01-01/objects/offeringcoupon)· offering coupon connected to the payment

[`offering_coupon_id` ](#field-offering-coupon-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of coupon

[`offering_id` ](#field-offering-id)· [`ID` ](/reference/2026-01-01/scalars/id)· offering id

[`original_price` ](#field-original-price)· [`String` ](/reference/2026-01-01/scalars/string)· original price

[`payment_medium` ](#field-payment-medium)· [`ID` ](/reference/2026-01-01/scalars/id)· payment medium

[`provider` ](#field-provider)· [`User` ](/reference/2026-01-01/objects/user)· provider

[`receipt_last_sent_at` ](#field-receipt-last-sent-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· receipt last sent at date

[`recipient` ](#field-recipient)· [`User` ](/reference/2026-01-01/objects/user)· recipient of this payment

[`recipient_id` ](#field-recipient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of receiver

[`recurring_payment` ](#field-recurring-payment)· [`RecurringPayment` ](/reference/2026-01-01/objects/recurringpayment)· recurring payment connected to the payment

[`refund_amount` ](#field-refund-amount)· [`String` ](/reference/2026-01-01/scalars/string)· amount of refund

[`refund_date` ](#field-refund-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date of refund

[`refund_items` ](#field-refund-items)· [`[RefundItem!]` ](/reference/2026-01-01/objects/refunditem)· the related refundings

[`requested_payer` ](#field-requested-payer)· [`RequestedPayer` ](/reference/2026-01-01/objects/requestedpayer)· Individual responsible for payment. If user\_id, user exists in Healthie, if not, individual doesn't have a Healthie account

[`requested_payment` ](#field-requested-payment)· [`RequestedPayment` ](/reference/2026-01-01/objects/requestedpayment)· the connected requested payment

[`requested_payment_id` ](#field-requested-payment-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of requested payment (we call them invoices in our UI)

[`sender` ](#field-sender)· [`User` ](/reference/2026-01-01/objects/user)· sender of this payment

[`sender_id` ](#field-sender-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of sender

[`shown_description` ](#field-shown-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description text to show for the payment

[`shown_note` ](#field-shown-note)· [`String` ](/reference/2026-01-01/scalars/string)· The note text to show for the payment

[`state` ](#field-state)· [`BillingItemState` ](/reference/2026-01-01/enums/billingitemstate)· Enum status of billing item succeeded/failed

[`stripe_charge_id` ](#field-stripe-charge-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of stripe charge

[`stripe_error` ](#field-stripe-error)· [`String` ](/reference/2026-01-01/scalars/string)· A JSON hash containing information on why Stripe was unable to process a charge

[`successful_retried_payment` ](#field-successful-retried-payment)· [`BillingItem` ](/reference/2026-01-01/objects/billingitem)· if a failed payment is retried successfully then this will reference that successful payment

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· updated at date

[`user_package_selection` ](#field-user-package-selection)· [`UserPackageSelection` ](/reference/2026-01-01/objects/userpackageselection)· User Package Selection connected to this payment

## Used By

[`BillingItem.successful_retried_payment`](/reference/2026-01-01/objects/billingitem)

[`BillingItemEdge.node`](/reference/2026-01-01/objects/billingitemedge)

[`BillingItemPaginationConnection.nodes`](/reference/2026-01-01/objects/billingitempaginationconnection)

[`ChargeBack.billing_item`](/reference/2026-01-01/objects/chargeback)

[`RecurringPayment.last_billing_item`](/reference/2026-01-01/objects/recurringpayment)

[`RequestedPayment.billing_items`](/reference/2026-01-01/objects/requestedpayment)

[`User.billing_items`](/reference/2026-01-01/objects/user)

[`User.last_billing_item`](/reference/2026-01-01/objects/user)

[`UserPackageSelection.billing_item`](/reference/2026-01-01/objects/userpackageselection)

[`cancelRecurringPaymentPayload.billingItem`](/reference/2026-01-01/objects/cancelrecurringpaymentpayload)

[`completeCheckoutPayload.billingItem`](/reference/2026-01-01/objects/completecheckoutpayload)

[`createBillingItemPayload.billingItem`](/reference/2026-01-01/objects/createbillingitempayload)

[`deleteBillingItemPayload.billingItem`](/reference/2026-01-01/objects/deletebillingitempayload)

[`updateBillingItemPayload.billingItem`](/reference/2026-01-01/objects/updatebillingitempayload)

[`Query.billingItem`](/reference/2026-01-01/queries/billingitem)

## Definition

```
"""
Billing
"""
type BillingItem {
  """
  Raw amount value (use amount_paid_string for displaying money amounts)
  """
  amount_paid: String


  """
  Formatted money amount with 2 decimal places - use this field for displaying payment amounts
  """
  amount_paid_string: String


  """
  Fee charged by stripe in cents
  """
  application_fee_amount: String


  """
  card brand used for this charge (e.g. visa, mastercard) for succeeded payments
  """
  card_brand: String


  """
  last 4 digits of the card used for this specific charge for succeeded payments
  """
  card_last4: String


  """
  card brand and last4 digits in the event of a failed charge
  """
  card_source: String


  """
  the related charge backs
  """
  charge_backs: [ChargeBack!]


  """
  coupon code
  """
  coupon_code: String


  """
  cpt codes super bills id
  """
  cpt_codes_super_bills_id: ID


  """
  created at date
  """
  created_at: ISO8601DateTime!


  """
  type of currency
  """
  currency: String


  """
  date payment was deleted
  """
  deleted_at: ISO8601DateTime


  """
  Error message returned when payment failed
  """
  failure_reason: String


  """
  Name of person who gifted this package(if applicable). Returns nil if not an offering or if not a gift
  """
  gifted_by: String


  """
  Name of person who received this package as a gift. Returns nil if not an offering or if not a gift
  """
  gifted_to: String


  """
  The unique identifier of the billing item
  """
  id: ID!


  """
  id of invoice
  """
  invoice_id: ID
    @deprecated(
      reason: "Use requested_payment_id instead. This will return the same data as that"
    )


  """
  canceled indicator
  """
  is_canceled: Boolean


  """
  Whether this payment was made outside of Healthie
  """
  is_outside_payment: Boolean


  """
  Whether this payment is recurring
  """
  is_recurring: Boolean


  """
  The index number of partial payment
  """
  item_position_number: Int


  """
  The payment, after refunds are taken out
  """
  net_payment: String


  """
  Nil unless the payment is an uncharged upcoming scheduled payment. Otherwise, is the payment amount that is scheduled to be charged
  """
  next_scheduled_payment_amount: String


  """
  payment note
  """
  note: String


  """
  offering connected to the payment
  """
  offering: Offering


  """
  offering coupon connected to the payment
  """
  offering_coupon: OfferingCoupon


  """
  id of coupon
  """
  offering_coupon_id: ID


  """
  offering id
  """
  offering_id: ID


  """
  original price
  """
  original_price: String


  """
  payment medium
  """
  payment_medium: ID


  """
  provider
  """
  provider: User


  """
  receipt last sent at date
  """
  receipt_last_sent_at: ISO8601DateTime


  """
  recipient of this payment
  """
  recipient: User


  """
  id of receiver
  """
  recipient_id: ID


  """
  recurring payment connected to the payment
  """
  recurring_payment: RecurringPayment


  """
  amount of refund
  """
  refund_amount: String


  """
  date of refund
  """
  refund_date: ISO8601DateTime


  """
  the related refundings
  """
  refund_items: [RefundItem!]


  """
  Individual responsible for payment. If user_id, user exists in Healthie, if not, individual doesn't have a Healthie account
  """
  requested_payer: RequestedPayer


  """
  the connected requested payment
  """
  requested_payment: RequestedPayment


  """
  id of requested payment (we call them invoices in our UI)
  """
  requested_payment_id: ID


  """
  sender of this payment
  """
  sender: User


  """
  id of sender
  """
  sender_id: ID


  """
  The description text to show for the payment
  """
  shown_description: String


  """
  The note text to show for the payment
  """
  shown_note: String


  """
  Enum status of billing item succeeded/failed
  """
  state: BillingItemState


  """
  id of stripe charge
  """
  stripe_charge_id: ID


  """
  A JSON hash containing information on why Stripe was unable to process a charge
  """
  stripe_error: String


  """
  if a failed payment is retried successfully then this will reference that successful payment
  """
  successful_retried_payment: BillingItem


  """
  updated at date
  """
  updated_at: ISO8601DateTime


  """
  User Package Selection connected to this payment
  """
  user_package_selection: UserPackageSelection
}
```
