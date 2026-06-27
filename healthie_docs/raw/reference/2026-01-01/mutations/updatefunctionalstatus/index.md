---
title: updateFunctionalStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefunctionalstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefunctionalstatus/index.md
---

Update a FunctionalStatus Object

## Arguments

[`input` ](#argument-input)· [`updateFunctionalStatusInput` ](/reference/2026-01-01/input-objects/updatefunctionalstatusinput)· Parameters for updateFunctionalStatus

## Returns

[`updateFunctionalStatusPayload`](/reference/2026-01-01/objects/updatefunctionalstatuspayload)

## Example

```
mutation updateFunctionalStatus($input: updateFunctionalStatusInput) {
  updateFunctionalStatus(input: $input) {
    functional_status
    messages
  }
}
```
