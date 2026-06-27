---
title: bulkCreateEntries | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkcreateentries/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkcreateentries/index.md
---

creates bulk Entries (intended for apple health only for the time being)

## Arguments

[`input` ](#argument-input)· [`bulkCreateEntriesInput` ](/reference/2026-01-01/input-objects/bulkcreateentriesinput)· Parameters for bulkCreateEntries

## Returns

[`bulkCreateEntriesPayload`](/reference/2026-01-01/objects/bulkcreateentriespayload)

## Example

```
mutation bulkCreateEntries($input: bulkCreateEntriesInput) {
  bulkCreateEntries(input: $input) {
    entries
    messages
  }
}
```
