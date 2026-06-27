---
title: receivedFax | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/receivedfax/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/receivedfax/index.md
---

Fetch Received Fax by ID

## Arguments

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the Received Fax

## Returns

[`ReceivedFax`](/reference/2026-01-01/objects/receivedfax)

## Example

```
query receivedFax($id: ID) {
  receivedFax(id: $id) {
    archived
    comments
    created_at
    from_number
    id
    referring_provider_name
    viewed_by_current_user
  }
}
```
