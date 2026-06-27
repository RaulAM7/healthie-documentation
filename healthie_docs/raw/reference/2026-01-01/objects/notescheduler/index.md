---
title: NoteScheduler | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/notescheduler/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/notescheduler/index.md
---

Scheduled chat notes

## Fields

[`first_four_invitees` ](#field-first-four-invitees)· [`[User!]!` ](/reference/2026-01-01/objects/user)· required · Scheduled messsage blast: get first four users

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the scheduler

[`invitees` ](#field-invitees)· [`[User!]!` ](/reference/2026-01-01/objects/user)· required · Scheduled messsage blast: get all invitees

[`invitees_count` ](#field-invitees-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of invitees

[`last_task` ](#field-last-task)· [`Task` ](/reference/2026-01-01/objects/task)· Get last conversation task

[`note` ](#field-note)· [`Note` ](/reference/2026-01-01/objects/note)· The note

[`note_content` ](#field-note-content)· [`String` ](/reference/2026-01-01/scalars/string)· The content of the note

[`participant_ids` ](#field-participant-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Get all directly selected user ids

[`selected_user_groups` ](#field-selected-user-groups)· [`[UserGroup!]` ](/reference/2026-01-01/objects/usergroup)· Get all directly selected user groups

[`selected_users` ](#field-selected-users)· [`[User!]` ](/reference/2026-01-01/objects/user)· Get all directly selected users

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time when the scheduler was last updated.

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner user of a note scheduler

## Used By

[`NoteSchedulerEdge.node`](/reference/2026-01-01/objects/notescheduleredge)

[`NoteSchedulerPaginationConnection.nodes`](/reference/2026-01-01/objects/noteschedulerpaginationconnection)

[`updateNoteSchedulerPayload.noteScheduler`](/reference/2026-01-01/objects/updatenoteschedulerpayload)

[`Query.note_scheduler`](/reference/2026-01-01/queries/note-scheduler)

## Definition

```
"""
Scheduled chat notes
"""
type NoteScheduler {
  """
  Scheduled messsage blast: get first four users
  """
  first_four_invitees: [User!]!


  """
  The unique identifier of the scheduler
  """
  id: ID!


  """
  Scheduled messsage blast: get all invitees
  """
  invitees: [User!]!


  """
  The number of invitees
  """
  invitees_count: Int


  """
  Get last conversation task
  """
  last_task: Task


  """
  The note
  """
  note: Note


  """
  The content of the note
  """
  note_content: String


  """
  Get all directly selected user ids
  """
  participant_ids: [ID]


  """
  Get all directly selected user groups
  """
  selected_user_groups: [UserGroup!]


  """
  Get all directly selected users
  """
  selected_users: [User!]


  """
  The date and time when the scheduler was last updated.
  """
  updated_at: ISO8601DateTime!


  """
  Owner user of a note scheduler
  """
  user: User
}
```
