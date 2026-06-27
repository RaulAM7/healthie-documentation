---
title: transactions | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/transactions/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/transactions/index.md
---

fetch transactions for the current user

## Arguments

[`payout_id` ](#argument-payout-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`[TransactionType!]`](/reference/2026-01-01/objects/transactiontype)

## Example

```
query transactions($payout_id: ID, $user_id: ID) {
  transactions(payout_id: $payout_id, user_id: $user_id) {
    currency
    displayed_amount
    source_name
  }
}
```
