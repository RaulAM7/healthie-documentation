---
title: RequestedPayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpayment/index.md
---

A request, from a provider to a client, to make a payment

## Fields

[`appointment` ](#field-appointment)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· The appointment associated with this requested payment

[`appointment_id` ](#field-appointment-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the appointment associated with this requested payment

[`balance_due` ](#field-balance-due)· [`Float` ](/reference/2026-01-01/scalars/float)· The balance due on this invoice (based on payments and write-offs)

[`billing_item_id` ](#field-billing-item-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the filled form that completes the request

[`billing_items` ](#field-billing-items)· [`[BillingItem!]!` ](/reference/2026-01-01/objects/billingitem)· required · The payments that completes the request

[`cms1500_id` ](#field-cms1500-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the CMS1500 to pay for

[`cms1500_service_date` ](#field-cms1500-service-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The CMS1500 service date

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the requested payment record was created

[`currency` ](#field-currency)· [`String` ](/reference/2026-01-01/scalars/string)· The currency of the requested payment (invoice)

[`date_to_show` ](#field-date-to-show)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The relevant date to show

[`debt` ](#field-debt)· [`Int` ](/reference/2026-01-01/scalars/int)· Balance to pay

deprecated

use debt\_decimal instead

[`debt_decimal` ](#field-debt-decimal)· [`Float` ](/reference/2026-01-01/scalars/float)· The debt, including decimals

[`details` ](#field-details)· [`String` ](/reference/2026-01-01/scalars/string)· The details of the invoice (based off of associated item)

[`email_sent_at` ](#field-email-sent-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The datetime that the share email was last sent, nil if never

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the payment

[`invoice_id` ](#field-invoice-id)· [`String` ](/reference/2026-01-01/scalars/string)· The generated invoice ID

[`invoice_type` ](#field-invoice-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of invoice

[`is_manually_paid` ](#field-is-manually-paid)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if requested payment was manually paid

[`is_preview` ](#field-is-preview)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if the invoice is still in preview mode

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000.

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Extra details on the invoice

[`offering` ](#field-offering)· [`Offering` ](/reference/2026-01-01/objects/offering)· The offering to purchase

[`offering_id` ](#field-offering-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the offering to buy

[`offering_price_at_invoice_creation` ](#field-offering-price-at-invoice-creation)· [`String` ](/reference/2026-01-01/scalars/string)· The price of the offering at the time of invoice creation

[`other_requested_payer` ](#field-other-requested-payer)· [`RequestedPayer` ](/reference/2026-01-01/objects/requestedpayer)· The requested payer. This will return null if the requested payer exists as a client in Healthie

[`paid_at` ](#field-paid-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The datetime that the invoice was paid

[`paid_percent` ](#field-paid-percent)· [`Int` ](/reference/2026-01-01/scalars/int)· Percent from total price which has been paid (if status == Partial)

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· price of payment requested

[`recipient` ](#field-recipient)· [`User` ](/reference/2026-01-01/objects/user)· The recipient (client)

[`recipient_id` ](#field-recipient-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the recipient (client)

[`requested_payer` ](#field-requested-payer)· [`RequestedPayer` ](/reference/2026-01-01/objects/requestedpayer)· Individual responsible for payment. If user\_id, the user exists in Healthie, otherwise the individual doesn't have a Healthie account.

[`requested_payer_id` ](#field-requested-payer-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the requested payer

[`requested_payment_template` ](#field-requested-payment-template)· [`RequestedPaymentTemplate` ](/reference/2026-01-01/objects/requestedpaymenttemplate)· The template used to create this requested payment

[`sender` ](#field-sender)· [`User` ](/reference/2026-01-01/objects/user)· The sender (provider)

[`sender_id` ](#field-sender-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the sender (provider)

[`service_date` ](#field-service-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The service date

[`services_provided` ](#field-services-provided)· [`String` ](/reference/2026-01-01/scalars/string)· The services provided

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the request

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the requested payment record was last updated

[`user_package_selection` ](#field-user-package-selection)· [`UserPackageSelection` ](/reference/2026-01-01/objects/userpackageselection)· User Package Selection connected to this requested payment

[`write_off_amount` ](#field-write-off-amount)· [`Float` ](/reference/2026-01-01/scalars/float)· The total amount written off

[`write_offs` ](#field-write-offs)· [`[WriteOff!]` ](/reference/2026-01-01/objects/writeoff)· The write-offs associated with this requested payment

## Used By

[`Appointment.requested_payment`](/reference/2026-01-01/objects/appointment)

[`BillingItem.requested_payment`](/reference/2026-01-01/objects/billingitem)

[`PatientEncounter.requested_payments`](/reference/2026-01-01/objects/patientencounter)

[`RequestedPaymentEdge.node`](/reference/2026-01-01/objects/requestedpaymentedge)

[`RequestedPaymentPaginationConnection.nodes`](/reference/2026-01-01/objects/requestedpaymentpaginationconnection)

[`RequestedPaymentTemplate.requested_payment`](/reference/2026-01-01/objects/requestedpaymenttemplate)

[`UserPackageSelection.requested_payment`](/reference/2026-01-01/objects/userpackageselection)

[`WriteOff.requested_payment`](/reference/2026-01-01/objects/writeoff)

[`createRequestedPaymentPayload.requestedPayment`](/reference/2026-01-01/objects/createrequestedpaymentpayload)

[`deleteRequestedPaymentPayload.requested_payment`](/reference/2026-01-01/objects/deleterequestedpaymentpayload)

[`updateRequestedPaymentPayload.requested_payment`](/reference/2026-01-01/objects/updaterequestedpaymentpayload)

[`Query.requestedPayment`](/reference/2026-01-01/queries/requestedpayment)

## Definition

```
"""
A request, from a provider to a client, to make a payment
"""
type RequestedPayment {
  """
  The appointment associated with this requested payment
  """
  appointment: Appointment


  """
  The ID of the appointment associated with this requested payment
  """
  appointment_id: String


  """
  The balance due on this invoice (based on payments and write-offs)
  """
  balance_due: Float


  """
  The id of the filled form that completes the request
  """
  billing_item_id: String


  """
  The payments that completes the request
  """
  billing_items(
    """
    Only return successful billing items
    """
    only_successful: Boolean = true
  ): [BillingItem!]!


  """
  The ID of the CMS1500 to pay for
  """
  cms1500_id: String


  """
  The CMS1500 service date
  """
  cms1500_service_date: ISO8601DateTime


  """
  The time the requested payment record was created
  """
  created_at: ISO8601DateTime!


  """
  The currency of the requested payment (invoice)
  """
  currency: String


  """
  The relevant date to show
  """
  date_to_show: ISO8601DateTime


  """
  Balance to pay
  """
  debt: Int @deprecated(reason: "use debt_decimal instead")


  """
  The debt, including decimals
  """
  debt_decimal: Float


  """
  The details of the invoice (based off of associated item)
  """
  details: String


  """
  The datetime that the share email was last sent, nil if never
  """
  email_sent_at: ISO8601DateTime


  """
  The unique identifier of the payment
  """
  id: ID!


  """
  The generated invoice ID
  """
  invoice_id: String


  """
  The type of invoice
  """
  invoice_type: String


  """
  True if requested payment was manually paid
  """
  is_manually_paid: Boolean


  """
  True if the invoice is still in preview mode
  """
  is_preview: Boolean!


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000.
  """
  metadata: String


  """
  Extra details on the invoice
  """
  notes: String


  """
  The offering to purchase
  """
  offering: Offering


  """
  The ID of the offering to buy
  """
  offering_id: String


  """
  The price of the offering at the time of invoice creation
  """
  offering_price_at_invoice_creation: String


  """
  The requested payer. This will return null if the requested payer exists as a client in Healthie
  """
  other_requested_payer: RequestedPayer


  """
  The datetime that the invoice was paid
  """
  paid_at: ISO8601DateTime


  """
  Percent from total price which has been paid (if status == Partial)
  """
  paid_percent: Int


  """
  price of payment requested
  """
  price: String


  """
  The recipient (client)
  """
  recipient: User


  """
  The ID of the recipient (client)
  """
  recipient_id: String


  """
  Individual responsible for payment. If user_id, the user exists in Healthie, otherwise the individual doesn't have a Healthie account.
  """
  requested_payer: RequestedPayer


  """
  The ID of the requested payer
  """
  requested_payer_id: String


  """
  The template used to create this requested payment
  """
  requested_payment_template: RequestedPaymentTemplate


  """
  The sender (provider)
  """
  sender: User


  """
  The ID of the sender (provider)
  """
  sender_id: String


  """
  The service date
  """
  service_date: ISO8601DateTime


  """
  The services provided
  """
  services_provided: String


  """
  The status of the request
  """
  status: String


  """
  The time the requested payment record was last updated
  """
  updated_at: ISO8601DateTime!


  """
  User Package Selection connected to this requested payment
  """
  user_package_selection: UserPackageSelection


  """
  The total amount written off
  """
  write_off_amount: Float


  """
  The write-offs associated with this requested payment
  """
  write_offs: [WriteOff!]
}
```
