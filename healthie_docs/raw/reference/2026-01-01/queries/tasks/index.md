---
title: tasks | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/tasks/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/tasks/index.md
---

All tasks assigned to a provider or client

## Arguments

[`assigned_to_user` ](#argument-assigned-to-user)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, only tasks assigned to the current user will be returned

[`assignees` ](#argument-assignees)· [`[ID]` ](/reference/2026-01-01/scalars/id)· If present, only tasks assigned to the given users will be returned.

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`completed_status` ](#argument-completed-status)· [`String`](/reference/2026-01-01/scalars/string)

[`created_by_self` ](#argument-created-by-self)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Nil -> does nothing, false -> tasks created by others, true -> tasks created by current user

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`show_hidden` ](#argument-show-hidden)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`smart` ](#argument-smart)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Nil -> all tasks, false -> non-smart tasks, true -> smart tasks

[`type` ](#argument-type)· [`String`](/reference/2026-01-01/scalars/string)

[`sort_by` ](#argument-sort-by)· [`String` ](/reference/2026-01-01/scalars/string)· \<column-name>\_\<order> (i.e completed\_asc, assignee\_desc)

[`order_by` ](#argument-order-by)· [`TaskOrderKeys`](/reference/2026-01-01/enums/taskorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`TaskPaginationConnection`](/reference/2026-01-01/objects/taskpaginationconnection)

## Example

```
query tasks(
  $assigned_to_user: Boolean
  $assignees: [ID]
  $client_id: ID
  $completed_status: String
  $created_by_self: Boolean
  $keywords: String
  $show_hidden: Boolean
  $smart: Boolean
  $type: String
  $sort_by: String
  $order_by: TaskOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  tasks(
    assigned_to_user: $assigned_to_user
    assignees: $assignees
    client_id: $client_id
    completed_status: $completed_status
    created_by_self: $created_by_self
    keywords: $keywords
    show_hidden: $show_hidden
    smart: $smart
    type: $type
    sort_by: $sort_by
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
