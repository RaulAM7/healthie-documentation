---
title: Appointments | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/scheduling/appointments/index
  md: https://docs.gethealthie.com/guides/scheduling/appointments/index.md
---

# Appointment Types

## The Appointment Type Object

```
// Some Example Fields for an Appointment Type.


{
  "id": "1",
  "name": "Initial Consultation",
  "is_group": false,
  "bookable_by_groups": false,
  "bookable_without_group": true,
  "length": 60, # length in minutes
  "available_contact_types": [
    "Healthie Video Call",
    "In Person",
    "Phone Call"
  ],
  "is_waitlist_enabled": false
}
```

Appointments Types are `AppointmentType` objects.

`AppointmentType` objects are used for 1:1 appointments, group appointments, and blocks to availability. You can view the full list of available fields [here](/reference/2024-06-01/objects/appointmenttype).

If you have questions about the overall functionality of appointment’s feature, you can find information [here](https://help.gethealthie.com/article/130-setting-appointment-types-and-enabling-disabling-clients-to-book).

## Retrieving an Appointment Type

```
query getAppointmentType($id: ID) {
  appointmentType(id: $id) {
    id
    name
    available_contact_types
    length
  }
}
```

Retrieving a specific Appointment Type is done via the `appointmentType` query.

Returns an [`AppointmentType`](/reference/2024-06-01/objects/appointmenttype) object.

## Creating an Appointment Type

```
mutation createAppointmentType(
  $name: String
  $length: Int
  $clients_can_book: Boolean
  $is_group: Boolean
  $bookable_without_group: Boolean
  $is_waitlist_enabled: Boolean
  $user_group_id: String
  $specific_groups: Boolean
  $bookable_group_ids: String
  $contact_type_overrides: [String]
  $appointment_setting: AppointmentTypeAppointmentSettingInput
) {
  createAppointmentType(
    input: {
      name: $name
      length: $length
      clients_can_book: $clients_can_book
      is_group: $is_group
      bookable_without_group: $bookable_without_group
      is_waitlist_enabled: $is_waitlist_enabled
      user_group_id: $user_group_id
      specific_groups: $specific_groups
      bookable_group_ids: $bookable_group_ids
      contact_type_overrides: $contact_type_overrides
      appointment_setting: $appointment_setting
    }
  ) {
    appointmentType {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Appointments are created using the `createAppointmentType` mutation.

The `createAppointmentType` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createappointmenttypeinput). We will go over some of inputs used to create an appointment type.

| Input                       | Info                                                                                                                                                                                                                                          |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                      | **Required**. The name of the appointment type.                                                                                                                                                                                               |
| `length`                    | **Required**. The length of the appointment type in minutes.                                                                                                                                                                                  |
| `is_group`                  | Optional. When `true`, indicates that this appointment type is used for group appointments.                                                                                                                                                   |
| `clients_can_book`          | Optional. When `false`, clients will not have the ability to self-book this appointment.                                                                                                                                                      |
| `contact_type_overrides`    | Optional. Available contact types for the appointment type. Provide one or more from `["video_chat", "in_person", "phone_call"]`.                                                                                                             |
| `specific_groups`           | Optional. Set to `true` if only specific groups should be able to book this meeting. To be used with `bookable_group_ids` and `bookable_without_group`.                                                                                       |
| `bookable_group_ids`        | Optional. A comma-separated list (`"1,2"`) of Client Group IDs that are able to book this appointment type. Use `"all"` for all groups.                                                                                                       |
| `bookable_without_group`    | Optional. If set to `true`, only clients with no groups can book this appointment type.                                                                                                                                                       |
| `user_group_id`             | Optional. ID of the Client Group that the Client will be placed in after booking.                                                                                                                                                             |
| `insurance_billing_enabled` | Optional. When `true`, enables automatic insurance billing for appointments of this type. Required for insurance auto-billing to function.                                                                                                    |
| `appointment_setting`       | Optional. [`AppointmentTypeAppointmentSettingInputObjectType`](/reference/2024-06-01/input-objects/appointmenttypeappointmentsettinginput) input object. Please refer to [Appointment Settings](#appointment-settings) for further reference. |

Returns a [`createAppointmentTypePayload`](/reference/2024-06-01/objects/createappointmenttypepayload) object.

## Updating an Appointment Type

```
mutation updateAppointmentType(
  $id: ID
  $name: String
  $length: Int
  $clients_can_book: Boolean
  $is_group: Boolean
  $bookable_without_group: Boolean
  $is_waitlist_enabled: Boolean
  $user_group_id: String
  $specific_groups: Boolean
  $bookable_group_ids: String
  $contact_type_overrides: [String]
  $appointment_setting: AppointmentTypeAppointmentSettingInput
) {
  updateAppointmentType(
    input: {
      id: $id
      name: $name
      length: $length
      clients_can_book: $clients_can_book
      is_group: $is_group
      bookable_without_group: $bookable_without_group
      is_waitlist_enabled: $is_waitlist_enabled
      user_group_id: $user_group_id
      specific_groups: $specific_groups
      bookable_group_ids: $bookable_group_ids
      contact_type_overrides: $contact_type_overrides
      appointment_setting: $appointment_setting
    }
  ) {
    appointmentType {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Appointment Types are updated via the `updateAppointmentType` mutation.

The `updateAppointmentType` mutation is called from an authenticated account.

We will go over some of them available to providers and staff below. The `updateAppointmentType` mutation shares many common inputs with [`createAppointmentType`](#creating-an-appointment-type) and those inputs (e.g `length` or `contact_type_overrides` work the same in both places).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateappointmenttypeinput).

| Input | Info                                                |
| ----- | --------------------------------------------------- |
| `id`  | **Required**. ID of the Appointment Type to update. |

Returns a [`updateAppointmentTypePayload`](/reference/2024-06-01/objects/updateappointmenttypepayload) object.

## Deleting an Appointment Type

Appointment Types can be (soft) deleted by authorized providers and staff members via the `deleteAppointmentType` mutation.

```
mutation deleteAppointmentType($id: ID) {
  deleteAppointmentType(input: { id: $id }) {
    appointmentType {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteAppointmentType` mutation is called from an authenticated provider/staff account.

| Input | Info                                                |
| ----- | --------------------------------------------------- |
| `id`  | **Required**. ID of the Appointment Type to delete. |

Returns a [`deleteAppointmentTypePayload`](/reference/2024-06-01/objects/deleteappointmenttypepayload) object.

## Listing Appointment Types

```
query getAppointmentTypes(
  $offset: Int
  $should_paginate: Boolean
  $page_size: Int
  $keywords: String
  $show_group: Boolean
  $provider_id: String
  $clients_can_book: Boolean
  $appointment_type_ids: String
  $with_deleted_appt_types: Boolean
) {
  appointmentTypes(
    offset: $offset
    should_paginate: $should_paginate
    page_size: $page_size
    keywords: $keywords
    show_group: $show_group
    provider_id: $provider_id
    clients_can_book: $clients_can_book
    appointment_type_ids: $appointment_type_ids
    with_deleted_appt_types: $with_deleted_appt_types
  ) {
    id
    name
    available_contact_types
    length
    is_group
    is_waitlist_enabled
  }
}
```

A list of Appointment Types can be retrieved via the `appointmentTypes` query. This query is called from an authenticated account.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/appointmenttypes#arguments).

We will go over some of them below.

| Input                  | Info                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------- |
| `should_paginate`      | Defaults to `true`. When `false`, the returned patient list is not paginated.       |
| `keywords`             | Optional. A term to search Appointment Types by. Can be searched by the name field. |
| `appointment_type_ids` | A *JSONified* array of Appt Type IDs to fetch. Example: `["1", "2"]`.               |

Returns a list of [`AppointmentType`](/reference/2024-06-01/objects/appointmenttype) objects.

## Using Appointment Type Credits

You may want to grant a number of credits to users for booking specific appointment types based on your subscription model. You can add credits to a user with the `updateClient` mutation, using the `appointment_type_credits_attributes` field. The credits can be queried on the User object using the `appointment_type_credits` field. Visit our [API Explorer](https://docs.gethealthie.com/docs/explorer.html) for more details.

# Appointment Settings

## The Appointment Setting Object

```
//  Some Example Fields for an Appointment Setting.


{
  "id": "1",
  "allow_clients_to_cancel_appt": true,
  "allow_clients_to_reschedule_appt": true,
  "allow_past_appointment_rescheduling": false,
  "always_send_confirm_notification": false,
  "appointment_locations": [
    {
      "id": "1",
      "location": "Bob's Office"
    }
  ],
  "appt_type_confirmed_email": false,
  "appt_type_reminder_email": false,
  "appt_type_website_booking_email": false,
  "ask_clients_to_confirm": false,
  "ask_to_confirm_via_text": false,
  "auto_invoicing": false,
  "buffer": "0",
  "calendar_color_schemes": [],
  "calendar_interval": "30",
  "cant_cancel_message": "Please contact provider to cancel",
  "cant_reschedule_message": "Please contact provider to reschedule",
  "client_should_call_provider": false,
  "clients_have_billing": true,
  "confirm_by_default": false
}
```

Appointment Settings are `AppointmentSetting` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/appointmentsetting).

## Retrieving an Appointment Setting

```
query getAppointmentSetting($id: ID, $provider_id: ID) {
  appointmentSetting(id: $id, provider_id: $provider_id) {
    id
    name
    available_contact_types
    length
  }
}
```

Retrieving a specific Appointment Setting is done via the `appointmentSetting` query.

Please refer to [`AppointmentSetting`](/reference/2024-06-01/objects/appointmentsetting) object definition for a list of all available fields.

| Input         | Info                                                       |
| ------------- | ---------------------------------------------------------- |
| `id`          | Either this or `provider_id` is required.                  |
| `provider_id` | Optional. Get Appointment Setting for a specific Provider. |

Returns an [`AppointmentSetting`](/reference/2024-06-01/objects/appointmenttype) object.

## Creating an Appointment Setting

```
mutation createAppointmentSetting(
  $buffer: String
  $minimum_advance_cancel_time: Int
  $minimum_advance_reschedule_time: Int
  $minimum_advance_schedule_time: Int
  $end_reminder_one_hour_before: Boolean
  $ask_clients_to_confirm: Boolean
) {
  createAppointmentSetting(
    input: {
      buffer: $buffer
      minimum_advance_cancel_time: $minimum_advance_cancel_time
      minimum_advance_reschedule_time: $minimum_advance_reschedule_time
      minimum_advance_schedule_time: $minimum_advance_schedule_time
      end_reminder_one_hour_before: $end_reminder_one_hour_before
      ask_clients_to_confirm: $ask_clients_to_confirm
    }
  ) {
    appointmentSetting {
      buffer
      minimum_advance_cancel_time
      minimum_advance_reschedule_time
      minimum_advance_schedule_time
      end_reminder_one_hour_before
      ask_clients_to_confirm
    }


    messages {
      field
      message
    }
  }
}
```

Appointment Settings are created using the `createAppointmentSetting` mutation.

The `createAppointmentSetting` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createappointmentsettinginput).

Returns a [`createAppointmentSettingPayload`](/reference/2024-06-01/objects/createappointmentsettingpayload) object.

## Updating an Appointment Setting

```
mutation updateAppointmentSetting(
  $id: ID
  $buffer: String
  $minimum_advance_cancel_time: Int
  $minimum_advance_reschedule_time: Int
  $minimum_advance_schedule_time: Int
  $end_reminder_one_hour_before: Boolean
  $ask_clients_to_confirm: Boolean
) {
  updateAppointmentSetting(
    input: {
      id: $id
      buffer: $buffer
      minimum_advance_cancel_time: $minimum_advance_cancel_time
      minimum_advance_reschedule_time: $minimum_advance_reschedule_time
      minimum_advance_schedule_time: $minimum_advance_schedule_time
      end_reminder_one_hour_before: $end_reminder_one_hour_before
      ask_clients_to_confirm: $ask_clients_to_confirm
    }
  ) {
    appointmentSetting {
      buffer
      minimum_advance_cancel_time
      minimum_advance_reschedule_time
      minimum_advance_schedule_time
      end_reminder_one_hour_before
      ask_clients_to_confirm
    }


    messages {
      field
      message
    }
  }
}
```

Appointment Settings are updated via the `updateAppointmentSetting` mutation.

The `updateAppointmentSetting` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateappointmentsettinginput).

We will go over some of them below. The `updateAppointmentSetting` mutation shares many common inputs with `createAppointmentSetting` and those inputs (e.g `ask_clients_to_confirm` or `buffer` work the same in both places).

| Input | Info                                                   |
| ----- | ------------------------------------------------------ |
| `id`  | **Required**. ID of the Appointment Setting to update. |

Returns an [`updateAppointmentSettingPayload`](/reference/2024-06-01/objects/updateappointmentsettingpayload) object.

# Appointments

## The Appointment Object

```
 # Some Example Fields for a 1:1 appointment.


{
  "appointment": {
    "id": "9900",
    "date": "2020-05-08 21:00:00 UTC",
    "contact_type": "Secure Videochat",
    "appointment_type_id": "1128",
    "pm_status": "Occurred",
    "provider": {
      "id": "11",
      "full_name": "Jonas Salk"
    },
    "form_answer_group": {
      "id": "1234",
      "finished": true,
      "form_answers": [
        {
          "answer": "Example answer",
          "label": "Test field",
          "id": "123321",
          "displayed_answer": "Example answer"
        }
      ]
    },
    "filled_embed_form": {
      "id": "5678",
      "finished": true,
      "form_answers": [
        {
          "answer": "Example answer",
          "label": "Test field",
          "id": "553321",
          "displayed_answer": "Example answer"
        }
      ]
    },
    "user": {
      "id": "311",
      "full_name": "Example Patient"
    }
  }
}
```

Appointments are `Appointment` objects.

`Appointment` objects are used for 1:1 appointments, group appointments, and blocks to availability. You can view the full list of available fields [here](/reference/2024-06-01/objects/appointment).

Appointments are considered active if they are 1) not deleted, 2) have a `pm_status` that is not “Cancelled”, “Re-Scheduled”, or “No-Show”. If you have questions about the overall functionality of appointment’s feature, you can find information [here](https://help.gethealthie.com/category/1062-scheduling-appointments).

Appointments can have two [`FormAnswerGroup`](/reference/2024-06-01/objects/formanswergroup) objects attached: `filled_embed_form` which is normally added at the time of booking, and `form_answer_group` which is added during the appointment session. Each of these has a one-to-one relationship with the `Appointment` object.

## Creating an Appointment

Appointments are created in two main ways, `createAppointment` and `completeCheckout`.

`completeCheckout` books the appointment from the patient’s perspective (and can be done unathenticated).

`createAppointment` books the appointment from a staff member’s perspective, requires authentication, and allows for scheduling appointments outside of available slots. Note that `createAppointment` does not enforce availability **unless the argument `enforce_availability: true` is passed in**, but `completeCheckout` does enforce availability. This prevents patients from self-scheduling over existing appointments.

The code sample to the right is an example of a simple `createAppointment` mutation.

| Method                           | Corresponding Mutation |
| -------------------------------- | ---------------------- |
| Added by a provider/staff member | `createAppointment`    |
| Added by a patient (client)      | `completeCheckout`     |

### `createAppointment` Mutation

```
mutation createAppointment(
  $user_id: String, # ID of patient in Healthie
  $appointment_type_id: String, # ID of appointment type in Healthie
  $contact_type: String, # e.g "Phone Call"
  $other_party_id: String, # ID of provider in Healthie. Defaults to authenticated user if left blank,
  $datetime: String, # Timestamp in YYYY-MM-DD HH:MM:SS or ISO8601 format, supercedes date, time params.
) {
  createAppointment(
    input: {
      user_id: $user_id,
      appointment_type_id: $appointment_type_id,
      contact_type: $contact_type,
      other_party_id: $other_party_id,
      datetime: $datetime,
    }
  ) {
    appointment {
      id
    }
    messages {
      field
      message
    }
  }
```

The `createAppointment` mutation must be called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createappointmentinput). We will go over some of inputs used to create an appointment with a client below.

| Input                 | Info                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `datetime`            | Required. The datetime of the appointment in ISO8601 format.                                                                                                                                                        |
| `appointment_type_id` | Required. The ID of the appointment type                                                                                                                                                                            |
| `contact_type`        | Required. How the appointment will be conducted. You can see the list of available ones via the `contactTypes` query                                                                                                |
| `other_party_id`      | Required. ID of the provider. Defaults to the authenticated user’s ID                                                                                                                                               |
| `user_id`             | For 1:1 appointments, this is the ID of the client. For group appointments, leave this out                                                                                                                          |
| `attendee_ids`        | A comma-seprated list of client IDs to add to the appointment. For 1:1 appointments, leave this out                                                                                                                 |
| `providers`           | A comma-seprated list of provider IDs to add to the appointment as additional providers. For 1:1 appointments, leave this out. The ID of the primary provider `other_party_id `should not be included in this list. |

### `completeCheckout` Mutation

For information on `completeCheckout`, take a look at “Step 4 - Book the appointment” in the patient self-scheduling example [here](/docs#patient-self-scheduling).

## Retrieving an Appointment

```
query getAppointment($id: ID) {
  appointment(id: $id) {
    id
    date
    contact_type
    pm_status
    provider {
      id
      full_name
    }
    user {
      id
      full_name
    }
    appointment_type {
      id
      name
    }
  }
}
```

Retrieving a specific appointment’s information is done via the `appointment` query.

| Input             | Info                                                                           |
| ----------------- | ------------------------------------------------------------------------------ |
| `id`              | Required. The ID of the appointment.                                           |
| `include_deleted` | When true, an appointment can be retrieved, even if it was previously deleted. |

## Updating an Appointment

Regardless of user type, Appointments are updated via the `updateAppointment` mutation. However, the allowed and required inputs vary slightly based on whether a provider or a client is the one updating.

| Method                          | Corresponding Mutation |
| ------------------------------- | ---------------------- |
| Updated by a provider or client | `updateAppointment`    |

### `updateAppointment` Mutation

```
mutation updateAppointment(
    $pm_status: String,
    $datetime: String,
    $id: ID,
  ) {
    updateAppointment(
      input: {
        $pm_status: String,
        $datetime: String,
        $id: ID,
      }
    ) {
      appointment {
        id
        date
      }
      messages {
        field
        message
      }
    }
  }
```

The `updateAppointment` mutation is called from an authenticated account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateappointmentinput).

We will go over some of them available to providers and staff below. The `updateAppointment` mutation shares many common inputs with `createAppointment` and those inputs (e.g `other_party_id` or `date` work the same in both places).

| Input       | Info                                                                                                                                                              |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`        | Required                                                                                                                                                          |
| `pm_status` | The status of the appointment. Can be one of “Occurred”, “No-Show”, “Re-Scheduled”, “Cancelled”. If enabled, “Late Cancellation” and “Checked-In” are also valid. |

For more information on updating an appointment as a patient, please look at the example [here](/docs#patient-rescheduling)

## Deleting/Cancelling an appointment.

Appointments can be (soft) deleted by authorized providers and staff members via the `deleteAppointment` mutation. Appointments can be cancelled (without deleting them) by patients via `deleteAppointment` or providers and staff via `updateAppointment`.

| Method                                                  | Corresponding Mutation |
| ------------------------------------------------------- | ---------------------- |
| Deleted by a provider/staff member                      | `deleteAppointment`    |
| Canceled by a patient (but still visible)               | `deleteAppointment`    |
| Canceled by a provider/staff member (but still visible) | `updateAppointment`    |

### `deleteAppointment` mutation

```
mutation deleteAppointment($id: ID, $deleteRecurring: Boolean) {
  deleteAppointment(input: { id: $id, deleteRecurring: $deleteRecurring }) {
    appointment {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `deleteAppointment` mutation is called from an authenticated account. If it is called from a provider/staff account, the appointment is deleted, and is no longer visible. When it is called from a patient account, the appointment’s `pm_status` is set to Cancelled, and the appointment is still visible.

| Input             | Info                                                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `id`              | Required                                                                                                                   |
| `deleteRecurring` | Boolean. For recurring appointments only. When true, all subsequent instances of the appointment will be canceled as well. |

## Listing Appointments

```
query appointments(
  $user_id: ID
  $filter: String
  $order_by: String
  $should_paginate: Boolean
  $offset: Int
  $is_active: Boolean
  $with_all_statuses: Boolean
) {
  appointmentsCount(user_id: $user_id, filter: $filter, is_org: true, is_active: $is_active)
  appointments(
    is_active: $is_active
    user_id: $user_id
    filter: $filter
    is_org: true
    order_by: $order_by
    should_paginate: $should_paginate
    offset: $offset
    with_all_statuses: $with_all_statuses
  ) {
    id
    date
    contact_type
    length
    location
    provider {
      id
      full_name
    }


    appointment_type {
      name
      id
    }


    attendees {
      id
      full_name
      first_name
      avatar_url
      phone_number
    }
  }
}
```

A list of appointments can be retrieved via the `appointments` query. This query is called from an authenticated account.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/appointments#arguments).

We will go over some of them below.

| Input               | Info                                                                                                                                                                 |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `should_paginate`   | Defaults to false. When false, the returned patient list is not paginated.                                                                                           |
| `filter`            | Optional. Defaults to `filter` (so by default just future appointments will be returned). Options are \[“didnt-occur”, “future”, “upcoming”, ‘past’. “ended”, “all”] |
| `order_by`          | View the enum [here](/schema/appointmentorderkeys.doc) to see all potential options.                                                                                 |
| `user_id`           | Optional. When passed in, appointments for that specific user will be returned. Defaults to current user.                                                            |
| `is_org`            | Optional. When passed in from a provider or staff account, appointments from all providers in the organization can be returned.                                      |
| `is_active`         | Optional. When true, no non-active (canceled, no-showed, rescheduled, etc) appointments will be returned.                                                            |
| `with_all_statuses` | Optional. When true, all appointments, regardless of `pm_status`, will be returned. This takes precendece over the `didnt-occur` filter and `is_active`.             |

## Recurring Appointments

### The Recurring Appointment Object

```
// Example Fields for a Recurring Appointment.


{
  "id": "123",
  "repeat_interval": "Weekly",
  "repeat_times": "10",
  "join_all": true,
  "previous_recurring_appointment_id": "456"
}
```

Recurring Appointments are `RecurringAppointment` objects that define the pattern for a series of appointments.

You can view the full list of available fields [here](/reference/2024-06-01/objects/recurringappointment).

### Creating Recurring Appointments

Recurring appointments are created by including the `recurring_appointment` parameter when using the `createAppointment` mutation:

```
mutation createRecurringAppointment(
  $user_id: String
  $appointment_type_id: String
  $contact_type: String
  $other_party_id: String
  $datetime: String
  $recurring_appointment: RecurringAppointmentInput
) {
  createAppointment(
    input: {
      user_id: $user_id
      appointment_type_id: $appointment_type_id
      contact_type: $contact_type
      other_party_id: $other_party_id
      datetime: $datetime
      recurring_appointment: $recurring_appointment
    }
  ) {
    appointment {
      id
      recurring_appointment_id
      current_position_in_recurring_series
      recurring_appointment {
        id
        repeat_times
        repeat_interval
        join_all
        previous_recurring_appointment_id
      }
    }
    messages {
      field
      message
    }
  }
}
```

### Recurring Appointment Parameters

| Input             | Info                                                                                                                                                                                          |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `repeat_interval` | **Required**. How often the appointment repeats. Valid values: `"Weekly"`, `"Biweekly"`, `"Monthly"`, `"Every 4 Weeks"`                                                                       |
| `repeat_times`    | **Required**. Total number of appointments in the series (including the first one). Must be a string representation of an integer (e.g., `"5"` for 5 appointments)                            |
| `join_all`        | Optional. When `true`, automatically registers all attendees for every appointment in the series. When `false`, attendees must be added to each appointment individually. Defaults to `false` |

### Example Variables

```
{
  "user_id": "123",
  "appointment_type_id": "456",
  "contact_type": "Healthie Video Call",
  "other_party_id": "789",
  "datetime": "2024-03-15T14:00:00Z",
  "recurring_appointment": {
    "repeat_interval": "Weekly",
    "repeat_times": "8",
    "join_all": true
  }
}
```

This creates a series of 8 weekly appointments starting on March 15, 2024, with all attendees automatically registered for each session.

### Updating Recurring Appointments

Recurring appointments can be updated using the `updateAppointment` mutation. The behavior depends on which appointment in the series you’re updating.

```
mutation updateRecurringAppointment(
  $id: ID
  $updateRecurring: Boolean
  $date: String
  $time: String
  $recurring_appointment: RecurringAppointmentInput
) {
  updateAppointment(
    input: {
      id: $id
      updateRecurring: $updateRecurring
      date: $date
      time: $time
      recurring_appointment: $recurring_appointment
    }
  ) {
    appointment {
      id
      recurring_appointment_id
      current_position_in_recurring_series
      recurring_appointment {
        id
        repeat_times
        repeat_interval
        join_all
        previous_recurring_appointment_id
      }
    }
    messages {
      field
      message
    }
  }
}
```

### Update Parameters

| Input                   | Info                                                                                                                                            |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                    | **Required**. ID of the specific appointment instance to update                                                                                 |
| `updateRecurring`       | Optional. When `true`, applies changes to all future appointments in the series. When `false` or omitted, only updates the specific appointment |
| `recurring_appointment` | Optional. Object containing updated recurring appointment parameters (`repeat_interval`, `repeat_times`, `join_all`)                            |

### Recurring Appointment Splitting Behavior

Updating an appointment in the middle of a recurring series will automatically split the series into separate recurring series if one of the following scenarios is true:

### When Splitting Occurs

1. **Updating any appointment other than the first in the series** with `updateRecurring: true`
2. **Changing the `repeat_interval`** of the recurring series
3. **Making time/date changes** to appointments.

### Splitting Process

When a recurring appointment series is split:

1. **Original series** keeps appointments up to the edited appointment
2. **New recurring appointment** is created for the edited appointment and all future appointments
3. **`previous_recurring_appointment_id`** is set on the new recurring appointment to reference the original series
4. **Appointment counts** are automatically adjusted for both series

### Example: Splitting a Weekly Series

```
// Original series: 10 weekly appointments
// User updates appointment #5 with new time


// Result:
// - Original series: appointments 1-4 (repeat_times = 4)
// - New series: appointments 5-10 (repeat_times = 6, previous_recurring_appointment_id = original_id)
```

### Tracking Split History

The `previous_recurring_appointment_id` field allows you to trace the history of split recurring appointments:

```
# This points to the original recurring appointment this was split from
query getRecurringAppointmentHistory($id: ID) {
  recurringAppointment: appointment(id: $id) {
    recurring_appointment {
      id
      previous_recurring_appointment_id
    }
  }
}
```

### Non-splitting Scenarios

The splitting of a recurring appointment series does **not** occur when:

* Updating the **first appointment** in a series (updates apply to entire series)
* Only changing `repeat_times` without changing `repeat_interval`
* Making changes with `updateRecurring: false` (affects only single appointment)

### Deleting Recurring Appointments

Use the `deleteAppointment` mutation with the `deleteRecurring` parameter:

```
mutation deleteRecurringAppointment($id: ID, $deleteRecurring: Boolean) {
  deleteAppointment(input: { id: $id, deleteRecurring: $deleteRecurring }) {
    appointment {
      id
    }
    messages {
      field
      message
    }
  }
}
```

| Input             | Info                                                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `id`              | **Required**. ID of any appointment in the recurring series                                                                   |
| `deleteRecurring` | **Required**. When `true`, deletes all future appointments in the series. When `false`, deletes only the specific appointment |

## Appointment Booking Warnings

The `appointmentBookingWarnings` query can be used to return:

1. a list of any possible conflicting events for a specific date and time (as well as for recurring event instances)
2. a list of clients that do not have any credits available for booking (if using the Client Credit System)

Returns an array of [`AppointmentBookingWarning`](/schema/appointmentbookingwarning.doc) objects. Conflicting events will have a `category` of “Event Conflicts,” and clients without the necessary credits will have a category of “Credit Deficits.” It is possible to have both types of warnings returned in the same response, if there are events existing in the date/time requested, and the proposed client does not have the appropriate amount of credit.

```
query getAppointmentBookingWarnings(
  $appointment_type_id: ID
  $provider_id: ID
  $date: String
  $time: String
  $timezone: String
) {
  appointmentBookingWarnings(
    appointment_type_id: $appointment_type_id
    provider_id: $provider_id
    date: $date
    time: $time
    timezone: $timezone
  ) {
    category
    subtitle
    potential_issues
    potential_issue_ids
  }
}
```

```
# Sample parameters for a request


{
    "appointment_type_id": "1",
    "provider_id":"3",
    "date":"July 11, 2024",
    "time":"12 00",
    "timezone":"America/New_York"
}


# Sample response returning a conflicting event


{
    "data": {
        "appointmentBookingWarnings": [
            {
                "category": "Event Conflicts",
                "subtitle": "Existing event(s) for the provider conflict with this one. Would you like to book this event anyway?",
                "potential_issues": [
                    "1:1 Session - Jul 11, 12:00 PM EDT",
                    "1:1 Session - Jul 11, 12:30 PM EDT"
                ],
                "potential_issue_ids": [
                    "2111",
                    "2112"
                ]
            }
        ]
    }
}
```

Here are the available parameters available when checking for conflicting events and credit deficits.

| Input                     | Info                                                                                                                                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `provider_id`             | The calendar of this provider will be searched for conflicting events.                                                                                                                                                                                 |
| `date`                    | What date to search for conflicts. Example: “May 23, 2024”                                                                                                                                                                                             |
| `time`                    | The time to search for a conflicting event, which is combined with the `date` field above. Format is “HH MM” in 24-hour time.                                                                                                                          |
| `timezone`                | Optional. Timezone used for the `date` and `time` arguments. Defaults to the timezone of the `provider_id` used in query. Timezone value must be on [this list of timezone identifiers](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| `appointment_type_id`     | Appointment type is used to determine what span of time to use when checking for conflicts (30 minutes, 60 minutes, etc.). Either this parameter or `length_in_minutes` are required.                                                                  |
| `length_in_minutes`       | Specific span of time starting from `date` and `time` to check for conflicting events. Either this parameter or `appointment_type_id` are required.                                                                                                    |
| `attendee_ids`            | Optional. This parameter (a comma-delimited string of client IDs) is used for checking whether the passed attendees have enough credits available for booking. The `appointment_type_id` parameter is required when using this parameter.              |
| `additional_provider_ids` | Optional. Additional providers whose calendars should be searched for conflicting events. Should be a comma-delimited string of provider IDs.                                                                                                          |
| `recurring_appt_id`       | Optional. When rescheduling an existing recurring appointment, passing the `recurring_appt_id` will ensure any existing recurring events in series will not be returned as conflicts.                                                                  |
| `current_appt_id`         | Optional. When rescheduling an existing appointment, passing this parameter ensures that appointment will not show as a conflict.                                                                                                                      |
| `is_repeating`            | Optional. Whether to repeat the search based on repeating options. Defaults to `false`.                                                                                                                                                                |
| `repeat_interval`         | Optional. What interval to check again for conflicts. Options are “Weekly”, “Biweekly”, “Monthly”, or “Every 4 Weeks”.                                                                                                                                 |
| `repeat_times`            | Optional. How many times to check the repeat interval for conflicts.                                                                                                                                                                                   |

# Insurance Billing for Appointments

Healthie supports automatic insurance billing for appointments through insurance-enabled appointment types. When appointments are marked as “Occurred”, the system automatically calculates and charges patients their insurance responsibility amounts.

## Insurance-Enabled Appointment Types

To enable automatic insurance billing, set `insurance_billing_enabled: true` when creating appointment types:

```
mutation createInsuranceEnabledAppointmentType(
  $name: String
  $length: Int
  $insurance_billing_enabled: Boolean
) {
  createAppointmentType(
    input: {
      name: $name
      length: $length
      insurance_billing_enabled: $insurance_billing_enabled
    }
  ) {
    appointmentType {
      id
      name
      insurance_billing_enabled
    }
  }
}
```

### Requirements

Insurance-enabled appointment types require:

* **Plus plan or above** with insurance billing automation access
* **CPT codes** linked to appointment types (for coinsurance calculations)
* **Contracted rates** configured by payer
* **Patient primary insurance** with billing method configured

## How It Works

When an appointment with `insurance_billing_enabled: true` is marked as “Occurred”:

1. **Validates** patient has primary insurance with billing method configured
2. **Calculates** patient responsibility (copay/coinsurance/deductible)
3. **Creates** billing item with calculated amount
4. **Triggers** auto-charge or auto-invoice based on patient payment method

For comprehensive setup instructions, configuration examples, troubleshooting, and complete API workflows, see the **[Insurance Auto-Billing](/guides/billing/insurance-auto-billing/)** guide.
