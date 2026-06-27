---
title: createNote | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createnote/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createnote/index.md
---

Create a note. Cannot create notes in conversations exceeding 256 members.

## Arguments

[`input` ](#argument-input)· [`createNoteInput!` ](/reference/2026-01-01/input-objects/createnoteinput)· required · Parameters for createNote

## Returns

[`createNotePayload`](/reference/2026-01-01/objects/createnotepayload)

## Example

```
mutation createNote($input: createNoteInput!) {
  createNote(input: $input) {
    messages
    note
  }
}
```
