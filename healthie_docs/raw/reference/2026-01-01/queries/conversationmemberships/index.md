---
title: conversationMemberships | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/conversationmemberships/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/conversationmemberships/index.md
---

Fetch paginated conversation memberships collection

## Arguments

[`active_status` ](#argument-active-status)· [`String`](/reference/2026-01-01/scalars/string)

[`client_id` ](#argument-client-id)· [`String`](/reference/2026-01-01/scalars/string)

[`conversation_type` ](#argument-conversation-type)· [`String`](/reference/2026-01-01/scalars/string)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`notes_type` ](#argument-notes-type)· [`String`](/reference/2026-01-01/scalars/string)

[`only_include_shared_memberships` ](#argument-only-include-shared-memberships)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true with client\_id, only returns client messages that are shared with the provider

[`org_chat` ](#argument-org-chat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If TRUE: fetch organization members conversations

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the provider to get conversation for (if nil, will return current users)

[`provider_ids` ](#argument-provider-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Used to filter org chat conversations by provider ids

[`read_status` ](#argument-read-status)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`ConversationMembershipOrderKeys`](/reference/2026-01-01/enums/conversationmembershiporderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ConversationMembershipPaginationConnection`](/reference/2026-01-01/objects/conversationmembershippaginationconnection)

## Example

```
query conversationMemberships(
  $active_status: String
  $client_id: String
  $conversation_type: String
  $keywords: String
  $notes_type: String
  $only_include_shared_memberships: Boolean
  $org_chat: Boolean
  $provider_id: ID
  $provider_ids: [ID]
  $read_status: String
  $order_by: ConversationMembershipOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  conversationMemberships(
    active_status: $active_status
    client_id: $client_id
    conversation_type: $conversation_type
    keywords: $keywords
    notes_type: $notes_type
    only_include_shared_memberships: $only_include_shared_memberships
    org_chat: $org_chat
    provider_id: $provider_id
    provider_ids: $provider_ids
    read_status: $read_status
    order_by: $order_by
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
