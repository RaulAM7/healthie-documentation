---
title: conversation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/conversation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/conversation/index.md
---

fetch a conversation by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· (DEPRECATED - NO LONGER NEEDED) ID of the provider to get conversation for (if nil, will return current users)

## Returns

[`Conversation`](/reference/2026-01-01/objects/conversation)

## Example

```
query conversation($id: ID, $provider_id: ID) {
  conversation(id: $id, provider_id: $provider_id) {
    closed_by
    closed_date
    community_chat
    community_chat_prefix
    conversation_memberships
    conversation_memberships_count
    created_at
    current_user_conversation_membership
    dietitian_id
    first_four_invitees
    id
    includes_multiple_clients
    invitees
    is_hidden_for_client
    last_message_content
    last_note_viewed_id
    metadata
    name
    notes
    owner
    patient_id
    updated_at
    user_groups
  }
}
```
