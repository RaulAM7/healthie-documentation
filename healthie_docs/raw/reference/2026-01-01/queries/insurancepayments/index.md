---
title: insurancePayments | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/insurancepayments/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/insurancepayments/index.md
---

Fetch insurance payments for authenticated provider

## Arguments

[`start_paid_date` ](#argument-start-paid-date)· [`ISO8601Date`](/reference/2026-01-01/scalars/iso8601date)

[`end_paid_date` ](#argument-end-paid-date)· [`ISO8601Date`](/reference/2026-01-01/scalars/iso8601date)

[`order_by` ](#argument-order-by)· [`InsurancePaymentsOrderKeys`](/reference/2026-01-01/enums/insurancepaymentsorderkeys)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`deposit_status` ](#argument-deposit-status)· [`InsurancePaymentsDepositStatusEnum`](/reference/2026-01-01/enums/insurancepaymentsdepositstatusenum)

[`payer` ](#argument-payer)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`InsurancePaymentConnection`](/reference/2026-01-01/objects/insurancepaymentconnection)

## Example

```
query insurancePayments(
  $start_paid_date: ISO8601Date
  $end_paid_date: ISO8601Date
  $order_by: InsurancePaymentsOrderKeys
  $keywords: String
  $deposit_status: InsurancePaymentsDepositStatusEnum
  $payer: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  insurancePayments(
    start_paid_date: $start_paid_date
    end_paid_date: $end_paid_date
    order_by: $order_by
    keywords: $keywords
    deposit_status: $deposit_status
    payer: $payer
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
