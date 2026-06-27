---
title: AppointmentSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentsetting/index.md
---

Appointment Setting options that a provider can customize

## Fields

[`accepted_insurance_plans` ](#field-accepted-insurance-plans)· [`[AcceptedInsurancePlan!]` ](/reference/2026-01-01/objects/acceptedinsuranceplan)· Insurance plans that are accepted by the provider

[`allow_appointment_type_pricing` ](#field-allow-appointment-type-pricing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not providers will be able to set pricing per appointment type

[`allow_clients_to_cancel_appt` ](#field-allow-clients-to-cancel-appt)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, clients will be able to cancel an appointment

[`allow_clients_to_reschedule_appt` ](#field-allow-clients-to-reschedule-appt)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, clients will be able to reschedule an appointment

[`allow_external_videochat_urls` ](#field-allow-external-videochat-urls)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, providers can specify external url (e.g., Doxy, VSee) for Video Call appointments.

[`allow_past_appointment_rescheduling` ](#field-allow-past-appointment-rescheduling)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, a client can reschedule a past appointment (on the Web/API only)

[`allow_specific_client_pricing` ](#field-allow-specific-client-pricing)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not clients will have specific pricing for appointment types

[`allow_specific_provider_pricing` ](#field-allow-specific-provider-pricing)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not providers will have specific pricing for appointment types

[`always_send_confirm_notification` ](#field-always-send-confirm-notification)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Always notify the provider when the client books

[`appointment_locations` ](#field-appointment-locations)· [`[AppointmentLocation!]` ](/reference/2026-01-01/objects/appointmentlocation)· Appointment Locations for this Appointment Setting

[`appointment_type_confirmed_email` ](#field-appointment-type-confirmed-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Have different appointment confirmation emails for each appointment type

[`appointment_type_reminder_email` ](#field-appointment-type-reminder-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Have different appointment reminder emails for each appointment type

[`appointment_type_reminder_override` ](#field-appointment-type-reminder-override)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, and when the appointment setting is associated to a specific appointment type, the reminder settings will override the provider's normal ones

[`appointment_type_website_booking_email` ](#field-appointment-type-website-booking-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Have different website booking emails for each appointment type

[`appt_type_confirmed_email` ](#field-appt-type-confirmed-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Separate confirmation emails for different appointment types

[`appt_type_reminder_email` ](#field-appt-type-reminder-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Separate reminder emails for different appointment types

[`appt_type_website_booking_email` ](#field-appt-type-website-booking-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Separate website booking emails for different appointment types

[`ask_clients_to_confirm` ](#field-ask-clients-to-confirm)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Ask clients to confirm their appointment

[`ask_to_confirm_via_text` ](#field-ask-to-confirm-via-text)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, clients can confirm their appointment via text

[`auto_charge_enabled` ](#field-auto-charge-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True when either auto\_schedule\_charges\_for\_late\_cancellation\_no\_show or charge\_for\_occurred\_appts

[`auto_create_cms1500` ](#field-auto-create-cms1500)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, after an appointment has been set as occurred, a CMS 1500 claim can be automatically created for the session

[`auto_invoicing` ](#field-auto-invoicing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Auto-generate a payment request when an appointment is scheduled

[`auto_schedule_charges_for_late_cancellation_no_show` ](#field-auto-schedule-charges-for-late-cancellation-no-show)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· when true, a scheduled charge will be created when an appointment is marked as late cancellation or no show

[`auto_submit_cms1500` ](#field-auto-submit-cms1500)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, it will be automatically submitted to the clearinghouse on the following Friday at 11:59 PM

[`base_calendar_interval` ](#field-base-calendar-interval)· [`BaseCalendarInterval!` ](/reference/2026-01-01/enums/basecalendarinterval)· required · The base minute interval (FIVE\_MINUTES, TEN\_MINUTES, FIFTEEN\_MINUTES) that all availability operations are performed with

[`booking_interval_restriction` ](#field-booking-interval-restriction)· [`Int` ](/reference/2026-01-01/scalars/int)· Allow clients to book appointments at none, 20, 30, 60 intervals

[`buffer` ](#field-buffer)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of minutes to maintain between appointments (prevent back to back appointments)

[`calendar_color_schemes` ](#field-calendar-color-schemes)· [`[CalendarColorScheme!]` ](/reference/2026-01-01/objects/calendarcolorscheme)· The color schemes defined for this appointment setting

[`calendar_interval` ](#field-calendar-interval)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: Calendar interval

deprecated

Use \`calendar\_view\_setting\` instead

[`calendar_text` ](#field-calendar-text)· [`String` ](/reference/2026-01-01/scalars/string)· Text to display above the client's calendar within Healthie

[`cant_cancel_message` ](#field-cant-cancel-message)· [`String` ](/reference/2026-01-01/scalars/string)· Message to show clients when they are not allowed to cancel

[`cant_reschedule_message` ](#field-cant-reschedule-message)· [`String` ](/reference/2026-01-01/scalars/string)· Message to show clients when they are not allowed to cancel

[`charge_for_occured_appts` ](#field-charge-for-occured-appts)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not client with valid payment method will be charged for occurred appointments

deprecated

Use \`charge\_for\_occurred\_appts\` instead

[`charge_for_occurred_appts` ](#field-charge-for-occurred-appts)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not client with valid payment method will be charged for occurred appointments

[`client_cancel_reason_required` ](#field-client-cancel-reason-required)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, clients must provide a cancellation reason when cancelling

[`client_should_call_provider` ](#field-client-should-call-provider)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, clients will be able to call to provider

[`clients_have_billing` ](#field-clients-have-billing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, the billing tab is hidden from clients

[`confirm_by_default` ](#field-confirm-by-default)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Confirm all client-created appointments by default

[`contact_type_overrides` ](#field-contact-type-overrides)· [`[ContactType!]` ](/reference/2026-01-01/objects/contacttype)· Contact type overrides for this appointment setting

[`default_appt_form_to_group` ](#field-default-appt-form-to-group)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Show the group appointment form first

[`default_charting_template_id` ](#field-default-charting-template-id)· [`String` ](/reference/2026-01-01/scalars/string)· The template selected will automatically appear when a new chart note is started

[`default_charting_template_name` ](#field-default-charting-template-name)· [`String` ](/reference/2026-01-01/scalars/string)· The template name selected

[`default_group_charting_template` ](#field-default-group-charting-template)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· The form that should be pre-selected when creating a new group charting note

[`default_to_zoom` ](#field-default-to-zoom)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Use Zoom for all telehealth appointments

[`default_video_service` ](#field-default-video-service)· [`String` ](/reference/2026-01-01/scalars/string)· Video service to use for telehealth appointments ('internal', 'zoom', or 'external')

[`disallowed_reschedulable_statuses` ](#field-disallowed-reschedulable-statuses)· [`[String]` ](/reference/2026-01-01/scalars/string)· Prevent the client from rescheduling a past appointment with one of these statuses

[`enable_appointment_requests` ](#field-enable-appointment-requests)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to allow appointment requests

[`enable_checked_in_status` ](#field-enable-checked-in-status)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Enable the additional "Checked-In" status for appointments.

[`enable_late_cancellation_status` ](#field-enable-late-cancellation-status)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Enable the additional "Late Cancellation" status for appointments.

[`end_time` ](#field-end-time)· [`String` ](/reference/2026-01-01/scalars/string)· The end time to show when setting weekly availability

[`fb_pixel` ](#field-fb-pixel)· [`String` ](/reference/2026-01-01/scalars/string)· Facebook pixel code that runs when the client completes the embedded scheduler/purchaser

[`give_notes_name` ](#field-give-notes-name)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Assign a name to chart notes

deprecated

This now always returns true

[`hide_insurance_getting_started_info` ](#field-hide-insurance-getting-started-info)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, hide insurance getting started info

[`hide_link` ](#field-hide-link)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Hide links to Healthie from appointment reminders

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the setting

[`insurance_eligibility_integration` ](#field-insurance-eligibility-integration)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, it will show the option to run an insurance eligibility check for a client

[`insurance_specific_cpt_code_pricing` ](#field-insurance-specific-cpt-code-pricing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, CPT codes can be set for each insurance plan

[`invoice_clients_without_payment_method` ](#field-invoice-clients-without-payment-method)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to send invoice to client without a valid payment card/method

[`late_cancellation_fee` ](#field-late-cancellation-fee)· [`Int` ](/reference/2026-01-01/scalars/int)· The fee (in cents) to use for appointments marked as late cancellation

[`max_days_in_future` ](#field-max-days-in-future)· [`String` ](/reference/2026-01-01/scalars/string)· The maximum number of days in advance a client can book

[`maximum_past_reschedule_time` ](#field-maximum-past-reschedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· DEPRECATED: Maximum time a client must wait before being able to reschedule a past appointment

deprecated

No longer supported

[`minimum_advance_cancel_time` ](#field-minimum-advance-cancel-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Minimum time before the appointment when client still can cancel it (in minutes)

[`minimum_advance_reschedule_time` ](#field-minimum-advance-reschedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Minimum time before the appointment when client still can reschedule it (in minutes)

[`minimum_advance_schedule_time` ](#field-minimum-advance-schedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Minimum time before the desired appointment type where client still can schedule it (in minutes)

[`minimum_days_in_advance` ](#field-minimum-days-in-advance)· [`String` ](/reference/2026-01-01/scalars/string)· The minimum days in advance a client has to book

[`minimum_past_reschedule_time` ](#field-minimum-past-reschedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· DEPRECATED: Minimum time a client must wait before being able to reschedule a past appointment

deprecated

No longer supported

[`no_show_fee` ](#field-no-show-fee)· [`Int` ](/reference/2026-01-01/scalars/int)· The fee (in cents) to use for appointments marked as no show

[`only_book` ](#field-only-book)· [`String` ](/reference/2026-01-01/scalars/string)· Either "even" or "hour" to restrict booking to even hours or half hours.

deprecated

Use booking\_interval\_restriction instead

[`only_book_even` ](#field-only-book-even)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to restrict booking to even hours or half hours.

deprecated

Use booking\_interval\_restriction instead

[`only_book_hour` ](#field-only-book-hour)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to restrict booking to even hours or half hours.

deprecated

Use booking\_interval\_restriction instead

[`owner` ](#field-owner)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this appointment\_setting

[`patient_reschedule_count_cap` ](#field-patient-reschedule-count-cap)· [`String` ](/reference/2026-01-01/scalars/string)· The maximum number of times a patient can self reschedule

[`pm_statuses` ](#field-pm-statuses)· [`[String]` ](/reference/2026-01-01/scalars/string)· Appointment statuses that can be applied to an appointment. Includes default ones plus any custom

[`prevent_client_booking` ](#field-prevent-client-booking)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Prevent clients from booking an appointment

[`prevent_no_credit_booking` ](#field-prevent-no-credit-booking)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Prevent clients from booking if they do not have the needed credit

[`provider_cancel_reason_required` ](#field-provider-cancel-reason-required)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, providers must provide a cancellation reason when cancelling

[`reply_to_provider` ](#field-reply-to-provider)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, replies to automatic notifications will go to the provider

[`require_selected_location_for_all_contact_types` ](#field-require-selected-location-for-all-contact-types)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, providers and staff will always be asked to select an appointment location when scheduling, even if its a video chat.

[`reschedule_max_days_before_date` ](#field-reschedule-max-days-before-date)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: The minimum number of days beyond the current appointment date that the patient can reschedule to

deprecated

No longer supported

[`reschedule_max_days_from_date` ](#field-reschedule-max-days-from-date)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: The maximum number of days beyond the current appointment date that the patient can reschedule to

deprecated

No longer supported

[`restore_credit_on_cancel` ](#field-restore-credit-on-cancel)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Give clients their credit back when an appointment is cancelled

[`same_day_appointments` ](#field-same-day-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, clients are prevented from scheduling appointments the day of

[`send_appointment_cancellation_email` ](#field-send-appointment-cancellation-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, no appointment cancel emails are sent to patients.

[`send_appointment_update_email` ](#field-send-appointment-update-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, no appointment update emails are sent to patients.

[`send_booking_notice` ](#field-send-booking-notice)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send clients an email when a provider schedules an appointment

[`send_email_before_appointment` ](#field-send-email-before-appointment)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send an email 5 minutes before a video chat starts

[`send_embeddable_appt_creator_email` ](#field-send-embeddable-appt-creator-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Sends a confirmation email to the client when the client initially books an appointment

[`send_intake_forms_reminder` ](#field-send-intake-forms-reminder)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send email reminder to complete intake forms two days before

[`send_push_before_appointment` ](#field-send-push-before-appointment)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send a push notification 5 minutes before a video chat starts

[`send_reminder_four_days_before` ](#field-send-reminder-four-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send an email reminder four days before the appointment

[`send_reminder_one_day_before` ](#field-send-reminder-one-day-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send an email reminder one day before the appointment

[`send_reminder_one_hour_before` ](#field-send-reminder-one-hour-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send an email reminder one hour before the appointment

[`send_reminder_three_days_before` ](#field-send-reminder-three-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send an email reminder three days before the appointment

[`send_reminder_two_days_before` ](#field-send-reminder-two-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send an email reminder two days before the appointment

[`send_reminder_two_hours_before` ](#field-send-reminder-two-hours-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send an email reminder two hours before the appointment

[`send_text_reminder_five_minutes_before` ](#field-send-text-reminder-five-minutes-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· NOTE: Your organization MUST have its own Twilio account configured to have this feature, and have AppointmentSetting.send\_email\_before\_appointment enabled

[`send_text_reminder_four_days_before` ](#field-send-text-reminder-four-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send a text reminder four days before the appointment

[`send_text_reminder_one_day_before` ](#field-send-text-reminder-one-day-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send a text reminder one day before the appointment

[`send_text_reminder_one_hour_before` ](#field-send-text-reminder-one-hour-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send a text reminder one hour before the appointment

[`send_text_reminder_three_days_before` ](#field-send-text-reminder-three-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send a text reminder three days before the appointment

[`send_text_reminder_two_days_before` ](#field-send-text-reminder-two-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send a text reminder two days before the appointment

[`send_text_reminder_two_hours_before` ](#field-send-text-reminder-two-hours-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send a text reminder two hours before the appointment

[`set_default_videochat_url` ](#field-set-default-videochat-url)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, providers can set a default external link for video call sessions.

[`show_care_plans` ](#field-show-care-plans)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If True, provider will see Care Plans option on a Client profile page

[`show_cms1500s` ](#field-show-cms1500s)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, show cms1500s

[`show_faxes` ](#field-show-faxes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, the faxing tab on the left hand side is hidden from providers

[`show_insurance_authorization` ](#field-show-insurance-authorization)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, show the insurance authorization section on the clients profile

[`show_office_ally` ](#field-show-office-ally)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, show office ally

[`show_superbills` ](#field-show-superbills)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, show superbills

[`start_fb_pixel` ](#field-start-fb-pixel)· [`String` ](/reference/2026-01-01/scalars/string)· Facebook pixel code that runs when the client starts the embedded scheduler/purchaser

[`start_time` ](#field-start-time)· [`String` ](/reference/2026-01-01/scalars/string)· The start time to show when setting weekly availability

[`times_by_appointment_type` ](#field-times-by-appointment-type)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Set different availability for each appointment type

[`times_by_contact_type` ](#field-times-by-contact-type)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Set different availability for each contact type

[`times_by_location` ](#field-times-by-location)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Set different availability for each appointment location

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last date and time that the appointment setting was updated

[`use_appointment_type_cpt_units_and_fees` ](#field-use-appointment-type-cpt-units-and-fees)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, cpt units and fees can be associated with appointment types

[`use_client_credit_system` ](#field-use-client-credit-system)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to use the client credit system

[`use_client_sources` ](#field-use-client-sources)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, you can see where each client came from

[`use_zoom_waiting_room` ](#field-use-zoom-waiting-room)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, clients will be placed in a waiting room instead of joining the Zoom call directly

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the user

[`video_url_default` ](#field-video-url-default)· [`VideoUrlDefault` ](/reference/2026-01-01/objects/videourldefault)· Default video url settings

[`zoom_open_preference` ](#field-zoom-open-preference)· [`String` ](/reference/2026-01-01/scalars/string)· Preference for how Zoom calls should open ('embedded\_zoom' for browser, 'zoom\_app' for Zoom app)

## Used By

[`AppointmentType.appointment_setting`](/reference/2026-01-01/objects/appointmenttype)

[`User.appointment_setting`](/reference/2026-01-01/objects/user)

[`createAcceptedInsurancePlanPayload.appointment_setting`](/reference/2026-01-01/objects/createacceptedinsuranceplanpayload)

[`createAppointmentSettingPayload.appointmentSetting`](/reference/2026-01-01/objects/createappointmentsettingpayload)

[`deleteAcceptedInsurancePlanPayload.appointment_setting`](/reference/2026-01-01/objects/deleteacceptedinsuranceplanpayload)

[`updateAppointmentSettingPayload.appointmentSetting`](/reference/2026-01-01/objects/updateappointmentsettingpayload)

[`Query.appointmentSetting`](/reference/2026-01-01/queries/appointmentsetting)

## Definition

```
"""
Appointment Setting options that a provider can customize
"""
type AppointmentSetting {
  """
  Insurance plans that are accepted by the provider
  """
  accepted_insurance_plans: [AcceptedInsurancePlan!]


  """
  Whether or not providers will be able to set pricing per appointment type
  """
  allow_appointment_type_pricing: Boolean


  """
  If true, clients will be able to cancel an appointment
  """
  allow_clients_to_cancel_appt: Boolean


  """
  If true, clients will be able to reschedule an appointment
  """
  allow_clients_to_reschedule_appt: Boolean!


  """
  When true, providers can specify external url (e.g., Doxy, VSee) for Video Call appointments.
  """
  allow_external_videochat_urls: Boolean!


  """
  When true, a client can reschedule a past appointment (on the Web/API only)
  """
  allow_past_appointment_rescheduling: Boolean!


  """
  Whether or not clients will have specific pricing for appointment types
  """
  allow_specific_client_pricing: Boolean!


  """
  Whether or not providers will have specific pricing for appointment types
  """
  allow_specific_provider_pricing: Boolean!


  """
  Always notify the provider when the client books
  """
  always_send_confirm_notification: Boolean


  """
  Appointment Locations for this Appointment Setting
  """
  appointment_locations: [AppointmentLocation!]


  """
  Have different appointment confirmation emails for each appointment type
  """
  appointment_type_confirmed_email: Boolean


  """
  Have different appointment reminder emails for each appointment type
  """
  appointment_type_reminder_email: Boolean


  """
  When true, and when the appointment setting is associated to a specific appointment type, the reminder settings will override the provider's normal ones
  """
  appointment_type_reminder_override: Boolean


  """
  Have different website booking emails for each appointment type
  """
  appointment_type_website_booking_email: Boolean


  """
  Separate confirmation emails for different appointment types
  """
  appt_type_confirmed_email: Boolean


  """
  Separate reminder emails for different appointment types
  """
  appt_type_reminder_email: Boolean


  """
  Separate website booking emails for different appointment types
  """
  appt_type_website_booking_email: Boolean


  """
  Ask clients to confirm their appointment
  """
  ask_clients_to_confirm: Boolean


  """
  If true, clients can confirm their appointment via text
  """
  ask_to_confirm_via_text: Boolean


  """
  True when either auto_schedule_charges_for_late_cancellation_no_show or charge_for_occurred_appts
  """
  auto_charge_enabled: Boolean


  """
  When true, after an appointment has been set as occurred, a CMS 1500 claim can be automatically created for the session
  """
  auto_create_cms1500: Boolean


  """
  Auto-generate a payment request when an appointment is scheduled
  """
  auto_invoicing: Boolean


  """
  when true, a scheduled charge will be created when an appointment is marked as late cancellation or no show
  """
  auto_schedule_charges_for_late_cancellation_no_show: Boolean


  """
  When true, it will be automatically submitted to the clearinghouse on the following Friday at 11:59 PM
  """
  auto_submit_cms1500: Boolean


  """
  The base minute interval (FIVE_MINUTES, TEN_MINUTES, FIFTEEN_MINUTES) that all availability operations are performed with
  """
  base_calendar_interval: BaseCalendarInterval!


  """
  Allow clients to book appointments at none, 20, 30, 60 intervals
  """
  booking_interval_restriction: Int


  """
  The amount of minutes to maintain between appointments (prevent back to back appointments)
  """
  buffer: String


  """
  The color schemes defined for this appointment setting
  """
  calendar_color_schemes: [CalendarColorScheme!]


  """
  DEPRECATED: Calendar interval
  """
  calendar_interval: String
    @deprecated(reason: "Use `calendar_view_setting` instead")


  """
  Text to display above the client's calendar within Healthie
  """
  calendar_text: String


  """
  Message to show clients when they are not allowed to cancel
  """
  cant_cancel_message: String


  """
  Message to show clients when they are not allowed to cancel
  """
  cant_reschedule_message: String


  """
  Whether or not client with valid payment method will be charged for occurred appointments
  """
  charge_for_occured_appts: Boolean
    @deprecated(reason: "Use `charge_for_occurred_appts` instead")


  """
  Whether or not client with valid payment method will be charged for occurred appointments
  """
  charge_for_occurred_appts: Boolean


  """
  When true, clients must provide a cancellation reason when cancelling
  """
  client_cancel_reason_required: Boolean


  """
  If true, clients will be able to call to provider
  """
  client_should_call_provider: Boolean


  """
  When false, the billing tab is hidden from clients
  """
  clients_have_billing: Boolean


  """
  Confirm all client-created appointments by default
  """
  confirm_by_default: Boolean


  """
  Contact type overrides for this appointment setting
  """
  contact_type_overrides: [ContactType!]


  """
  Show the group appointment form first
  """
  default_appt_form_to_group: Boolean


  """
  The template selected will automatically appear when a new chart note is started
  """
  default_charting_template_id: String


  """
  The template name selected
  """
  default_charting_template_name: String


  """
  The form that should be pre-selected when creating a new group charting note
  """
  default_group_charting_template: CustomModuleForm


  """
  Use Zoom for all telehealth appointments
  """
  default_to_zoom: Boolean


  """
  Video service to use for telehealth appointments ('internal', 'zoom', or 'external')
  """
  default_video_service: String


  """
  Prevent the client from rescheduling a past appointment with one of these statuses
  """
  disallowed_reschedulable_statuses: [String]


  """
  Whether or not to allow appointment requests
  """
  enable_appointment_requests: Boolean


  """
  Enable the additional "Checked-In" status for appointments.
  """
  enable_checked_in_status: Boolean


  """
  Enable the additional "Late Cancellation" status for appointments.
  """
  enable_late_cancellation_status: Boolean


  """
  The end time to show when setting weekly availability
  """
  end_time: String


  """
  Facebook pixel code that runs when the client completes the embedded scheduler/purchaser
  """
  fb_pixel: String


  """
  Assign a name to chart notes
  """
  give_notes_name: Boolean @deprecated(reason: "This now always returns true")


  """
  If true, hide insurance getting started info
  """
  hide_insurance_getting_started_info: Boolean


  """
  Hide links to Healthie from appointment reminders
  """
  hide_link: Boolean


  """
  The unique identifier of the setting
  """
  id: ID!


  """
  When true, it will show the option to run an insurance eligibility check for a client
  """
  insurance_eligibility_integration: Boolean


  """
  When true, CPT codes can be set for each insurance plan
  """
  insurance_specific_cpt_code_pricing: Boolean


  """
  Whether or not to send invoice to client without a valid payment card/method
  """
  invoice_clients_without_payment_method: Boolean


  """
  The fee (in cents) to use for appointments marked as late cancellation
  """
  late_cancellation_fee: Int


  """
  The maximum number of days in advance a client can book
  """
  max_days_in_future: String


  """
  DEPRECATED: Maximum time a client must wait before being able to reschedule a past appointment
  """
  maximum_past_reschedule_time: Int @deprecated


  """
  Minimum time before the appointment when client still can cancel it (in minutes)
  """
  minimum_advance_cancel_time: Int


  """
  Minimum time before the appointment when client still can reschedule it (in minutes)
  """
  minimum_advance_reschedule_time: Int


  """
  Minimum time before the desired appointment type where client still can schedule it (in minutes)
  """
  minimum_advance_schedule_time: Int


  """
  The minimum days in advance a client has to book
  """
  minimum_days_in_advance: String


  """
  DEPRECATED: Minimum time a client must wait before being able to reschedule a past appointment
  """
  minimum_past_reschedule_time: Int @deprecated


  """
  The fee (in cents) to use for appointments marked as no show
  """
  no_show_fee: Int


  """
  Either "even" or "hour" to restrict booking to even hours or half hours.
  """
  only_book: String
    @deprecated(reason: "Use booking_interval_restriction instead")


  """
  Whether or not to restrict booking to even hours or half hours.
  """
  only_book_even: Boolean
    @deprecated(reason: "Use booking_interval_restriction instead")


  """
  Whether or not to restrict booking to even hours or half hours.
  """
  only_book_hour: Boolean
    @deprecated(reason: "Use booking_interval_restriction instead")


  """
  Owner of this appointment_setting
  """
  owner: User


  """
  The maximum number of times a patient can self reschedule
  """
  patient_reschedule_count_cap: String


  """
  Appointment statuses that can be applied to an appointment. Includes default ones plus any custom
  """
  pm_statuses: [String]


  """
  Prevent clients from booking an appointment
  """
  prevent_client_booking: Boolean


  """
  Prevent clients from booking if they do not have the needed credit
  """
  prevent_no_credit_booking: Boolean


  """
  When true, providers must provide a cancellation reason when cancelling
  """
  provider_cancel_reason_required: Boolean


  """
  When true, replies to automatic notifications will go to the provider
  """
  reply_to_provider: Boolean


  """
  When true, providers and staff will always be asked to select an appointment location when scheduling, even if its a video chat.
  """
  require_selected_location_for_all_contact_types: Boolean


  """
  DEPRECATED: The minimum number of days beyond the current appointment date that the patient can reschedule to
  """
  reschedule_max_days_before_date: String @deprecated


  """
  DEPRECATED: The maximum number of days beyond the current appointment date that the patient can reschedule to
  """
  reschedule_max_days_from_date: String @deprecated


  """
  Give clients their credit back when an appointment is cancelled
  """
  restore_credit_on_cancel: Boolean


  """
  When true, clients are prevented from scheduling appointments the day of
  """
  same_day_appointments: Boolean


  """
  When false, no appointment cancel emails are sent to patients.
  """
  send_appointment_cancellation_email: Boolean


  """
  When false, no appointment update emails are sent to patients.
  """
  send_appointment_update_email: Boolean


  """
  Send clients an email when a provider schedules an appointment
  """
  send_booking_notice: Boolean


  """
  Send an email 5 minutes before a video chat starts
  """
  send_email_before_appointment: Boolean


  """
  Sends a confirmation email to the client when the client initially books an appointment
  """
  send_embeddable_appt_creator_email: Boolean


  """
  Send email reminder to complete intake forms two days before
  """
  send_intake_forms_reminder: Boolean


  """
  Send a push notification 5 minutes before a video chat starts
  """
  send_push_before_appointment: Boolean


  """
  Send an email reminder four days before the appointment
  """
  send_reminder_four_days_before: Boolean


  """
  Send an email reminder one day before the appointment
  """
  send_reminder_one_day_before: Boolean


  """
  Send an email reminder one hour before the appointment
  """
  send_reminder_one_hour_before: Boolean


  """
  Send an email reminder three days before the appointment
  """
  send_reminder_three_days_before: Boolean


  """
  Send an email reminder two days before the appointment
  """
  send_reminder_two_days_before: Boolean


  """
  Send an email reminder two hours before the appointment
  """
  send_reminder_two_hours_before: Boolean


  """
  NOTE: Your organization MUST have its own Twilio account configured to have this feature, and have AppointmentSetting.send_email_before_appointment enabled
  """
  send_text_reminder_five_minutes_before: Boolean


  """
  Send a text reminder four days before the appointment
  """
  send_text_reminder_four_days_before: Boolean


  """
  Send a text reminder one day before the appointment
  """
  send_text_reminder_one_day_before: Boolean


  """
  Send a text reminder one hour before the appointment
  """
  send_text_reminder_one_hour_before: Boolean


  """
  Send a text reminder three days before the appointment
  """
  send_text_reminder_three_days_before: Boolean


  """
  Send a text reminder two days before the appointment
  """
  send_text_reminder_two_days_before: Boolean


  """
  Send a text reminder two hours before the appointment
  """
  send_text_reminder_two_hours_before: Boolean


  """
  When true, providers can set a default external link for video call sessions.
  """
  set_default_videochat_url: Boolean


  """
  If True, provider will see Care Plans option on a Client profile page
  """
  show_care_plans: Boolean


  """
  If true, show cms1500s
  """
  show_cms1500s: Boolean


  """
  When false, the faxing tab on the left hand side is hidden from providers
  """
  show_faxes: Boolean


  """
  If true, show the insurance authorization section on the clients profile
  """
  show_insurance_authorization: Boolean


  """
  If true, show office ally
  """
  show_office_ally: Boolean


  """
  If true, show superbills
  """
  show_superbills: Boolean


  """
  Facebook pixel code that runs when the client starts the embedded scheduler/purchaser
  """
  start_fb_pixel: String


  """
  The start time to show when setting weekly availability
  """
  start_time: String


  """
  Set different availability for each appointment type
  """
  times_by_appointment_type: Boolean


  """
  Set different availability for each contact type
  """
  times_by_contact_type: Boolean


  """
  Set different availability for each appointment location
  """
  times_by_location: Boolean


  """
  The last date and time that the appointment setting was updated
  """
  updated_at: ISO8601DateTime


  """
  If true, cpt units and fees can be associated with appointment types
  """
  use_appointment_type_cpt_units_and_fees: Boolean


  """
  Whether or not to use the client credit system
  """
  use_client_credit_system: Boolean


  """
  If true, you can see where each client came from
  """
  use_client_sources: Boolean


  """
  If true, clients will be placed in a waiting room instead of joining the Zoom call directly
  """
  use_zoom_waiting_room: Boolean


  """
  The id of the user
  """
  user_id: String


  """
  Default video url settings
  """
  video_url_default: VideoUrlDefault


  """
  Preference for how Zoom calls should open ('embedded_zoom' for browser, 'zoom_app' for Zoom app)
  """
  zoom_open_preference: String
}
```
