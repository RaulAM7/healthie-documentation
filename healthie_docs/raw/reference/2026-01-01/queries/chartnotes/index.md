---
title: chartNotes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/chartnotes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/chartnotes/index.md
---

Load all charting notes accessible by this user

## Arguments

[`tag_ids` ](#argument-tag-ids)· [`[ID!]`](/reference/2026-01-01/scalars/id)

[`end_date` ](#argument-end-date)· [`ISO8601Date`](/reference/2026-01-01/scalars/iso8601date)

[`start_date` ](#argument-start-date)· [`ISO8601Date`](/reference/2026-01-01/scalars/iso8601date)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`provider_ids` ](#argument-provider-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`chart_note_status` ](#argument-chart-note-status)· [`ChartNoteStatus` ](/reference/2026-01-01/enums/chartnotestatus)· Chart note status to filter by

[`custom_module_form_ids` ](#argument-custom-module-form-ids)· [`[ID!]`](/reference/2026-01-01/scalars/id)

[`exclude_requested_and_intake_flow_forms` ](#argument-exclude-requested-and-intake-flow-forms)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Exclude forms completed via form requests or intake flows

[`primary_payer_ids` ](#argument-primary-payer-ids)· [`[ID!]` ](/reference/2026-01-01/scalars/id)· Filter by primary insurance plan IDs

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`FormAnswerGroupPaginationConnection`](/reference/2026-01-01/objects/formanswergrouppaginationconnection)

## Example

```
query chartNotes(
  $tag_ids: [ID!]
  $end_date: ISO8601Date
  $start_date: ISO8601Date
  $user_id: ID
  $provider_ids: [ID]
  $chart_note_status: ChartNoteStatus
  $custom_module_form_ids: [ID!]
  $exclude_requested_and_intake_flow_forms: Boolean
  $primary_payer_ids: [ID!]
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  chartNotes(
    tag_ids: $tag_ids
    end_date: $end_date
    start_date: $start_date
    user_id: $user_id
    provider_ids: $provider_ids
    chart_note_status: $chart_note_status
    custom_module_form_ids: $custom_module_form_ids
    exclude_requested_and_intake_flow_forms: $exclude_requested_and_intake_flow_forms
    primary_payer_ids: $primary_payer_ids
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
