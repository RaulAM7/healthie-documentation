---
title: OnboardingFlow | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/onboardingflow/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/onboardingflow/index.md
---

An onboarding flow that is comprised of onboarding items

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date this onboarding flow was created

[`has_forms_after_welcome` ](#field-has-forms-after-welcome)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the flow has additional form steps after the welcome screen

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the flow

[`is_multiple_providers` ](#field-is-multiple-providers)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Check if current user organization has more than 1 provider

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of this onboarding flow

[`onboarding_items` ](#field-onboarding-items)· [`[OnboardingItem!]!` ](/reference/2026-01-01/objects/onboardingitem)· required · All onboarding items that make up the onboarding flow

[`onboarding_items_count` ](#field-onboarding-items-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of onboarding items in the flow

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this onboarding flow

[`user_groups` ](#field-user-groups)· [`[UserGroup!]` ](/reference/2026-01-01/objects/usergroup)· The user groups this onboarding flow is associated with

[`user_groups_count` ](#field-user-groups-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of user groups this onboarding flow is associated with

[`user_groups_name_string` ](#field-user-groups-name-string)· [`String` ](/reference/2026-01-01/scalars/string)· The combined name list of the user groups this onboarding flow is associated with

## Used By

[`OnboardingFlowEdge.node`](/reference/2026-01-01/objects/onboardingflowedge)

[`OnboardingFlowPaginationConnection.nodes`](/reference/2026-01-01/objects/onboardingflowpaginationconnection)

[`OnboardingItem.onboarding_flow`](/reference/2026-01-01/objects/onboardingitem)

[`User.default_onboarding_flow`](/reference/2026-01-01/objects/user)

[`UserGroup.onboarding_flow`](/reference/2026-01-01/objects/usergroup)

[`createOnboardingFlowPayload.onboardingFlow`](/reference/2026-01-01/objects/createonboardingflowpayload)

[`deleteOnboardingFlowPayload.onboardingFlow`](/reference/2026-01-01/objects/deleteonboardingflowpayload)

[`updateOnboardingFlowPayload.onboardingFlow`](/reference/2026-01-01/objects/updateonboardingflowpayload)

[`Query.onboardingFlow`](/reference/2026-01-01/queries/onboardingflow)

## Definition

```
"""
An onboarding flow that is comprised of onboarding items
"""
type OnboardingFlow {
  """
  The date this onboarding flow was created
  """
  created_at: ISO8601DateTime!


  """
  If true, the flow has additional form steps after the welcome screen
  """
  has_forms_after_welcome: Boolean


  """
  The unique identifier of the flow
  """
  id: ID!


  """
  Check if current user organization has more than 1 provider
  """
  is_multiple_providers: Boolean


  """
  The name of this onboarding flow
  """
  name: String


  """
  All onboarding items that make up the onboarding flow
  """
  onboarding_items(
    """
    If true, only return custom module forms
    """
    custom_module_forms_only: Boolean = false
  ): [OnboardingItem!]!


  """
  The number of onboarding items in the flow
  """
  onboarding_items_count: Int


  """
  Owner of this onboarding flow
  """
  user: User


  """
  The user groups this onboarding flow is associated with
  """
  user_groups: [UserGroup!]


  """
  The number of user groups this onboarding flow is associated with
  """
  user_groups_count: Int


  """
  The combined name list of the user groups this onboarding flow is associated with
  """
  user_groups_name_string: String
}
```
