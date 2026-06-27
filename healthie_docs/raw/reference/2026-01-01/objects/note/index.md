---
title: Note | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/note/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/note/index.md
---

Chat message object

## Fields

[`attached_audio_url` ](#field-attached-audio-url)· [`String` ](/reference/2026-01-01/scalars/string)· url for note audio

[`attached_image_url` ](#field-attached-image-url)· [`String` ](/reference/2026-01-01/scalars/string)· url for note image

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· note content

[`conversation_id` ](#field-conversation-id)· [`ID` ](/reference/2026-01-01/scalars/id)· conversation id

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time at which this note was created

[`creator` ](#field-creator)· [`User` ](/reference/2026-01-01/objects/user)· User who created note

[`creator_display_name` ](#field-creator-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· Display name of the creator based on conversation type and user permissions

[`deleted_by_user` ](#field-deleted-by-user)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if this note deleted by a user

[`document_id` ](#field-document-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id for note document

[`document_name` ](#field-document-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of attached document

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the note

[`image_name` ](#field-image-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of attached image

[`is_autoresponse` ](#field-is-autoresponse)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if this note is using as auto response message

[`on_behalf_user` ](#field-on-behalf-user)· [`User` ](/reference/2026-01-01/objects/user)· A User which created a Note on behalf of a Conversation Owner

[`recipient_id` ](#field-recipient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· receiver of note

deprecated

Use conversation\_memberships of conversation instead

[`scheduled_at` ](#field-scheduled-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Scheduled sent at

[`scheduled_conversation_id` ](#field-scheduled-conversation-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The conversation id associated with the note scheduler of a note, if any

[`task` ](#field-task)· [`Task` ](/reference/2026-01-01/objects/task)· Get associated task with a chat message

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time at which this note was updated or marked as deleted by a user

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· creator of note

[`viewed` ](#field-viewed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· conditional to see if user recipient viewed note. In community chats, you need to pass in a viewer\_id

## Used By

[`Conversation.notes`](/reference/2026-01-01/objects/conversation)

[`NoteEdge.node`](/reference/2026-01-01/objects/noteedge)

[`NotePaginationConnection.nodes`](/reference/2026-01-01/objects/notepaginationconnection)

[`NoteScheduler.note`](/reference/2026-01-01/objects/notescheduler)

[`Subscription.noteAddedSubscription`](/reference/2026-01-01/objects/subscription)

[`Task.note`](/reference/2026-01-01/objects/task)

[`createNotePayload.note`](/reference/2026-01-01/objects/createnotepayload)

[`deleteNotePayload.note`](/reference/2026-01-01/objects/deletenotepayload)

[`updateNotePayload.note`](/reference/2026-01-01/objects/updatenotepayload)

[`Query.note`](/reference/2026-01-01/queries/note)

## Definition

```
"""
Chat message object
"""
type Note {
  """
  url for note audio
  """
  attached_audio_url: String


  """
  url for note image
  """
  attached_image_url: String


  """
  note content
  """
  content: String


  """
  conversation id
  """
  conversation_id: ID


  """
  The time at which this note was created
  """
  created_at: ISO8601DateTime!


  """
  User who created note
  """
  creator: User


  """
  Display name of the creator based on conversation type and user permissions
  """
  creator_display_name: String


  """
  True if this note deleted by a user
  """
  deleted_by_user: Boolean!


  """
  id for note document
  """
  document_id: ID


  """
  Name of attached document
  """
  document_name: String


  """
  The unique identifier of the note
  """
  id: ID!


  """
  Name of attached image
  """
  image_name: String


  """
  True if this note is using as auto response message
  """
  is_autoresponse: Boolean!


  """
  A User which created a Note on behalf of a Conversation Owner
  """
  on_behalf_user: User


  """
  receiver of note
  """
  recipient_id: ID
    @deprecated(reason: "Use conversation_memberships of conversation instead")


  """
  Scheduled sent at
  """
  scheduled_at: ISO8601DateTime


  """
  The conversation id associated with the note scheduler of a note, if any
  """
  scheduled_conversation_id: ID


  """
  Get associated task with a chat message
  """
  task: Task


  """
  The time at which this note was updated or marked as deleted by a user
  """
  updated_at: ISO8601DateTime!


  """
  creator of note
  """
  user_id: ID


  """
  conditional to see if user recipient viewed note. In community chats, you need to pass in a viewer_id
  """
  viewed(
    """
    ID of the user that you want to check has viewed the note
    """
    viewer_id: ID
  ): Boolean
}
```
