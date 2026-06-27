---
title: createClient | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createclient/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createclient/index.md
---

Create a Client

## Arguments

[`input` ](#argument-input)· [`createClientInput` ](/reference/2026-01-01/input-objects/createclientinput)· Parameters for createClient

## Returns

[`createClientPayload`](/reference/2026-01-01/objects/createclientpayload)

## Example

```
mutation createClient($input: createClientInput) {
  createClient(input: $input) {
    messages
    user
  }
}
```
