---
title: deleteFunctionalStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefunctionalstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefunctionalstatus/index.md
---

Delete a FunctionalStatus Object

## Arguments

[`input` ](#argument-input)· [`deleteFunctionalStatusInput` ](/reference/2026-01-01/input-objects/deletefunctionalstatusinput)· Parameters for deleteFunctionalStatus

## Returns

[`deleteFunctionalStatusPayload`](/reference/2026-01-01/objects/deletefunctionalstatuspayload)

## Example

```
mutation deleteFunctionalStatus($input: deleteFunctionalStatusInput) {
  deleteFunctionalStatus(input: $input) {
    functional_status
    messages
  }
}
```
