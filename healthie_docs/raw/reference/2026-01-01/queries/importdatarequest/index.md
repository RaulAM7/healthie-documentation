---
title: importDataRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/importdatarequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/importdatarequest/index.md
---

fetch import data request by user\_id

## Arguments

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`ImportDataRequest`](/reference/2026-01-01/objects/importdatarequest)

## Example

```
query importDataRequest($user_id: ID) {
  importDataRequest(user_id: $user_id) {
    clients_template
    created_at
    display_name
    extension
    optional_comment
    request_type
  }
}
```
