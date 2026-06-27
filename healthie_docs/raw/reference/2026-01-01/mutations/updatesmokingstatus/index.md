---
title: updateSmokingStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesmokingstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesmokingstatus/index.md
---

Update a Smoking Status

## Arguments

[`input` ](#argument-input)· [`updateSmokingStatusInput` ](/reference/2026-01-01/input-objects/updatesmokingstatusinput)· Parameters for updateSmokingStatus

## Returns

[`updateSmokingStatusPayload`](/reference/2026-01-01/objects/updatesmokingstatuspayload)

## Example

```
mutation updateSmokingStatus($input: updateSmokingStatusInput) {
  updateSmokingStatus(input: $input) {
    messages
    smokingStatus
  }
}
```
