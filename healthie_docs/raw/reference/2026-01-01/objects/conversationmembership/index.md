---
title: ConversationMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationmembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationmembership/index.md
---

ConversationMembership entry, returns basic info related to conversation participant

## Fields

[`archived` ](#field-archived)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Toggle for archive status

[`conversation_id` ](#field-conversation-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Conversation id of conversation membership

[`conversation_role` ](#field-conversation-role)· [`String` ](/reference/2026-01-01/scalars/string)· Role in conversation

[`convo` ](#field-convo)· [`Conversation` ](/reference/2026-01-01/objects/conversation)· Conversation linked to this membership

[`convo_updated_at` ](#field-convo-updated-at)· [`User` ](/reference/2026-01-01/objects/user)· The time the conversation of the

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the Conversation Membership was created

[`creator` ](#field-creator)· [`User` ](/reference/2026-01-01/objects/user)· The creator of this ConversationMembership

[`display_avatar` ](#field-display-avatar)· [`String` ](/reference/2026-01-01/scalars/string)· URL to the avatar to display

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· Either the name of the owner or conversation subject?

[`display_name_and_initial` ](#field-display-name-and-initial)· [`String` ](/reference/2026-01-01/scalars/string)· The first name and last name initial of the owner

[`display_other_user_first_name` ](#field-display-other-user-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· Display the other user first name for non group convos

[`display_other_user_name` ](#field-display-other-user-name)· [`String` ](/reference/2026-01-01/scalars/string)· Display title or other user name for non group convos

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the membership

[`last_task` ](#field-last-task)· [`Task` ](/reference/2026-01-01/objects/task)· Get last conversation task

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Datetime membership was updated

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The creator of membership

[`user_list_as_display_name` ](#field-user-list-as-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The list of users in conversation (to use in place of display name

[`viewed` ](#field-viewed)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the conversation has been viewed

## Used By

[`Conversation.conversation_memberships`](/reference/2026-01-01/objects/conversation)

[`Conversation.current_user_conversation_membership`](/reference/2026-01-01/objects/conversation)

[`ConversationMembershipEdge.node`](/reference/2026-01-01/objects/conversationmembershipedge)

[`ConversationMembershipPaginationConnection.nodes`](/reference/2026-01-01/objects/conversationmembershippaginationconnection)

[`Subscription.conversationMembershipAddedSubscription`](/reference/2026-01-01/objects/subscription)

[`Subscription.conversationMembershipUpdatedSubscription`](/reference/2026-01-01/objects/subscription)

[`deleteConversationMembershipPayload.conversationMembership`](/reference/2026-01-01/objects/deleteconversationmembershippayload)

[`updateConversationMembershipPayload.conversation_membership`](/reference/2026-01-01/objects/updateconversationmembershippayload)

[`Query.conversationMembership`](/reference/2026-01-01/queries/conversationmembership)

[`Query.lastCM`](/reference/2026-01-01/queries/lastcm)

## Definition

```
"""
ConversationMembership entry, returns basic info related to conversation participant
"""
type ConversationMembership {
  """
  Toggle for archive status
  """
  archived: Boolean!


  """
  Conversation id of conversation membership
  """
  conversation_id: ID


  """
  Role in conversation
  """
  conversation_role: String


  """
  Conversation linked to this membership
  """
  convo: Conversation


  """
  The time the conversation of the
  """
  convo_updated_at: User


  """
  The date the Conversation Membership was created
  """
  created_at: ISO8601DateTime!


  """
  The creator of this ConversationMembership
  """
  creator: User


  """
  URL to the avatar to display
  """
  display_avatar: String


  """
  Either the name of the owner or conversation subject?
  """
  display_name: String


  """
  The first name and last name initial of the owner
  """
  display_name_and_initial: String


  """
  Display the other user first name for non group convos
  """
  display_other_user_first_name: String


  """
  Display title or other user name for non group convos
  """
  display_other_user_name: String


  """
  The unique identifier of the membership
  """
  id: ID!


  """
  Get last conversation task
  """
  last_task(
    """
    The type of the notes
    """
    notes_type: String = "inbox"
  ): Task


  """
  Datetime membership was updated
  """
  updated_at: ISO8601DateTime!


  """
  The creator of membership
  """
  user_id: ID


  """
  The list of users in conversation (to use in place of display name
  """
  user_list_as_display_name: String


  """
  Whether the conversation has been viewed
  """
  viewed: Boolean!
}
```
