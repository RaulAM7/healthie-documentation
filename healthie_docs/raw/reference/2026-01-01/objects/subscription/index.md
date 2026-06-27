---
title: Subscription | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/subscription/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/subscription/index.md
---

Subscriptions for events tracking

## Fields

[`appointmentUserDevicesSubscription` ](#field-appointmentuserdevicessubscription)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· Track changes in appointments where user is participated

[`conversationChangedSubscription` ](#field-conversationchangedsubscription)· [`Conversation` ](/reference/2026-01-01/objects/conversation)· Track changes in conversations

[`conversationMembershipAddedSubscription` ](#field-conversationmembershipaddedsubscription)· [`ConversationMembership` ](/reference/2026-01-01/objects/conversationmembership)· Track new members of conversations

[`conversationMembershipUpdatedSubscription` ](#field-conversationmembershipupdatedsubscription)· [`ConversationMembership` ](/reference/2026-01-01/objects/conversationmembership)· Track new updates to members of conversations

[`formAnswerGroupModifiedSubscription` ](#field-formanswergroupmodifiedsubscription)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· Track modifications of form answer groups

[`groupAppointmentClientsAddedSubscription` ](#field-groupappointmentclientsaddedsubscription)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· Track clients added to group appointment

[`noteAddedSubscription` ](#field-noteaddedsubscription)· [`Note` ](/reference/2026-01-01/objects/note)· Track added notes

[`userUpdatedSubscription` ](#field-userupdatedsubscription)· [`UserNotificationsCount` ](/reference/2026-01-01/objects/usernotificationscount)· Track user updates

[`videoChatsSubscription` ](#field-videochatssubscription)· [`VideoChatsSubscriptionPayload` ](/reference/2026-01-01/objects/videochatssubscriptionpayload)· Track video chats

## Definition

```
"""
Subscriptions for events tracking
"""
type Subscription {
  """
  Track changes in appointments where user is participated
  """
  appointmentUserDevicesSubscription(
    """
    The ID of the appointment to track
    """
    id: ID
  ): Appointment


  """
  Track changes in conversations
  """
  conversationChangedSubscription(
    """
    The ID of the conversation to track
    """
    id: ID
  ): Conversation


  """
  Track new members of conversations
  """
  conversationMembershipAddedSubscription(
    """
    The notes_type state of conversations, for getting last_task
    """
    notesType: String
  ): ConversationMembership


  """
  Track new updates to members of conversations
  """
  conversationMembershipUpdatedSubscription(
    """
    The notes_type state of conversations, for getting last_task
    """
    notesType: String
  ): ConversationMembership


  """
  Track modifications of form answer groups
  """
  formAnswerGroupModifiedSubscription(
    """
    The ID of trackable FormAnswerGroup
    """
    id: ID
  ): FormAnswerGroup


  """
  Track clients added to group appointment
  """
  groupAppointmentClientsAddedSubscription: Appointment


  """
  Track added notes
  """
  noteAddedSubscription(
    """
    The ID of the conversation to track
    """
    conversationId: String


    """
    The order of sorting results
    """
    sortBy: String = "created_at_desc" @deprecated(reason: "Not used")
  ): Note


  """
  Track user updates
  """
  userUpdatedSubscription: UserNotificationsCount


  """
  Track video chats
  """
  videoChatsSubscription: VideoChatsSubscriptionPayload
}
```
