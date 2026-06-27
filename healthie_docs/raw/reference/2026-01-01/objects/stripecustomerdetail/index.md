---
title: StripeCustomerDetail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecustomerdetail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecustomerdetail/index.md
---

Details of the client's credit card

## Fields

[`bank_type` ](#field-bank-type)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the bank the bank account is with (nil for 'Card' source types)

[`card_type` ](#field-card-type)· [`String` ](/reference/2026-01-01/scalars/string)· The brand of the card

[`card_type_label` ](#field-card-type-label)· [`String` ](/reference/2026-01-01/scalars/string)· The type of card indicated by the user. Defaults to personal, Options are 'hsa', 'fsa', and 'personal'

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· Stripe card country

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date this payment method was created/added

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · Pagination cursor

[`expiration` ](#field-expiration)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The expiration date of the card

[`expiring_next_month` ](#field-expiring-next-month)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the card is expiring next month

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the customer detail object

[`last_four` ](#field-last-four)· [`String` ](/reference/2026-01-01/scalars/string)· The last 4 digits of the credit card

[`source_status` ](#field-source-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the payment method

[`source_type` ](#field-source-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of payment method (either 'Card' or 'Bank Account')

[`stripe_id` ](#field-stripe-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the client (in Stripe)

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The client associated with stripe account(in Healthie)

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the client (in Healthie)

[`zip` ](#field-zip)· [`String` ](/reference/2026-01-01/scalars/string)· Stripe card address zip

## Used By

[`StripeCustomerDetailEdge.node`](/reference/2026-01-01/objects/stripecustomerdetailedge)

[`StripeCustomerDetailPaginationConnection.nodes`](/reference/2026-01-01/objects/stripecustomerdetailpaginationconnection)

[`User.stripe_customer_detail`](/reference/2026-01-01/objects/user)

[`User.stripe_customer_details`](/reference/2026-01-01/objects/user)

[`bulkUpdateCardIssuesPayload.card_issues`](/reference/2026-01-01/objects/bulkupdatecardissuespayload)

[`createStripeCustomerDetailPayload.stripe_customer_detail`](/reference/2026-01-01/objects/createstripecustomerdetailpayload)

[`deleteStripeCustomerDetailPayload.stripe_customer_detail`](/reference/2026-01-01/objects/deletestripecustomerdetailpayload)

[`updateStripeCustomerDetailPayload.stripe_customer_detail`](/reference/2026-01-01/objects/updatestripecustomerdetailpayload)

## Definition

```
"""
Details of the client's credit card
"""
type StripeCustomerDetail {
  """
  The name of the bank the bank account is with (nil for 'Card' source types)
  """
  bank_type: String


  """
  The brand of the card
  """
  card_type: String


  """
  The type of card indicated by the user. Defaults to personal, Options are 'hsa', 'fsa', and 'personal'
  """
  card_type_label: String


  """
  Stripe card country
  """
  country: String


  """
  The date this payment method was created/added
  """
  created_at: ISO8601DateTime


  """
  Pagination cursor
  """
  cursor: Cursor!


  """
  The expiration date of the card
  """
  expiration: ISO8601DateTime


  """
  Whether the card is expiring next month
  """
  expiring_next_month: Boolean


  """
  The unique identifier of the customer detail object
  """
  id: ID!


  """
  The last 4 digits of the credit card
  """
  last_four: String


  """
  The status of the payment method
  """
  source_status: String


  """
  The type of payment method (either 'Card' or 'Bank Account')
  """
  source_type: String


  """
  The ID of the client (in Stripe)
  """
  stripe_id: String


  """
  The client associated with stripe account(in Healthie)
  """
  user: User


  """
  The ID of the client (in Healthie)
  """
  user_id: String


  """
  Stripe card address zip
  """
  zip: String
}
```
