---
title: users | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/users/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/users/index.md
---

Fetch paginated patients collection (use organizationMembers query for providers)

## Arguments

[`active_status` ](#argument-active-status)· [`String` ](/reference/2026-01-01/scalars/string)· Possible options: \[active, archived]

[`conversation_id` ](#argument-conversation-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filters users to invitees of the specified conversation.

[`convo_patients_only` ](#argument-convo-patients-only)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true and conversation\_id is provided, only patient invitees of the conversation are returned.

[`email` ](#argument-email)· [`String` ](/reference/2026-01-01/scalars/string)· Does nothing

[`expect_conversation_id` ](#argument-expect-conversation-id)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When this is true, but conversation\_id is nil, we return no users

[`from_superadmin` ](#argument-from-superadmin)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true and the current user is a super admin, fetches a user by email or id bypassing organization-level filtering.

[`group_id` ](#argument-group-id)· [`String` ](/reference/2026-01-01/scalars/string)· Filters users to those assigned to the specified user group.

[`has_cc_on_file` ](#argument-has-cc-on-file)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only clients with credit cards will be returned. Passing false does nothing

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Used with from\_superadmin to fetch a single user by ID, bypassing organization-level filtering.

[`ids` ](#argument-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Returns organization-level patients matching the provided list of IDs.

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Searches users by name, email, date of birth, record identifier, and other fields.

[`limited_to_provider` ](#argument-limited-to-provider)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only patients directly assigned to the provider rather than all organization-level patients.

[`provider_id` ](#argument-provider-id)· [`String` ](/reference/2026-01-01/scalars/string)· Fetches patients for the specified provider instead of the current user. The current user must belong to the same organization.

[`show_all_by_default` ](#argument-show-all-by-default)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· when false, an empty collection is returned unless keywords or a conversation\_id are provided

[`sort_by` ](#argument-sort-by)· [`String` ](/reference/2026-01-01/scalars/string)· Options are email, first\_name\_asc, first\_name\_desc, last\_name\_asc, last\_name\_desc, created\_at\_desc, created\_at\_asc, updated\_at\_desc, updated\_at\_asc, group\_name\_asc, group\_name\_desc, provider\_name\_asc, provider\_name\_desc, next\_appt\_asc, next\_appt\_desc. Defaults to last\_name\_desc

[`order_by` ](#argument-order-by)· [`UserOrderKeys` ](/reference/2026-01-01/enums/userorderkeys)· Specifies the sort order for results. Defaults to last\_name\_asc.

[`tag_ids` ](#argument-tag-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· When passed in, only clients with at least ONE of the passed-in tags will be returned.

[`with_feature_toggles` ](#argument-with-feature-toggles)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, eagerly loads feature toggle data for the returned users.

[`include_suborg_patients` ](#argument-include-suborg-patients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, excludes patients from sub-organizations.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`UserConnection!`](/reference/2026-01-01/objects/userconnection)

## Example

```
query users(
  $active_status: String
  $conversation_id: ID
  $convo_patients_only: Boolean
  $email: String
  $expect_conversation_id: Boolean
  $from_superadmin: Boolean
  $group_id: String
  $has_cc_on_file: Boolean
  $id: ID
  $ids: [ID]
  $keywords: String
  $limited_to_provider: Boolean
  $provider_id: String
  $show_all_by_default: Boolean
  $sort_by: String
  $order_by: UserOrderKeys
  $tag_ids: [ID]
  $with_feature_toggles: Boolean
  $include_suborg_patients: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  users(
    active_status: $active_status
    conversation_id: $conversation_id
    convo_patients_only: $convo_patients_only
    email: $email
    expect_conversation_id: $expect_conversation_id
    from_superadmin: $from_superadmin
    group_id: $group_id
    has_cc_on_file: $has_cc_on_file
    id: $id
    ids: $ids
    keywords: $keywords
    limited_to_provider: $limited_to_provider
    provider_id: $provider_id
    show_all_by_default: $show_all_by_default
    sort_by: $sort_by
    order_by: $order_by
    tag_ids: $tag_ids
    with_feature_toggles: $with_feature_toggles
    include_suborg_patients: $include_suborg_patients
    after: $after
    before: $before
    first: $first
    last: $last
  )
}
```
