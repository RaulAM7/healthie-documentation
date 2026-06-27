---
title: deleteFormAnswerFileAttachment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteformanswerfileattachment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteformanswerfileattachment/index.md
---

Delete a FormAnswer file attachment

## Arguments

[`input` ](#argument-input)· [`deleteFormAnswerFileAttachmentInput` ](/reference/2026-01-01/input-objects/deleteformanswerfileattachmentinput)· Parameters for deleteFormAnswerFileAttachment

## Returns

[`deleteFormAnswerFileAttachmentPayload`](/reference/2026-01-01/objects/deleteformanswerfileattachmentpayload)

## Example

```
mutation deleteFormAnswerFileAttachment(
  $input: deleteFormAnswerFileAttachmentInput
) {
  deleteFormAnswerFileAttachment(input: $input) {
    file_attachment
    messages
  }
}
```
