---
title: tags | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/tags/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/tags/index.md
---

A collection of tags related to current patient/provider/organization

## Arguments

[`applied_to_providers` ](#argument-applied-to-providers)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only returns tags applied to providers in the organization.

[`ids` ](#argument-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Filter results to only tags with the specified IDs.

[`order_by` ](#argument-order-by)· [`TagOrderKeys` ](/reference/2026-01-01/enums/tagorderkeys)· Sort order for returned tags. Supports sorting by name, patient count, organization member count, or creator name. Defaults to name ascending. See 'Tag Order Keys' for more information.

[`user_id` ](#argument-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter results to tags owned by the specified user. Ignored if the current user has see\_all\_clients permission.

[`sort_by` ](#argument-sort-by)· [`String` ](/reference/2026-01-01/scalars/string)· Options are name\_desc, name\_asc, active\_users\_desc, active\_users\_asc, added\_by\_asc, added\_by\_desc, org\_members\_asc, org\_members\_desc

## Returns

[`[Tag!]`](/reference/2026-01-01/objects/tag)

## Example

```
query tags(
  $applied_to_providers: Boolean
  $ids: [ID]
  $order_by: TagOrderKeys
  $user_id: ID
  $sort_by: String
) {
  tags(
    applied_to_providers: $applied_to_providers
    ids: $ids
    order_by: $order_by
    user_id: $user_id
    sort_by: $sort_by
  ) {
    active_users_count
    added_by
    archived_users_count
    created_at
    id
    name
    org_members_count
    patients_tagged_count
    providers_tagged_count
    tagged_users
    updated_at
    user
  }
}
```
