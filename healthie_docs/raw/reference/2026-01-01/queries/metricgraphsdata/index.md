---
title: metricGraphsData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/metricgraphsdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/metricgraphsdata/index.md
---

Fetch data for the metric graphs for a given user

## Arguments

[`end_date` ](#argument-end-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· End of the date range, must be sent in with a start date. Timestamp in YYYY-MM-DD HH:MM:SS or ISO8601 format.

[`has_third_party_source` ](#argument-has-third-party-source)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, returns no third-party data. When true, returns only third-party data. If not passed in, will return all data

[`start_date` ](#argument-start-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Start of the date range, must be sent in with an end date. Timestamp in YYYY-MM-DD HH:MM:SS or ISO8601 format.

[`user_id` ](#argument-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user to fetch data for. Defaults to the current user.

## Returns

[`[MetricGraphDataType!]!`](/reference/2026-01-01/objects/metricgraphdatatype)

## Example

```
query metricGraphsData(
  $end_date: ISO8601Date
  $has_third_party_source: Boolean
  $start_date: ISO8601Date
  $user_id: String
) {
  metricGraphsData(
    end_date: $end_date
    has_third_party_source: $has_third_party_source
    start_date: $start_date
    user_id: $user_id
  )
}
```
