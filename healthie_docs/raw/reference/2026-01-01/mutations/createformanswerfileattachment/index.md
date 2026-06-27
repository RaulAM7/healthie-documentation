---
title: createFormAnswerFileAttachment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createformanswerfileattachment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createformanswerfileattachment/index.md
---

Attach an already uploaded file to a form answer

## Arguments

[`input` ](#argument-input)· [`createFormAnswerFileAttachmentInput` ](/reference/2026-01-01/input-objects/createformanswerfileattachmentinput)· Parameters for createFormAnswerFileAttachment

## Returns

[`createFormAnswerFileAttachmentPayload`](/reference/2026-01-01/objects/createformanswerfileattachmentpayload)

## Example

```
mutation createFormAnswerFileAttachment(
  $input: createFormAnswerFileAttachmentInput
) {
  createFormAnswerFileAttachment(input: $input) {
    file_attachment
    messages
  }
}
```
