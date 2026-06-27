---
title: createFolder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfolder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfolder/index.md
---

create Folder

## Arguments

[`input` ](#argument-input)· [`createFolderInput` ](/reference/2026-01-01/input-objects/createfolderinput)· Parameters for createFolder

## Returns

[`createFolderPayload`](/reference/2026-01-01/objects/createfolderpayload)

## Example

```
mutation createFolder($input: createFolderInput) {
  createFolder(input: $input) {
    folder
    messages
  }
}
```
