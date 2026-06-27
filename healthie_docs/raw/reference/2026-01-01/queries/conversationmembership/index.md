---
title: conversationMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/conversationmembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/conversationmembership/index.md
---

fetch a conversation membership by id

## Arguments

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the conversation, will return the membership object for the conversation owner

[`conversation_membership_id` ](#argument-conversation-membership-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the conversation membership, must have access to the conversation to use

## Returns

[`ConversationMembership`](/reference/2026-01-01/objects/conversationmembership)

## Example

```
query conversationMembership($id: ID, $conversation_membership_id: ID) {
  conversationMembership(
    id: $id
    conversation_membership_id: $conversation_membership_id
  ) {
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
