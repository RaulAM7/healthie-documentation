---
title: appointmentBookingWarnings | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentbookingwarnings/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentbookingwarnings/index.md
---

Return potential booking issues for an appointment, date, time, repeats, attendees, and provider.

## Arguments

[`appointment_type_id` ](#argument-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· (optional) appointment type used to check for credits and for appointment duration.

[`attendee_ids` ](#argument-attendee-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· (optional) IDs of clients assigned to the appointment.

[`date` ](#argument-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date to check for conflicting events and credit deficits.

[`is_repeating` ](#argument-is-repeating)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· (optional) whether this is a repeating appointment.

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the provider to check for conflicting events.

[`repeat_interval` ](#argument-repeat-interval)· [`String` ](/reference/2026-01-01/scalars/string)· (optional) what type of interval for repeating appointments (Weekly, Monthly, Biweekly, Every 4 Weeks).

[`repeat_times` ](#argument-repeat-times)· [`String` ](/reference/2026-01-01/scalars/string)· (optional) how many times the appointment repeats.

[`recurring_appt_id` ](#argument-recurring-appt-id)· [`ID` ](/reference/2026-01-01/scalars/id)· (optional) used to skip checking for conflicts on recurring appointments.

[`time` ](#argument-time)· [`String` ](/reference/2026-01-01/scalars/string)· The time to check (in conjunction with date parameter) for conflicting events.

[`timezone` ](#argument-timezone)· [`String` ](/reference/2026-01-01/scalars/string)· (optional) Timezone used when looking for conflicting events. Will default to timezone of provider if not provided.

[`current_appt_id` ](#argument-current-appt-id)· [`String` ](/reference/2026-01-01/scalars/string)· (optional) used to skip checking for conflicts on single appointments.

[`is_group_appt` ](#argument-is-group-appt)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· (optional) whether an existing appointment being checked is a group appointment or not.

[`is_editing` ](#argument-is-editing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· (optional) whether editing an existing appointment or not.

[`additional_providers` ](#argument-additional-providers)· [`String` ](/reference/2026-01-01/scalars/string)· (optional) for group appointments where org members are added as attending

[`length_in_minutes` ](#argument-length-in-minutes)· [`Int` ](/reference/2026-01-01/scalars/int)· (optional) used when checking for conflicts for blocks, which have no appointment type with length

## Returns

[`[AppointmentBookingWarning!]`](/reference/2026-01-01/objects/appointmentbookingwarning)

## Example

```
query appointmentBookingWarnings(
  $appointment_type_id: ID
  $attendee_ids: [ID]
  $date: ISO8601DateTime
  $is_repeating: Boolean
  $provider_id: ID
  $repeat_interval: String
  $repeat_times: String
  $recurring_appt_id: ID
  $time: String
  $timezone: String
  $current_appt_id: String
  $is_group_appt: Boolean
  $is_editing: Boolean
  $additional_providers: String
  $length_in_minutes: Int
) {
  appointmentBookingWarnings(
    appointment_type_id: $appointment_type_id
    attendee_ids: $attendee_ids
    date: $date
    is_repeating: $is_repeating
    provider_id: $provider_id
    repeat_interval: $repeat_interval
    repeat_times: $repeat_times
    recurring_appt_id: $recurring_appt_id
    time: $time
    timezone: $timezone
    current_appt_id: $current_appt_id
    is_group_appt: $is_group_appt
    is_editing: $is_editing
    additional_providers: $additional_providers
    length_in_minutes: $length_in_minutes
  ) {
    category
    potential_issue_ids
    potential_issues
    subtitle
  }
}
```
