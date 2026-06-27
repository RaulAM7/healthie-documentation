---
title: updateNote | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenote/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenote/index.md
---

Update a Note

## Arguments

[`input` ](#argument-input)· [`updateNoteInput` ](/reference/2026-01-01/input-objects/updatenoteinput)· Parameters for updateNote

## Returns

[`updateNotePayload`](/reference/2026-01-01/objects/updatenotepayload)

## Example

```
mutation updateNote($input: updateNoteInput) {
  updateNote(input: $input) {
    messages
    note
  }
}
```
