---
title: availabilities | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/availabilities/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/availabilities/index.md
---

Fetch availabilities for range

## Arguments

[`appointment_location_id` ](#argument-appointment-location-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`appointment_type_id` ](#argument-appointment-type-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`appointment_type_ids` ](#argument-appointment-type-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Array of IDs of appointment types to filter availabilities

[`availability_provider_id` ](#argument-availability-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the provider to show availabilities for, supercedes provider id and is\_org

[`contact_type_id` ](#argument-contact-type-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`endDate` ](#argument-enddate)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`end_date_padding` ](#argument-end-date-padding)· [`Int` ](/reference/2026-01-01/scalars/int)· Amount of hours after the endDate to pull availabilities in for. This is helpful when using this query with some calendar display libraries

[`includeRepeating` ](#argument-includerepeating)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`is_org` ](#argument-is-org)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`is_repeating` ](#argument-is-repeating)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`one_time` ](#argument-one-time)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`provider_ids` ](#argument-provider-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`include_suborganizations` ](#argument-include-suborganizations)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, availability from suborganization providers can be included

[`show_availability` ](#argument-show-availability)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`startDate` ](#argument-startdate)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`start_date_padding` ](#argument-start-date-padding)· [`Int` ](/reference/2026-01-01/scalars/int)· Amount of hours before the startDate to pull availabilities in for. This is helpful when using this query with some calendar display libraries

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`organization_id` ](#argument-organization-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the organization to pull availability for. Default to current user organization if not set. Ignored if is\_org is false

[`timezone` ](#argument-timezone)· [`String`](/reference/2026-01-01/scalars/string)

[`state_license` ](#argument-state-license)· [`String`](/reference/2026-01-01/scalars/string)

[`tag_ids` ](#argument-tag-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`insurance_plan_ids` ](#argument-insurance-plan-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

## Returns

[`[Availability!]`](/reference/2026-01-01/objects/availability)

## Example

```
query availabilities(
  $appointment_location_id: ID
  $appointment_type_id: ID
  $appointment_type_ids: [ID]
  $availability_provider_id: ID
  $contact_type_id: ID
  $endDate: ISO8601DateTime
  $end_date_padding: Int
  $includeRepeating: Boolean
  $is_org: Boolean
  $is_repeating: Boolean
  $one_time: Boolean
  $provider_id: ID
  $provider_ids: [ID]
  $include_suborganizations: Boolean
  $show_availability: Boolean
  $startDate: ISO8601DateTime
  $start_date_padding: Int
  $user_id: ID
  $organization_id: ID
  $timezone: String
  $state_license: String
  $tag_ids: [ID]
  $insurance_plan_ids: [ID]
) {
  availabilities(
    appointment_location_id: $appointment_location_id
    appointment_type_id: $appointment_type_id
    appointment_type_ids: $appointment_type_ids
    availability_provider_id: $availability_provider_id
    contact_type_id: $contact_type_id
    endDate: $endDate
    end_date_padding: $end_date_padding
    includeRepeating: $includeRepeating
    is_org: $is_org
    is_repeating: $is_repeating
    one_time: $one_time
    provider_id: $provider_id
    provider_ids: $provider_ids
    include_suborganizations: $include_suborganizations
    show_availability: $show_availability
    startDate: $startDate
    start_date_padding: $start_date_padding
    user_id: $user_id
    organization_id: $organization_id
    timezone: $timezone
    state_license: $state_license
    tag_ids: $tag_ids
    insurance_plan_ids: $insurance_plan_ids
  ) {
    appointment_location_id
    appointment_type_id
    appointment_types
    contact_type_id
    created_at
    day_of_week
    duration_string
    end_on
    id
    is_repeating
    origin_start_date
    range_end
    range_start
    repeating_availability_id
    resourceId
    timezone
    timezone_abbr
    updated_at
    user
    user_id
  }
}
```
