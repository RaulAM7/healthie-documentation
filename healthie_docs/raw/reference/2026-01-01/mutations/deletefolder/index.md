---
title: deleteFolder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefolder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefolder/index.md
---

Destroy a Folder

## Arguments

[`input` ](#argument-input)· [`deleteFolderInput` ](/reference/2026-01-01/input-objects/deletefolderinput)· Parameters for deleteFolder

## Returns

[`deleteFolderPayload`](/reference/2026-01-01/objects/deletefolderpayload)

## Example

```
mutation deleteFolder($input: deleteFolderInput) {
  deleteFolder(input: $input) {
    folder
    messages
  }
}
```
