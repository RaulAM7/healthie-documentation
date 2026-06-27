---
title: scheduledMessageBlasts | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/scheduledmessageblasts/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/scheduledmessageblasts/index.md
---

Fetch paginated scheduled message blasts collection

## Arguments

[`org_chat` ](#argument-org-chat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If True - returns organization membership scheduled message blasts

[`client_id` ](#argument-client-id)· [`String` ](/reference/2026-01-01/scalars/string)· Only include relevant scheduled message blasts for client

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the provider to get conversation for (if nil, will return current users)

[`provider_ids` ](#argument-provider-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Used to filter org chat conversations by provider ids

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`NoteSchedulerPaginationConnection`](/reference/2026-01-01/objects/noteschedulerpaginationconnection)

## Example

```
query scheduledMessageBlasts(
  $org_chat: Boolean
  $client_id: String
  $provider_id: ID
  $provider_ids: [ID]
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  scheduledMessageBlasts(
    org_chat: $org_chat
    client_id: $client_id
    provider_id: $provider_id
    provider_ids: $provider_ids
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
