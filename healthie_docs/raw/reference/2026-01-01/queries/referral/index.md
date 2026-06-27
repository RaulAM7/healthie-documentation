---
title: referral | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/referral/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/referral/index.md
---

Fetch Referral by ID

## Arguments

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the Referral

## Returns

[`Referral`](/reference/2026-01-01/objects/referral)

## Example

```
query referral($id: ID) {
  referral(id: $id) {
    created_at
    id
    metadata
    referral_reason
    referring_physician
    referring_physician_id
    updated_at
    user
    user_id
  }
}
```
