---
title: deleteComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecomment/index.md
---

Destroy a Comment

## Arguments

[`input` ](#argument-input)· [`deleteCommentInput` ](/reference/2026-01-01/input-objects/deletecommentinput)· Parameters for deleteComment

## Returns

[`deleteCommentPayload`](/reference/2026-01-01/objects/deletecommentpayload)

## Example

```
mutation deleteComment($input: deleteCommentInput) {
  deleteComment(input: $input) {
    comment
    messages
  }
}
```
