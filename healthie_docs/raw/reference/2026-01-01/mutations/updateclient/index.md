---
title: updateClient | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateclient/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateclient/index.md
---

Update Client

## Arguments

[`input` ](#argument-input)· [`updateClientInput!` ](/reference/2026-01-01/input-objects/updateclientinput)· required · Parameters for updateClient

## Returns

[`updateClientPayload`](/reference/2026-01-01/objects/updateclientpayload)

## Example

```
mutation updateClient($input: updateClientInput!) {
  updateClient(input: $input) {
    messages
    user
  }
}
```
