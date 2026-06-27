---
title: Scheduling | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/scheduling/patient_scheduling/index
  md: https://docs.gethealthie.com/guides/scheduling/patient_scheduling/index.md
---

## Patient Self-Scheduling

Client self-scheduling is a common use case for our API. With the API, you can build a self-scheduling experience with a much more customized UI than [Healthie’s built-in embeds](https://help.gethealthie.com/article/75-integrate-healthie-with-website) allow for.

[Our example repo](https://github.com/healthie/healthie_sample_booking_widget) is an example (built with React) on how to implement self-scheduling with the API. Let’s break down the API calls we make in that widget.

```
query appointmentTypes($clients_can_book: Boolean, $provider_id: String) {
  appointmentTypes(provider_id: $provider_id, clients_can_book: $clients_can_book) {
    id
    name
    length
    available_contact_types
    is_group
  }
}
```

**1) Get Potential Appointment and Contact Types**

All self-scheduled appointments in Healthie require an appointment type and a contact type. In this `appointmentTypes` query, we grab all appointment types that are bookable by clients, and the contact type options for each appointment type. We will use these in subsequent queries to receive accurate availability, and ultimately book the appointment. If you already know what appointment type and contact type you want the user to book, you can skip this step, and proceed to step 2.

```
query daysAvailableForRange(
  $provider_id: String
  $date_from_month: String
  $end_date: String
  $start_date: String
  $org_level: Boolean
  $contact_type: String
  $timezone: String
  $provider_ids: [String]
  $appt_type_id: String
  $appt_loc_id: String
  $clients_can_join_waitlist: Boolean
  $appointment_to_reschedule_id: ID
  $start_range_boundary: String
  $end_range_boundary: String
  $licensed_in_state: String
  $tag_ids: [ID]
) {
  daysAvailableForRange(
    provider_id: $provider_id
    date_from_month: $date_from_month
    end_date: $end_date
    start_date: $start_date
    org_level: $org_level
    contact_type: $contact_type
    timezone: $timezone
    provider_ids: $provider_ids
    appt_type_id: $appt_type_id
    appt_loc_id: $appt_loc_id
    clients_can_join_waitlist: $clients_can_join_waitlist
    appointment_to_reschedule_id: $appointment_to_reschedule_id
    start_date_boundary: $start_range_boundary
    end_date_boundary: $end_range_boundary
    licensed_in_state: $licensed_in_state
    tag_ids: $tag_ids
  )
}
```

**2) Get Available Days**

A very common self-scheduling UI component is to present the client with days that have open time. The client then selects a day to see the specific available time slots. This interface is used in Healthie’s hosted widgets, in the open source example, and in other popular tools like Calendly. To power this, we can call the `daysAvailableForRange` query. This query should be used to query for large time ranges, whereas the `availableSlotsForRange` query should be used to query for individual available appointment slots on a specific day.

To clarify, the `daysAvailableForRange` query will return an array of days on which a provider has availability, whereas `availableSlotsForRange` returns individual appointment slots which are available to be booked.

This query example shows 16 arguments, but only two are required, `provider_id` and `appt_type_id`. If `start_date` is passed in, then `end_date` is required too, and vice-versa.

`appt_type_id` is the ID of the appointment type you grabbed in step 1. `provider_id` is the ID of the provider (or just a provider in the organization in the case of searching availability across multiple providers), and `date_from_month` is a date (e.g “2021-10-10”) in the month that you want to search available days in. If `date_from_month` is not passed in, the query will default to the current date. `start_date` and `end_date` allow users to set a custom date range, and will override `date_from_month` if both are passed.

Users can also optionally pass in `start_date_boundary` and `end_date_boundary` to prevent this query from returning dates prior to the `start_date_boundary` or after the `end_date_boundary`.

To briefly go over some of the other potential arguments, `org_level` determines if you want availability just for the given `provider_id`, or for multiple providers in the given provider’s organization. It defaults to false.

If you send in `org_level` as true, you can also send in an array of `provider_ids`. This argument lets you search against a given subset of providers in the organization. For example, my organization has 10 providers, I can send in an array with five ids, and the query will only return availabilities for those five providers.

Finally, the `timezone` argument determines what timezone to calculate the availability in. It takes in a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If you don’t send this in, the query will use the provider’s timezone.

This query will return an array of days with availability from the given month. e.g \[“2021-10-10”, “2021-10-15”, “2021-10-20”]. We then have the user select a day, and move to step 3. If we already knew the appointment type, contact type, and date the user wanted, we could have skipped the first two steps.

```
query availableSlotsForRange(
  $provider_id: String
  $start_date: String
  $end_date: String
  $org_level: Boolean
  $contact_type: String
  $timezone: String
  $provider_ids: [String]
  $appt_type_id: String
  $appointment_type_id: ID
  $appt_loc_id: String
  $clients_can_join_waitlist: Boolean,
  $appointment_to_reschedule_id: ID,
  $start_range_boundary: String,
  $end_range_boundary: String,
  $licensed_in_state: String
  $tag_ids: [ID]
) {
  availableSlotsForRange(
    provider_id: $provider_id
    start_date: $start_date
    end_date: $end_date
    contact_type: $contact_type
    timezone: $timezone
    org_level: $org_level
    provider_ids: $provider_ids
    appt_type_id: $appt_type_id
    appt_loc_id: $appt_loc_id
    clients_can_join_waitlist: $clients_can_join_waitlist,
    appointment_to_reschedule_id: $appointment_to_reschedule_id,
    start_date_boundary: $start_range_boundary,
    end_date_boundary: $end_range_boundary,
    licensed_in_state: $licensed_in_state,
    tag_ids: $tag_ids
  ) {
    user_id
    date
    appointment_id
    is_fully_booked
    has_waitlist_enabled
  }
  appointmentType(id: $appointment_type_id) {
    id
    name
    length
    no_availability_message
    availability_exists_for (
      provider_id: $provider_id,
      org_level: $org_level,
      appointment_location_id: $appt_loc_id
    )
  }
}
```

**3) Get Available Slots**

Now that we have the day, the next step is to get specific available time slots on that day. To do so, we use the `availableSlotsForRange` query. Many of the above arguments match `daysAvailableForRange`. `start_date` and `end_date` are both required and are used to set up the range of time that we check availability for. For example, if I send in a `start_date` of “2021-10-10”, an `end_date` of “2021-10-12”, and a timezone of `America/New_York`, the query will check availability starting at “2021-10-10 00:00:00 EDT -04:00” to “2021-10-12 23:59:59 EDT -04:00”.

While it is possible to query `availableSlotsForRange` across multiple days, we generally recommend querying across a range of 24 hours or less. Longer date ranges will take longer to process and may result in timeout errors. We recommend first using `daysAvailableForRange` to query for available days, and then query `availableSlotsForRange` on a specific available day to get each available slot.

In our case, we are just checking availability on one day, so we would send in an identical `start_date` and `end_date`.

| Input                 | Info                                                                                                                                                                                                                          |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `provider_id`         | **Required**. The ID of the provider to search available slots for.                                                                                                                                                           |
| `start_date`          | **Required**. Date in the `YYYY-MM-DD` format indicating the lower date range boundary to return available slots for.                                                                                                         |
| `end_date`            | **Required**. Date in the `YYYY-MM-DD` format indicating the upper date range boundary to return available slots for.                                                                                                         |
| `timezone`            | Timezone used for the `start_date` and `end_date` arguments. Defaults to the patient’s timezone. Timezone value must be on [this list of timezone identifiers](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| `start_date_boundary` | Date in the `YYYY-MM-DD` format indicating. If provided, the query will not return any slots before this date even if `start_date` is before this date.                                                                       |
| `end_date_boundary`   | Date in the `YYYY-MM-DD` format. If provided, the query will not return any slots after this date even if `end_date` is after this date.                                                                                      |

The query returns an array of [`PotentialAppointmentSlots`](/reference/2024-06-01/objects/potentialappointmentslot). We have the user select one of those slots, and use the `user_id` and `date` from the slot in the next (and final) step. Please note the `date` here is a full datetime string (e.g “2021-10-10 10:00:00 EDT -04:00”) and `user_id` is the ID of the available provider.

```
mutation completeCheckout(
  $appointment_type_id: String
  $contact_type: String
  $date: String
  $first_name: String
  $last_name: String
  $email: String
  $phone_number: String
  $provider_id: String
  $timezone: String
) {
  completeCheckout(
    input: {
      appointment_type_id: $appointment_type_id
      contact_type: $contact_type
      date: $date
      timezone: $timezone
      first_name: $first_name
      last_name: $last_name
      email: $email
      phone_number: $phone_number
      provider_id: $provider_id
    }
  ) {
    appointment {
      provider {
        id
        full_name
      }
      id
      date
      contact_type
      appointment_type {
        id
        name
        length
      }
    }
    messages {
      field
      message
    }
  }
}
```

**4) Book the Appointment**

Now, we have the desired appointment type, contact type, appointment date/time, and provider. That means we have everything we need to schedule the appointment. To do so, we use the `completeCheckout` mutation.

The `contact_type`, `date`, `timezone`, `appointment_type_id`, and `provider_id` should match what we collected in the prior steps. If the client is authenticated, then those are the only fields you need. However, in our example, the client is unauthenticated, so we need to send in some info about them as well. That extra info (`email`, `first_name`, `last_name`, and `phone_number`) are used to either match the appointment to an existing client in the provider’s account, or create a client record on the fly.

## Patient Rescheduling

In addition to scheduling new appointments, The Healthie API can also be used to allow patients to reschedule already booked ones. A patient’s ability to reschedule is controlled by your appointment settings. You can find more info on adjusting those [here](https://help.gethealthie.com/article/154-cancelling-an-appointment-on-calendar).

The rescheduling workflow is similar to self-scheduling, but has some key differences. Here are the API steps we use for patient rescheduling. All of the below steps are meant to be taken from an authenticated patient account.

```
query appointments(
  $filter: String # "upcoming"
  $should_paginate: Boolean # true
  $is_active: Boolean # true
) {
  appointmentsCount(filter: $filter, is_active: $is_active)
  appointments(is_active: $is_active, filter: $filter, should_paginate: $should_paginate) {
    id
    date
    other_party_id
    appointment_type_id
  }
}
```

**1) Get The Appointment ID**

To check availability and reschedule an appointment, you will need the ID for the appointment, the provider (`other_party_id`), and appointment type. Here’s a query to get paginated upcoming active appointments for a patient. These IDs will be used in the subsequent steps.

```
query daysAvailableForRange(
  $provider_id: String # Should be the other_party_id from Step 1
  $date_from_month: String
  $timezone: String
  $appt_type_id: String # should be the appointment_type_id from Step 1
  $appointment_to_reschedule_id: ID # should be the ID of the appointment from Step 1
) {
  daysAvailableForRange(
    provider_id: $provider_id
    date_from_month: $date_from_month
    timezone: $timezone
    appt_type_id: $appt_type_id
    appointment_to_reschedule_id: $appointment_to_reschedule_id
  )
}
```

**2) Get Available Days**

In our rescheduling UI, we present the patient with days that have open time. The patient then selects a day to see the specific available time slots. To power this, we can call the `daysAvailableForRange` query.

| Input                          | Info                                                                                                                                                                                                                                          |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `provider_id`                  | Required. The provider whose availability should be checked. Needs to match the `other_party_id` of the appointment that is being rescheduled.                                                                                                |
| `appt_type_id`                 | Required. The ID of the appointment’s appointment type. Needs to match the `appointment_type_id` of the appointment that is being rescheduled.                                                                                                |
| `date_from_month`              | Required. A date (e.g “2021-11-20”) from the month that you want to check available days in.                                                                                                                                                  |
| `appointment_to_reschedule_id` | Required. Needs to match the `id` of the appointment that is being rescheduled.                                                                                                                                                               |
| `timezone`                     | Optional. Determines what timezone to calculate the availability in. Defaults to the patient account’s timezone. Timezone value must be on [this list of timezone identifiers](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |

This query will return an array of days with availability from the given month. e.g \[“2021-11-20”, “2021-11-28”, “2021-11-29”]. We then have the patient select a day, and move to step 3.

```
query availableSlotsForRange(
  $provider_id: String
  $start_date: String
  $end_date: String
  $timezone: String
  $appt_type_id: String
  $appointment_to_reschedule_id: ID
) {
  availableSlotsForRange(
    provider_id: $provider_id
    start_date: $start_date
    end_date: $end_date
    timezone: $timezone
    appt_type_id: $appt_type_id
    appointment_to_reschedule_id: $appointment_to_reschedule_id
  ) {
    user_id
    date
  }
}
```

**3) Get Available Slots**

Now that we have the day, the next step is to get specific available time slots on that day. To do so, we use the `availableSlotsForRange` query. The arguments are very similar to the `daysAvailableForRange`. In all cases, those arguments do the same thing, so let’s focus on the one difference, `start_date` and `end_date`.

`start_date` and `end_date` are both required and are used to set up the range of time that we check availability for. For example, if I send in a `start_date` of “2021-10-10”, an `end_date` of “2021-10-12”, and a timezone of `America/New_York`, the query will check availability starting at “2021-10-10 00:00:00 EDT -04:00” to “2021-10-12 23:59:59 EDT -04:00”.

In our case, we are just checking availability on one day, so we would send in an identical `start_date` and `end_date`.

| Input                 | Info                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `provider_id`         | **Required**. The ID of the provider to search available slots for.                                                                                     |
| `start_date`          | **Required**. Date in the `YYYY-MM-DD` format indicating the lower date range boundary to return available slots for.                                   |
| `end_date`            | **Required**. Date in the `YYYY-MM-DD` format indicating the upper date range boundary to return available slots for.                                   |
| `timezone`            | Timezone used for the `start_date` and `end_date` arguments. Defaults to the patient’s timezone.                                                        |
| `start_date_boundary` | Date in the `YYYY-MM-DD` format indicating. If provided, the query will not return any slots before this date even if `start_date` is before this date. |
| `end_date_boundary`   | Date in the `YYYY-MM-DD` format. If provided, the query will not return any slots after this date even if `end_date` is after this date.                |

The query returns an array of [`PotentialAppointmentSlots`](/reference/2024-06-01/objects/potentialappointmentslot). We have the user select one of those slots, and use the `user_id` and `date` from the slot in the next (and final) step. Please note the `date` here is a full datetime string (e.g “2021-10-10 10:00:00 EDT -04:00”) and `user_id` is the ID of the available provider.

```
mutation updateAppointment(
    $client_updating: Boolean, # true
    $datetime: String,
    $id: ID,
  ) {
    updateAppointment(
      input: {
        $client_updating: Boolean,
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

**4) Update the Appointment**

Finally, we can use the `updateAppointment` mutation to move the appointment to the new available slot.

| Input             | Info                                                                                      |
| ----------------- | ----------------------------------------------------------------------------------------- |
| `id`              | Required. The ID of the appointment to update.                                            |
| `datetime`        | Required. This should be the `date` from the slot that was selected in the previous step. |
| `client_updating` | Required. Needs to be true.                                                               |

In the case that the slot is no longer available (e.g another patient simultaneously booked an appointment for the same slot), an error will be returned in the `messages` of the response.
