---
title: notes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/notes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/notes/index.md
---

Fetch paginated Note collection for given conversation

## Arguments

[`conversation_id` ](#argument-conversation-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`ids` ](#argument-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`org_chat` ](#argument-org-chat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If TRUE: get base user as a conversation owner

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`scheduled_notes` ](#argument-scheduled-notes)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`since_note_id` ](#argument-since-note-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`NoteOrderKeys`](/reference/2026-01-01/enums/noteorderkeys)

[`with_tasks` ](#argument-with-tasks)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If TRUE: get notes with tasks

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`NotePaginationConnection`](/reference/2026-01-01/objects/notepaginationconnection)

## Example

```
query notes(
  $conversation_id: ID
  $ids: [ID]
  $keywords: String
  $org_chat: Boolean
  $provider_id: ID
  $scheduled_notes: Boolean
  $since_note_id: ID
  $sort_by: String
  $order_by: NoteOrderKeys
  $with_tasks: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  notes(
    conversation_id: $conversation_id
    ids: $ids
    keywords: $keywords
    org_chat: $org_chat
    provider_id: $provider_id
    scheduled_notes: $scheduled_notes
    since_note_id: $since_note_id
    sort_by: $sort_by
    order_by: $order_by
    with_tasks: $with_tasks
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
