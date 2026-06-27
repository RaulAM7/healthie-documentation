---
title: createFunctionalStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfunctionalstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfunctionalstatus/index.md
---

Create a FunctionalStatus Object

## Arguments

[`input` ](#argument-input)· [`createFunctionalStatusInput` ](/reference/2026-01-01/input-objects/createfunctionalstatusinput)· Parameters for createFunctionalStatus

## Returns

[`createFunctionalStatusPayload`](/reference/2026-01-01/objects/createfunctionalstatuspayload)

## Example

```
mutation createFunctionalStatus($input: createFunctionalStatusInput) {
  createFunctionalStatus(input: $input) {
    functional_status
    messages
  }
}
```
