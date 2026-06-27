---
title: createSavedFilter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsavedfilter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsavedfilter/index.md
---

Create a new saved filter

## Arguments

[`input` ](#argument-input)· [`createSavedFilterInput` ](/reference/2026-01-01/input-objects/createsavedfilterinput)· Parameters for createSavedFilter

## Returns

[`createSavedFilterPayload`](/reference/2026-01-01/objects/createsavedfilterpayload)

## Example

```
mutation createSavedFilter($input: createSavedFilterInput) {
  createSavedFilter(input: $input) {
    messages
    savedFilter
  }
}
```
