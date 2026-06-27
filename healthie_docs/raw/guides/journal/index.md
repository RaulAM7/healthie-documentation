---
title: Journal Entries | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/journal/index
  md: https://docs.gethealthie.com/guides/journal/index.md
---

# Journal Entries

You can learn more about the Journal feature in general [on Healthie’s Help platform](https://help.gethealthie.com/article/100-tracking-clients-activity-on-website-and-mobile-apps).

## The Journal Entry Object

```
{
  "id": "15",
  "description": "Example entry",
  "created_at": "2022-08-03 09:55:55 -0400",
  "type": "FoodEntry",
  "name": "Food",
  "viewed": false,
  "healthiness_info_hex_value": "#35b032",
  "has_subentries": false,
  "previous_water_intake_stat": 0,
  "default_water_intake_for_entry_user": 0,
  "poster": {
    "id": "7"
  }
}
```

Journal Entries are `Entry` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/entry).

## Listing Entries

```
query entries(
  $offset: Int
  $type: String
  $keywords: String
  $entry_id: String
  $category: String
  $client_id: String
  $is_org: Boolean
  $end_range: String
  $start_range: String
  $group_id: String
  $sort_by: String
  $end_datetime_range: String
  $start_datetime_range: String
  $summary_view: Boolean
) {
  entries(
    offset: $offset
    type: $type
    keywords: $keywords
    entry_id: $entry_id
    category: $category
    client_id: $client_id
    is_org: $is_org
    end_range: $end_range
    start_range: $start_range
    group_id: $group_id
    sort_by: $sort_by
    end_datetime_range: $end_datetime_range
    start_datetime_range: $start_datetime_range
    summary_view: $summary_view
  ) {
    id
    type
    added_by_user {
      id
    }
    category
    emotions
    name
    description
  }
}
```

Listing Entries is done via the `entries` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/entries#arguments).

| Input       | Info                                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `type`      | Optional. Entry type, can be one of: `FoodEntry`, `MirrorEntry`, `MetricEntry`, `WorkoutEntry`, `SleepEntry`, or `NoteEntry`. |
| `keywords`  | Optional. Keywords to search by. Entries can be searched by description.                                                      |
| `entry_id`  | Optional. ID of a single Entry to search.                                                                                     |
| `client_id` | Optional. ID of the Patient associated with this Entry.                                                                       |

Returns a list of [`Entry`](/reference/2024-06-01/objects/entry) objects.

## Retrieving a Program

```
query entry($id: ID, $type: String, $client_id: ID) {
  entry(id: $id, type: $type, client_id: $client_id) {
    id
    type
    category
    emotions
    name
    description
  }
}
```

Retrieving a specific Entry is done via the `entry` query.

| Input       | Info                                                                               |
| ----------- | ---------------------------------------------------------------------------------- |
| `id`        | Optional. ID of the Entry to query.                                                |
| `client_id` | Optional. Used together with `type`. Returns the last Entry for a specific Client. |
| `type`      | Optional. **Required when using `client_id`.** Fetches an Entry of specific type.  |

Returns an [`Entry`](/reference/2024-06-01/objects/entry) object.

## Creating an Entry

```
mutation createEntry($type: String, $description: String, $user_id: String, $percieved_hungriness: String) {
  createEntry(
    input: { type: $type, description: $description, user_id: $user_id, percieved_hungriness: $percieved_hungriness }
  ) {
    entry {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Entries are created via the `createEntry` mutation. Let’s break down the inputs that mutation accepts.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createentryinput).

| Input                  | Info                                                                                                                                                                       |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                 | Optional. Valid options are- `MetricEntry`
- `FoodEntry`
- `WorkoutEntry`
- `MirrorEntry`
- `SleepEntry`
- `NoteEntry`
- `WaterIntakeEntry`
- `PoopEntry`
- `SymptomEntry` |
| `created_at`           | Optional. Date for the new Entry.                                                                                                                                          |
| `user_id`              | Optional. ID of the Patient, otherwise the currently authenticated User will be associated.                                                                                |
| `percieved_hungriness` | Optional. A string index of hungriness.- `"1"` - not hungry
- `"2"` - somewhat hungry
- `"3"` - very hungry                                                                |

Returns a [`createEntryPayload`](/reference/2024-06-01/objects/createentrypayload) object.

## Updating an Entry

```
mutation updateEntry($id: ID, $type: String, $description: String, $user_id: String, $percieved_hungriness: String) {
  updateEntry(
    input: {
      id: $id
      type: $type
      description: $description
      user_id: $user_id
      percieved_hungriness: $percieved_hungriness
    }
  ) {
    entry {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateEntry` mutation shares many common inputs with [`createEntry`](#creating-an-entry) and those inputs (e.g `type` or `user_id` work the same in both places).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateentryinput).

| Input | Info                                         |
| ----- | -------------------------------------------- |
| `id`  | **Required**. The ID of the Entry to update. |

Returns an [`updateEntryPayload`](/reference/2024-06-01/objects/updateentrypayload) object.

## Deleting an Entry

Journal Entries can be (soft) deleted by authorized providers and staff members via the `deleteEntry` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleteentryinput).

```
mutation deleteEntry($id: ID) {
  deleteEntry(input: { id: $id }) {
    entry {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteEntry` mutation is called from an authenticated provider/staff account.

| Input | Info                                     |
| ----- | ---------------------------------------- |
| `id`  | **Required**. ID of the Entry to delete. |

Returns a [`deleteEntryPayload`](/reference/2024-06-01/objects/deleteentrypayload) object.
