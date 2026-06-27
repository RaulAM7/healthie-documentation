---
title: deleteCustomModuleFileAttachment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustommodulefileattachment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustommodulefileattachment/index.md
---

Delete a CustomModule file attachment. If the underlying blob is shared by other attachments, only the attachment record is removed. Otherwise, the blob is purged from storage. Requires edit permissions on the CustomModule.

## Arguments

[`input` ](#argument-input)· [`DeleteCustomModuleFileAttachmentInput` ](/reference/2026-01-01/input-objects/deletecustommodulefileattachmentinput)· Parameters for DeleteCustomModuleFileAttachment

## Returns

[`DeleteCustomModuleFileAttachmentPayload`](/reference/2026-01-01/objects/deletecustommodulefileattachmentpayload)

## Example

```
mutation deleteCustomModuleFileAttachment(
  $input: DeleteCustomModuleFileAttachmentInput
) {
  deleteCustomModuleFileAttachment(input: $input) {
    file_attachment
    messages
  }
}
```
