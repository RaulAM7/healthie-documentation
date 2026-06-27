---
title: createEbook | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createebook/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createebook/index.md
---

create ebook

## Arguments

[`input` ](#argument-input)· [`createEbookInput` ](/reference/2026-01-01/input-objects/createebookinput)· Parameters for createEbook

## Returns

[`createEbookPayload`](/reference/2026-01-01/objects/createebookpayload)

## Example

```
mutation createEbook($input: createEbookInput) {
  createEbook(input: $input) {
    messages
    visitor
  }
}
```
