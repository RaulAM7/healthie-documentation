---
title: daysAvailableForRange | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/daysavailableforrange/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/daysavailableforrange/index.md
---

get open appointment times for a range (considered public)

## Arguments

[`appointment_to_reschedule_id` ](#argument-appointment-to-reschedule-id)· [`ID` ](/reference/2026-01-01/scalars/id)· (optional) The ID of the appointment that will be rescheduled. Only needed if you want to use appointment-specific rescheduling restrictions

[`appt_loc_id` ](#argument-appt-loc-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`appt_type_id` ](#argument-appt-type-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`clients_can_join_waitlist` ](#argument-clients-can-join-waitlist)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`contact_type` ](#argument-contact-type)· [`String`](/reference/2026-01-01/scalars/string)

[`date_from_month` ](#argument-date-from-month)· [`String` ](/reference/2026-01-01/scalars/string)· If not provided, defaults to the current date

[`end_date` ](#argument-end-date)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`end_date_boundary` ](#argument-end-date-boundary)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· When passed in, slots after this will not be returned. Inclusive.

[`length` ](#argument-length)· [`String`](/reference/2026-01-01/scalars/string)

[`licensed_in_state` ](#argument-licensed-in-state)· [`String` ](/reference/2026-01-01/scalars/string)· Two letter state abbreviation (e.g. "CA", "NY")

[`accepts_insurance_plan_id` ](#argument-accepts-insurance-plan-id)· [`ID` ](/reference/2026-01-01/scalars/id)· When passed, only considers providers who accept the given insurance plan

[`exclude_provider_ids` ](#argument-exclude-provider-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· When passed, excludes the given provider IDs from the results. Supersedes provider\_ids if both are provided. Only supported when org\_level is true.

[`org_level` ](#argument-org-level)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Required True if querying multiple providers

[`outside_factors` ](#argument-outside-factors)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`provider_id` ](#argument-provider-id)· [`String` ](/reference/2026-01-01/scalars/string)· Required

[`provider_ids` ](#argument-provider-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`tag_ids` ](#argument-tag-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Filters the provider list to only include users who have all of the specified tags applied. Ignored if org\_level is not true

[`start_date` ](#argument-start-date)· [`String` ](/reference/2026-01-01/scalars/string)· When passed in, supercedes date\_from\_month. Must be passed in along with end\_date

[`start_date_boundary` ](#argument-start-date-boundary)· [`String` ](/reference/2026-01-01/scalars/string)· When passed in, slots before this will not be returned. YYYY-MM-DD format

[`timezone` ](#argument-timezone)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`[String]`](/reference/2026-01-01/scalars/string)

## Example

```
query daysAvailableForRange(
  $appointment_to_reschedule_id: ID
  $appt_loc_id: ID
  $appt_type_id: ID
  $clients_can_join_waitlist: Boolean
  $contact_type: String
  $date_from_month: String
  $end_date: ISO8601DateTime
  $end_date_boundary: ISO8601Date
  $length: String
  $licensed_in_state: String
  $accepts_insurance_plan_id: ID
  $exclude_provider_ids: [ID]
  $org_level: Boolean
  $outside_factors: Boolean
  $provider_id: String
  $provider_ids: [ID]
  $tag_ids: [ID]
  $start_date: String
  $start_date_boundary: String
  $timezone: String
) {
  daysAvailableForRange(
    appointment_to_reschedule_id: $appointment_to_reschedule_id
    appt_loc_id: $appt_loc_id
    appt_type_id: $appt_type_id
    clients_can_join_waitlist: $clients_can_join_waitlist
    contact_type: $contact_type
    date_from_month: $date_from_month
    end_date: $end_date
    end_date_boundary: $end_date_boundary
    length: $length
    licensed_in_state: $licensed_in_state
    accepts_insurance_plan_id: $accepts_insurance_plan_id
    exclude_provider_ids: $exclude_provider_ids
    org_level: $org_level
    outside_factors: $outside_factors
    provider_id: $provider_id
    provider_ids: $provider_ids
    tag_ids: $tag_ids
    start_date: $start_date
    start_date_boundary: $start_date_boundary
    timezone: $timezone
  )
}
```
