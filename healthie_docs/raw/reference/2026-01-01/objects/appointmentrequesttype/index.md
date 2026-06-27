---
title: AppointmentRequestType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentrequesttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentrequesttype/index.md
---

Appointment Request for a provider waitlist

## Fields

[`appointment_location` ](#field-appointment-location)· [`AppointmentLocation` ](/reference/2026-01-01/objects/appointmentlocation)· The appointment location requested for the appointment

[`appointment_type` ](#field-appointment-type)· [`AppointmentType` ](/reference/2026-01-01/objects/appointmenttype)· The appointment type requested for the appointment

[`booking_params` ](#field-booking-params)· [`JSON` ](/reference/2026-01-01/scalars/json)· The booking parameters for the appointment request

[`closed_at` ](#field-closed-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date and time the appointment request was closed

[`closed_by` ](#field-closed-by)· [`User` ](/reference/2026-01-01/objects/user)· The user who closed the appointment request

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time the appointment request was created

[`current_status` ](#field-current-status)· [`AppointmentRequestStatus!` ](/reference/2026-01-01/enums/appointmentrequeststatus)· required · The current status of the appointment request

[`email` ](#field-email)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The email address of the patient requesting the appointment

[`first_appointment` ](#field-first-appointment)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· The first appointment scheduled from this request

[`first_name` ](#field-first-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The first name of the patient requesting the appointment

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the appointment request

[`last_name` ](#field-last-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The last name of the patient requesting the appointment

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· If there is an existing patient record for the patient requesting the appointment

[`phone` ](#field-phone)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The phone number of the patient requesting the appointment

[`provider` ](#field-provider)· [`User` ](/reference/2026-01-01/objects/user)· The provider assigned to the appointment request, if provided

[`provider_notes` ](#field-provider-notes)· [`String` ](/reference/2026-01-01/scalars/string)· The notes for the appointment request

[`reason` ](#field-reason)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The notes for the appointment request

[`selected_contact_type` ](#field-selected-contact-type)· [`String` ](/reference/2026-01-01/scalars/string)· The contact type selected for the appointment request

[`selected_state` ](#field-selected-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state selected for the appointment request

[`slots` ](#field-slots)· [`[AppointmentRequestSlotType!]!` ](/reference/2026-01-01/objects/appointmentrequestslottype)· required · The slots for the appointment request

[`timezone` ](#field-timezone)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The timezone of the patient requesting the appointment

## Used By

[`AppointmentRequestTypeConnection.nodes`](/reference/2026-01-01/objects/appointmentrequesttypeconnection)

[`AppointmentRequestTypeEdge.node`](/reference/2026-01-01/objects/appointmentrequesttypeedge)

[`createAppointmentRequestPayload.appointmentRequest`](/reference/2026-01-01/objects/createappointmentrequestpayload)

[`deleteAppointmentRequestPayload.appointmentRequest`](/reference/2026-01-01/objects/deleteappointmentrequestpayload)

[`updateAppointmentRequestPayload.appointmentRequest`](/reference/2026-01-01/objects/updateappointmentrequestpayload)

[`Query.appointmentRequest`](/reference/2026-01-01/queries/appointmentrequest)

## Definition

```
"""
Appointment Request for a provider waitlist
"""
type AppointmentRequestType {
  """
  The appointment location requested for the appointment
  """
  appointment_location: AppointmentLocation


  """
  The appointment type requested for the appointment
  """
  appointment_type: AppointmentType


  """
  The booking parameters for the appointment request
  """
  booking_params: JSON


  """
  The date and time the appointment request was closed
  """
  closed_at: ISO8601DateTime


  """
  The user who closed the appointment request
  """
  closed_by: User


  """
  The date and time the appointment request was created
  """
  created_at: ISO8601DateTime!


  """
  The current status of the appointment request
  """
  current_status: AppointmentRequestStatus!


  """
  The email address of the patient requesting the appointment
  """
  email: String!


  """
  The first appointment scheduled from this request
  """
  first_appointment: Appointment


  """
  The first name of the patient requesting the appointment
  """
  first_name: String!


  """
  The unique identifier of the appointment request
  """
  id: ID!


  """
  The last name of the patient requesting the appointment
  """
  last_name: String!


  """
  If there is an existing patient record for the patient requesting the appointment
  """
  patient: User


  """
  The phone number of the patient requesting the appointment
  """
  phone: String!


  """
  The provider assigned to the appointment request, if provided
  """
  provider: User


  """
  The notes for the appointment request
  """
  provider_notes: String


  """
  The notes for the appointment request
  """
  reason: String!


  """
  The contact type selected for the appointment request
  """
  selected_contact_type: String


  """
  The state selected for the appointment request
  """
  selected_state: String


  """
  The slots for the appointment request
  """
  slots: [AppointmentRequestSlotType!]!


  """
  The timezone of the patient requesting the appointment
  """
  timezone: String!
}
```
