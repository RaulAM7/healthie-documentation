---
title: deleteWithingsConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletewithingsconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletewithingsconnection/index.md
---

Destroy Withings Connection

## Arguments

[`input` ](#argument-input)· [`deleteWithingsConnectionInput` ](/reference/2026-01-01/input-objects/deletewithingsconnectioninput)· Parameters for deleteWithingsConnection

## Returns

[`deleteWithingsConnectionPayload`](/reference/2026-01-01/objects/deletewithingsconnectionpayload)

## Example

```
mutation deleteWithingsConnection($input: deleteWithingsConnectionInput) {
  deleteWithingsConnection(input: $input) {
    messages
    withings_connection
  }
}
```
