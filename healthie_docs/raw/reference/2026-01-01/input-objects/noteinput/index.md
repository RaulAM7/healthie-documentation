---
title: NoteInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/noteinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/noteinput/index.md
---

Payload for a note

## Fields

[`attached_document` ](#field-attached-document)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The document attached to the note

[`attached_image` ](#field-attached-image)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The image attached to the note

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· The content of the note

## Used By

[`createConversationInput.note`](/reference/2026-01-01/input-objects/createconversationinput)

[`createMessageBlastInput.note`](/reference/2026-01-01/input-objects/createmessageblastinput)

## Definition

```
"""
Payload for a note
"""
input NoteInput {
  """
  The document attached to the note
  """
  attached_document: Upload


  """
  The image attached to the note
  """
  attached_image: Upload


  """
  The content of the note
  """
  content: String
}
```
