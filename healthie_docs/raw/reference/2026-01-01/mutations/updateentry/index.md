---
title: updateEntry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateentry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateentry/index.md
---

Updates an Entry and returns an Entry

## Arguments

[`input` ](#argument-input)· [`updateEntryInput` ](/reference/2026-01-01/input-objects/updateentryinput)· Parameters for updateEntry

## Returns

[`updateEntryPayload`](/reference/2026-01-01/objects/updateentrypayload)

## Example

```
mutation updateEntry($input: updateEntryInput) {
  updateEntry(input: $input) {
    entry
    messages
  }
}
```
