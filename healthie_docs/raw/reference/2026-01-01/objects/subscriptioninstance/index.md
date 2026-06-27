---
title: SubscriptionInstance | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/subscriptioninstance/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/subscriptioninstance/index.md
---

a subscription object

## Fields

[`access_will_stop_at` ](#field-access-will-stop-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When a customer cancels, or is set to cancel, this will be a datetime of when access will cease

[`amount_saved_if_plan_switched` ](#field-amount-saved-if-plan-switched)· [`Int` ](/reference/2026-01-01/scalars/int)· Amount difference if switching to annual/monthly

[`amount_savings_on_base_plan` ](#field-amount-savings-on-base-plan)· [`String` ](/reference/2026-01-01/scalars/string)· Amount savings from monthly to annual

[`annual_total` ](#field-annual-total)· [`String` ](/reference/2026-01-01/scalars/string)· Total cost of subscription for the year

[`card_expiration` ](#field-card-expiration)· [`String` ](/reference/2026-01-01/scalars/string)· Expiration of credit card on Stripe

[`card_expired` ](#field-card-expired)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Returns true if card is expired

[`card_type` ](#field-card-type)· [`String` ](/reference/2026-01-01/scalars/string)· Type of credit card on Stripe (Mastercard, Visa, Amex, etc.)

[`client_count` ](#field-client-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Number of clients under the user that owns the subscription

[`cost_of_annual_base_plan` ](#field-cost-of-annual-base-plan)· [`String` ](/reference/2026-01-01/scalars/string)· Cost per month of annual plan

[`credit_balance` ](#field-credit-balance)· [`Float` ](/reference/2026-01-01/scalars/float)· Credit balance on Stripe customer

[`days_left_in_trial` ](#field-days-left-in-trial)· [`Int` ](/reference/2026-01-01/scalars/int)· Shows how many days are left in the users trial

[`discounts` ](#field-discounts)· [`[Discount!]` ](/reference/2026-01-01/objects/discount)· Discounts currently active on Stripe account

[`discounts_if_switched` ](#field-discounts-if-switched)· [`[Discount!]` ](/reference/2026-01-01/objects/discount)· Array of discounts applied in Stripe (most possible is 2)

[`has_scheduled_change` ](#field-has-scheduled-change)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Returns true if there is already a scheduled subscription change on this account

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the subscription

[`interval` ](#field-interval)· [`String` ](/reference/2026-01-01/scalars/string)· The interval of the subscription

[`invoice_if_switched` ](#field-invoice-if-switched)· [`StripeInvoice` ](/reference/2026-01-01/objects/stripeinvoice)· Example of next invoice if switching plan

[`is_trialing` ](#field-is-trialing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Returns true if the user is trialing

[`last_four` ](#field-last-four)· [`String` ](/reference/2026-01-01/scalars/string)· Last four digits of credit card on Stripe

[`last_invoice` ](#field-last-invoice)· [`StripeInvoice` ](/reference/2026-01-01/objects/stripeinvoice)· Last attempted invoice in Stripe

[`locked_out_at` ](#field-locked-out-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When the user is scheduled to be locked out due to non-payment

[`month_total` ](#field-month-total)· [`String` ](/reference/2026-01-01/scalars/string)· Total cost of subscription for the month

deprecated

This field is no longer supported and always returns null. Use monthly\_cost\_of\_base\_plan instead.

[`monthly_cost_of_annual_base_plan` ](#field-monthly-cost-of-annual-base-plan)· [`String` ](/reference/2026-01-01/scalars/string)· Cost per month of annual plan

[`monthly_cost_of_base_plan` ](#field-monthly-cost-of-base-plan)· [`String` ](/reference/2026-01-01/scalars/string)· Cost per month for base plan

[`paid_for_providers` ](#field-paid-for-providers)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of providers that the subscription covers

[`paid_for_support` ](#field-paid-for-support)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of support staff that the subscription covers

[`percent_change_if_plan_switched` ](#field-percent-change-if-plan-switched)· [`Int` ](/reference/2026-01-01/scalars/int)· Percent difference if switching to annual/monthly

[`percent_savings_on_base_plan` ](#field-percent-savings-on-base-plan)· [`Int` ](/reference/2026-01-01/scalars/int)· Percent savings from monthly to annual

[`plan_add_ons` ](#field-plan-add-ons)· [`[StripePlan!]` ](/reference/2026-01-01/objects/stripeplan)· Array of line items applied to Stripe subscription other than base plan (i.e fax line, extra providers, office ally etc.)

[`plan_id` ](#field-plan-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the plan in Healthie

[`plan_name` ](#field-plan-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the plan in Stripe

[`set_to_cancel` ](#field-set-to-cancel)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Returns true if the user is set to cancel

[`stripe_balance` ](#field-stripe-balance)· [`String` ](/reference/2026-01-01/scalars/string)· Remaining balance on stripe customer

[`stripe_id` ](#field-stripe-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the customer in Stripe

[`stripe_plan` ](#field-stripe-plan)· [`String` ](/reference/2026-01-01/scalars/string)· Stripe Subscription plan name

[`stripe_subscription_id` ](#field-stripe-subscription-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the subscription in Stripe

[`trial_end_at` ](#field-trial-end-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When the trial ends

[`upcoming_invoice` ](#field-upcoming-invoice)· [`StripeInvoice` ](/reference/2026-01-01/objects/stripeinvoice)· Upcoming invoice in Stripe

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this subscription

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user who owns the subscription

## Used By

[`Organization.owner_subscription`](/reference/2026-01-01/objects/organization)

[`User.subscription`](/reference/2026-01-01/objects/user)

[`createSubscriptionPayload.subscription`](/reference/2026-01-01/objects/createsubscriptionpayload)

[`updateSubscriptionPayload.subscription`](/reference/2026-01-01/objects/updatesubscriptionpayload)

[`Query.subscription`](/reference/2026-01-01/queries/subscription)

## Definition

```
"""
a subscription object
"""
type SubscriptionInstance {
  """
  When a customer cancels, or is set to cancel, this will be a datetime of when access will cease
  """
  access_will_stop_at: ISO8601DateTime


  """
  Amount difference if switching to annual/monthly
  """
  amount_saved_if_plan_switched: Int


  """
  Amount savings from monthly to annual
  """
  amount_savings_on_base_plan: String


  """
  Total cost of subscription for the year
  """
  annual_total: String


  """
  Expiration of credit card on Stripe
  """
  card_expiration: String


  """
  Returns true if card is expired
  """
  card_expired: Boolean


  """
  Type of credit card on Stripe (Mastercard, Visa, Amex, etc.)
  """
  card_type: String


  """
  Number of clients under the user that owns the subscription
  """
  client_count: Int


  """
  Cost per month of annual plan
  """
  cost_of_annual_base_plan: String


  """
  Credit balance on Stripe customer
  """
  credit_balance: Float


  """
  Shows how many days are left in the users trial
  """
  days_left_in_trial: Int


  """
  Discounts currently active on Stripe account
  """
  discounts: [Discount!]


  """
  Array of discounts applied in Stripe (most possible is 2)
  """
  discounts_if_switched: [Discount!]


  """
  Returns true if there is already a scheduled subscription change on this account
  """
  has_scheduled_change: Boolean


  """
  The unique identifier of the subscription
  """
  id: ID!


  """
  The interval of the subscription
  """
  interval: String


  """
  Example of next invoice if switching plan
  """
  invoice_if_switched: StripeInvoice


  """
  Returns true if the user is trialing
  """
  is_trialing: Boolean


  """
  Last four digits of credit card on Stripe
  """
  last_four: String


  """
  Last attempted invoice in Stripe
  """
  last_invoice: StripeInvoice


  """
  When the user is scheduled to be locked out due to non-payment
  """
  locked_out_at: ISO8601DateTime


  """
  Total cost of subscription for the month
  """
  month_total: String
    @deprecated(
      reason: "This field is no longer supported and always returns null. Use monthly_cost_of_base_plan instead."
    )


  """
  Cost per month of annual plan
  """
  monthly_cost_of_annual_base_plan: String


  """
  Cost per month for base plan
  """
  monthly_cost_of_base_plan: String


  """
  The number of providers that the subscription covers
  """
  paid_for_providers: Int


  """
  The number of support staff that the subscription covers
  """
  paid_for_support: Int


  """
  Percent difference if switching to annual/monthly
  """
  percent_change_if_plan_switched: Int


  """
  Percent savings from monthly to annual
  """
  percent_savings_on_base_plan: Int


  """
  Array of line items applied to Stripe subscription other than base plan (i.e fax line, extra providers, office ally etc.)
  """
  plan_add_ons: [StripePlan!]


  """
  The ID of the plan in Healthie
  """
  plan_id: String


  """
  Name of the plan in Stripe
  """
  plan_name: String


  """
  Returns true if the user is set to cancel
  """
  set_to_cancel: Boolean


  """
  Remaining balance on stripe customer
  """
  stripe_balance: String


  """
  The ID of the customer in Stripe
  """
  stripe_id: String


  """
  Stripe Subscription plan name
  """
  stripe_plan: String


  """
  The ID of the subscription in Stripe
  """
  stripe_subscription_id: String


  """
  When the trial ends
  """
  trial_end_at: ISO8601DateTime


  """
  Upcoming invoice in Stripe
  """
  upcoming_invoice: StripeInvoice


  """
  Owner of this subscription
  """
  user: User


  """
  The ID of the user who owns the subscription
  """
  user_id: String
}
```
