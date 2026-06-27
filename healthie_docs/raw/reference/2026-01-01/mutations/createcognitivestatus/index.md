---
title: createCognitiveStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcognitivestatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcognitivestatus/index.md
---

Create a CognitiveStatus Object

## Arguments

[`input` ](#argument-input)· [`createCognitiveStatusInput` ](/reference/2026-01-01/input-objects/createcognitivestatusinput)· Parameters for createCognitiveStatus

## Returns

[`createCognitiveStatusPayload`](/reference/2026-01-01/objects/createcognitivestatuspayload)

## Example

```
mutation createCognitiveStatus($input: createCognitiveStatusInput) {
  createCognitiveStatus(input: $input) {
    cognitive_status
    messages
  }
}
```
