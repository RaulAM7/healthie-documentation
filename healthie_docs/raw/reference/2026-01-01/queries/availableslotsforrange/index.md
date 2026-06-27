---
title: availableSlotsForRange | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/availableslotsforrange/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/availableslotsforrange/index.md
---

Get open appointment times for a date range. Returns array of dates sorted in ascending order (considered public)

## Arguments

[`appointment_to_reschedule_id` ](#argument-appointment-to-reschedule-id)· [`ID` ](/reference/2026-01-01/scalars/id)· (optional) The ID of the appointment that will be rescheduled. Only needed if you want to use appointment-specific rescheduling restrictions

[`appointment_type_ids` ](#argument-appointment-type-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· An array of group appointment type IDs can be passed in. When passed in, will return availability for multiple group appointment Overrides appt\_type\_id.

[`appt_loc_id` ](#argument-appt-loc-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`appt_type_id` ](#argument-appt-type-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`clients_can_join_waitlist` ](#argument-clients-can-join-waitlist)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`contact_type` ](#argument-contact-type)· [`String`](/reference/2026-01-01/scalars/string)

[`end_date` ](#argument-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· If not provided, defaults to the current date

[`end_date_boundary` ](#argument-end-date-boundary)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· When passed in, slots after this will not be returned. Inclusive.

[`length` ](#argument-length)· [`String`](/reference/2026-01-01/scalars/string)

[`licensed_in_state` ](#argument-licensed-in-state)· [`String` ](/reference/2026-01-01/scalars/string)· Two letter state abbreviation (e.g. "CA", "NY")

[`accepts_insurance_plan_id` ](#argument-accepts-insurance-plan-id)· [`ID` ](/reference/2026-01-01/scalars/id)· When passed, only considers providers who accept the given insurance plan

[`exclude_provider_ids` ](#argument-exclude-provider-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· When passed, excludes the given provider IDs from the results. Supersedes provider\_ids if both are provided. Only supported when org\_level is true.

[`make_unique` ](#argument-make-unique)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, multiple slots for the same time (for different providers) will be returned.

[`org_level` ](#argument-org-level)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`outside_factors` ](#argument-outside-factors)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`provider_id` ](#argument-provider-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Required

[`provider_ids` ](#argument-provider-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`tag_ids` ](#argument-tag-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Filters the provider list to only include users who have all of the specified tags applied. Ignored if org\_level is not true

[`start_date` ](#argument-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· If not provided, defaults to the current date

[`start_date_boundary` ](#argument-start-date-boundary)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· When passed in, slots before this will not be returned.

[`timezone` ](#argument-timezone)· [`String` ](/reference/2026-01-01/scalars/string)· When passed in, slots will be calculated with the specified timezone

## Returns

[`[PotentialAppointmentSlot!]`](/reference/2026-01-01/objects/potentialappointmentslot)

## Example

```
query availableSlotsForRange(
  $appointment_to_reschedule_id: ID
  $appointment_type_ids: [ID]
  $appt_loc_id: ID
  $appt_type_id: ID
  $clients_can_join_waitlist: Boolean
  $contact_type: String
  $end_date: ISO8601DateTime
  $end_date_boundary: ISO8601Date
  $length: String
  $licensed_in_state: String
  $accepts_insurance_plan_id: ID
  $exclude_provider_ids: [ID]
  $make_unique: Boolean
  $org_level: Boolean
  $outside_factors: Boolean
  $provider_id: ID!
  $provider_ids: [ID]
  $tag_ids: [ID]
  $start_date: ISO8601DateTime
  $start_date_boundary: ISO8601Date
  $timezone: String
) {
  availableSlotsForRange(
    appointment_to_reschedule_id: $appointment_to_reschedule_id
    appointment_type_ids: $appointment_type_ids
    appt_loc_id: $appt_loc_id
    appt_type_id: $appt_type_id
    clients_can_join_waitlist: $clients_can_join_waitlist
    contact_type: $contact_type
    end_date: $end_date
    end_date_boundary: $end_date_boundary
    length: $length
    licensed_in_state: $licensed_in_state
    accepts_insurance_plan_id: $accepts_insurance_plan_id
    exclude_provider_ids: $exclude_provider_ids
    make_unique: $make_unique
    org_level: $org_level
    outside_factors: $outside_factors
    provider_id: $provider_id
    provider_ids: $provider_ids
    tag_ids: $tag_ids
    start_date: $start_date
    start_date_boundary: $start_date_boundary
    timezone: $timezone
  ) {
    appointment_id
    appointment_type
    color
    date
    has_waitlist_enabled
    is_fully_booked
    length
    user_id
  }
}
```
