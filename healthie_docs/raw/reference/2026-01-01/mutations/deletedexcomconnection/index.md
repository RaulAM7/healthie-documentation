---
title: deleteDexcomConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletedexcomconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletedexcomconnection/index.md
---

Destroy Dexcom Connection

## Arguments

[`input` ](#argument-input)· [`deleteDexcomConnectionInput` ](/reference/2026-01-01/input-objects/deletedexcomconnectioninput)· Parameters for deleteDexcomConnection

## Returns

[`deleteDexcomConnectionPayload`](/reference/2026-01-01/objects/deletedexcomconnectionpayload)

## Example

```
mutation deleteDexcomConnection($input: deleteDexcomConnectionInput) {
  deleteDexcomConnection(input: $input) {
    dexcom_connection
    messages
  }
}
```
