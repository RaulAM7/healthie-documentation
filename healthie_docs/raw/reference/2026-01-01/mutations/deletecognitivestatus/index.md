---
title: deleteCognitiveStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecognitivestatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecognitivestatus/index.md
---

Delete a CognitivesStatus Object

## Arguments

[`input` ](#argument-input)· [`deleteCognitiveStatusInput` ](/reference/2026-01-01/input-objects/deletecognitivestatusinput)· Parameters for deleteCognitiveStatus

## Returns

[`deleteCognitiveStatusPayload`](/reference/2026-01-01/objects/deletecognitivestatuspayload)

## Example

```
mutation deleteCognitiveStatus($input: deleteCognitiveStatusInput) {
  deleteCognitiveStatus(input: $input) {
    cognitive_status
    messages
  }
}
```
