---
title: tagsPaginated | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/tagspaginated/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/tagspaginated/index.md
---

A paginated collection of tags related to current patient/provider/organization

## Arguments

[`applied_to_providers` ](#argument-applied-to-providers)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only returns tags applied to providers in the organization.

[`ids` ](#argument-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Filter results to only tags with the specified IDs.

[`order_by` ](#argument-order-by)· [`TagOrderKeys` ](/reference/2026-01-01/enums/tagorderkeys)· Sort order for returned tags. Supports sorting by name, patient count, organization member count, or creator name. Defaults to name ascending. See 'Tag Order Keys' for more information.

[`user_id` ](#argument-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter results to tags owned by the specified user. Ignored if the current user has see\_all\_clients permission.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`TagPaginationConnection`](/reference/2026-01-01/objects/tagpaginationconnection)

## Example

```
query tagsPaginated(
  $applied_to_providers: Boolean
  $ids: [ID]
  $order_by: TagOrderKeys
  $user_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  tagsPaginated(
    applied_to_providers: $applied_to_providers
    ids: $ids
    order_by: $order_by
    user_id: $user_id
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
