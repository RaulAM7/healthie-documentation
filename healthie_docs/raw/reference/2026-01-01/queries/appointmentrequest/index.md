---
title: appointmentRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentrequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentrequest/index.md
---

Fetch a single appointment requests for a provider or organization

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the appointment request

## Returns

[`AppointmentRequestType`](/reference/2026-01-01/objects/appointmentrequesttype)

## Example

```
query appointmentRequest($id: ID!) {
  appointmentRequest(id: $id) {
    appointment_location
    appointment_type
    booking_params
    closed_at
    closed_by
    created_at
    current_status
    email
    first_appointment
    first_name
    id
    last_name
    patient
    phone
    provider
    provider_notes
    reason
    selected_contact_type
    selected_state
    slots
    timezone
  }
}
```
