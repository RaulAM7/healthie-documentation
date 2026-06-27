---
title: Appointment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointment/index.md
---

An appointment object containing information about the appointment, including the attendees, date, location, and more.

## Fields

[`actual_duration` ](#field-actual-duration)· [`Int` ](/reference/2026-01-01/scalars/int)· The actual length of the appointment (in minutes). Filled in by the provider after the appointment

[`add_to_gcal_link` ](#field-add-to-gcal-link)· [`String` ](/reference/2026-01-01/scalars/string)· Get link to add appointment to google calendar

[`appointment_category` ](#field-appointment-category)· [`String` ](/reference/2026-01-01/scalars/string)· Category of the appointment: expected values are "Individual" and "Group"

[`appointment_inclusions_count` ](#field-appointment-inclusions-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of people (both providers and attendees) who are in the appointment

[`appointment_label` ](#field-appointment-label)· [`String` ](/reference/2026-01-01/scalars/string)· A label for the appointment

[`appointment_location_id` ](#field-appointment-location-id)· [`String` ](/reference/2026-01-01/scalars/string)· the ID of the appointment location

[`appointment_request_id` ](#field-appointment-request-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment request this appointment fulfills

[`appointment_type` ](#field-appointment-type)· [`AppointmentType` ](/reference/2026-01-01/objects/appointmenttype)· The type of the appointment

[`appointment_type_id` ](#field-appointment-type-id)· [`Int` ](/reference/2026-01-01/scalars/int)· The ID of the type of appointment this is

[`assigned_groups` ](#field-assigned-groups)· [`[UserGroup!]` ](/reference/2026-01-01/objects/usergroup)· List of assigned user groups to the group appointment

[`attended_clients` ](#field-attended-clients)· [`[AppointmentInclusionType!]` ](/reference/2026-01-01/objects/appointmentinclusiontype)· Client inclusions which includes all attendees even if they didnt show up for the appointment

[`attendees` ](#field-attendees)· [`[User!]!` ](/reference/2026-01-01/objects/user)· required · All attendees for the appointment.

[`attendees_on_waitlist` ](#field-attendees-on-waitlist)· [`[User!]` ](/reference/2026-01-01/objects/user)· Pending Appointment inclusions

[`backgroundColor` ](#field-backgroundcolor)· [`String` ](/reference/2026-01-01/scalars/string)· The backgroundColor color of the appointment

[`can_be_rescheduled` ](#field-can-be-rescheduled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Returns true if the patient can reschedule the appointment

[`can_client_cancel` ](#field-can-client-cancel)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if client able to cancel an appointment

[`can_client_reschedule` ](#field-can-client-reschedule)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if client able to reschedule an appointment

[`cancellation_reason` ](#field-cancellation-reason)· [`CancellationReason` ](/reference/2026-01-01/objects/cancellationreason)· The cancellation reason for this appointment

[`client_confirmed` ](#field-client-confirmed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· false if the client needs to confirm the appointment, and has not

[`client_updating` ](#field-client-updating)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment updating on client side or not

[`confirmed` ](#field-confirmed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider has confirmed the appointment or not

[`connected_chart_note_locked` ](#field-connected-chart-note-locked)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if appointment is locked

[`connected_chart_note_string` ](#field-connected-chart-note-string)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the connected chart note

[`contact_type` ](#field-contact-type)· [`String` ](/reference/2026-01-01/scalars/string)· How the provider and attendees will connect (i.e In-Person or through the phone)

[`conversation_id` ](#field-conversation-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of conversation related to the current appointment(only for group appts 10/2020)

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time that the appointment was created

[`credit_was_used` ](#field-credit-was-used)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if a credit was used for this appointment

[`current_position_in_recurring_series` ](#field-current-position-in-recurring-series)· [`Int` ](/reference/2026-01-01/scalars/int)· The position of the appointment in the recurring series

[`date` ](#field-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date and time of the appointment

[`default_color` ](#field-default-color)· [`String` ](/reference/2026-01-01/scalars/string)· default color of appointment based on confirmation/type

[`deleted_at` ](#field-deleted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time the appointment was deleted. It is blank if the appointment is not deleted.

[`effective_pricing_method` ](#field-effective-pricing-method)· [`AppointmentPricingMethod` ](/reference/2026-01-01/enums/appointmentpricingmethod)· The effective pricing method for this appointment (calculated or stored)

[`end` ](#field-end)· [`String` ](/reference/2026-01-01/scalars/string)· The end time of the appointment

[`external_id_type` ](#field-external-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of connection to an external calendar

[`external_videochat_url` ](#field-external-videochat-url)· [`String` ](/reference/2026-01-01/scalars/string)· A URL to an external video chat site for the session

[`filled_embed_form` ](#field-filled-embed-form)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· The custom answers filled out by the booker of the appointment

[`form_answer_group` ](#field-form-answer-group)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· The Form answer group first associated with the appointment

[`form_answer_groups` ](#field-form-answer-groups)· [`[FormAnswerGroup!]` ](/reference/2026-01-01/objects/formanswergroup)· All Form answer groups associated with the appointment

[`generated_form_answer_group` ](#field-generated-form-answer-group)· [`GeneratedFormAnswerGroupType` ](/reference/2026-01-01/objects/generatedformanswergrouptype)· The AI Scribe generated form answer group associated with the appointment

[`generated_token` ](#field-generated-token)· [`String` ](/reference/2026-01-01/scalars/string)· open tok token

[`has_expanded_vbc_charting_fields` ](#field-has-expanded-vbc-charting-fields)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, additional group charting fields are visible in the Healthie UI

[`has_in_progress_job` ](#field-has-in-progress-job)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Returns true if the appointment has in progress job

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the appointment

[`initiator_id` ](#field-initiator-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of user that created of appointment

[`insurance_billing_enabled` ](#field-insurance-billing-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, insurance billing will be enabled for this appointment

[`is_blocker` ](#field-is-blocker)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether this appointment is specifically meant to block availability

[`is_group` ](#field-is-group)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicates whether it's a group appointment

[`is_zoom_chat` ](#field-is-zoom-chat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the video chat uses Zoom or Healthie Default telehealth

[`last_client_conversation_id` ](#field-last-client-conversation-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of last conversation between provider and client in appointment

[`last_updated_by_id` ](#field-last-updated-by-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the provider who last updated the appointment record, if available

[`late_cancellation_fee` ](#field-late-cancellation-fee)· [`Int` ](/reference/2026-01-01/scalars/int)· The Late Cancellation Fee (in cents) for this appointment

[`length` ](#field-length)· [`Int` ](/reference/2026-01-01/scalars/int)· The length of the appointment (in minutes)

[`location` ](#field-location)· [`String` ](/reference/2026-01-01/scalars/string)· The plaintext location of the appointment (only used for in-person appointments)

[`locationResource` ](#field-locationresource)· [`String` ](/reference/2026-01-01/scalars/string)· Location Resource

[`max_attendees` ](#field-max-attendees)· [`String` ](/reference/2026-01-01/scalars/string)· How many attendees can register for an appointment (only used for Group Appointments)

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· a serialized JSON string of metadata

[`minimum_advance_cancel_time` ](#field-minimum-advance-cancel-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Minimum time before the appointment when client can still cancel it

[`minimum_advance_reschedule_time` ](#field-minimum-advance-reschedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Minimum time (in minutes) before the appointment when client can still reschedule it

[`no_show_fee` ](#field-no-show-fee)· [`Int` ](/reference/2026-01-01/scalars/int)· The No Show Fee (in cents) for this appointment

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Quick notes on the appointment (only visible to providers)

[`organization_id` ](#field-organization-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the organization the appointment belongs to

[`other_cancellation_reason` ](#field-other-cancellation-reason)· [`String` ](/reference/2026-01-01/scalars/string)· Free text reason when "Other" cancellation reason is selected

[`other_party_id` ](#field-other-party-id)· [`Int` ](/reference/2026-01-01/scalars/int)· The id of the provider

[`patient_reschedule_count` ](#field-patient-reschedule-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of times a patient rescheduled an appointment

[`pm_status` ](#field-pm-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the appointment. Can be one of "Occurred", "No-Show", "Re-Scheduled", "Cancelled." If enabled, "Late Cancellation" and "Checked-In" are also valid.

[`pm_status_changed_at` ](#field-pm-status-changed-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date and time the status of the appointment was last updated

[`pm_status_last_changed_by_id` ](#field-pm-status-last-changed-by-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user who last changed the status of the appointment, if available

[`pricing_info` ](#field-pricing-info)· [`AppointmentPricingInfoType` ](/reference/2026-01-01/objects/appointmentpricinginfotype)· Get the pricing info for this appointment

[`provider` ](#field-provider)· [`User` ](/reference/2026-01-01/objects/user)· The provider for the appointment

[`provider_name` ](#field-provider-name)· [`String` ](/reference/2026-01-01/scalars/string)· Provider name

[`providers` ](#field-providers)· [`[User!]!` ](/reference/2026-01-01/objects/user)· required · All providers for the appointment.

[`reason` ](#field-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The clients reason for scheduling the appointment

[`recurring_appointment` ](#field-recurring-appointment)· [`RecurringAppointment` ](/reference/2026-01-01/objects/recurringappointment)· The related recurring appointment series

[`recurring_appointment_id` ](#field-recurring-appointment-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the recurring appointment

deprecated

Use recurring\_appointment instead

[`repeat` ](#field-repeat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether this is a repeating appointment or not

deprecated

Use recurring\_appointment instead

[`repeat_interval` ](#field-repeat-interval)· [`String` ](/reference/2026-01-01/scalars/string)· How often to repeat the appointment (e.g Daily or Monthly)

deprecated

Use recurring\_appointment instead

[`repeat_times` ](#field-repeat-times)· [`Int` ](/reference/2026-01-01/scalars/int)· How many times does the appointment repeat

deprecated

Use recurring\_appointment instead

[`requested_payment` ](#field-requested-payment)· [`RequestedPayment` ](/reference/2026-01-01/objects/requestedpayment)· A requested payment for this appointment

[`resourceId` ](#field-resourceid)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user, used for the calendar

[`room_id` ](#field-room-id)· [`ID` ](/reference/2026-01-01/scalars/id)· the ID of the room

[`scheduled_by` ](#field-scheduled-by)· [`String` ](/reference/2026-01-01/scalars/string)· A string containing info on how the appointment was scheduled

[`session_id` ](#field-session-id)· [`String` ](/reference/2026-01-01/scalars/string)· The OpenTok session ID for the appointment

[`should_create_cms1500_for_occurred_appointments` ](#field-should-create-cms1500-for-occurred-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, a cms1500 should be created when the appointment status is set to occurred

[`start` ](#field-start)· [`String` ](/reference/2026-01-01/scalars/string)· The start time of the appointment

[`textColor` ](#field-textcolor)· [`String` ](/reference/2026-01-01/scalars/string)· The font color of the appointment

[`time_recurring_override` ](#field-time-recurring-override)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the time of this appointment has been separated from the other recurring appointments in the series

[`timezone_abbr` ](#field-timezone-abbr)· [`String` ](/reference/2026-01-01/scalars/string)· Timezone abbreviation of the date of the appointment

[`title` ](#field-title)· [`String` ](/reference/2026-01-01/scalars/string)· The title of the appointment

[`transcripts` ](#field-transcripts)· [`[Transcript!]` ](/reference/2026-01-01/objects/transcript)· Can only be returned via querying a single appointment, not a collection. Transcripts for the appointment (in VTT format)

[`unauthenticated_ics_link` ](#field-unauthenticated-ics-link)· [`String` ](/reference/2026-01-01/scalars/string)· Unauthenticated link to download an ICS file for the appointment

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last date and time that the appointment was updated

[`use_embedded_zoom` ](#field-use-embedded-zoom)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment should use embedded Zoom in browser

[`use_zoom` ](#field-use-zoom)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment is through Zoom or not

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The client in a 1:1 appointment

[`user_id` ](#field-user-id)· [`Int` ](/reference/2026-01-01/scalars/int)· The id of the client (if a 1:1 appointment). If a group appointment, will be nil

[`will_be_scribed` ](#field-will-be-scribed)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if this appointment is configured to be summarized by AI Scribe

[`zoom_appointment` ](#field-zoom-appointment)· [`ZoomAppointment` ](/reference/2026-01-01/objects/zoomappointment)· Zoom meeting info. Appointment should have a valid zoom link and the user should have the permission to access the meeting. Otherwise returns nil

[`zoom_cloud_recording_files` ](#field-zoom-cloud-recording-files)· [`[ZoomCloudRecordingFile!]` ](/reference/2026-01-01/objects/zoomcloudrecordingfile)· Detailed information about Zoom cloud recording files for this appointment

[`zoom_cloud_recording_urls` ](#field-zoom-cloud-recording-urls)· [`[String]` ](/reference/2026-01-01/scalars/string)· URLs for Zoom cloud recordings for this appointment

[`zoom_co_host_links` ](#field-zoom-co-host-links)· [`[ZoomCoHostLink!]` ](/reference/2026-01-01/objects/zoomcohostlink)· ZAK tokens for each org member co-host on this Zoom group appointment. Returns an empty array when the feature flag is disabled, there is no Zoom meeting, or there are no other org member providers with a valid zoom\_id.

[`zoom_dial_in_info` ](#field-zoom-dial-in-info)· [`String` ](/reference/2026-01-01/scalars/string)· The dial-in info provided by zoom if appoint has zoom links.(separated by newline characters)

[`zoom_dial_in_info_html` ](#field-zoom-dial-in-info-html)· [`String` ](/reference/2026-01-01/scalars/string)· The dial-in info provided by zoom if appoint has zoom links.(separated by break tags)

[`zoom_dial_in_numbers_json` ](#field-zoom-dial-in-numbers-json)· [`[String]` ](/reference/2026-01-01/scalars/string)· An array of JSON objects containing the different dial in numbers for the Zoom call

[`zoom_join_url` ](#field-zoom-join-url)· [`String` ](/reference/2026-01-01/scalars/string)· The join link for other attendees of the Zoom call

[`zoom_meeting_id` ](#field-zoom-meeting-id)· [`String` ](/reference/2026-01-01/scalars/string)· The Meeting ID for the Zoom call

[`zoom_start_url` ](#field-zoom-start-url)· [`String` ](/reference/2026-01-01/scalars/string)· The host link to start the Zoom call

## Used By

[`AppointmentCreditChange.appointment`](/reference/2026-01-01/objects/appointmentcreditchange)

[`AppointmentEdge.node`](/reference/2026-01-01/objects/appointmentedge)

[`AppointmentInclusionType.appointment`](/reference/2026-01-01/objects/appointmentinclusiontype)

[`AppointmentPaginationConnection.nodes`](/reference/2026-01-01/objects/appointmentpaginationconnection)

[`AppointmentRequestType.first_appointment`](/reference/2026-01-01/objects/appointmentrequesttype)

[`FormAnswerGroup.appointment`](/reference/2026-01-01/objects/formanswergroup)

[`GeneratedFormAnswerGroupType.appointment`](/reference/2026-01-01/objects/generatedformanswergrouptype)

[`PatientEncounter.appointment`](/reference/2026-01-01/objects/patientencounter)

[`RequestedPayment.appointment`](/reference/2026-01-01/objects/requestedpayment)

[`Subscription.appointmentUserDevicesSubscription`](/reference/2026-01-01/objects/subscription)

[`Subscription.groupAppointmentClientsAddedSubscription`](/reference/2026-01-01/objects/subscription)

[`User.appointments`](/reference/2026-01-01/objects/user)

[`User.last_app`](/reference/2026-01-01/objects/user)

[`User.next_app`](/reference/2026-01-01/objects/user)

[`User.upcoming_appointments`](/reference/2026-01-01/objects/user)

[`completeCheckoutPayload.appointment`](/reference/2026-01-01/objects/completecheckoutpayload)

[`completeCheckoutPayload.appointments`](/reference/2026-01-01/objects/completecheckoutpayload)

[`createAppointmentFormAnswerGroupConnectionPayload.appointment`](/reference/2026-01-01/objects/createappointmentformanswergroupconnectionpayload)

[`createAppointmentPayload.appointment`](/reference/2026-01-01/objects/createappointmentpayload)

[`deleteAppointmentPayload.appointment`](/reference/2026-01-01/objects/deleteappointmentpayload)

[`updateAppointmentPayload.appointment`](/reference/2026-01-01/objects/updateappointmentpayload)

[`Query.appointment`](/reference/2026-01-01/queries/appointment)

[`Query.closeToCurrentVideoChats`](/reference/2026-01-01/queries/closetocurrentvideochats)

[`Query.currentVideoChats`](/reference/2026-01-01/queries/currentvideochats)

[`Query.nextAppointment`](/reference/2026-01-01/queries/nextappointment)

## Definition

```
"""
An appointment object containing information about the appointment, including the attendees, date, location, and more.
"""
type Appointment {
  """
  The actual length of the appointment (in minutes). Filled in by the provider after the appointment
  """
  actual_duration: Int


  """
  Get link to add appointment to google calendar
  """
  add_to_gcal_link: String


  """
  Category of the appointment: expected values are "Individual" and "Group"
  """
  appointment_category: String


  """
  The number of people (both providers and attendees) who are in the appointment
  """
  appointment_inclusions_count: Int


  """
  A label for the appointment
  """
  appointment_label: String


  """
  the ID of the appointment location
  """
  appointment_location_id: String


  """
  The ID of the appointment request this appointment fulfills
  """
  appointment_request_id: ID


  """
  The type of the appointment
  """
  appointment_type: AppointmentType


  """
  The ID of the type of appointment this is
  """
  appointment_type_id: Int


  """
  List of assigned user groups to the group appointment
  """
  assigned_groups: [UserGroup!]


  """
  Client inclusions which includes all attendees even if they didnt show up for the appointment
  """
  attended_clients: [AppointmentInclusionType!]


  """
  All attendees for the appointment.
  """
  attendees: [User!]!


  """
  Pending Appointment inclusions
  """
  attendees_on_waitlist: [User!]


  """
  The backgroundColor color of the appointment
  """
  backgroundColor(
    """
    The time the appointment setting was last updated
    """
    appointment_setting_updated_at: ISO8601DateTime
  ): String


  """
  Returns true if the patient can reschedule the appointment
  """
  can_be_rescheduled: Boolean


  """
  True if client able to cancel an appointment
  """
  can_client_cancel: Boolean


  """
  True if client able to reschedule an appointment
  """
  can_client_reschedule: Boolean


  """
  The cancellation reason for this appointment
  """
  cancellation_reason: CancellationReason


  """
  false if the client needs to confirm the appointment, and has not
  """
  client_confirmed(
    """
    Whether or not the appointment requires client confirmation
    """
    known_requires_client_confirmed: Boolean
  ): Boolean


  """
  Whether the appointment updating on client side or not
  """
  client_updating: Boolean


  """
  The status of whether the provider has confirmed the appointment or not
  """
  confirmed: Boolean


  """
  True if appointment is locked
  """
  connected_chart_note_locked: Boolean


  """
  The status of the connected chart note
  """
  connected_chart_note_string: String


  """
  How the provider and attendees will connect (i.e In-Person or through the phone)
  """
  contact_type: String


  """
  The ID of conversation related to the current appointment(only for group appts 10/2020)
  """
  conversation_id: ID


  """
  The date and time that the appointment was created
  """
  created_at: ISO8601DateTime!


  """
  True if a credit was used for this appointment
  """
  credit_was_used: Boolean


  """
  The position of the appointment in the recurring series
  """
  current_position_in_recurring_series: Int


  """
  The date and time of the appointment
  """
  date: ISO8601DateTime


  """
  default color of appointment based on confirmation/type
  """
  default_color: String


  """
  The time the appointment was deleted. It is blank if the appointment is not deleted.
  """
  deleted_at: ISO8601DateTime


  """
  The effective pricing method for this appointment (calculated or stored)
  """
  effective_pricing_method: AppointmentPricingMethod


  """
  The end time of the appointment
  """
  end: String


  """
  The type of connection to an external calendar
  """
  external_id_type: String


  """
  A URL to an external video chat site for the session
  """
  external_videochat_url: String


  """
  The custom answers filled out by the booker of the appointment
  """
  filled_embed_form: FormAnswerGroup


  """
  The Form answer group first associated with the appointment
  """
  form_answer_group: FormAnswerGroup


  """
  All Form answer groups associated with the appointment
  """
  form_answer_groups: [FormAnswerGroup!]


  """
  The AI Scribe generated form answer group associated with the appointment
  """
  generated_form_answer_group: GeneratedFormAnswerGroupType


  """
  open tok token
  """
  generated_token: String


  """
  When true, additional group charting fields are visible in the Healthie UI
  """
  has_expanded_vbc_charting_fields: Boolean


  """
  Returns true if the appointment has in progress job
  """
  has_in_progress_job: Boolean


  """
  The unique identifier of the appointment
  """
  id: ID!


  """
  ID of user that created of appointment
  """
  initiator_id: ID


  """
  When true, insurance billing will be enabled for this appointment
  """
  insurance_billing_enabled: Boolean


  """
  The status of whether this appointment is specifically meant to block availability
  """
  is_blocker: Boolean


  """
  Indicates whether it's a group appointment
  """
  is_group: Boolean


  """
  The status of whether the video chat uses Zoom or Healthie Default telehealth
  """
  is_zoom_chat: Boolean


  """
  id of last conversation between provider and client in appointment
  """
  last_client_conversation_id: ID


  """
  The ID of the provider who last updated the appointment record, if available
  """
  last_updated_by_id: ID


  """
  The Late Cancellation Fee (in cents) for this appointment
  """
  late_cancellation_fee: Int


  """
  The length of the appointment (in minutes)
  """
  length: Int


  """
  The plaintext location of the appointment (only used for in-person appointments)
  """
  location: String


  """
  Location Resource
  """
  locationResource: String


  """
  How many attendees can register for an appointment (only used for Group Appointments)
  """
  max_attendees: String


  """
  a serialized JSON string of metadata
  """
  metadata: JSON


  """
  Minimum time before the appointment when client can still cancel it
  """
  minimum_advance_cancel_time: Int


  """
  Minimum time (in minutes) before the appointment when client can still reschedule it
  """
  minimum_advance_reschedule_time: Int


  """
  The No Show Fee (in cents) for this appointment
  """
  no_show_fee: Int


  """
  Quick notes on the appointment (only visible to providers)
  """
  notes: String


  """
  The ID of the organization the appointment belongs to
  """
  organization_id: ID


  """
  Free text reason when "Other" cancellation reason is selected
  """
  other_cancellation_reason: String


  """
  The id of the provider
  """
  other_party_id: Int


  """
  The number of times a patient rescheduled an appointment
  """
  patient_reschedule_count: Int


  """
  The status of the appointment. Can be one of "Occurred", "No-Show", "Re-Scheduled", "Cancelled." If enabled, "Late Cancellation" and "Checked-In" are also valid.
  """
  pm_status(
    """
    Check if client cancelled the appointment
    """
    check_for_client_cancel: Boolean = false
  ): String


  """
  The date and time the status of the appointment was last updated
  """
  pm_status_changed_at: ISO8601DateTime


  """
  The ID of the user who last changed the status of the appointment, if available
  """
  pm_status_last_changed_by_id: ID


  """
  Get the pricing info for this appointment
  """
  pricing_info: AppointmentPricingInfoType


  """
  The provider for the appointment
  """
  provider: User


  """
  Provider name
  """
  provider_name: String


  """
  All providers for the appointment.
  """
  providers(
    """
    Return an empty array unless there is more than one provider
    """
    empty_unless_multiple: Boolean = false
  ): [User!]!


  """
  The clients reason for scheduling the appointment
  """
  reason: String


  """
  The related recurring appointment series
  """
  recurring_appointment: RecurringAppointment


  """
  The ID of the recurring appointment
  """
  recurring_appointment_id: String
    @deprecated(reason: "Use recurring_appointment instead")


  """
  The status of whether this is a repeating appointment or not
  """
  repeat: Boolean @deprecated(reason: "Use recurring_appointment instead")


  """
  How often to repeat the appointment (e.g Daily or Monthly)
  """
  repeat_interval: String
    @deprecated(reason: "Use recurring_appointment instead")


  """
  How many times does the appointment repeat
  """
  repeat_times: Int @deprecated(reason: "Use recurring_appointment instead")


  """
  A requested payment for this appointment
  """
  requested_payment: RequestedPayment


  """
  The ID of the user, used for the calendar
  """
  resourceId: String


  """
  the ID of the room
  """
  room_id: ID


  """
  A string containing info on how the appointment was scheduled
  """
  scheduled_by: String


  """
  The OpenTok session ID for the appointment
  """
  session_id: String


  """
  When true, a cms1500 should be created when the appointment status is set to occurred
  """
  should_create_cms1500_for_occurred_appointments: Boolean


  """
  The start time of the appointment
  """
  start: String


  """
  The font color of the appointment
  """
  textColor: String


  """
  The status of whether the time of this appointment has been separated from the other recurring appointments in the series
  """
  time_recurring_override: Boolean


  """
  Timezone abbreviation of the date of the appointment
  """
  timezone_abbr: String


  """
  The title of the appointment
  """
  title: String


  """
  Can only be returned via querying a single appointment, not a collection. Transcripts for the appointment (in VTT format)
  """
  transcripts(
    """
    Filter by specific transcript type. If not provided, returns all transcript types.
    """
    transcript_type: TranscriptTypeEnum


    """
    Filter by transcript statuses. If not provided, just returns completed.
    """
    status: [TranscriptStatusEnum]
  ): [Transcript!]


  """
  Unauthenticated link to download an ICS file for the appointment
  """
  unauthenticated_ics_link: String


  """
  The last date and time that the appointment was updated
  """
  updated_at: ISO8601DateTime


  """
  Whether the appointment should use embedded Zoom in browser
  """
  use_embedded_zoom: Boolean


  """
  Whether the appointment is through Zoom or not
  """
  use_zoom: Boolean


  """
  The client in a 1:1 appointment
  """
  user: User


  """
  The id of the client (if a 1:1 appointment). If a group appointment, will be nil
  """
  user_id: Int


  """
  True if this appointment is configured to be summarized by AI Scribe
  """
  will_be_scribed: Boolean!


  """
  Zoom meeting info. Appointment should have a valid zoom link and the user should have the permission to access the meeting. Otherwise returns nil
  """
  zoom_appointment: ZoomAppointment


  """
  Detailed information about Zoom cloud recording files for this appointment
  """
  zoom_cloud_recording_files: [ZoomCloudRecordingFile!]


  """
  URLs for Zoom cloud recordings for this appointment
  """
  zoom_cloud_recording_urls: [String]


  """
  ZAK tokens for each org member co-host on this Zoom group appointment. Returns an empty array when the feature flag is disabled, there is no Zoom meeting, or there are no other org member providers with a valid zoom_id.
  """
  zoom_co_host_links: [ZoomCoHostLink!]


  """
  The dial-in info provided by zoom if appoint has zoom links.(separated by newline characters)
  """
  zoom_dial_in_info: String


  """
  The dial-in info provided by zoom if appoint has zoom links.(separated by break tags)
  """
  zoom_dial_in_info_html: String


  """
  An array of JSON objects containing the different dial in numbers for the Zoom call
  """
  zoom_dial_in_numbers_json: [String]


  """
  The join link for other attendees of the Zoom call
  """
  zoom_join_url: String


  """
  The Meeting ID for the Zoom call
  """
  zoom_meeting_id: String


  """
  The host link to start the Zoom call
  """
  zoom_start_url: String
}
```
