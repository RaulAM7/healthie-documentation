---
title: deleteHealthConcern | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletehealthconcern/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletehealthconcern/index.md
---

Delete a HealthConcern Object

## Arguments

[`input` ](#argument-input)· [`deleteHealthConcernInput` ](/reference/2026-01-01/input-objects/deletehealthconcerninput)· Parameters for deleteHealthConcern

## Returns

[`deleteHealthConcernPayload`](/reference/2026-01-01/objects/deletehealthconcernpayload)

## Example

```
mutation deleteHealthConcern($input: deleteHealthConcernInput) {
  deleteHealthConcern(input: $input) {
    health_concern
    messages
  }
}
```
