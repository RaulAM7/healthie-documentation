---
title: formTypesToRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/formtypestorequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/formtypestorequest/index.md
---

Fetch available forms to request

## Arguments

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`[FormTypesToRequest!]`](/reference/2026-01-01/objects/formtypestorequest)

## Example

```
query formTypesToRequest($keywords: String, $sort_by: String) {
  formTypesToRequest(keywords: $keywords, sort_by: $sort_by) {
    id
    is_video
    item_type
    name
  }
}
```
