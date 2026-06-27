---
title: task | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/task/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/task/index.md
---

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Task`](/reference/2026-01-01/objects/task)

## Example

```
query task($id: ID) {
  task(id: $id) {
    assignees
    client
    client_id
    comments
    complete
    completed_at
    completed_by
    completed_by_id
    content
    created_at
    created_by_generator_id
    created_by_id
    creator
    due_date
    hidden
    id
    metadata
    note
    note_path
    position
    priority
    ref_source
    reminder
    seen
    smart
    smart_category
    updated_at
    user
    user_id
  }
}
```
