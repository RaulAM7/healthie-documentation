---
title: shareAnswersAsDocument | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/shareanswersasdocument/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/shareanswersasdocument/index.md
---

Add form answer group answers as document viewable by client

## Arguments

[`input` ](#argument-input)· [`shareAnswersAsDocumentInput` ](/reference/2026-01-01/input-objects/shareanswersasdocumentinput)· Parameters for shareAnswersAsDocument

## Returns

[`shareAnswersAsDocumentPayload`](/reference/2026-01-01/objects/shareanswersasdocumentpayload)

## Example

```
mutation shareAnswersAsDocument($input: shareAnswersAsDocumentInput) {
  shareAnswersAsDocument(input: $input) {
    document
    messages
  }
}
```
