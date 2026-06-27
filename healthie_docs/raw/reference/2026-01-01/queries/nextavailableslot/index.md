---
title: nextAvailableSlot | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/nextavailableslot/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/nextavailableslot/index.md
---

get open appointment times for a range (considered public)

## Arguments

[`appointment_to_reschedule_id` ](#argument-appointment-to-reschedule-id)· [`ID` ](/reference/2026-01-01/scalars/id)· (optional) The ID of the appointment that will be rescheduled. Only needed if you want to use appointment-specific rescheduling restrictions

[`appt_loc_id` ](#argument-appt-loc-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`appt_type_id` ](#argument-appt-type-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`contact_type` ](#argument-contact-type)· [`String`](/reference/2026-01-01/scalars/string)

[`end_date_boundary` ](#argument-end-date-boundary)· [`String` ](/reference/2026-01-01/scalars/string)· When passed in, slots after this will not be returned. Inclusive. YYYY-MM-DD format

[`length` ](#argument-length)· [`String`](/reference/2026-01-01/scalars/string)

[`licensed_in_state` ](#argument-licensed-in-state)· [`String` ](/reference/2026-01-01/scalars/string)· Two letter state abbreviation (e.g. "CA", "NY")

[`accepts_insurance_plan_id` ](#argument-accepts-insurance-plan-id)· [`ID` ](/reference/2026-01-01/scalars/id)· When passed, only considers providers who accept the given insurance plan

[`org_level` ](#argument-org-level)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`outside_factors` ](#argument-outside-factors)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`provider_id` ](#argument-provider-id)· [`String` ](/reference/2026-01-01/scalars/string)· Required

[`provider_ids` ](#argument-provider-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`tag_ids` ](#argument-tag-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Filters the provider list to only include users who have all of the specified tags applied. Ignored if org\_level is not true

[`start_date_boundary` ](#argument-start-date-boundary)· [`String` ](/reference/2026-01-01/scalars/string)· When passed in, slots before this will not be returned. YYYY-MM-DD format

[`timezone` ](#argument-timezone)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query nextAvailableSlot(
  $appointment_to_reschedule_id: ID
  $appt_loc_id: ID
  $appt_type_id: ID
  $contact_type: String
  $end_date_boundary: String
  $length: String
  $licensed_in_state: String
  $accepts_insurance_plan_id: ID
  $org_level: Boolean
  $outside_factors: Boolean
  $provider_id: String
  $provider_ids: [ID]
  $tag_ids: [ID]
  $start_date_boundary: String
  $timezone: String
) {
  nextAvailableSlot(
    appointment_to_reschedule_id: $appointment_to_reschedule_id
    appt_loc_id: $appt_loc_id
    appt_type_id: $appt_type_id
    contact_type: $contact_type
    end_date_boundary: $end_date_boundary
    length: $length
    licensed_in_state: $licensed_in_state
    accepts_insurance_plan_id: $accepts_insurance_plan_id
    org_level: $org_level
    outside_factors: $outside_factors
    provider_id: $provider_id
    provider_ids: $provider_ids
    tag_ids: $tag_ids
    start_date_boundary: $start_date_boundary
    timezone: $timezone
  )
}
```
