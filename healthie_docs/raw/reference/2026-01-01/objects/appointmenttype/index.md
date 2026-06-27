---
title: AppointmentType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttype/index.md
---

An object containing information about the type of appointment

## Fields

[`advance_pricing_for_clients_count` ](#field-advance-pricing-for-clients-count)· [`String` ](/reference/2026-01-01/scalars/string)· The number of clients with advance pricing for this appointment type

[`advance_pricing_for_providers_count` ](#field-advance-pricing-for-providers-count)· [`String` ](/reference/2026-01-01/scalars/string)· The number of providers with advance pricing for this appointment type

[`appointment_autocomplete_form` ](#field-appointment-autocomplete-form)· [`AppointmentAutocompleteForm` ](/reference/2026-01-01/objects/appointmentautocompleteform)· The autocomplete form for AI-generated charting notes associated with this appointment type

[`appointment_setting` ](#field-appointment-setting)· [`AppointmentSetting` ](/reference/2026-01-01/objects/appointmentsetting)· The appointment setting associated with this appointment type. An associated appointment setting overrides the providers general one.

[`appointment_type_cpt_code` ](#field-appointment-type-cpt-code)· [`AppointmentTypeCptCodeType` ](/reference/2026-01-01/objects/appointmenttypecptcodetype)· The cpt code and units for this appointment type

[`auto_increase_charge_for_actual_duration` ](#field-auto-increase-charge-for-actual-duration)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the appointment pricing will be automatically increase based on actual duration

[`availability_exists_for` ](#field-availability-exists-for)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Is true if upcoming availability exists

[`available_contact_types` ](#field-available-contact-types)· [`[String]` ](/reference/2026-01-01/scalars/string)· List of available contact types for this appointment type

[`bookable_by_groups` ](#field-bookable-by-groups)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, this appointment type is bookable by user groups associated through appointment\_type\_user\_groups and appointment type is NOT bookable by ALL users

[`bookable_groups` ](#field-bookable-groups)· [`[UserGroup!]` ](/reference/2026-01-01/objects/usergroup)· user groups that can book this appointment type. Associated through appointment\_type\_user\_groups

[`bookable_without_group` ](#field-bookable-without-group)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, this appointment type is bookable by users without a user group

[`client_call_provider` ](#field-client-call-provider)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Checks to see if the client call to provider

[`client_display_description` ](#field-client-display-description)· [`String` ](/reference/2026-01-01/scalars/string)· Custom description shown to clients when self-scheduling

[`client_display_name` ](#field-client-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· A name to use in the client scheduling widget instead of the default name field. Falls back to name if not set.

[`client_facing_display_name` ](#field-client-facing-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The raw client-facing display name without fallback to name. Used for editing.

[`clients_can_book` ](#field-clients-can-book)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the client can self-book this type of appointment

[`clients_have_credit` ](#field-clients-have-credit)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Checks to see if the client has enough credit to book

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the Appointment Type was created

[`custom_text_reminder_body` ](#field-custom-text-reminder-body)· [`String` ](/reference/2026-01-01/scalars/string)· If the provider's organization has this feature, this will customize the content of SMS reminder's Healthie sends.

[`deleted_at` ](#field-deleted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date time appointment type was deleted

[`dont_ask_for_reason` ](#field-dont-ask-for-reason)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the client will not be asked to add a reason when booking an appointment of this type

[`embed_question_form_id` ](#field-embed-question-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the embedded custom module form

[`form_requests_after_appointment` ](#field-form-requests-after-appointment)· [`[AppointmentTypeFormConnection!]` ](/reference/2026-01-01/objects/appointmenttypeformconnection)· All form requests which should be created after appointment

[`form_requests_after_appointment_booking` ](#field-form-requests-after-appointment-booking)· [`[AppointmentTypeFormConnection!]` ](/reference/2026-01-01/objects/appointmenttypeformconnection)· All form requests which should be created after appointment booking

[`form_requests_before_appointment` ](#field-form-requests-before-appointment)· [`[AppointmentTypeFormConnection!]` ](/reference/2026-01-01/objects/appointmenttypeformconnection)· All form requests which should be created before appointment

[`has_available_group_appts` ](#field-has-available-group-appts)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Is true if group appointment available

[`has_specific_appointment_settings` ](#field-has-specific-appointment-settings)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, this appointment type has specific appointment settings that override the general ones

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the appointment type

[`insurance_billing_enabled` ](#field-insurance-billing-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not this appointment type will have insurance billing enabled

[`is_group` ](#field-is-group)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether appointments of this types are group appointments or not

[`is_waitlist_enabled` ](#field-is-waitlist-enabled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether waitlist is enabled for an appointment or not

[`length` ](#field-length)· [`Int` ](/reference/2026-01-01/scalars/int)· The length of the appointment type (in minutes)

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000. Only accessible by staff and providers

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· the name of the appointment type

[`no_availability_message` ](#field-no-availability-message)· [`String` ](/reference/2026-01-01/scalars/string)· A custom message to display if there are no available slots on a given day for an appointment type.

[`organization_id` ](#field-organization-id)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · The organization that the appointment type belongs to

[`position` ](#field-position)· [`Int` ](/reference/2026-01-01/scalars/int)· The position of the appointment type when shown in a list of other appointment types

[`price_and_cpt_price` ](#field-price-and-cpt-price)· [`PriceAndCptPriceType` ](/reference/2026-01-01/objects/priceandcptpricetype)· The price and cpt\_code\_price

[`pricing` ](#field-pricing)· [`String` ](/reference/2026-01-01/scalars/string)· The pricing for this appointment type

[`pricing_info` ](#field-pricing-info)· [`AppointmentPricingInfoType` ](/reference/2026-01-01/objects/appointmentpricinginfotype)· Get the pricing info for this appointment type

[`pricing_option` ](#field-pricing-option)· [`String` ](/reference/2026-01-01/scalars/string)· Pricing option for this appointment type

[`provider_appt_type_connections` ](#field-provider-appt-type-connections)· [`[ProviderApptTypeConnection!]` ](/reference/2026-01-01/objects/providerappttypeconnection)· providers associated with appointment type

[`require_cc_at_booking` ](#field-require-cc-at-booking)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, certain clients (limited to non-established clients only and does not include provider-booked appointments) will be required to provide a credit card for booking

[`require_in_state_clients` ](#field-require-in-state-clients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When this setting is turned on, provider state licensing requirements will be enforced when clients try to schedule appointments.

[`require_specific_providers` ](#field-require-specific-providers)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not appointment type should use specific providers

[`row_order` ](#field-row-order)· [`String` ](/reference/2026-01-01/scalars/string)· position of appointment type when displayed in packages list

[`time_on_label` ](#field-time-on-label)· [`String` ](/reference/2026-01-01/scalars/string)· A label that includes the length of the appointment

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the Appointment Type was updated

[`user_group` ](#field-user-group)· [`UserGroup` ](/reference/2026-01-01/objects/usergroup)· The user group associated with this appointment type.

[`user_group_id` ](#field-user-group-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the group clients are placed in after booking

[`user_id` ](#field-user-id)· [`Int` ](/reference/2026-01-01/scalars/int)· The creator of the appointment type

[`valid_state_licensing_for` ](#field-valid-state-licensing-for)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If provider state matches users or appointment type doesn't require state license restrictions.

## Used By

[`Appointment.appointment_type`](/reference/2026-01-01/objects/appointment)

[`AppointmentRequestType.appointment_type`](/reference/2026-01-01/objects/appointmentrequesttype)

[`AppointmentTypeCredit.appointment_type`](/reference/2026-01-01/objects/appointmenttypecredit)

[`AppointmentTypeEdge.node`](/reference/2026-01-01/objects/appointmenttypeedge)

[`AppointmentTypePaginationConnection.nodes`](/reference/2026-01-01/objects/appointmenttypepaginationconnection)

[`Availability.appointment_types`](/reference/2026-01-01/objects/availability)

[`OfferingInclude.appointment_type`](/reference/2026-01-01/objects/offeringinclude)

[`PotentialAppointmentSlot.appointment_type`](/reference/2026-01-01/objects/potentialappointmentslot)

[`User.appointment_types`](/reference/2026-01-01/objects/user)

[`createAppointmentTypePayload.appointmentType`](/reference/2026-01-01/objects/createappointmenttypepayload)

[`deleteAppointmentTypePayload.appointmentType`](/reference/2026-01-01/objects/deleteappointmenttypepayload)

[`updateAppointmentTypePayload.appointmentType`](/reference/2026-01-01/objects/updateappointmenttypepayload)

[`Query.appointmentType`](/reference/2026-01-01/queries/appointmenttype)

## Definition

```
"""
An object containing information about the type of appointment
"""
type AppointmentType {
  """
  The number of clients with advance pricing for this appointment type
  """
  advance_pricing_for_clients_count: String


  """
  The number of providers with advance pricing for this appointment type
  """
  advance_pricing_for_providers_count: String


  """
  The autocomplete form for AI-generated charting notes associated with this appointment type
  """
  appointment_autocomplete_form: AppointmentAutocompleteForm


  """
  The appointment setting associated with this appointment type. An associated appointment setting overrides the providers general one.
  """
  appointment_setting: AppointmentSetting


  """
  The cpt code and units for this appointment type
  """
  appointment_type_cpt_code: AppointmentTypeCptCodeType


  """
  When true, the appointment pricing will be automatically increase based on actual duration
  """
  auto_increase_charge_for_actual_duration: Boolean


  """
  Is true if upcoming availability exists
  """
  availability_exists_for(
    """
    The appointment location id
    """
    appointment_location_id: String


    """
    The org level
    """
    org_level: Boolean = false


    """
    The provider id
    """
    provider_id: String


    """
    The list of provider ids
    """
    provider_ids: [ID]
  ): Boolean


  """
  List of available contact types for this appointment type
  """
  available_contact_types: [String]


  """
  When true, this appointment type is bookable by user groups associated through appointment_type_user_groups and appointment type is NOT bookable by ALL users
  """
  bookable_by_groups: Boolean


  """
  user groups that can book this appointment type. Associated through appointment_type_user_groups
  """
  bookable_groups: [UserGroup!]


  """
  When true, this appointment type is bookable by users without a user group
  """
  bookable_without_group: Boolean!


  """
  Checks to see if the client call to provider
  """
  client_call_provider: Boolean


  """
  Custom description shown to clients when self-scheduling
  """
  client_display_description: String


  """
  A name to use in the client scheduling widget instead of the default name field. Falls back to name if not set.
  """
  client_display_name: String


  """
  The raw client-facing display name without fallback to name. Used for editing.
  """
  client_facing_display_name: String


  """
  The status of whether the client can self-book this type of appointment
  """
  clients_can_book: Boolean!


  """
  Checks to see if the client has enough credit to book
  """
  clients_have_credit: Boolean


  """
  The date the Appointment Type was created
  """
  created_at: ISO8601DateTime!


  """
  If the provider's organization has this feature, this will customize the content of SMS reminder's Healthie sends.
  """
  custom_text_reminder_body: String


  """
  Date time appointment type was deleted
  """
  deleted_at: ISO8601DateTime


  """
  When true, the client will not be asked to add a reason when booking an appointment of this type
  """
  dont_ask_for_reason: Boolean


  """
  ID of the embedded custom module form
  """
  embed_question_form_id: String


  """
  All form requests which should be created after appointment
  """
  form_requests_after_appointment: [AppointmentTypeFormConnection!]


  """
  All form requests which should be created after appointment booking
  """
  form_requests_after_appointment_booking: [AppointmentTypeFormConnection!]


  """
  All form requests which should be created before appointment
  """
  form_requests_before_appointment: [AppointmentTypeFormConnection!]


  """
  Is true if group appointment available
  """
  has_available_group_appts(
    """
    The appointment location id
    """
    appointment_location_id: String


    """
    The provider id
    """
    provider_id: String
  ): Boolean


  """
  When true, this appointment type has specific appointment settings that override the general ones
  """
  has_specific_appointment_settings: Boolean


  """
  The unique identifier of the appointment type
  """
  id: ID!


  """
  Whether or not this appointment type will have insurance billing enabled
  """
  insurance_billing_enabled: Boolean


  """
  The status of whether appointments of this types are group appointments or not
  """
  is_group: Boolean!


  """
  The status of whether waitlist is enabled for an appointment or not
  """
  is_waitlist_enabled: Boolean!


  """
  The length of the appointment type (in minutes)
  """
  length: Int


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000. Only accessible by staff and providers
  """
  metadata: String


  """
  the name of the appointment type
  """
  name: String


  """
  A custom message to display if there are no available slots on a given day for an appointment type.
  """
  no_availability_message: String


  """
  The organization that the appointment type belongs to
  """
  organization_id: Int!


  """
  The position of the appointment type when shown in a list of other appointment types
  """
  position: Int


  """
  The price and cpt_code_price
  """
  price_and_cpt_price: PriceAndCptPriceType


  """
  The pricing for this appointment type
  """
  pricing: String


  """
  Get the pricing info for this appointment type
  """
  pricing_info: AppointmentPricingInfoType


  """
  Pricing option for this appointment type
  """
  pricing_option: String


  """
  providers associated with appointment type
  """
  provider_appt_type_connections: [ProviderApptTypeConnection!]


  """
  When true, certain clients (limited to non-established clients only and does not include provider-booked appointments) will be required to provide a credit card for booking
  """
  require_cc_at_booking: Boolean


  """
  When this setting is turned on, provider state licensing requirements will be enforced when clients try to schedule appointments.
  """
  require_in_state_clients: Boolean


  """
  Whether or not appointment type should use specific providers
  """
  require_specific_providers: Boolean!


  """
  position of appointment type when displayed in packages list
  """
  row_order: String


  """
  A label that includes the length of the appointment
  """
  time_on_label: String


  """
  The date the Appointment Type was updated
  """
  updated_at: ISO8601DateTime!


  """
  The user group associated with this appointment type.
  """
  user_group: UserGroup


  """
  The ID of the group clients are placed in after booking
  """
  user_group_id: String


  """
  The creator of the appointment type
  """
  user_id: Int


  """
  If provider state matches users or appointment type doesn't require state license restrictions.
  """
  valid_state_licensing_for(
    """
    The client state of residence
    """
    client_state_of_residence: String


    """
    The org level
    """
    org_level: Boolean = false


    """
    The provider id
    """
    provider_id: String


    """
    The list of provider ids
    """
    provider_ids: [ID]
  ): Boolean
}
```
