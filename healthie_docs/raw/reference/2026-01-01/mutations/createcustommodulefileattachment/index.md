---
title: createCustomModuleFileAttachment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustommodulefileattachment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustommodulefileattachment/index.md
---

Attach an already uploaded file to a form answer

## Arguments

[`input` ](#argument-input)· [`CreateCustomModuleFileAttachmentInput` ](/reference/2026-01-01/input-objects/createcustommodulefileattachmentinput)· Parameters for CreateCustomModuleFileAttachment

## Returns

[`CreateCustomModuleFileAttachmentPayload`](/reference/2026-01-01/objects/createcustommodulefileattachmentpayload)

## Example

```
mutation createCustomModuleFileAttachment(
  $input: CreateCustomModuleFileAttachmentInput
) {
  createCustomModuleFileAttachment(input: $input) {
    file_attachment
    messages
  }
}
```
