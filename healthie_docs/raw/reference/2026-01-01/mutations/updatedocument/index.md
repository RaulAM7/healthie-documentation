---
title: updateDocument | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatedocument/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatedocument/index.md
---

Update a Document and return Document

## Arguments

[`input` ](#argument-input)· [`updateDocumentInput` ](/reference/2026-01-01/input-objects/updatedocumentinput)· Parameters for updateDocument

## Returns

[`updateDocumentPayload`](/reference/2026-01-01/objects/updatedocumentpayload)

## Example

```
mutation updateDocument($input: updateDocumentInput) {
  updateDocument(input: $input) {
    document
    messages
  }
}
```
