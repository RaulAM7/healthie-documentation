---
title: mergeClients | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/mergeclients/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/mergeclients/index.md
---

all data related to the merging account (form answers, billing items, charting notes, etc) will be associated with the selected account after merging. The selected account's client profile information will remain unchanged (name, DOB, etc)

## Arguments

[`input` ](#argument-input)· [`mergeClientsInput` ](/reference/2026-01-01/input-objects/mergeclientsinput)· Parameters for mergeClients

## Returns

[`mergeClientsPayload`](/reference/2026-01-01/objects/mergeclientspayload)

## Example

```
mutation mergeClients($input: mergeClientsInput) {
  mergeClients(input: $input) {
    messages
    user
  }
}
```
