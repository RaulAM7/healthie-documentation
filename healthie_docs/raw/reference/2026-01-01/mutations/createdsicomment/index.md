---
title: createDsiComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createdsicomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createdsicomment/index.md
---

Create a DSI comment

## Arguments

[`input` ](#argument-input)· [`createDsiCommentInput` ](/reference/2026-01-01/input-objects/createdsicommentinput)· Parameters for createDsiComment

## Returns

[`createDsiCommentPayload`](/reference/2026-01-01/objects/createdsicommentpayload)

## Example

```
mutation createDsiComment($input: createDsiCommentInput) {
  createDsiComment(input: $input) {
    dsi_comment
    messages
  }
}
```
