---
title: createEntry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createentry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createentry/index.md
---

creates a new Entry

## Arguments

[`input` ](#argument-input)· [`createEntryInput` ](/reference/2026-01-01/input-objects/createentryinput)· Parameters for createEntry

## Returns

[`createEntryPayload`](/reference/2026-01-01/objects/createentrypayload)

## Example

```
mutation createEntry($input: createEntryInput) {
  createEntry(input: $input) {
    entry
    messages
  }
}
```
