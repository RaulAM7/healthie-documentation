---
title: createSmokingStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsmokingstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsmokingstatus/index.md
---

Create a Smoking Status

## Arguments

[`input` ](#argument-input)· [`createSmokingStatusInput` ](/reference/2026-01-01/input-objects/createsmokingstatusinput)· Parameters for createSmokingStatus

## Returns

[`createSmokingStatusPayload`](/reference/2026-01-01/objects/createsmokingstatuspayload)

## Example

```
mutation createSmokingStatus($input: createSmokingStatusInput) {
  createSmokingStatus(input: $input) {
    messages
    smokingStatus
  }
}
```
