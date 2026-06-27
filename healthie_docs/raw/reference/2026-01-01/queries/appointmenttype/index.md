---
title: appointmentType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmenttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmenttype/index.md
---

fetch an appointment type by id (considered public)

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`AppointmentType`](/reference/2026-01-01/objects/appointmenttype)

## Example

```
query appointmentType($id: ID) {
  appointmentType(id: $id) {
    advance_pricing_for_clients_count
    advance_pricing_for_providers_count
    appointment_autocomplete_form
    appointment_setting
    appointment_type_cpt_code
    auto_increase_charge_for_actual_duration
    availability_exists_for
    available_contact_types
    bookable_by_groups
    bookable_groups
    bookable_without_group
    client_call_provider
    client_display_description
    client_display_name
    client_facing_display_name
    clients_can_book
    clients_have_credit
    created_at
    custom_text_reminder_body
    deleted_at
    dont_ask_for_reason
    embed_question_form_id
    form_requests_after_appointment
    form_requests_after_appointment_booking
    form_requests_before_appointment
    has_available_group_appts
    has_specific_appointment_settings
    id
    insurance_billing_enabled
    is_group
    is_waitlist_enabled
    length
    metadata
    name
    no_availability_message
    organization_id
    position
    price_and_cpt_price
    pricing
    pricing_info
    pricing_option
    provider_appt_type_connections
    require_cc_at_booking
    require_in_state_clients
    require_specific_providers
    row_order
    time_on_label
    updated_at
    user_group
    user_group_id
    user_id
    valid_state_licensing_for
  }
}
```
