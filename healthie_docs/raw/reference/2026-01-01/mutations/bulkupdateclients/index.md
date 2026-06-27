---
title: bulkUpdateClients | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkupdateclients/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkupdateclients/index.md
---

Update multiple clients at once. Will change user group for multiple clients if user\_group\_id passed, otherwise clients will be archived

## Arguments

[`input` ](#argument-input)· [`bulkUpdateClientsInput` ](/reference/2026-01-01/input-objects/bulkupdateclientsinput)· Parameters for bulkUpdateClients

## Returns

[`bulkUpdateClientsPayload`](/reference/2026-01-01/objects/bulkupdateclientspayload)

## Example

```
mutation bulkUpdateClients($input: bulkUpdateClientsInput) {
  bulkUpdateClients(input: $input) {
    messages
    users
  }
}
```
