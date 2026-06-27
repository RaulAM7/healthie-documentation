---
title: completeCourseDocument | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/completecoursedocument/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/completecoursedocument/index.md
---

Create CompletedCourseItem for related document

## Arguments

[`input` ](#argument-input)· [`completeCourseDocumentInput` ](/reference/2026-01-01/input-objects/completecoursedocumentinput)· Parameters for completeCourseDocument

## Returns

[`completeCourseDocumentPayload`](/reference/2026-01-01/objects/completecoursedocumentpayload)

## Example

```
mutation completeCourseDocument($input: completeCourseDocumentInput) {
  completeCourseDocument(input: $input) {
    completedCourseItem
    messages
  }
}
```
