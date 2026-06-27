---
title: sentFax | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sentfax/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sentfax/index.md
---

Fetch sent Fax by ID

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the sent Fax

## Returns

[`SentFax`](/reference/2026-01-01/objects/sentfax)

## Example

```
query sentFax($id: ID!) {
  sentFax(id: $id) {
    created_at
    destination_number
    id
    parsed_form_answer_group_ids
    patient
    resendable
    sender
    status
    status_display_string
    updated_at
  }
}
```
