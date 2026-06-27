---
title: deleteDocument | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletedocument/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletedocument/index.md
---

Destroy a Document

## Arguments

[`input` ](#argument-input)· [`deleteDocumentInput` ](/reference/2026-01-01/input-objects/deletedocumentinput)· Parameters for deleteDocument

## Returns

[`deleteDocumentPayload`](/reference/2026-01-01/objects/deletedocumentpayload)

## Example

```
mutation deleteDocument($input: deleteDocumentInput) {
  deleteDocument(input: $input) {
    document
    messages
  }
}
```
