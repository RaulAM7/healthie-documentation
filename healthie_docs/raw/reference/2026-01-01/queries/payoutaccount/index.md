---
title: payoutAccount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/payoutaccount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/payoutaccount/index.md
---

Fetch a single payout account by ID

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · ID of the payout account to fetch

## Returns

[`PayoutAccount`](/reference/2026-01-01/objects/payoutaccount)

## Example

```
query payoutAccount($id: ID!) {
  payoutAccount(id: $id) {
    created_at
    id
    name
    updated_at
    uuid
  }
}
```
