---
title: appointmentSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentsetting/index.md
---

fetch a Appointment Setting by id (considered public)

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`AppointmentSetting`](/reference/2026-01-01/objects/appointmentsetting)

## Example

```
query appointmentSetting($id: ID, $provider_id: ID) {
  appointmentSetting(id: $id, provider_id: $provider_id) {
    accepted_insurance_plans
    allow_appointment_type_pricing
    allow_clients_to_cancel_appt
    allow_clients_to_reschedule_appt
    allow_external_videochat_urls
    allow_past_appointment_rescheduling
    allow_specific_client_pricing
    allow_specific_provider_pricing
    always_send_confirm_notification
    appointment_locations
    appointment_type_confirmed_email
    appointment_type_reminder_email
    appointment_type_reminder_override
    appointment_type_website_booking_email
    appt_type_confirmed_email
    appt_type_reminder_email
    appt_type_website_booking_email
    ask_clients_to_confirm
    ask_to_confirm_via_text
    auto_charge_enabled
    auto_create_cms1500
    auto_invoicing
    auto_schedule_charges_for_late_cancellation_no_show
    auto_submit_cms1500
    base_calendar_interval
    booking_interval_restriction
    buffer
    calendar_color_schemes
    calendar_text
    cant_cancel_message
    cant_reschedule_message
    charge_for_occurred_appts
    client_cancel_reason_required
    client_should_call_provider
    clients_have_billing
    confirm_by_default
    contact_type_overrides
    default_appt_form_to_group
    default_charting_template_id
    default_charting_template_name
    default_group_charting_template
    default_to_zoom
    default_video_service
    disallowed_reschedulable_statuses
    enable_appointment_requests
    enable_checked_in_status
    enable_late_cancellation_status
    end_time
    fb_pixel
    hide_insurance_getting_started_info
    hide_link
    id
    insurance_eligibility_integration
    insurance_specific_cpt_code_pricing
    invoice_clients_without_payment_method
    late_cancellation_fee
    max_days_in_future
    minimum_advance_cancel_time
    minimum_advance_reschedule_time
    minimum_advance_schedule_time
    minimum_days_in_advance
    no_show_fee
    owner
    patient_reschedule_count_cap
    pm_statuses
    prevent_client_booking
    prevent_no_credit_booking
    provider_cancel_reason_required
    reply_to_provider
    require_selected_location_for_all_contact_types
    restore_credit_on_cancel
    same_day_appointments
    send_appointment_cancellation_email
    send_appointment_update_email
    send_booking_notice
    send_email_before_appointment
    send_embeddable_appt_creator_email
    send_intake_forms_reminder
    send_push_before_appointment
    send_reminder_four_days_before
    send_reminder_one_day_before
    send_reminder_one_hour_before
    send_reminder_three_days_before
    send_reminder_two_days_before
    send_reminder_two_hours_before
    send_text_reminder_five_minutes_before
    send_text_reminder_four_days_before
    send_text_reminder_one_day_before
    send_text_reminder_one_hour_before
    send_text_reminder_three_days_before
    send_text_reminder_two_days_before
    send_text_reminder_two_hours_before
    set_default_videochat_url
    show_care_plans
    show_cms1500s
    show_faxes
    show_insurance_authorization
    show_office_ally
    show_superbills
    start_fb_pixel
    start_time
    times_by_appointment_type
    times_by_contact_type
    times_by_location
    updated_at
    use_appointment_type_cpt_units_and_fees
    use_client_credit_system
    use_client_sources
    use_zoom_waiting_room
    user_id
    video_url_default
    zoom_open_preference
  }
}
```
