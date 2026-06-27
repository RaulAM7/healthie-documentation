---
title: createComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcomment/index.md
---

create Comment

## Arguments

[`input` ](#argument-input)· [`createCommentInput!` ](/reference/2026-01-01/input-objects/createcommentinput)· required · Parameters for createComment

## Returns

[`createCommentPayload`](/reference/2026-01-01/objects/createcommentpayload)

## Example

```
mutation createComment($input: createCommentInput!) {
  createComment(input: $input) {
    comment
    messages
  }
}
```
