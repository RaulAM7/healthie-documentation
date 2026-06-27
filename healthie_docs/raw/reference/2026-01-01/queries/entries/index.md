---
title: entries | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/entries/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/entries/index.md
---

Fetch paginated entries collection

## Arguments

[`category` ](#argument-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of entry (e.g Weight or Blood Pressure) to return.

[`client_id` ](#argument-client-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the client whose entries to return.

[`end_datetime_range` ](#argument-end-datetime-range)· [`String` ](/reference/2026-01-01/scalars/string)· This field takes in a datetime string, and returns entries before that datetime. Must be sent in with a start\_datetime\_range.

[`end_range` ](#argument-end-range)· [`String` ](/reference/2026-01-01/scalars/string)· This field takes in a date (e.g 2020-11-29), and returns entries before the beginning of that day. Must be sent in with a start\_range.

[`entry_id` ](#argument-entry-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of a specific entry to return.

[`group_id` ](#argument-group-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of a user group to filter entries by.

[`include_inactive` ](#argument-include-inactive)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, includes entries from deactivated users. Only applies when no client\_id is provided.

[`is_org` ](#argument-is-org)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns entries for all client in the organization.

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· A search string to filter entries by.

[`sort_by` ](#argument-sort-by)· [`String` ](/reference/2026-01-01/scalars/string)· Options are \[created\_at::desc,created\_at::asc, metric\_stat::desc, metric\_stat::asc, unsorted].

[`order_by` ](#argument-order-by)· [`EntryOrderKeys` ](/reference/2026-01-01/enums/entryorderkeys)· The sort order for returned entries.

[`start_datetime_range` ](#argument-start-datetime-range)· [`String` ](/reference/2026-01-01/scalars/string)· This field takes in a datetime string, and returns entries after that datetime. Must be sent in with a end\_datetime\_range.

[`start_range` ](#argument-start-range)· [`String` ](/reference/2026-01-01/scalars/string)· This field takes in a date (e.g 2020-11-28), and returns entries starting at the beginning of that day.

[`summary_view` ](#argument-summary-view)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns all matching entries with associated meals included, without pagination.

[`type` ](#argument-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of entry (e.g MetricEntry) to return.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`EntryPaginationConnection`](/reference/2026-01-01/objects/entrypaginationconnection)

## Example

```
query entries(
  $category: String
  $client_id: String
  $end_datetime_range: String
  $end_range: String
  $entry_id: String
  $group_id: String
  $include_inactive: Boolean
  $is_org: Boolean
  $keywords: String
  $sort_by: String
  $order_by: EntryOrderKeys
  $start_datetime_range: String
  $start_range: String
  $summary_view: Boolean
  $type: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  entries(
    category: $category
    client_id: $client_id
    end_datetime_range: $end_datetime_range
    end_range: $end_range
    entry_id: $entry_id
    group_id: $group_id
    include_inactive: $include_inactive
    is_org: $is_org
    keywords: $keywords
    sort_by: $sort_by
    order_by: $order_by
    start_datetime_range: $start_datetime_range
    start_range: $start_range
    summary_view: $summary_view
    type: $type
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
