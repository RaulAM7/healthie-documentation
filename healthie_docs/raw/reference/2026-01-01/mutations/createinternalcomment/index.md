---
title: createInternalComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createinternalcomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createinternalcomment/index.md
---

Create an internal comment on a task or other commentable object.

## Arguments

[`input` ](#argument-input)· [`CreateInternalCommentInput` ](/reference/2026-01-01/input-objects/createinternalcommentinput)· Parameters for CreateInternalComment

## Returns

[`CreateInternalCommentPayload`](/reference/2026-01-01/objects/createinternalcommentpayload)

## Example

```
mutation createInternalComment($input: CreateInternalCommentInput) {
  createInternalComment(input: $input) {
    internal_comment
    messages
  }
}
```
