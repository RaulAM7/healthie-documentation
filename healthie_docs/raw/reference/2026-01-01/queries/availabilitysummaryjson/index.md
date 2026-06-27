---
title: availabilitySummaryJson | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/availabilitysummaryjson/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/availabilitysummaryjson/index.md
---

(Limited availability, subject to breaking changes). JSONified Hash with summary of availability.

## Arguments

[`date` ](#argument-date)· [`String` ](/reference/2026-01-01/scalars/string)· Date (in YYYY-MM-DD) to retrieve availability summary for

[`organization_id` ](#argument-organization-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the suborganization to retrieve data for

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query availabilitySummaryJson($date: String, $organization_id: ID) {
  availabilitySummaryJson(date: $date, organization_id: $organization_id)
}
```
