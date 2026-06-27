---
title: comment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/comment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/comment/index.md
---

Fetch comment

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Comment`](/reference/2026-01-01/objects/comment)

## Example

```
query comment($id: ID) {
  comment(id: $id) {
    author
    content
    created_at
    creator
    entry_id
    id
    is_reaction
    poster
    user_id
  }
}
```
