---
title: auditLog | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/auditlog/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/auditlog/index.md
---

Fetch paginated Audit Log collection

## Arguments

[`acting_user_id` ](#argument-acting-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Use this to retrieve the log of all the actions taken by a specific user. Pass in 'no\_author' to retrieve only audit events performed automatically (with no user). Leave blank for all users.

[`resource_name` ](#argument-resource-name)· [`AuditEventResourceName` ](/reference/2026-01-01/enums/auditeventresourcename)· Use this in conjunction with the resource\_id to retrieve the audit log of a specific resource. Leave blank for all resources.

[`resource_id` ](#argument-resource-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Use this in conjunction with the resource\_name to retrieve the audit log of a specific resource. Leave blank for all resources.

[`event_type` ](#argument-event-type)· [`AuditEventType` ](/reference/2026-01-01/enums/auditeventtype)· Use this to filter by the type of audit event.

[`occurred_after` ](#argument-occurred-after)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When passed in, only audit events that occurred after the specified DateTime are returned.

[`occurred_before` ](#argument-occurred-before)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When passed in, only audit events that occurred before the specified DateTime are returned.

[`order_by` ](#argument-order-by)· [`AuditEventOrderKeys`](/reference/2026-01-01/enums/auditeventorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`AuditEventPaginationConnection`](/reference/2026-01-01/objects/auditeventpaginationconnection)

## Example

```
query auditLog(
  $acting_user_id: ID
  $resource_name: AuditEventResourceName
  $resource_id: ID
  $event_type: AuditEventType
  $occurred_after: ISO8601DateTime
  $occurred_before: ISO8601DateTime
  $order_by: AuditEventOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  auditLog(
    acting_user_id: $acting_user_id
    resource_name: $resource_name
    resource_id: $resource_id
    event_type: $event_type
    occurred_after: $occurred_after
    occurred_before: $occurred_before
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
