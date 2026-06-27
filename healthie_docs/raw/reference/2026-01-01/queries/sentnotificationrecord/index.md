---
title: sentNotificationRecord | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sentnotificationrecord/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sentnotificationrecord/index.md
---

Fetch a single notification record by ID.

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the sent notification record to return.

## Returns

[`SentNotificationRecord`](/reference/2026-01-01/objects/sentnotificationrecord)

## Example

```
query sentNotificationRecord($id: ID!) {
  sentNotificationRecord(id: $id) {
    category
    created_at
    delivery_status
    id
    notification_description
    notification_type
    representation_type
    user_id
  }
}
```
