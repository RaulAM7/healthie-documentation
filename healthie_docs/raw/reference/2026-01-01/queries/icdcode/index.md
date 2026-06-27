---
title: icdCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/icdcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/icdcode/index.md
---

Fetch ICD Code by ID

## Arguments

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the ICD code.

## Returns

[`IcdCode`](/reference/2026-01-01/objects/icdcode)

## Example

```
query icdCode($id: ID) {
  icdCode(id: $id) {
    category
    code
    created_at
    description
    display_name
    id
    is_favorite
    updated_at
  }
}
```
