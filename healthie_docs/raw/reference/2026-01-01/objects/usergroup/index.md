---
title: UserGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/usergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/usergroup/index.md
---

A user group, returns basic info about the user group

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the user group was created

[`doc_share_id` ](#field-doc-share-id)· [`String` ](/reference/2026-01-01/scalars/string)· An ID used for document, course, and conversation sharing

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the user group

[`invite_code` ](#field-invite-code)· [`String` ](/reference/2026-01-01/scalars/string)· The invite code

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the user group

[`onboarding_flow` ](#field-onboarding-flow)· [`OnboardingFlow` ](/reference/2026-01-01/objects/onboardingflow)· Onboarding Flow of this user group

[`onboarding_flow_id` ](#field-onboarding-flow-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the associated onboarding flow

[`recurring_forms` ](#field-recurring-forms)· [`[RecurringForm!]` ](/reference/2026-01-01/objects/recurringform)· Recurring Form Names for this user group

[`recurring_forms_count` ](#field-recurring-forms-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Recurring Forms Count for this user group

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this user group

[`user_ids` ](#field-user-ids)· [`[String]` ](/reference/2026-01-01/scalars/string)· ids of user in group

[`users` ](#field-users)· [`[User!]!` ](/reference/2026-01-01/objects/user)· required · All patients associated with this user group.

[`users_count` ](#field-users-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of users in the group

[`users_with_membership` ](#field-users-with-membership)· [`[User!]` ](/reference/2026-01-01/objects/user)· Users in user group with course membership

## Used By

[`Appointment.assigned_groups`](/reference/2026-01-01/objects/appointment)

[`AppointmentType.bookable_groups`](/reference/2026-01-01/objects/appointmenttype)

[`AppointmentType.user_group`](/reference/2026-01-01/objects/appointmenttype)

[`CarePlan.user_group`](/reference/2026-01-01/objects/careplan)

[`Conversation.user_groups`](/reference/2026-01-01/objects/conversation)

[`Course.user_groups`](/reference/2026-01-01/objects/course)

[`CourseGroup.user_group`](/reference/2026-01-01/objects/coursegroup)

[`Document.user_groups`](/reference/2026-01-01/objects/document)

[`FeatureToggle.user_group`](/reference/2026-01-01/objects/featuretoggle)

[`Folder.user_groups`](/reference/2026-01-01/objects/folder)

[`NoteScheduler.selected_user_groups`](/reference/2026-01-01/objects/notescheduler)

[`OnboardingFlow.user_groups`](/reference/2026-01-01/objects/onboardingflow)

[`Organization.user_groups`](/reference/2026-01-01/objects/organization)

[`RecurringForm.userGroups`](/reference/2026-01-01/objects/recurringform)

[`User.user_group`](/reference/2026-01-01/objects/user)

[`UserGroupEdge.node`](/reference/2026-01-01/objects/usergroupedge)

[`UserGroupPaginationConnection.nodes`](/reference/2026-01-01/objects/usergrouppaginationconnection)

[`createGroupPayload.user_group`](/reference/2026-01-01/objects/creategrouppayload)

[`deleteUserGroupPayload.user_group`](/reference/2026-01-01/objects/deleteusergrouppayload)

[`updateUserGroupPayload.user_group`](/reference/2026-01-01/objects/updateusergrouppayload)

[`Query.userGroup`](/reference/2026-01-01/queries/usergroup)

## Definition

```
"""
A user group, returns basic info about the user group
"""
type UserGroup {
  """
  The date the user group was created
  """
  created_at: ISO8601DateTime!


  """
  An ID used for document, course, and conversation sharing
  """
  doc_share_id: String


  """
  The unique identifier of the user group
  """
  id: ID!


  """
  The invite code
  """
  invite_code: String


  """
  The name of the user group
  """
  name: String


  """
  Onboarding Flow of this user group
  """
  onboarding_flow: OnboardingFlow


  """
  The id of the associated onboarding flow
  """
  onboarding_flow_id: String


  """
  Recurring Form Names for this user group
  """
  recurring_forms: [RecurringForm!]


  """
  Recurring Forms Count for this user group
  """
  recurring_forms_count: Int


  """
  Owner of this user group
  """
  user: User


  """
  ids of user in group
  """
  user_ids: [String]


  """
  All patients associated with this user group.
  """
  users(
    """
    The active status of the users in the group. Can be "active" or "inactive"
    """
    active_status: String


    """
    The id of the conversation to filter users by
    """
    convo_id: ID


    """
    Sort the returned users by last name
    """
    should_sort: Boolean = true
  ): [User!]!


  """
  The number of users in the group
  """
  users_count: Int


  """
  Users in user group with course membership
  """
  users_with_membership: [User!]
}
```
