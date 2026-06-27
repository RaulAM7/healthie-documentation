---
title: billingItems | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/billingitems/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/billingitems/index.md
---

Fetch paginated Billing Items collection

## Arguments

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`created_at_end` ](#argument-created-at-end)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· YYYY-MM-DD format

[`created_at_start` ](#argument-created-at-start)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· YYYY-MM-DD format

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`offerings_only` ](#argument-offerings-only)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`BillingItemOrderKeys`](/reference/2026-01-01/enums/billingitemorderkeys)

[`state` ](#argument-state)· [`String` ](/reference/2026-01-01/scalars/string)· (DEPRECATED) Use 'status' field instead with type - \[String]

[`status` ](#argument-status)· [`[String]` ](/reference/2026-01-01/scalars/string)· Status of the billing item. Can be 'failed', 'paused', 'succeeded', 'scheduled', or \`stopped' (e.g. \['succeeded', 'scheduled'])

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`BillingItemPaginationConnection`](/reference/2026-01-01/objects/billingitempaginationconnection)

## Example

```
query billingItems(
  $client_id: ID
  $created_at_end: ISO8601DateTime
  $created_at_start: ISO8601DateTime
  $keywords: String
  $offerings_only: Boolean
  $provider_id: ID
  $sort_by: String
  $order_by: BillingItemOrderKeys
  $state: String
  $status: [String]
  $user_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  billingItems(
    client_id: $client_id
    created_at_end: $created_at_end
    created_at_start: $created_at_start
    keywords: $keywords
    offerings_only: $offerings_only
    provider_id: $provider_id
    sort_by: $sort_by
    order_by: $order_by
    state: $state
    status: $status
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
