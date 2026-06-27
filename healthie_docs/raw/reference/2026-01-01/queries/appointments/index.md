---
title: appointments | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointments/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointments/index.md
---

Fetch paginated appointment collection

## Arguments

[`colorSchemeId` ](#argument-colorschemeid)· [`String` ](/reference/2026-01-01/scalars/string)· Sets the color scheme ID for background color calculation.

[`currentWeek` ](#argument-currentweek)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns appointments for the current week based on the user's timezone.

[`endDate` ](#argument-enddate)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· End of the date range, must be sent in with a start date.

[`exclude_appointments_with_invoice` ](#argument-exclude-appointments-with-invoice)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, all appointments with invoices will be excluded.

[`filter` ](#argument-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Options are 'future', 'past', 'ended', 'didnt-occur'.

[`filter_by_appointment_location_ids` ](#argument-filter-by-appointment-location-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Returns appointments of the specified appointment locations. Overrides filter\_by\_location\_id.

[`filter_by_appointment_status` ](#argument-filter-by-appointment-status)· [`String` ](/reference/2026-01-01/scalars/string)· Filters appointments by a single appointment status. Overridden by filter\_by\_appointment\_statuses.

[`filter_by_appointment_statuses` ](#argument-filter-by-appointment-statuses)· [`[String]` ](/reference/2026-01-01/scalars/string)· Returns appointments of the specified appointment statuses. Overrides filter\_by\_appointment\_status.

[`filter_by_appointment_type_id` ](#argument-filter-by-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filters appointments by a single appointment type. Overridden by filter\_by\_appointment\_type\_ids.

[`filter_by_appointment_type_ids` ](#argument-filter-by-appointment-type-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Returns appointments of the specified appointment types. Overrides filter\_by\_appointment\_type\_id.

[`filter_by_contact_types` ](#argument-filter-by-contact-types)· [`String` ](/reference/2026-01-01/scalars/string)· Comma-separated list of contact types to filter appointments by.

[`filter_by_chart_note_written` ](#argument-filter-by-chart-note-written)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only appointments without an associated chart note will be returned. When false, only appointments with an associated chart note will be returned. If nil, has no effect.

[`filter_by_client_confirmed` ](#argument-filter-by-client-confirmed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only client-confirmed appointments. When false, returns only appointments not confirmed by the client.

[`filter_by_location_id` ](#argument-filter-by-location-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filters appointments by a single location. Overridden by filter\_by\_appointment\_location\_ids.

[`filter_by_provider_confirmed` ](#argument-filter-by-provider-confirmed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only provider-confirmed appointments. When false, returns only appointments not confirmed by the provider.

[`filter_synced_appointments` ](#argument-filter-synced-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, no pulled-in synced appointments will be included.

[`filter_by_invoices` ](#argument-filter-by-invoices)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only appointments up to the next future scheduled appointment will be included.

[`use_provider_inclusions` ](#argument-use-provider-inclusions)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, uses provider inclusions for lookup of providers.

[`include_blockers` ](#argument-include-blockers)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, includes blocker appointments in the results.

[`include_nil_blockers` ](#argument-include-nil-blockers)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns blocking appointments with no appointment type/location/status.

[`include_suborganizations` ](#argument-include-suborganizations)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, includes all providers in the organization and sub-organizations.

[`insurance_plan_ids` ](#argument-insurance-plan-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Filters providers by insurance plans. Used in conjunction with is\_org.

[`is_active` ](#argument-is-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only active appointments.

[`is_confirmed` ](#argument-is-confirmed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only confirmed appointments. When false, returns only unconfirmed appointments.

[`is_org` ](#argument-is-org)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns appointments for all providers in the org.

[`is_upcoming` ](#argument-is-upcoming)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only upcoming appointments.

[`is_with_clients` ](#argument-is-with-clients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only appointments that include a client.

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Keyword search term for filtering appointments.

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filters appointments for a specific provider.

[`provider_ids` ](#argument-provider-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Filters appointments for multiple providers.

[`show_appointments` ](#argument-show-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, excludes regular appointments and only returns synced appointments.

[`sort_by` ](#argument-sort-by)· [`String` ](/reference/2026-01-01/scalars/string)· Allowed options are date\_desc, date\_asc, created\_at\_desc, created\_at\_asc, updated\_at\_desc, and updated\_at\_asc

[`order_by` ](#argument-order-by)· [`AppointmentOrderKeys` ](/reference/2026-01-01/enums/appointmentorderkeys)· Specifies the sort order for the returned appointments.

[`specificDay` ](#argument-specificday)· [`String` ](/reference/2026-01-01/scalars/string)· Filters appointments to a specific day.

[`startDate` ](#argument-startdate)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Start of the date range, must be sent in with an end date.

[`unconfirmed` ](#argument-unconfirmed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only unconfirmed appointments.

[`organization_id` ](#argument-organization-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the organization to pull appointments for. Defaults to current user organization if not set. Ignored if is\_org is false.

[`user_id` ](#argument-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filters appointments for a specific client.

[`with_all_statuses` ](#argument-with-all-statuses)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, includes appointments with all statuses, not just active ones.

[`with_others` ](#argument-with-others)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, excludes blocker appointments from the results.

[`without_status` ](#argument-without-status)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only appointments without a status.

[`attendee_ids` ](#argument-attendee-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Returns appointments for the specified attendee IDs.

[`state_license` ](#argument-state-license)· [`String` ](/reference/2026-01-01/scalars/string)· Filters providers by state license. Used in conjunction with is\_org.

[`tag_ids` ](#argument-tag-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Filters providers by tags. Used in conjunction with is\_org.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`AppointmentPaginationConnection`](/reference/2026-01-01/objects/appointmentpaginationconnection)

## Example

```
query appointments(
  $colorSchemeId: String
  $currentWeek: Boolean
  $endDate: ISO8601DateTime
  $exclude_appointments_with_invoice: Boolean
  $filter: String
  $filter_by_appointment_location_ids: [ID]
  $filter_by_appointment_status: String
  $filter_by_appointment_statuses: [String]
  $filter_by_appointment_type_id: ID
  $filter_by_appointment_type_ids: [ID]
  $filter_by_contact_types: String
  $filter_by_chart_note_written: Boolean
  $filter_by_client_confirmed: Boolean
  $filter_by_location_id: ID
  $filter_by_provider_confirmed: Boolean
  $filter_synced_appointments: Boolean
  $filter_by_invoices: Boolean
  $use_provider_inclusions: Boolean
  $include_blockers: Boolean
  $include_nil_blockers: Boolean
  $include_suborganizations: Boolean
  $insurance_plan_ids: [ID]
  $is_active: Boolean
  $is_confirmed: Boolean
  $is_org: Boolean
  $is_upcoming: Boolean
  $is_with_clients: Boolean
  $keywords: String
  $provider_id: ID
  $provider_ids: [ID]
  $show_appointments: Boolean
  $sort_by: String
  $order_by: AppointmentOrderKeys
  $specificDay: String
  $startDate: ISO8601DateTime
  $unconfirmed: Boolean
  $organization_id: ID
  $user_id: ID
  $with_all_statuses: Boolean
  $with_others: Boolean
  $without_status: Boolean
  $attendee_ids: [ID]
  $state_license: String
  $tag_ids: [ID]
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  appointments(
    colorSchemeId: $colorSchemeId
    currentWeek: $currentWeek
    endDate: $endDate
    exclude_appointments_with_invoice: $exclude_appointments_with_invoice
    filter: $filter
    filter_by_appointment_location_ids: $filter_by_appointment_location_ids
    filter_by_appointment_status: $filter_by_appointment_status
    filter_by_appointment_statuses: $filter_by_appointment_statuses
    filter_by_appointment_type_id: $filter_by_appointment_type_id
    filter_by_appointment_type_ids: $filter_by_appointment_type_ids
    filter_by_contact_types: $filter_by_contact_types
    filter_by_chart_note_written: $filter_by_chart_note_written
    filter_by_client_confirmed: $filter_by_client_confirmed
    filter_by_location_id: $filter_by_location_id
    filter_by_provider_confirmed: $filter_by_provider_confirmed
    filter_synced_appointments: $filter_synced_appointments
    filter_by_invoices: $filter_by_invoices
    use_provider_inclusions: $use_provider_inclusions
    include_blockers: $include_blockers
    include_nil_blockers: $include_nil_blockers
    include_suborganizations: $include_suborganizations
    insurance_plan_ids: $insurance_plan_ids
    is_active: $is_active
    is_confirmed: $is_confirmed
    is_org: $is_org
    is_upcoming: $is_upcoming
    is_with_clients: $is_with_clients
    keywords: $keywords
    provider_id: $provider_id
    provider_ids: $provider_ids
    show_appointments: $show_appointments
    sort_by: $sort_by
    order_by: $order_by
    specificDay: $specificDay
    startDate: $startDate
    unconfirmed: $unconfirmed
    organization_id: $organization_id
    user_id: $user_id
    with_all_statuses: $with_all_statuses
    with_others: $with_others
    without_status: $without_status
    attendee_ids: $attendee_ids
    state_license: $state_license
    tag_ids: $tag_ids
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
