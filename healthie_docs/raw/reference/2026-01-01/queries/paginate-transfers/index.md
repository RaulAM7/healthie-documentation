---
title: paginate_transfers | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/paginate-transfers/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/paginate-transfers/index.md
---

returns true if the there are more transfers to load

## Arguments

[`limit` ](#argument-limit)· [`Int`](/reference/2026-01-01/scalars/int)

[`payout_account_id` ](#argument-payout-account-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter transfers to a specific payout account in the current organization. Defaults to the current user's account when omitted.

[`starting_after` ](#argument-starting-after)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`Boolean`](/reference/2026-01-01/scalars/boolean)

## Example

```
query paginate_transfers(
  $limit: Int
  $payout_account_id: ID
  $starting_after: String
) {
  paginate_transfers(
    limit: $limit
    payout_account_id: $payout_account_id
    starting_after: $starting_after
  )
}
```
