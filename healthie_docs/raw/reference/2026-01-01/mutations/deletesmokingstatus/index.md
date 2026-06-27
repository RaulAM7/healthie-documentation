---
title: deleteSmokingStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesmokingstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesmokingstatus/index.md
---

Delete a Smoking Status

## Arguments

[`input` ](#argument-input)· [`deleteSmokingStatusInput` ](/reference/2026-01-01/input-objects/deletesmokingstatusinput)· Parameters for deleteSmokingStatus

## Returns

[`deleteSmokingStatusPayload`](/reference/2026-01-01/objects/deletesmokingstatuspayload)

## Example

```
mutation deleteSmokingStatus($input: deleteSmokingStatusInput) {
  deleteSmokingStatus(input: $input) {
    messages
    smokingStatus
  }
}
```
