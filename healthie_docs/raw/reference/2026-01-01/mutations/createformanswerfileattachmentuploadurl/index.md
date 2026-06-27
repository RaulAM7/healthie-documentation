---
title: createFormAnswerFileAttachmentUploadUrl | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createformanswerfileattachmentuploadurl/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createformanswerfileattachmentuploadurl/index.md
---

Create a pre-signed expiring upload URL for uploading a form answer file attachment.

## Arguments

[`input` ](#argument-input)· [`createFormAnswerFileAttachmentUploadUrlInput` ](/reference/2026-01-01/input-objects/createformanswerfileattachmentuploadurlinput)· Parameters for createFormAnswerFileAttachmentUploadUrl

## Returns

[`createFormAnswerFileAttachmentUploadUrlPayload`](/reference/2026-01-01/objects/createformanswerfileattachmentuploadurlpayload)

## Example

```
mutation createFormAnswerFileAttachmentUploadUrl(
  $input: createFormAnswerFileAttachmentUploadUrlInput
) {
  createFormAnswerFileAttachmentUploadUrl(input: $input) {
    headers
    messages
    upload_id
    upload_url
  }
}
```
