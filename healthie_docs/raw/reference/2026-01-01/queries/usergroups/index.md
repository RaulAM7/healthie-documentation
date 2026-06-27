---
title: userGroups | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/usergroups/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/usergroups/index.md
---

Fetch paginated user groups collection

## Arguments

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`check_group_level_actions` ](#argument-check-group-level-actions)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· checks the allow\_group\_level\_actions permission on org membership

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`UserGroupOrderKeys`](/reference/2026-01-01/enums/usergrouporderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`UserGroupPaginationConnection`](/reference/2026-01-01/objects/usergrouppaginationconnection)

## Example

```
query userGroups(
  $keywords: String
  $check_group_level_actions: Boolean
  $sort_by: String
  $order_by: UserGroupOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  userGroups(
    keywords: $keywords
    check_group_level_actions: $check_group_level_actions
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
