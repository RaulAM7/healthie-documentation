---
title: createHealthConcern | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createhealthconcern/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createhealthconcern/index.md
---

Create a HealthConcern Object

## Arguments

[`input` ](#argument-input)· [`createHealthConcernInput` ](/reference/2026-01-01/input-objects/createhealthconcerninput)· Parameters for createHealthConcern

## Returns

[`createHealthConcernPayload`](/reference/2026-01-01/objects/createhealthconcernpayload)

## Example

```
mutation createHealthConcern($input: createHealthConcernInput) {
  createHealthConcern(input: $input) {
    health_concern
    messages
  }
}
```
