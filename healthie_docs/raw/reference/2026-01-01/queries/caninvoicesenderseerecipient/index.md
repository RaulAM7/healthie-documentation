---
title: canInvoiceSenderSeeRecipient | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/caninvoicesenderseerecipient/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/caninvoicesenderseerecipient/index.md
---

Check if provider has access to client

## Arguments

[`sender_id` ](#argument-sender-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Provider ID

[`recipient_id` ](#argument-recipient-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Client ID

## Returns

[`Boolean`](/reference/2026-01-01/scalars/boolean)

## Example

```
query canInvoiceSenderSeeRecipient($sender_id: ID!, $recipient_id: ID!) {
  canInvoiceSenderSeeRecipient(
    sender_id: $sender_id
    recipient_id: $recipient_id
  )
}
```
