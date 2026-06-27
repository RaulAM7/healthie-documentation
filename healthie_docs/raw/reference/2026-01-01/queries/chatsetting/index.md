---
title: chatSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/chatsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/chatsetting/index.md
---

fetch a Chat Setting

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user to fetch the chat setting for

## Returns

[`ChatSetting`](/reference/2026-01-01/objects/chatsetting)

## Example

```
query chatSetting($id: ID, $user_id: ID) {
  chatSetting(id: $id, user_id: $user_id) {
    auto_welcome_text
    content
    end_date
    hide_close_confirmation
    hide_org_chat_confirmation
    id
    is_active
    is_recurring_active
    no_end_date
    receive_notifications
    receive_notifications_recurring
    recurring_all_day
    recurring_content
    recurring_days_data
    recurring_end_time
    recurring_friday
    recurring_monday
    recurring_saturday
    recurring_start_time
    recurring_sunday
    recurring_thursday
    recurring_tuesday
    recurring_turned_on
    recurring_wednesday
    scheduled_turned_on
    send_auto_welcome
    start_date
    user_id
  }
}
```
