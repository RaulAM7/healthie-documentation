---
title: createCustomModuleFileAttachmentUploadUrl | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustommodulefileattachmentuploadurl/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustommodulefileattachmentuploadurl/index.md
---

Create a pre-signed expiring upload URL for uploading a custom module file attachment.

## Arguments

[`input` ](#argument-input)· [`CreateCustomModuleFileAttachmentUploadUrlInput` ](/reference/2026-01-01/input-objects/createcustommodulefileattachmentuploadurlinput)· Parameters for CreateCustomModuleFileAttachmentUploadUrl

## Returns

[`CreateCustomModuleFileAttachmentUploadUrlPayload`](/reference/2026-01-01/objects/createcustommodulefileattachmentuploadurlpayload)

## Example

```
mutation createCustomModuleFileAttachmentUploadUrl(
  $input: CreateCustomModuleFileAttachmentUploadUrlInput
) {
  createCustomModuleFileAttachmentUploadUrl(input: $input) {
    headers
    messages
    upload_id
    upload_url
  }
}
```
