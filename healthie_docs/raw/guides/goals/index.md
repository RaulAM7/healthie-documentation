---
title: Goals | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/goals/index
  md: https://docs.gethealthie.com/guides/goals/index.md
---

# Goals

For more information on the Goals feature in general, view our [help articles here](https://help.gethealthie.com/article/98-healthie-overview-goals-platform).

## The Goal object

```
{
  "id": "1",
  "name": "Download e-book on mindful eating"
}
```

Goals are `Goal` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/goal).

## Listing Goals

```
query goals($user_id: ID, $sort_by: String, $keywords: String, $status_filter: String, $frequency_filter: String) {
  goals(
    user_id: $user_id
    sort_by: $sort_by
    keywords: $keywords
    status_filter: $status_filter
    frequency_filter: $frequency_filter
  ) {
    id
    name
  }
}
```

Listing Goals is done via the `goals` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/goals#arguments).

| Input              | Info                                                                                                                                                                                                             |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort_by`          | Optional. Valid options are:- `start_date_asc`
- `start_date_desc` (default)
- `frequency_asc`
- `frequency_desc`
- `title_asc`
- `title_desc`
- `status_asc`
- `status_desc`
- `end_date_asc`
- `end_date_desc` |
| `user_id`          | Optional. ID of the Patient that is associated with the Goal.                                                                                                                                                    |
| `keywords`         | Optional. Can be searched by name or description.                                                                                                                                                                |
| `status_filter`    | Optional. Filters Goals by the completeness. Can be `complete` or `not_complete`.                                                                                                                                |
| `frequency_filter` | Optional. Filters Goals by the frequency. Can be `daily`, `weekly`, or `one_time`.                                                                                                                               |

Returns a list of [Goal](/reference/2024-06-01/objects/goal) objects.

## Retrieving a Goal

```
query goal($id: ID, $program_goal: Boolean, $client_id: ID, $last_client_goal: Boolean) {
  goal(id: $id, program_goal: $program_goal, client_id: $client_id, last_client_goal: $last_client_goal) {
    id
    name
  }
}
```

Retrieving a specific Goal is done via the `goal` query.

| Input              | Info                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| `id`               | Optional when using `client_id` and `last_client_goal`. ID of the Goal to query.                  |
| `client_id`        | Optional. **Required when using `last_client_goal`**. ID of the Patient associated with the Goal. |
| `last_client_goal` | Optional. If set to `true`, will return the last Goal for the Patient specified in `client_goal`. |

Returns a [Goal](/reference/2024-06-01/objects/goal) object.

## Creating a Goal

```
mutation createGoal(
  $name: String
  $user_id: ID
  $program_goal: Boolean
  $repeat: String
  $due_date: String
  $start_on: String
  $reminder: ReminderInput
  $care_plan_id: ID
) {
  createGoal(
    input: {
      name: $name
      user_id: $user_id
      program_goal: $program_goal
      repeat: $repeat
      due_date: $due_date
      start_on: $start_on
      reminder: $reminder
      care_plan_id: $care_plan_id
    }
  ) {
    goal {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/creategoalinput).

| Input          | Info                                                                                                                             |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | **Required**. Name of the Goal.                                                                                                  |
| `user_id`      | Optional. ID of the Patient to create the Goal for.                                                                              |
| `program_goal` | Optional. Set to `true` to create the Goal for a Program.                                                                        |
| `repeat`       | **Required**. The frequency of this Goal. Possible values are:- `Daily`
- `Weekly`
- `Once`                                      |
| `due_date`     | Optional. The date the Goal should end. Format should be: `yyyy-mm-dd`.                                                          |
| `start_on`     | Optional. The date the Goal should start. Format should be: `yyyy-mm-dd`.                                                        |
| `reminder`     | Optional. An input of type [`ReminderInput`](/reference/2024-06-01/input-objects/reminderinput) to set a reminder for this Goal. |
| `care_plan_id` | Optional. If provided, the Goal will be associated with a [Care Plan](/guides/care-plans).                                       |

Returns a [`createGoalPayload`](/reference/2024-06-01/objects/creategoalpayload) object.

## Updating a Goal

```
mutation updateGoal(
  $id: ID
  $name: String
  $user_id: ID
  $program_goal: Boolean
  $repeat: String
  $due_date: String
  $start_on: String
  $reminder: ReminderInput
) {
  updateGoal(
    input: {
      id: $id
      name: $name
      user_id: $user_id
      program_goal: $program_goal
      repeat: $repeat
      due_date: $due_date
      start_on: $start_on
      reminder: $reminder
    }
  ) {
    goal {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateGoal` has a very similar behavior to [`createGoal`](#creating-a-goal) mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updategoalinput).

| Input | Info                                        |
| ----- | ------------------------------------------- |
| `id`  | **Required**. The ID of the Goal to update. |

Returns an [`updateGoalPayload`](/reference/2024-06-01/objects/updategoalpayload) object.

## Deleting a Goal

Goals can be deleted by authorized providers and staff members via the `deleteGoal` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletegoalinput).

```
mutation deleteGoal($id: ID) {
  deleteGoal(input: { id: $id }) {
    goal {
      id
    }


    messages {
      field
      message
    }
  }
}
```

| Input | Info                                    |
| ----- | --------------------------------------- |
| `id`  | **Required**. ID of the Goal to delete. |

Returns a [`deleteGoalPayload`](/reference/2024-06-01/objects/deletegoalpayload) object.

## The Goal History object

```
{
  "id": "12345",
  "goal": {
    "id": "112233",
    "name": "Drink more water",
    "repeat": "Daily"
  },
  "completed_on": "2023-01-01"
}
```

Goal Hitstories are `GoalHistory` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/goalhistory).

## Listing Goal Histories

```
query goalHistories(
  $category: String
  $include_subgoals: Boolean
  $offset: Int
  $should_paginate: Boolean
  $unique: Boolean
  $user_id: ID
) {
  goalHistories(
    category: $category
    include_subgoals: $include_subgoals
    offset: $offset
    should_paginate: $should_paginate
    unique: $unique
    user_id: $user_id
  ) {
    id
    name
    goal {
      id
      name
      repeat
    }
    completed_on
  }
}
```

Listing Goal Histories is done via the `goalHistories` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/goalhistories#arguments).

| Input              | Info                                                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| `category`         | Optional. The frequency of the Goal. Valid options are:- `Daily`
- `Weekly`
- `Once`                                       |
| `include_subgoals` | Optional. Whether to include subgoals.                                                                                     |
| `user_id`          | Optional. ID of the Patient that is associated with the Goal History.                                                      |
| `unique`           | Optional. If set to `true`, will only return a single Goal History per Goal, while `false` will return all Goal Histories. |

Returns a list of [GoalHistory](/reference/2024-06-01/objects/goalhistory) objects.
