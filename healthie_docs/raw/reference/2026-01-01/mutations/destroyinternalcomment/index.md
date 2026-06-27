---
title: destroyInternalComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/destroyinternalcomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/destroyinternalcomment/index.md
---

Destroy an internal comment on a task or other commentable object.

## Arguments

[`input` ](#argument-input)· [`DestroyInternalCommentInput` ](/reference/2026-01-01/input-objects/destroyinternalcommentinput)· Parameters for DestroyInternalComment

## Returns

[`DestroyInternalCommentPayload`](/reference/2026-01-01/objects/destroyinternalcommentpayload)

## Example

```
mutation destroyInternalComment($input: DestroyInternalCommentInput) {
  destroyInternalComment(input: $input) {
    internal_comment
    messages
  }
}
```
