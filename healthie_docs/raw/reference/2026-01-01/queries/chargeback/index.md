---
title: chargeBack | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/chargeback/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/chargeback/index.md
---

fetch a chargeback by the Healthie ID or the Stripe Dispute ID.

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`stripe_dispute_id` ](#argument-stripe-dispute-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`ChargeBack`](/reference/2026-01-01/objects/chargeback)

## Example

```
query chargeBack($id: ID, $stripe_dispute_id: ID) {
  chargeBack(id: $id, stripe_dispute_id: $stripe_dispute_id) {
    billing_item
    created_at
    disputed_amount
    evidence
    evidence_fields_to_submit
    fee
    formatted_reason
    formatted_status
    id
    reason
    response_required_by
    status
    total_amount
    updated_at
  }
}
```
