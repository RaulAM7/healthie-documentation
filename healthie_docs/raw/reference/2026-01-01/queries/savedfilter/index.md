---
title: savedFilter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/savedfilter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/savedfilter/index.md
---

Fetch specific saved filter

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`uuid` ](#argument-uuid)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`SavedFilter`](/reference/2026-01-01/objects/savedfilter)

## Example

```
query savedFilter($id: ID, $uuid: ID) {
  savedFilter(id: $id, uuid: $uuid) {
    filter_data
    id
    name
    organization_id
    user_id
    uuid
  }
}
```
