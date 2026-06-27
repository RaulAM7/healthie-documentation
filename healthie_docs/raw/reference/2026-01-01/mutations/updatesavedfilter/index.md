---
title: updateSavedFilter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesavedfilter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesavedfilter/index.md
---

Update an existing saved filter

## Arguments

[`input` ](#argument-input)· [`updateSavedFilterInput` ](/reference/2026-01-01/input-objects/updatesavedfilterinput)· Parameters for updateSavedFilter

## Returns

[`updateSavedFilterPayload`](/reference/2026-01-01/objects/updatesavedfilterpayload)

## Example

```
mutation updateSavedFilter($input: updateSavedFilterInput) {
  updateSavedFilter(input: $input) {
    messages
    savedFilter
  }
}
```
