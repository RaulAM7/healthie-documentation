---
title: deleteSavedFilter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesavedfilter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesavedfilter/index.md
---

Delete a saved filter

## Arguments

[`input` ](#argument-input)· [`deleteSavedFilterInput` ](/reference/2026-01-01/input-objects/deletesavedfilterinput)· Parameters for deleteSavedFilter

## Returns

[`deleteSavedFilterPayload`](/reference/2026-01-01/objects/deletesavedfilterpayload)

## Example

```
mutation deleteSavedFilter($input: deleteSavedFilterInput) {
  deleteSavedFilter(input: $input) {
    messages
    savedFilter
  }
}
```
