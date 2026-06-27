---
title: plan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/plan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/plan/index.md
---

fetch a Plan by id (considered public)

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Plan`](/reference/2026-01-01/objects/plan)

## Example

```
query plan($id: ID) {
  plan(id: $id) {
    features
    header
    id
    subheader
  }
}
```
