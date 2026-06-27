---
title: note_scheduler | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/note-scheduler/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/note-scheduler/index.md
---

Fetch note scheduler by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`NoteScheduler`](/reference/2026-01-01/objects/notescheduler)

## Example

```
query note_scheduler($id: ID) {
  note_scheduler(id: $id) {
    first_four_invitees
    id
    invitees
    invitees_count
    last_task
    note
    note_content
    participant_ids
    selected_user_groups
    selected_users
    updated_at
    user
  }
}
```
