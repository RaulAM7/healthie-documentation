---
title: sentNotificationRecords | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sentnotificationrecords/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sentnotificationrecords/index.md
---

Fetch paginated sent notification records collection

## Arguments

[`end_date` ](#argument-end-date)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`org_level` ](#argument-org-level)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Used in conjunction with provider\_id. When true, returns sent notification records for all patients in the organization

[`patient_id` ](#argument-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the patient to return sent notification records for.

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· When passed in, returns sent notification records for the given provider's patients. Overrides patient\_id. Current user must be an admin to use this param

[`should_paginate` ](#argument-should-paginate)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Must be true if provider\_id is passed in.

[`start_date` ](#argument-start-date)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`status` ](#argument-status)· [`String`](/reference/2026-01-01/scalars/string)

[`type` ](#argument-type)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`SentNotificationRecordPaginationConnection`](/reference/2026-01-01/objects/sentnotificationrecordpaginationconnection)

## Example

```
query sentNotificationRecords(
  $end_date: ISO8601DateTime
  $org_level: Boolean
  $patient_id: ID
  $provider_id: ID
  $should_paginate: Boolean
  $start_date: ISO8601DateTime
  $status: String
  $type: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  sentNotificationRecords(
    end_date: $end_date
    org_level: $org_level
    patient_id: $patient_id
    provider_id: $provider_id
    should_paginate: $should_paginate
    start_date: $start_date
    status: $status
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
