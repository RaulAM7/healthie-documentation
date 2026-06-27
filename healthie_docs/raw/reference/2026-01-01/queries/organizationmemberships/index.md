---
title: organizationMemberships | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationmemberships/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationmemberships/index.md
---

Fetch paginated organization memberships collection

## Arguments

[`id` ](#argument-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the organization to load memberships for

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`OrganizationMembershipOrderKeys`](/reference/2026-01-01/enums/organizationmembershiporderkeys)

[`user_ids` ](#argument-user-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`OrganizationMembershipPaginationConnection`](/reference/2026-01-01/objects/organizationmembershippaginationconnection)

## Example

```
query organizationMemberships(
  $id: String
  $sort_by: String
  $order_by: OrganizationMembershipOrderKeys
  $user_ids: [ID]
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  organizationMemberships(
    id: $id
    sort_by: $sort_by
    order_by: $order_by
    user_ids: $user_ids
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
