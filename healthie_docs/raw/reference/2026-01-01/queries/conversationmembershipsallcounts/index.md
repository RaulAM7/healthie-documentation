---
title: conversationMembershipsAllCounts | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/conversationmembershipsallcounts/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/conversationmembershipsallcounts/index.md
---

All conversation membership tab counts in a single query

## Arguments

[`client_id` ](#argument-client-id)· [`String` ](/reference/2026-01-01/scalars/string)· Filter conversations by client user ID

[`conversation_type` ](#argument-conversation-type)· [`String` ](/reference/2026-01-01/scalars/string)· Filter by conversation type: all, individual, or community

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Search conversations by keyword

[`only_include_shared_memberships` ](#argument-only-include-shared-memberships)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true with client\_id, only returns client messages that are shared with the provider

[`org_chat` ](#argument-org-chat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If TRUE: count organization members conversations

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the provider to get conversation for (if nil, will return current users)

[`provider_ids` ](#argument-provider-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Used to filter org chat conversations by provider ids

[`read_status` ](#argument-read-status)· [`String` ](/reference/2026-01-01/scalars/string)· Filter by read status: all, read, or unread

## Returns

[`ConversationMembershipsAllCounts`](/reference/2026-01-01/objects/conversationmembershipsallcounts)

## Example

```
query conversationMembershipsAllCounts(
  $client_id: String
  $conversation_type: String
  $keywords: String
  $only_include_shared_memberships: Boolean
  $org_chat: Boolean
  $provider_id: ID
  $provider_ids: [ID]
  $read_status: String
) {
  conversationMembershipsAllCounts(
    client_id: $client_id
    conversation_type: $conversation_type
    keywords: $keywords
    only_include_shared_memberships: $only_include_shared_memberships
    org_chat: $org_chat
    provider_id: $provider_id
    provider_ids: $provider_ids
    read_status: $read_status
  ) {
    active_count
    archived_count
    closed_count
    scheduled_count
  }
}
```
