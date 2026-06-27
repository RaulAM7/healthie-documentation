---
title: deleteCarePlanConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecareplanconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecareplanconnection/index.md
---

Remove connection for related item(document/goal/recommendation)

## Arguments

[`input` ](#argument-input)· [`deleteCarePlanConnectionInput` ](/reference/2026-01-01/input-objects/deletecareplanconnectioninput)· Parameters for deleteCarePlanConnection

## Returns

[`deleteCarePlanConnectionPayload`](/reference/2026-01-01/objects/deletecareplanconnectionpayload)

## Example

```
mutation deleteCarePlanConnection($input: deleteCarePlanConnectionInput) {
  deleteCarePlanConnection(input: $input) {
    connection
    messages
  }
}
```
