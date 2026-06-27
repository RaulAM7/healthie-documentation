---
title: updateDsiComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatedsicomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatedsicomment/index.md
---

Update a DSI comment

## Arguments

[`input` ](#argument-input)· [`updateDsiCommentInput` ](/reference/2026-01-01/input-objects/updatedsicommentinput)· Parameters for updateDsiComment

## Returns

[`updateDsiCommentPayload`](/reference/2026-01-01/objects/updatedsicommentpayload)

## Example

```
mutation updateDsiComment($input: updateDsiCommentInput) {
  updateDsiComment(input: $input) {
    dsi_comment
    messages
  }
}
```
