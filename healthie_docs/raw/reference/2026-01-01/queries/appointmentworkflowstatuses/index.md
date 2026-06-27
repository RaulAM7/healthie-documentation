---
title: appointmentWorkflowStatuses | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentworkflowstatuses/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentworkflowstatuses/index.md
---

Fetch paginated appointment workflow statuses collection

## Arguments

[`range_start` ](#argument-range-start)· [`ISO8601Date`](/reference/2026-01-01/scalars/iso8601date)

[`range_end` ](#argument-range-end)· [`ISO8601Date`](/reference/2026-01-01/scalars/iso8601date)

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`cms1500_statuses` ](#argument-cms1500-statuses)· [`[Cms1500Status]`](/reference/2026-01-01/enums/cms1500status)

[`invoice_statuses` ](#argument-invoice-statuses)· [`[RequestedPaymentStatus]`](/reference/2026-01-01/enums/requestedpaymentstatus)

[`chart_note_statuses` ](#argument-chart-note-statuses)· [`[AppointmentWorkflowChartNoteStatus]`](/reference/2026-01-01/enums/appointmentworkflowchartnotestatus)

[`provider_ids` ](#argument-provider-ids)· [`[ID!]`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`AppointmentWorkflowStatusConnection`](/reference/2026-01-01/objects/appointmentworkflowstatusconnection)

## Example

```
query appointmentWorkflowStatuses(
  $range_start: ISO8601Date
  $range_end: ISO8601Date
  $client_id: ID
  $cms1500_statuses: [Cms1500Status]
  $invoice_statuses: [RequestedPaymentStatus]
  $chart_note_statuses: [AppointmentWorkflowChartNoteStatus]
  $provider_ids: [ID!]
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  appointmentWorkflowStatuses(
    range_start: $range_start
    range_end: $range_end
    client_id: $client_id
    cms1500_statuses: $cms1500_statuses
    invoice_statuses: $invoice_statuses
    chart_note_statuses: $chart_note_statuses
    provider_ids: $provider_ids
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
