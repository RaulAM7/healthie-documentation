---
title: AppointmentTypeAppointmentSettingInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmenttypeappointmentsettinginput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmenttypeappointmentsettinginput/index.md
---

Payload for an appointment setting

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the appointment setting will be deleted

[`allow_appointment_type_pricing` ](#field-allow-appointment-type-pricing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting allows appointment type pricing

[`allow_clients_to_cancel_appt` ](#field-allow-clients-to-cancel-appt)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting allows clients to cancel appointments

[`allow_clients_to_reschedule_appt` ](#field-allow-clients-to-reschedule-appt)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting allows clients to reschedule appointments

[`allow_past_appointment_rescheduling` ](#field-allow-past-appointment-rescheduling)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting allows past appointment rescheduling

[`allow_specific_client_pricing` ](#field-allow-specific-client-pricing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting allows specific client pricing

[`allow_specific_provider_pricing` ](#field-allow-specific-provider-pricing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting allows specific provider pricing

[`appointment_type_reminder_override` ](#field-appointment-type-reminder-override)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting overrides the appointment type reminder

[`booking_interval_restriction` ](#field-booking-interval-restriction)· [`Int` ](/reference/2026-01-01/scalars/int)· The booking interval restriction for the appointment setting

[`buffer` ](#field-buffer)· [`String` ](/reference/2026-01-01/scalars/string)· The buffer time for the appointment setting

[`charge_for_occured_appts` ](#field-charge-for-occured-appts)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting charges for occurred appointments

deprecated

Use \`charge\_for\_occurred\_appts\` instead

[`charge_for_occurred_appts` ](#field-charge-for-occurred-appts)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting charges for occurred appointments

[`disallowed_reschedulable_statuses` ](#field-disallowed-reschedulable-statuses)· [`[String]` ](/reference/2026-01-01/scalars/string)· The disallowed reschedulable statuses for the appointment setting

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment setting

[`invoice_clients_without_payment_method` ](#field-invoice-clients-without-payment-method)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting invoices clients without a payment method

[`max_days_in_future` ](#field-max-days-in-future)· [`String` ](/reference/2026-01-01/scalars/string)· The maximum number of days in the future when appointments can be scheduled

[`maximum_past_reschedule_time` ](#field-maximum-past-reschedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· DEPRECATED: The maximum number of minutes in the past that the patient can reschedule

deprecated

No longer supported

[`minimum_advance_cancel_time` ](#field-minimum-advance-cancel-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Prevents the patient from canceling too close the appointment time. In minutes

[`minimum_advance_reschedule_time` ](#field-minimum-advance-reschedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Prevents the patient from rescheduling too close the appointment time. In minutes

[`minimum_advance_schedule_time` ](#field-minimum-advance-schedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Prevents the patient from scheduling too close to the desired appointment time. In minutes

[`minimum_days_in_advance` ](#field-minimum-days-in-advance)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: Use minimum\_advance\_schedule\_time instead

deprecated

Use \`minimum\_advance\_schedule\_time\` instead

[`minimum_past_reschedule_time` ](#field-minimum-past-reschedule-time)· [`Int` ](/reference/2026-01-01/scalars/int)· DEPRECATED: The minimum number of minutes in the past that the patient can reschedule

deprecated

No longer supported

[`only_book` ](#field-only-book)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: Use booking\_interval\_restriction instead

deprecated

Use \`booking\_interval\_restriction\` instead

[`only_book_even` ](#field-only-book-even)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· DEPRECATED: Use booking\_interval\_restriction instead

deprecated

Use \`booking\_interval\_restriction\` instead

[`only_book_hour` ](#field-only-book-hour)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· DEPRECATED: Use booking\_interval\_restriction instead

deprecated

Use \`booking\_interval\_restriction\` instead

[`patient_reschedule_count_cap` ](#field-patient-reschedule-count-cap)· [`String` ](/reference/2026-01-01/scalars/string)· The maximum number of times a patient can reschedule an appointment

[`prevent_no_credit_booking` ](#field-prevent-no-credit-booking)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting prevents booking without credit

[`enable_appointment_requests` ](#field-enable-appointment-requests)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting allows appointment requests

[`pricing` ](#field-pricing)· [`String` ](/reference/2026-01-01/scalars/string)· The pricing for the appointment setting

[`reschedule_max_days_before_date` ](#field-reschedule-max-days-before-date)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: The maximum number of days before the appointment that the patient can reschedule

deprecated

No longer supported

[`reschedule_max_days_from_date` ](#field-reschedule-max-days-from-date)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: The maximum number of days after the appointment that the patient can reschedule

deprecated

No longer supported

[`same_day_appointments` ](#field-same-day-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting allows same day appointments

[`send_booking_notice` ](#field-send-booking-notice)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a booking notice

[`send_reminder_four_days_before` ](#field-send-reminder-four-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a reminder four days before the appointment

[`send_reminder_one_day_before` ](#field-send-reminder-one-day-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a reminder one day before the appointment

[`send_reminder_one_hour_before` ](#field-send-reminder-one-hour-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a reminder one hour before the appointment

[`send_reminder_three_days_before` ](#field-send-reminder-three-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a reminder three days before the appointment

[`send_reminder_two_days_before` ](#field-send-reminder-two-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a reminder two days before the appointment

[`send_reminder_two_hours_before` ](#field-send-reminder-two-hours-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a reminder two hours before the appointment

[`send_text_reminder_four_days_before` ](#field-send-text-reminder-four-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a text reminder four days before the appointment

[`send_text_reminder_one_day_before` ](#field-send-text-reminder-one-day-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a text reminder one day before the appointment

[`send_text_reminder_one_hour_before` ](#field-send-text-reminder-one-hour-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a text reminder one hour before the appointment

[`send_text_reminder_three_days_before` ](#field-send-text-reminder-three-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a text reminder three days before the appointment

[`send_text_reminder_two_days_before` ](#field-send-text-reminder-two-days-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a text reminder two days before the appointment

[`send_text_reminder_two_hours_before` ](#field-send-text-reminder-two-hours-before)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a text reminder two hours before the appointment

[`use_client_credit_system` ](#field-use-client-credit-system)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting uses the client credit system

[`send_appointment_cancellation_email` ](#field-send-appointment-cancellation-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends an email when the appointment is cancelled

[`send_appointment_update_email` ](#field-send-appointment-update-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends an email when the appointment is updated

[`send_embeddable_appt_creator_email` ](#field-send-embeddable-appt-creator-email)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment setting sends a confirmation email to the client when the client initially books an appointment

## Used By

[`createAppointmentTypeInput.appointment_setting`](/reference/2026-01-01/input-objects/createappointmenttypeinput)

[`updateAppointmentTypeInput.appointment_setting`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

## Definition

```
"""
Payload for an appointment setting
"""
input AppointmentTypeAppointmentSettingInput {
  """
  If true, the appointment setting will be deleted
  """
  _destroy: Boolean


  """
  Whether the appointment setting allows appointment type pricing
  """
  allow_appointment_type_pricing: Boolean


  """
  Whether the appointment setting allows clients to cancel appointments
  """
  allow_clients_to_cancel_appt: Boolean


  """
  Whether the appointment setting allows clients to reschedule appointments
  """
  allow_clients_to_reschedule_appt: Boolean


  """
  Whether the appointment setting allows past appointment rescheduling
  """
  allow_past_appointment_rescheduling: Boolean


  """
  Whether the appointment setting allows specific client pricing
  """
  allow_specific_client_pricing: Boolean


  """
  Whether the appointment setting allows specific provider pricing
  """
  allow_specific_provider_pricing: Boolean


  """
  Whether the appointment setting overrides the appointment type reminder
  """
  appointment_type_reminder_override: Boolean


  """
  The booking interval restriction for the appointment setting
  """
  booking_interval_restriction: Int


  """
  The buffer time for the appointment setting
  """
  buffer: String


  """
  Whether the appointment setting charges for occurred appointments
  """
  charge_for_occured_appts: Boolean
    @deprecated(reason: "Use `charge_for_occurred_appts` instead")


  """
  Whether the appointment setting charges for occurred appointments
  """
  charge_for_occurred_appts: Boolean


  """
  The disallowed reschedulable statuses for the appointment setting
  """
  disallowed_reschedulable_statuses: [String]


  """
  The ID of the appointment setting
  """
  id: ID


  """
  Whether the appointment setting invoices clients without a payment method
  """
  invoice_clients_without_payment_method: Boolean


  """
  The maximum number of days in the future when appointments can be scheduled
  """
  max_days_in_future: String


  """
  DEPRECATED: The maximum number of minutes in the past that the patient can reschedule
  """
  maximum_past_reschedule_time: Int @deprecated


  """
  Prevents the patient from canceling too close the appointment time. In minutes
  """
  minimum_advance_cancel_time: Int


  """
  Prevents the patient from rescheduling too close the appointment time. In minutes
  """
  minimum_advance_reschedule_time: Int


  """
  Prevents the patient from scheduling too close to the desired appointment time. In minutes
  """
  minimum_advance_schedule_time: Int


  """
  DEPRECATED: Use minimum_advance_schedule_time instead
  """
  minimum_days_in_advance: String
    @deprecated(reason: "Use `minimum_advance_schedule_time` instead")


  """
  DEPRECATED: The minimum number of minutes in the past that the patient can reschedule
  """
  minimum_past_reschedule_time: Int @deprecated


  """
  DEPRECATED: Use booking_interval_restriction instead
  """
  only_book: String
    @deprecated(reason: "Use `booking_interval_restriction` instead")


  """
  DEPRECATED: Use booking_interval_restriction instead
  """
  only_book_even: Boolean
    @deprecated(reason: "Use `booking_interval_restriction` instead")


  """
  DEPRECATED: Use booking_interval_restriction instead
  """
  only_book_hour: Boolean
    @deprecated(reason: "Use `booking_interval_restriction` instead")


  """
  The maximum number of times a patient can reschedule an appointment
  """
  patient_reschedule_count_cap: String


  """
  Whether the appointment setting prevents booking without credit
  """
  prevent_no_credit_booking: Boolean


  """
  Whether the appointment setting allows appointment requests
  """
  enable_appointment_requests: Boolean


  """
  The pricing for the appointment setting
  """
  pricing: String


  """
  DEPRECATED: The maximum number of days before the appointment that the patient can reschedule
  """
  reschedule_max_days_before_date: String @deprecated


  """
  DEPRECATED: The maximum number of days after the appointment that the patient can reschedule
  """
  reschedule_max_days_from_date: String @deprecated


  """
  Whether the appointment setting allows same day appointments
  """
  same_day_appointments: Boolean


  """
  Whether the appointment setting sends a booking notice
  """
  send_booking_notice: Boolean


  """
  Whether the appointment setting sends a reminder four days before the appointment
  """
  send_reminder_four_days_before: Boolean


  """
  Whether the appointment setting sends a reminder one day before the appointment
  """
  send_reminder_one_day_before: Boolean


  """
  Whether the appointment setting sends a reminder one hour before the appointment
  """
  send_reminder_one_hour_before: Boolean


  """
  Whether the appointment setting sends a reminder three days before the appointment
  """
  send_reminder_three_days_before: Boolean


  """
  Whether the appointment setting sends a reminder two days before the appointment
  """
  send_reminder_two_days_before: Boolean


  """
  Whether the appointment setting sends a reminder two hours before the appointment
  """
  send_reminder_two_hours_before: Boolean


  """
  Whether the appointment setting sends a text reminder four days before the appointment
  """
  send_text_reminder_four_days_before: Boolean


  """
  Whether the appointment setting sends a text reminder one day before the appointment
  """
  send_text_reminder_one_day_before: Boolean


  """
  Whether the appointment setting sends a text reminder one hour before the appointment
  """
  send_text_reminder_one_hour_before: Boolean


  """
  Whether the appointment setting sends a text reminder three days before the appointment
  """
  send_text_reminder_three_days_before: Boolean


  """
  Whether the appointment setting sends a text reminder two days before the appointment
  """
  send_text_reminder_two_days_before: Boolean


  """
  Whether the appointment setting sends a text reminder two hours before the appointment
  """
  send_text_reminder_two_hours_before: Boolean


  """
  Whether the appointment setting uses the client credit system
  """
  use_client_credit_system: Boolean


  """
  Whether the appointment setting sends an email when the appointment is cancelled
  """
  send_appointment_cancellation_email: Boolean


  """
  Whether the appointment setting sends an email when the appointment is updated
  """
  send_appointment_update_email: Boolean


  """
  Whether the appointment setting sends a confirmation email to the client when the client initially books an appointment
  """
  send_embeddable_appt_creator_email: Boolean
}
```
