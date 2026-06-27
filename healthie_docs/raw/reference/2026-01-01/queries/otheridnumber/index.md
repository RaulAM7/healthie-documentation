---
title: otherIdNumber | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/otheridnumber/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/otheridnumber/index.md
---

fetch an Other Id Number by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`OtherIdNumber`](/reference/2026-01-01/objects/otheridnumber)

## Example

```
query otherIdNumber($id: ID) {
  otherIdNumber(id: $id) {
    id
    label
    organization
    organization_id
    other_id
    other_id_qualifier
    user_id
  }
}
```
