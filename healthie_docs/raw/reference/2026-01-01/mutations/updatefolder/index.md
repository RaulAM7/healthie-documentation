---
title: updateFolder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefolder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefolder/index.md
---

Update a Folder and return Folder

## Arguments

[`input` ](#argument-input)· [`updateFolderInput` ](/reference/2026-01-01/input-objects/updatefolderinput)· Parameters for updateFolder

## Returns

[`updateFolderPayload`](/reference/2026-01-01/objects/updatefolderpayload)

## Example

```
mutation updateFolder($input: updateFolderInput) {
  updateFolder(input: $input) {
    folder
    messages
  }
}
```
