---
title: Conversation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/conversation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/conversation/index.md
---

An association between conversation holders

## Fields

[`closed_by` ](#field-closed-by)· [`User` ](/reference/2026-01-01/objects/user)· The user who closed the conversation

[`closed_date` ](#field-closed-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date the conversation was closed

[`community_chat` ](#field-community-chat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicates whether the conversation is a community chat.

[`community_chat_prefix` ](#field-community-chat-prefix)· [`String` ](/reference/2026-01-01/scalars/string)· Display default name for community chat

[`conversation_memberships` ](#field-conversation-memberships)· [`[ConversationMembership!]!` ](/reference/2026-01-01/objects/conversationmembership)· required · All ConversationMemberships associated with this conversation.

[`conversation_memberships_count` ](#field-conversation-memberships-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of users in the conversation

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the Conversation was created

[`current_user_conversation_membership` ](#field-current-user-conversation-membership)· [`ConversationMembership` ](/reference/2026-01-01/objects/conversationmembership)· The conversation membership for the current user

[`dietitian_id` ](#field-dietitian-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of dietitian

[`first_four_invitees` ](#field-first-four-invitees)· [`[User!]` ](/reference/2026-01-01/objects/user)· first four invitees to the conversation

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the conversation

[`includes_multiple_clients` ](#field-includes-multiple-clients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the conversation includes multiple clients

[`invitees` ](#field-invitees)· [`[User!]` ](/reference/2026-01-01/objects/user)· The invitees to the conversation

[`is_hidden_for_client` ](#field-is-hidden-for-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the conversation is hidden for the client

[`last_message_content` ](#field-last-message-content)· [`String` ](/reference/2026-01-01/scalars/string)· The content of the last note, with HTML stripped

[`last_note_viewed_id` ](#field-last-note-viewed-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the most recent note authored by the current viewer that has been read by the patient. Returns null when no message of the viewer's has been read yet, or when the concept doesn't apply (no current user, or the conversation has 0 or more than 1 patient).

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The subject of conversation

[`notes` ](#field-notes)· [`[Note!]!` ](/reference/2026-01-01/objects/note)· required · All notes associated with this conversation.

[`owner` ](#field-owner)· [`User` ](/reference/2026-01-01/objects/user)· owner of conversation

[`patient_id` ](#field-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of patient (only set when conversation was automatically created due to provider assignment; Please use invitees instead to access patient(s) in a conversation)

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The last time the conversation was updated

[`user_groups` ](#field-user-groups)· [`[UserGroup!]` ](/reference/2026-01-01/objects/usergroup)· invitees to the conversation

## Used By

[`ConversationEdge.node`](/reference/2026-01-01/objects/conversationedge)

[`ConversationMembership.convo`](/reference/2026-01-01/objects/conversationmembership)

[`ConversationPaginationConnection.nodes`](/reference/2026-01-01/objects/conversationpaginationconnection)

[`Subscription.conversationChangedSubscription`](/reference/2026-01-01/objects/subscription)

[`createConversationPayload.conversation`](/reference/2026-01-01/objects/createconversationpayload)

[`updateConversationPayload.conversation`](/reference/2026-01-01/objects/updateconversationpayload)

[`Query.conversation`](/reference/2026-01-01/queries/conversation)

## Definition

```
"""
An association between conversation holders
"""
type Conversation {
  """
  The user who closed the conversation
  """
  closed_by: User


  """
  The date the conversation was closed
  """
  closed_date: ISO8601DateTime


  """
  Indicates whether the conversation is a community chat.
  """
  community_chat: Boolean


  """
  Display default name for community chat
  """
  community_chat_prefix: String


  """
  All ConversationMemberships associated with this conversation.
  """
  conversation_memberships: [ConversationMembership!]!


  """
  The number of users in the conversation
  """
  conversation_memberships_count: Int


  """
  The time the Conversation was created
  """
  created_at: ISO8601DateTime!


  """
  The conversation membership for the current user
  """
  current_user_conversation_membership: ConversationMembership


  """
  ID of dietitian
  """
  dietitian_id: ID


  """
  first four invitees to the conversation
  """
  first_four_invitees: [User!]


  """
  The unique identifier of the conversation
  """
  id: ID!


  """
  Whether the conversation includes multiple clients
  """
  includes_multiple_clients: Boolean


  """
  The invitees to the conversation
  """
  invitees: [User!]


  """
  Whether the conversation is hidden for the client
  """
  is_hidden_for_client: Boolean


  """
  The content of the last note, with HTML stripped
  """
  last_message_content: String


  """
  ID of the most recent note authored by the current viewer that has been read by the patient. Returns null when no message of the viewer's has been read yet, or when the concept doesn't apply (no current user, or the conversation has 0 or more than 1 patient).
  """
  last_note_viewed_id: String


  """
  A serialized JSON string of metadata. Maximum character limit of 2,000.
  """
  metadata: JSON


  """
  The subject of conversation
  """
  name: String


  """
  All notes associated with this conversation.
  """
  notes: [Note!]!


  """
  owner of conversation
  """
  owner: User


  """
  ID of patient (only set when conversation was automatically created due to provider assignment; Please use invitees instead to access patient(s) in a conversation)
  """
  patient_id: ID


  """
  The last time the conversation was updated
  """
  updated_at: ISO8601DateTime!


  """
  invitees to the conversation
  """
  user_groups: [UserGroup!]
}
```
