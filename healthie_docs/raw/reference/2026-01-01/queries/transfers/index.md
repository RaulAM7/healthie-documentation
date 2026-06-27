---
title: transfers | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/transfers/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/transfers/index.md
---

fetch transfers for the current user

## Arguments

[`limit` ](#argument-limit)· [`Int`](/reference/2026-01-01/scalars/int)

[`payout_account_id` ](#argument-payout-account-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter transfers to a specific payout account in the current organization. Defaults to the current user's account when omitted.

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`TransferOrderKeys`](/reference/2026-01-01/enums/transferorderkeys)

[`starting_after` ](#argument-starting-after)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`[TransferType!]`](/reference/2026-01-01/objects/transfertype)

## Example

```
query transfers(
  $limit: Int
  $payout_account_id: ID
  $sort_by: String
  $order_by: TransferOrderKeys
  $starting_after: String
) {
  transfers(
    limit: $limit
    payout_account_id: $payout_account_id
    sort_by: $sort_by
    order_by: $order_by
    starting_after: $starting_after
  ) {
    amount
    currency
    displayed_amount
    displayed_expected_to_happen
    displayed_initiated
    expected_to_happen
    fees
    id
    initiated
    status
    transactions_count
    type
  }
}
```
