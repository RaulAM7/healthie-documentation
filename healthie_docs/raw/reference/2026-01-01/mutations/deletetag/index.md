---
title: deleteTag | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletetag/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletetag/index.md
---

Delete a custom user tag

## Arguments

[`input` ](#argument-input)· [`deleteTagInput` ](/reference/2026-01-01/input-objects/deletetaginput)· Parameters for deleteTag

## Returns

[`deleteTagPayload`](/reference/2026-01-01/objects/deletetagpayload)

## Example

```
mutation deleteTag($input: deleteTagInput) {
  deleteTag(input: $input) {
    messages
    removing_async
    tag
  }
}
```
