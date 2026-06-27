---
title: sentWebhooks | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sentwebhooks/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sentwebhooks/index.md
---

Fetch paginated SentWebhooks collection. SentWebhook records are available for 180 days.

## Arguments

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`SentWebhookOrderKeys`](/reference/2026-01-01/enums/sentwebhookorderkeys)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`sent_after` ](#argument-sent-after)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Filter sent webhooks sent on or after this date.

[`sent_before` ](#argument-sent-before)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Filter sent webhooks sent on or before this date. Only considered if \`sent\_after\` is provided. Defaults to the current date if not provided.

[`resource_id` ](#argument-resource-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter by the ID of the resource that triggered the webhook.

[`resource_type` ](#argument-resource-type)· [`SentWebhookResourceType` ](/reference/2026-01-01/enums/sentwebhookresourcetype)· Filter by the type of resource that triggered the webhook.

[`failed` ](#argument-failed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Filter for webhooks that did not receive a 2xx response status code.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`SentWebhookPaginationConnection`](/reference/2026-01-01/objects/sentwebhookpaginationconnection)

## Example

```
query sentWebhooks(
  $keywords: String
  $order_by: SentWebhookOrderKeys
  $sort_by: String
  $sent_after: ISO8601DateTime
  $sent_before: ISO8601DateTime
  $resource_id: ID
  $resource_type: SentWebhookResourceType
  $failed: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  sentWebhooks(
    keywords: $keywords
    order_by: $order_by
    sort_by: $sort_by
    sent_after: $sent_after
    sent_before: $sent_before
    resource_id: $resource_id
    resource_type: $resource_type
    failed: $failed
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
