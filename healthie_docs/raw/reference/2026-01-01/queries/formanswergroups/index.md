---
title: formAnswerGroups | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/formanswergroups/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/formanswergroups/index.md
---

All filled forms for a given set of arguments

## Arguments

[`custom_module_form_id` ](#argument-custom-module-form-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`date` ](#argument-date)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`filler_id` ](#argument-filler-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`form_answer_group_id` ](#argument-form-answer-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`ids` ](#argument-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Accepts an array of FormAnswerGroup ids

[`include_group_notes` ](#argument-include-group-notes)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`name` ](#argument-name)· [`String`](/reference/2026-01-01/scalars/string)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`locked_status` ](#argument-locked-status)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`signed_status` ](#argument-signed-status)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`updated_after` ](#argument-updated-after)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When passed in, only objects updated after the specified datetime are returned.

[`updated_before` ](#argument-updated-before)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When passed in, only objects updated before the specified datetime are returned.

[`order_by` ](#argument-order-by)· [`FormAnswerGroupOrderKeys`](/reference/2026-01-01/enums/formanswergrouporderkeys)

[`use_for_charting` ](#argument-use-for-charting)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only returns form answer groups for forms marked for charting use.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`FormAnswerGroupPaginationConnection`](/reference/2026-01-01/objects/formanswergrouppaginationconnection)

## Example

```
query formAnswerGroups(
  $custom_module_form_id: ID
  $date: ISO8601DateTime
  $filler_id: ID
  $form_answer_group_id: ID
  $ids: [ID]
  $include_group_notes: Boolean
  $name: String
  $user_id: ID
  $locked_status: Boolean
  $signed_status: Boolean
  $updated_after: ISO8601DateTime
  $updated_before: ISO8601DateTime
  $order_by: FormAnswerGroupOrderKeys
  $use_for_charting: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  formAnswerGroups(
    custom_module_form_id: $custom_module_form_id
    date: $date
    filler_id: $filler_id
    form_answer_group_id: $form_answer_group_id
    ids: $ids
    include_group_notes: $include_group_notes
    name: $name
    user_id: $user_id
    locked_status: $locked_status
    signed_status: $signed_status
    updated_after: $updated_after
    updated_before: $updated_before
    order_by: $order_by
    use_for_charting: $use_for_charting
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
