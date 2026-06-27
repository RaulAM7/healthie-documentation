---
title: Tasks | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/tasks/index
  md: https://docs.gethealthie.com/guides/tasks/index.md
---

# Tasks

You can learn more about the Tasks feature in general [on Healthie’s Help platform](https://help.gethealthie.com/article/439-overview-tasks).

## The Task Object

```
{
  "id": "1800",
  "client": {
    "id": 300
  },
  "user": {
    "id": "200"
  },
  "creator": {
    "id": "100"
  },
  "complete": false,
  "completed_at": null,
  "content": "Example task content",
  "created_at": "2022-01-01 09:45:20 -0400",
  "priority": 1,
  "position": 0,
  "seen": true,
  "reminder": {
    "id": "1190",
    "interval_type": "once",
    "interval_value": "2022-01-08",
    "is_enabled": true
  },
  "hidden": false,
  "due_date": "2022-01-10 00:00:00 -0400"
}
```

Tasks are `Task` objects.

Some of the Task properties are described below:

| Field      | Description                                                                    |
| ---------- | ------------------------------------------------------------------------------ |
| `priority` | `0` when standard priority, `1` if high priority                               |
| `client`   | A Patient object related to this Task. Null if the Task is not Patient-related |
| `creator`  | User who crated the Task. It’s not always the assignee (`user`)                |
| `position` | Position of the Task on the List                                               |
| `seen`     | Whether the Task has been seen by the owner (`user`)                           |
| `complete` | Whether the Task is complete                                                   |

You can view the full list of available fields [here](/reference/2024-06-01/objects/task).

## Retrieving a Task

```
query getTask($id: ID) {
  task(id: $id) {
    id
    client {
      id
    }
    user {
      id
    }
    creator {
      id
      email
    }
    complete
    completed_at
    content
    created_at
    priority
    position
    seen
    reminder {
      id
      interval_type
      interval_value
      is_enabled
    }
    hidden
    due_date
  }
}
```

Retrieving a Task is done via the `task` query.

| Input | Info                      |
| ----- | ------------------------- |
| `id`  | Required. ID of the Task. |

Returns a [`Task`](/reference/2024-06-01/objects/task) object.

## Listing Tasks

```
query tasks(
  $client_id: String
  $withoutPagination: Boolean
  $type: String
  $completed_status: String
  $sort_by: String
  $keywords: String
  $show_hidden: Boolean
  $created_by_self: Boolean
) {
  tasks(
    client_id: $client_id
    withoutPagination: $withoutPagination
    type: $type
    completed_status: $completed_status
    sort_by: $sort_by
    keywords: $keywords
    show_hidden: $show_hidden
    created_by_self: $created_by_self
  ) {
    id
    client {
      id
    }
    user {
      id
    }
    creator {
      id
      email
    }
    complete
    completed_at
    content
    created_at
    priority
    position
    seen
    reminder {
      id
      interval_type
      interval_value
      is_enabled
    }
    hidden
    due_date
  }
}
```

Listing Entries is done via the `tasks` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/tasks#arguments).

| Input               | Info                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`         | Optional. ID of the Patient associated with the Task.                                                                                                                                                                                                                                                                                                                                  |
| `withoutPagination` | Optional. Keywords to search by. Entries can be searched by description.                                                                                                                                                                                                                                                                                                               |
| `type`              | Optional. Possible values are:- `all` - returns all Tasks that are either assigned or created by the current User
- `assigned` - Tasks created by other Users and assigned to the current User                                                                                                                                                                                         |
| `completed_status`  | Optional.- `complete` - return only complete Tasks
- `incomplete` - return only incomplete Tasks                                                                                                                                                                                                                                                                                       |
| `created_by_self`   | Optional. If set to `true`, will return only Tasks created by the current User.                                                                                                                                                                                                                                                                                                        |
| `show_hidden`       | Optional. If set to `true`, will query hidden tasks.                                                                                                                                                                                                                                                                                                                                   |
| `keywords`          | Optional. Keywords to search Tasks by. Tasks can be searcheds by the content field.                                                                                                                                                                                                                                                                                                    |
| `sort_by`           | Optional. Possible values are:- `task_asc`
- `task_desc`
- `creator_asc`
- `creator_desc`
- `assignee_asc`
- `assignee_desc`
- `created_asc`
- `created_desc`
- `priority_asc`
- `priority_desc`
- `due_date_asc`
- `due_date_desc`
- `completed_asc`
- `completed_desc`By default, Healthie API returns Tasks ordered by position, creation date (newest first) and incomplete first. |

Returns a list of [`Task`](/reference/2024-06-01/objects/task) objects.

## Creating a Task

```
mutation createTask(
  $content: String
  $user_id: String
  $priority: Int
  $client_id: String
  $due_date: String
  $reminder: TaskReminderInput
) {
  createTask(
    input: {
      content: $content
      user_id: $user_id
      priority: $priority
      client_id: $client_id
      due_date: $due_date
      reminder: $reminder
    }
  ) {
    task {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Tasks are created via the `createTask` mutation. Let’s break down the inputs that this mutation accepts.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createtaskinput).

| Input                     | Info                                                                                                       |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `content`                 | Content of the Task                                                                                        |
| `user_id`                 | Optional. ID of the User to assign the Task to. If none provided, will assign the task to the current User |
| `priority`                | Optional. Possible values are:- `0` - normal priority
- `1` - high priority                                |
| `client_id`               | Optional. ID of the Patient related to this Task                                                           |
| `complete`                | Optional. Set to `true` if the Task is already complete                                                    |
| `due_date`                | Optional. A due date of the Task                                                                           |
| `reminder`                | Optional. A configuration object for the reminder. See descriptions below                                  |
| `reminder.is_enabled`     | Set to `true` to enable the reminder, `false` otherwise                                                    |
| `reminder.reminder_time`  | Time, expressed in number of minutes from midnight, to trigger the reminder at                             |
| `reminder.interval_type`  | Frequency of the reminder. Possible options are:- `daily`
- `weekly`
- `once` - default                    |
| `reminder.interval_value` | Date when to trigger the reminder                                                                          |

Returns a [`createTaskPayload`](/reference/2024-06-01/objects/createtaskpayload) object.

## Updating a Task

```
mutation updateTask(
  $id: String
  $position: Int
  $content: String
  $user_id: String
  $priority: Int
  $client_id: String
  $due_date: String
  $reminder: TaskReminderInput
) {
  updateTask(
    input: {
      id: $id
      position: $position
      content: $content
      user_id: $user_id
      priority: $priority
      client_id: $client_id
      due_date: $due_date
      reminder: $reminder
    }
  ) {
    task {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateTask` mutation shares many common inputs with [`createTask`](#creating-a-task) and those inputs (e.g `due_date` or `priority` work the same in both places).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatetaskinput).

| Input      | Info                                                |
| ---------- | --------------------------------------------------- |
| `id`       | **Required**. The ID of the Task to update.         |
| `position` | Optional. Set the position of the Task on the list. |

Returns an [`updateTaskPayload`](/reference/2024-06-01/objects/updatetaskpayload) object.

## Marking all Tasks as seen

```
mutation markTasksAsSeen($seen: Boolean, $update_all_tasks: Boolean) {
  updateTasksBulk(input: { seen: $seen, update_all_tasks: $update_all_tasks }) {
    messages {
      message
    }
  }
}
```

You can programmatically mark all Tasks of the current User as seen by using the `updateTasksBulk` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/bulkupdatetasksinput).

| Input              | Info                                                                                |
| ------------------ | ----------------------------------------------------------------------------------- |
| `seen`             | Set to `true` to mark Tasks as seen by the current User, `false` to mark as unseen. |
| `update_all_tasks` | Boolean indicating whether all User Tasks should be updated. Set to `true`.         |

Returns an [`bulkUpdateTasksPayload`](/reference/2024-06-01/objects/bulkupdatetaskspayload) object.

## Deleting a Task

Tasks can be deleted via the `deleteTask` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletetaskinput).

```
mutation deleteTask($id: ID) {
  deleteTask(input: { id: $id }) {
    task {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteTask` mutation is called from an authenticated provider/staff account.

| Input | Info                                    |
| ----- | --------------------------------------- |
| `id`  | **Required**. ID of the Task to delete. |

Returns a [`deleteTaskPayload`](/reference/2024-06-01/objects/deletetaskpayload) object.
