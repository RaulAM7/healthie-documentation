---
title: updateHealthConcern | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatehealthconcern/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatehealthconcern/index.md
---

Update a HealthConcern Object

## Arguments

[`input` ](#argument-input)· [`updateHealthConcernInput` ](/reference/2026-01-01/input-objects/updatehealthconcerninput)· Parameters for updateHealthConcern

## Returns

[`updateHealthConcernPayload`](/reference/2026-01-01/objects/updatehealthconcernpayload)

## Example

```
mutation updateHealthConcern($input: updateHealthConcernInput) {
  updateHealthConcern(input: $input) {
    health_concern
    messages
  }
}
```
