---
title: createDocument | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createdocument/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createdocument/index.md
---

create Document

## Arguments

[`input` ](#argument-input)· [`createDocumentInput` ](/reference/2026-01-01/input-objects/createdocumentinput)· Parameters for createDocument

## Returns

[`createDocumentPayload`](/reference/2026-01-01/objects/createdocumentpayload)

## Example

```
mutation createDocument($input: createDocumentInput) {
  createDocument(input: $input) {
    currentUser
    document
    messages
  }
}
```
