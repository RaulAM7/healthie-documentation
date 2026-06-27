---
title: createTag | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createtag/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createtag/index.md
---

Create a custom user tag

## Arguments

[`input` ](#argument-input)· [`createTagInput` ](/reference/2026-01-01/input-objects/createtaginput)· Parameters for createTag

## Returns

[`createTagPayload`](/reference/2026-01-01/objects/createtagpayload)

## Example

```
mutation createTag($input: createTagInput) {
  createTag(input: $input) {
    messages
    tag
  }
}
```
