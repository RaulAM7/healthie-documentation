---
title: updateInternalComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateinternalcomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateinternalcomment/index.md
---

Update an internal comment on a task or other commentable object. Only usable by the comment author.

## Arguments

[`input` ](#argument-input)· [`UpdateInternalCommentInput` ](/reference/2026-01-01/input-objects/updateinternalcommentinput)· Parameters for UpdateInternalComment

## Returns

[`UpdateInternalCommentPayload`](/reference/2026-01-01/objects/updateinternalcommentpayload)

## Example

```
mutation updateInternalComment($input: UpdateInternalCommentInput) {
  updateInternalComment(input: $input) {
    internal_comment
    messages
  }
}
```
