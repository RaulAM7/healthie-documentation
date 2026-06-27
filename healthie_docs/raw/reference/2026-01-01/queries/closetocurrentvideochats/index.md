---
title: closeToCurrentVideoChats | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/closetocurrentvideochats/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/closetocurrentvideochats/index.md
---

get current video chats for a user.

## Arguments

[`user_id` ](#argument-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· User to get video chats that are starting in the next 10 minutes

## Returns

[`[Appointment!]`](/reference/2026-01-01/objects/appointment)

## Example

```
query closeToCurrentVideoChats($user_id: String) {
  closeToCurrentVideoChats(user_id: $user_id) {
    actual_duration
    add_to_gcal_link
    appointment_category
    appointment_inclusions_count
    appointment_label
    appointment_location_id
    appointment_request_id
    appointment_type
    appointment_type_id
    assigned_groups
    attended_clients
    attendees
    attendees_on_waitlist
    backgroundColor
    can_be_rescheduled
    can_client_cancel
    can_client_reschedule
    cancellation_reason
    client_confirmed
    client_updating
    confirmed
    connected_chart_note_locked
    connected_chart_note_string
    contact_type
    conversation_id
    created_at
    credit_was_used
    current_position_in_recurring_series
    date
    default_color
    deleted_at
    effective_pricing_method
    end
    external_id_type
    external_videochat_url
    filled_embed_form
    form_answer_group
    form_answer_groups
    generated_form_answer_group
    generated_token
    has_expanded_vbc_charting_fields
    has_in_progress_job
    id
    initiator_id
    insurance_billing_enabled
    is_blocker
    is_group
    is_zoom_chat
    last_client_conversation_id
    last_updated_by_id
    late_cancellation_fee
    length
    location
    locationResource
    max_attendees
    metadata
    minimum_advance_cancel_time
    minimum_advance_reschedule_time
    no_show_fee
    notes
    organization_id
    other_cancellation_reason
    other_party_id
    patient_reschedule_count
    pm_status
    pm_status_changed_at
    pm_status_last_changed_by_id
    pricing_info
    provider
    provider_name
    providers
    reason
    recurring_appointment
    requested_payment
    resourceId
    room_id
    scheduled_by
    session_id
    should_create_cms1500_for_occurred_appointments
    start
    textColor
    time_recurring_override
    timezone_abbr
    title
    transcripts
    unauthenticated_ics_link
    updated_at
    use_embedded_zoom
    use_zoom
    user
    user_id
    will_be_scribed
    zoom_appointment
    zoom_cloud_recording_files
    zoom_cloud_recording_urls
    zoom_co_host_links
    zoom_dial_in_info
    zoom_dial_in_info_html
    zoom_dial_in_numbers_json
    zoom_join_url
    zoom_meeting_id
    zoom_start_url
  }
}
```
