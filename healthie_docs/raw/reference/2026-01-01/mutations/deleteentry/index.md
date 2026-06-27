---
title: deleteEntry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteentry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteentry/index.md
---

Destroy a Entry

## Arguments

[`input` ](#argument-input)· [`deleteEntryInput` ](/reference/2026-01-01/input-objects/deleteentryinput)· Parameters for deleteEntry

## Returns

[`deleteEntryPayload`](/reference/2026-01-01/objects/deleteentrypayload)

## Example

```
mutation deleteEntry($input: deleteEntryInput) {
  deleteEntry(input: $input) {
    entry
    messages
  }
}
```
