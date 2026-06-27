---
title: conversationMembershipInvitees | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/conversationmembershipinvitees/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/conversationmembershipinvitees/index.md
---

Fetch paginated conversation membership invitees collection

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ConversationMembershipPaginationConnection`](/reference/2026-01-01/objects/conversationmembershippaginationconnection)

## Example

```
query conversationMembershipInvitees(
  $id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  conversationMembershipInvitees(
    id: $id
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
