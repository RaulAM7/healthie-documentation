---
title: writeOff | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/writeoff/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/writeoff/index.md
---

Fetch Write Off by ID

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the Write Off

## Returns

[`WriteOff`](/reference/2026-01-01/objects/writeoff)

## Example

```
query writeOff($id: ID!) {
  writeOff(id: $id) {
    amount
    id
    other_reason
    requested_payment
    write_off_type
  }
}
```
