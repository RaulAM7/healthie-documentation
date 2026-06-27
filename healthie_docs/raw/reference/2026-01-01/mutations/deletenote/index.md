---
title: deleteNote | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletenote/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletenote/index.md
---

Destroy a Note

## Arguments

[`input` ](#argument-input)· [`deleteNoteInput` ](/reference/2026-01-01/input-objects/deletenoteinput)· Parameters for deleteNote

## Returns

[`deleteNotePayload`](/reference/2026-01-01/objects/deletenotepayload)

## Example

```
mutation deleteNote($input: deleteNoteInput) {
  deleteNote(input: $input) {
    messages
    note
  }
}
```
