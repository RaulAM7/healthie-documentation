---
title: updateCognitiveStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecognitivestatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecognitivestatus/index.md
---

Update a CognitiveStatus Object

## Arguments

[`input` ](#argument-input)· [`updateCognitiveStatusInput` ](/reference/2026-01-01/input-objects/updatecognitivestatusinput)· Parameters for updateCognitiveStatus

## Returns

[`updateCognitiveStatusPayload`](/reference/2026-01-01/objects/updatecognitivestatuspayload)

## Example

```
mutation updateCognitiveStatus($input: updateCognitiveStatusInput) {
  updateCognitiveStatus(input: $input) {
    cognitive_status
    messages
  }
}
```
