---
title: shareable | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/shareable/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/shareable/index.md
---

A document or folder that can be shared with users or groups

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the shareable record

[`shareable_type` ](#argument-shareable-type)· [`ShareableType!` ](/reference/2026-01-01/enums/shareabletype)· required · The type of shareable record (document or folder)

## Returns

[`Shareable`](/reference/2026-01-01/unions/shareable)

## Example

```
query shareable($id: ID!, $shareable_type: ShareableType!) {
  shareable(id: $id, shareable_type: $shareable_type)
}
```
