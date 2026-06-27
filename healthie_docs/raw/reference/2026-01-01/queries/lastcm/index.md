---
title: lastCM | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/lastcm/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/lastcm/index.md
---

Fetch most recent conversationMembership

## Arguments

[`active_status` ](#argument-active-status)· [`String`](/reference/2026-01-01/scalars/string)

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the provider to get conversation for (if nil, will return current users)

## Returns

[`ConversationMembership`](/reference/2026-01-01/objects/conversationmembership)

## Example

```
query lastCM($active_status: String, $provider_id: ID) {
  lastCM(active_status: $active_status, provider_id: $provider_id) {
    archived
    conversation_id
    conversation_role
    convo
    convo_updated_at
    created_at
    creator
    display_avatar
    display_name
    display_name_and_initial
    display_other_user_first_name
    display_other_user_name
    id
    last_task
    updated_at
    user_id
    user_list_as_display_name
    viewed
  }
}
```
