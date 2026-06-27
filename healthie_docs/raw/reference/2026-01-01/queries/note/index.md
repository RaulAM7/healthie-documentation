---
title: note | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/note/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/note/index.md
---

fetch a note by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Note`](/reference/2026-01-01/objects/note)

## Example

```
query note($id: ID) {
  note(id: $id) {
    attached_audio_url
    attached_image_url
    content
    conversation_id
    created_at
    creator
    creator_display_name
    deleted_by_user
    document_id
    document_name
    id
    image_name
    is_autoresponse
    on_behalf_user
    scheduled_at
    scheduled_conversation_id
    task
    updated_at
    user_id
    viewed
  }
}
```
