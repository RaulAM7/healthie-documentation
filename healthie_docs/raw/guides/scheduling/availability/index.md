---
title: Availability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/scheduling/availability/index
  md: https://docs.gethealthie.com/guides/scheduling/availability/index.md
---

## The Availability Object

```
{
  "id": "1",
  "day_of_week": 1,
  "duration_string": "5h",
  "is_repeating": false,
  "range_start": "2022-08-15 07:30:00 +0200",
  "range_end": "2022-08-15 12:30:00 +0200",
  "resourceId": "1",
  "timezone_abbr": "CEST",
  "user": {
    "email": "superadmin@example.com"
  }
}
```

Calendar Availability is represented using `Availability` objects.

`Availability` objects are used to allow booking [Appointments](/guides/scheduling/appointments).

You can view the full list of available fields [here](/reference/2024-06-01/objects/availability).

If you have questions about the overall functionality of the calendar availability feature, you can find information [here](https://help.gethealthie.com/article/341-setting-weekly-availability).

## Listing all Availabilities

```
query ($show_availability: Boolean, $one_time: Boolean, $is_repeating: Boolean, $startDate: String, $endDate: String) {
  availabilities(
    show_availability: $show_availability
    one_time: $one_time
    is_repeating: $is_repeating
    startDate: $startDate
    endDate: $endDate
  ) {
    id
    day_of_week
    duration_string
    is_repeating
    range_start
    range_end
    resourceId
    timezone_abbr
    user {
      email
    }
  }
}
```

A list of availabilities can be retrieved via the `availabilities` query. This query is called from an authenticated provider/staff account.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/availabilities#arguments).

Note

**Important**: one of `one_time` or `is_repeating` must be provided. Otherwise no results will be returned.

**Important**: if `is_repeating`, the `id` of the repeating availabilities will be returned as a unique identifier based on date and id of the availability . The ID of the repeating availability is the `repeating_availability_id`.

We will go over some of them below.

| Input               | Info                                                                                                                    |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `show_availability` | Optional. If set to `false`, no results will be returned.                                                               |
| `day_of_week`       | Optional. A 0-indexed day of the week the availability is on.                                                           |
| `one_time`          | Optional. Query only one-time availabilities. Either this or `is_repeating` must be provided.                           |
| `is_repeating`      | Optional. Query only repeating availabilities. Either this or `one_time` must be provided.                              |
| `includeRepeating`  | Optional. Include repeating availabilities in the query.                                                                |
| `startDate`         | Optional. Find only availabilities from a specific date (inclusive).                                                    |
| `endDate`           | Optional. Find only availabilities until a specific date (exclusive).                                                   |
| `is_org`            | Optional. If true, retrieves availabilities for providers in an organization. Must be `true` if passing `provider_ids`. |

Returns an array of [`Availability`](/reference/2024-06-01/objects/availability) objects.

## Retrieving an Availability

```
query availability($id: ID) {
  availability(id: $id) {
    id
    custom_modules {
      id
      day_of_week
      duration_string
      is_repeating
      range_start
      range_end
      resourceId
      timezone_abbr
      user {
        email
      }
    }
  }
}
```

Retrieving a specific availability information is done via the `availability` query.

| Input | Info                                  |
| ----- | ------------------------------------- |
| `id`  | Required. The ID of the availability. |

Returns an [`Availability`](/reference/2024-06-01/objects/availability) object.

## Creating an Availability

```
mutation createAvailability(
  $day_of_week: Int
  $is_repeating: Boolean
  $range_start: String
  $time: String
  $end_time: String
  $user_id: String
) {
  createAvailability(
    input: {
      day_of_week: $day_of_week
      is_repeating: $is_repeating
      range_start: $range_start
      time: $time
      end_time: $end_time
      user_id: $user_id
    }
  ) {
    availability {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Availabilities are created using the `createAvailability` mutation.

To create a recurring (weekly) availability, make sure to set `is_repeating` to `true` and specify the `day_of_week`. One availability is repeating once a week. You need to create five separate availabilities to define a Monday-Friday availability. Check out how to [create Availabilities in bulk](#creating-availabilities-in-bulk).

The `createAvailability` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createavailabilityinput).

| Input          | Info                                                                                                                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `range_start`  | **Required**. Date when the availability starts. For one-time availability, it’s the date of the availability. **Required date format**: `month_name DD, YYYY`, e.g., `August 16, 2022`. |
| `time`         | **Required**. Time when the availability starts. **Required time format**: `HH MM`, e.g., `07 30` or `19 00`.                                                                            |
| `end_time`     | **Required**. Time when the availability ends. **Required time format**: `HH MM`, e.g., `07 30` or `19 00`.                                                                              |
| `day_of_week`  | Optional. A 0-indexed day of the week the availability is on (`0` for Sunday, `1` for Monday, etc.). For repeating availabilities, it’s the day of the availability every week.          |
| `is_repeating` | Optional. If set to `true`, the availability will be repeating on the day specified in `day_of_week`.                                                                                    |
| `user_id`      | Optional. ID of the user to create the availability for.                                                                                                                                 |

Returns [`createAvailabilityPayload`](/reference/2024-06-01/objects/createavailabilitypayload).

## Updating an Availability

```
mutation editAvailability(
  $id: String
  $day_of_week: Int
  $is_repeating: Boolean
  $range_start: String
  $time: String
  $end_time: String
  $user_id: String
) {
  editAvailability(
    input: {
      id: $id
      day_of_week: $day_of_week
      is_repeating: $is_repeating
      range_start: $range_start
      time: $time
      end_time: $end_time
      user_id: $user_id
    }
  ) {
    availability {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Updating Availabilities is done using the `editAvailability` mutation.

The `editAvailability` mutation shares many common inputs with `createAvailability` and those inputs (e.g `range_start` or \`time“ work the same in both places).

The `editAvailability` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/editavailabilityinput).

| Input          | Info                                                                                                                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`           | **Required**. ID of the Availability to edit.                                                                                                                                            |
| `range_start`  | **Required**. Date when the availability starts. For one-time availability, it’s the date of the availability. **Required date format**: `month_name DD, YYYY`, e.g., `August 16, 2022`. |
| `time`         | **Required**. Time when the availability starts. **Required time format**: `HH MM`, e.g., `07 30` or `19 00`.                                                                            |
| `end_time`     | **Required**. Time when the availability ends. **Required time format**: `HH MM`, e.g., `07 30` or `19 00`.                                                                              |
| `day_of_week`  | Optional. A 0-indexed day of the week the availability is on (`0` for Sunday, `1` for Monday, etc.). For repeating availabilities, it’s the day of the availability every week.          |
| `is_repeating` | Optional. If set to `true`, the availability will be repeating on the day specified in `day_of_week`.                                                                                    |
| `user_id`      | Optional. ID of the user to create the availability for.                                                                                                                                 |

Returns [`editAvailabilityPayload`](/reference/2024-06-01/objects/editavailabilitypayload).

## Deleting an Availability

```
mutation deleteAvailability($id: ID) {
  deleteAvailability(input: { id: $id }) {
    availability {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `deleteAvailability` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleteavailabilityinput).

| Input | Info                                                |
| ----- | --------------------------------------------------- |
| `id`  | **Required**. The ID of the Availability to delete. |

Returns [`deleteAvailabilityPayload`](/reference/2024-06-01/objects/deleteavailabilitypayload).
