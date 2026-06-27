---
title: deleteShapaConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteshapaconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteshapaconnection/index.md
---

Destroy Shapa Connection

## Arguments

[`input` ](#argument-input)· [`deleteShapaConnectionInput` ](/reference/2026-01-01/input-objects/deleteshapaconnectioninput)· Parameters for deleteShapaConnection

## Returns

[`deleteShapaConnectionPayload`](/reference/2026-01-01/objects/deleteshapaconnectionpayload)

## Example

```
mutation deleteShapaConnection($input: deleteShapaConnectionInput) {
  deleteShapaConnection(input: $input) {
    messages
    shapa_connection
  }
}
```
