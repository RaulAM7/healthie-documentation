---
title: announcement | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/announcement/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/announcement/index.md
---

Fetch an announcement

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Announcement`](/reference/2026-01-01/objects/announcement)

## Example

```
query announcement($id: ID) {
  announcement(id: $id) {
    active
    announcement_image_name
    announcement_image_url
    description
    id
    last_toggled_at
    last_toggled_by
    name
    title
    user
    user_group_ids
    user_group_names
  }
}
```
