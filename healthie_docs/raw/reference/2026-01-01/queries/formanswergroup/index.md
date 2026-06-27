---
title: formAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/formanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/formanswergroup/index.md
---

Fetch a form answer group by id

## Arguments

[`for_superbills` ](#argument-for-superbills)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`external_id` ](#argument-external-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`appointment_form_answer_group_connection_id` ](#argument-appointment-form-answer-group-connection-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Return a FormAnswerGroup based on an associated appointment\_form\_answer\_group\_connection\_id

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`ids` ](#argument-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`track_opened_event` ](#argument-track-opened-event)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If TRUE, create form history 'opened' event

## Returns

[`FormAnswerGroup`](/reference/2026-01-01/objects/formanswergroup)

## Example

```
query formAnswerGroup(
  $for_superbills: Boolean
  $external_id: ID
  $appointment_form_answer_group_connection_id: ID
  $id: ID
  $ids: [ID]
  $track_opened_event: Boolean
) {
  formAnswerGroup(
    for_superbills: $for_superbills
    external_id: $external_id
    appointment_form_answer_group_connection_id: $appointment_form_answer_group_connection_id
    id: $id
    ids: $ids
    track_opened_event: $track_opened_event
  ) {
    appointment
    autoscored_sections
    chart_note_status
    charting_note_addendums
    cms1500
    created_at
    current_summary
    custom_module_form
    deleted_at
    documents
    external_id
    filler
    finished
    form_answer_group_audit_events
    form_answer_group_prescriptions
    form_answer_group_signings
    form_answer_group_users_connections
    form_answers
    frozen
    group_appointment_attendees
    id
    individual_client_notes
    individual_note
    is_group_appt_note
    is_locked
    lab_orders
    locked_at
    locked_by
    metadata
    name
    narx_checks
    offering_with_recommended_products
    provider_can_add_addendum
    provider_can_lock
    provider_can_sign
    provider_can_unlock
    record_created_at
    requested_form_completion
    updated_at
    user
    user_id
    versioning_stream_name
  }
}
```
