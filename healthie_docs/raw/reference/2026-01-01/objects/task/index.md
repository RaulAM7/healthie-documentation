---
title: Task | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/task/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/task/index.md
---

Tasks for providers to create, complete, and optionally assign to client profiles

## Fields

[`assignees` ](#field-assignees)· [`UserConnection` ](/reference/2026-01-01/objects/userconnection)· The providers and staff who are assigned to this task

[`client` ](#field-client)· [`User` ](/reference/2026-01-01/objects/user)· The client (patient) associated with this task

[`client_id` ](#field-client-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The identifier of the client (patient) associated with this task

[`comments` ](#field-comments)· [`InternalCommentPaginationConnection!` ](/reference/2026-01-01/objects/internalcommentpaginationconnection)· required · Fetch paginated comments collection

[`complete` ](#field-complete)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, user has marked task complete

[`completed_at` ](#field-completed-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date and time this task was completed

[`completed_by` ](#field-completed-by)· [`User` ](/reference/2026-01-01/objects/user)· User (provider or staff member) who completed this task

[`completed_by_id` ](#field-completed-by-id)· [`ID` ](/reference/2026-01-01/scalars/id)· User ID of the user (provider or staff member) who completed this task

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· Details describing this task

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date and time this task was created

[`created_by_generator_id` ](#field-created-by-generator-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of an auto generator

[`created_by_id` ](#field-created-by-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The identifier of the user (provider or staff member) who created this task

[`creator` ](#field-creator)· [`User` ](/reference/2026-01-01/objects/user)· The user (provider or staff member) who created this task

[`due_date` ](#field-due-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date and time this task was is due to be complete

[`hidden` ](#field-hidden)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, hide completed task from top nav bar

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the task

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`note` ](#field-note)· [`Note` ](/reference/2026-01-01/objects/note)· Get associated chat message with a task

[`note_path` ](#field-note-path)· [`String` ](/reference/2026-01-01/scalars/string)· Get relative path to view the note (chat message) associated with the task.

[`position` ](#field-position)· [`Int` ](/reference/2026-01-01/scalars/int)· Order in which tasks are displayed (ascending)

[`priority` ](#field-priority)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Level of urgency for this task(0 = standard priority, 1 = high priority)

[`ref_source` ](#field-ref-source)· [`String` ](/reference/2026-01-01/scalars/string)· ID of additional relation

[`reminder` ](#field-reminder)· [`Reminder` ](/reference/2026-01-01/objects/reminder)· Reminder object for a given goal

[`seen` ](#field-seen)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the assigned user (provider or staff member) has viewed this task in top navbar

[`smart` ](#field-smart)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Indicates this was automatically created via smart task

[`smart_category` ](#field-smart-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of smart task

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last date and time that the task was updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The first user (provider or staff member) assigned to complete the task

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the first user (provider or staff member) assigned to this task

## Used By

[`ConversationMembership.last_task`](/reference/2026-01-01/objects/conversationmembership)

[`Note.task`](/reference/2026-01-01/objects/note)

[`NoteScheduler.last_task`](/reference/2026-01-01/objects/notescheduler)

[`TaskEdge.node`](/reference/2026-01-01/objects/taskedge)

[`TaskPaginationConnection.nodes`](/reference/2026-01-01/objects/taskpaginationconnection)

[`User.assigned_tasks`](/reference/2026-01-01/objects/user)

[`User.completed_tasks`](/reference/2026-01-01/objects/user)

[`User.incomplete_tasks`](/reference/2026-01-01/objects/user)

[`User.my_tasks`](/reference/2026-01-01/objects/user)

[`bulkDeleteTasksPayload.tasks`](/reference/2026-01-01/objects/bulkdeletetaskspayload)

[`bulkUpdateTasksPayload.tasks`](/reference/2026-01-01/objects/bulkupdatetaskspayload)

[`createTaskPayload.task`](/reference/2026-01-01/objects/createtaskpayload)

[`deleteTaskPayload.task`](/reference/2026-01-01/objects/deletetaskpayload)

[`updateTaskPayload.task`](/reference/2026-01-01/objects/updatetaskpayload)

[`Query.task`](/reference/2026-01-01/queries/task)

## Definition

```
"""
Tasks for providers to create, complete, and optionally assign to client profiles
"""
type Task {
  """
  The providers and staff who are assigned to this task
  """
  assignees(
    order_by: UserOrderKeys = LAST_NAME_ASC


    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): UserConnection


  """
  The client (patient) associated with this task
  """
  client: User


  """
  The identifier of the client (patient) associated with this task
  """
  client_id: ID


  """
  Fetch paginated comments collection
  """
  comments(
    order_by: InternalCommentsOrderKeys = CREATED_AT_ASC


    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): InternalCommentPaginationConnection!


  """
  If true, user has marked task complete
  """
  complete: Boolean


  """
  Date and time this task was completed
  """
  completed_at: ISO8601DateTime


  """
  User (provider or staff member) who completed this task
  """
  completed_by: User


  """
  User ID of the user (provider or staff member) who completed this task
  """
  completed_by_id: ID


  """
  Details describing this task
  """
  content: String


  """
  Date and time this task was created
  """
  created_at: ISO8601DateTime!


  """
  ID of an auto generator
  """
  created_by_generator_id: String


  """
  The identifier of the user (provider or staff member) who created this task
  """
  created_by_id: ID


  """
  The user (provider or staff member) who created this task
  """
  creator: User


  """
  Date and time this task was is due to be complete
  """
  due_date: ISO8601DateTime


  """
  If true, hide completed task from top nav bar
  """
  hidden: Boolean!


  """
  The unique identifier of the task
  """
  id: ID!


  """
  A serialized JSON string of metadata. Maximum character limit of 2,000.
  """
  metadata: JSON


  """
  Get associated chat message with a task
  """
  note: Note


  """
  Get relative path to view the note (chat message) associated with the task.
  """
  note_path: String


  """
  Order in which tasks are displayed (ascending)
  """
  position: Int


  """
  Level of urgency for this task(0 = standard priority, 1 = high priority)
  """
  priority: Int!


  """
  ID of additional relation
  """
  ref_source: String


  """
  Reminder object for a given goal
  """
  reminder: Reminder


  """
  If true, the assigned user (provider or staff member) has viewed this task in top navbar
  """
  seen: Boolean!


  """
  Indicates this was automatically created via smart task
  """
  smart: Boolean!


  """
  The category of smart task
  """
  smart_category: String


  """
  The last date and time that the task was updated
  """
  updated_at: ISO8601DateTime


  """
  The first user (provider or staff member) assigned to complete the task
  """
  user: User


  """
  The ID of the first user (provider or staff member) assigned to this task
  """
  user_id: ID
}
```
