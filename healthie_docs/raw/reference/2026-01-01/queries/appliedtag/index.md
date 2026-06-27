---
title: appliedTag | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appliedtag/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appliedtag/index.md
---

An applied tag to a user

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`include_deleted` ](#argument-include-deleted)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

## Returns

[`AppliedTag`](/reference/2026-01-01/objects/appliedtag)

## Example

```
query appliedTag($id: ID, $include_deleted: Boolean) {
  appliedTag(id: $id, include_deleted: $include_deleted) {
    created_at
    id
    tag
    tag_id
    updated_at
    user
    user_id
  }
}
```
