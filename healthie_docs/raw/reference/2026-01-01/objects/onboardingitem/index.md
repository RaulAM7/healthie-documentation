---
title: OnboardingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/onboardingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/onboardingitem/index.md
---

An onboarding item that has something for the client to complete

## Fields

[`attached_object_edit_url` ](#field-attached-object-edit-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL to go to to edit the attached object

[`billing_disclaimer` ](#field-billing-disclaimer)· [`String` ](/reference/2026-01-01/scalars/string)· Custom text above the billing info screen

[`completed_form_id` ](#field-completed-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· Return the ID of the associated completed form\_answer\_group

[`completed_onboarding_item` ](#field-completed-onboarding-item)· [`CompletedOnboardingItem` ](/reference/2026-01-01/objects/completedonboardingitem)· The completed onboarding item for the given user id (from args)

[`date_to_show` ](#field-date-to-show)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The relevant date to show

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The display name for the onboarding item (based off the attached object)

[`has_matrix_field` ](#field-has-matrix-field)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Onboarding item has matrix field

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the onboarding item

[`incomplete_form_id` ](#field-incomplete-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· Return the ID of the incomplete form

[`is_last_item` ](#field-is-last-item)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Show if it the last item in related onboarding flow

[`is_skippable` ](#field-is-skippable)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the user can skip this onboarding item

[`item_id` ](#field-item-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the associated item

[`item_type` ](#field-item-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of item attached to this onboarding item

[`onboarding_flow` ](#field-onboarding-flow)· [`OnboardingFlow` ](/reference/2026-01-01/objects/onboardingflow)· The user group this onboarding flow is assigned to

[`onboarding_flow_id` ](#field-onboarding-flow-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the onboarding flow

[`photo_id_disclaimer` ](#field-photo-id-disclaimer)· [`String` ](/reference/2026-01-01/scalars/string)· Custom text above the photo ID screen

[`policy_disclaimer` ](#field-policy-disclaimer)· [`String` ](/reference/2026-01-01/scalars/string)· Custom text above the insurance policy screen

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this onboarding item

[`view_url` ](#field-view-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL to view the onboarding item

[`welcome_text` ](#field-welcome-text)· [`String` ](/reference/2026-01-01/scalars/string)· Custom text for the welcome screen

## Used By

[`CompletedOnboardingItem.onboarding_item`](/reference/2026-01-01/objects/completedonboardingitem)

[`IntakeFlowItem.onboarding_item`](/reference/2026-01-01/objects/intakeflowitem)

[`OnboardingFlow.onboarding_items`](/reference/2026-01-01/objects/onboardingflow)

[`User.next_onboarding_step`](/reference/2026-01-01/objects/user)

[`createOnboardingItemPayload.onboardingItem`](/reference/2026-01-01/objects/createonboardingitempayload)

[`deleteOnboardingItemPayload.onboardingItem`](/reference/2026-01-01/objects/deleteonboardingitempayload)

[`updateOnboardingItemPayload.onboardingItem`](/reference/2026-01-01/objects/updateonboardingitempayload)

[`Query.onboardingItem`](/reference/2026-01-01/queries/onboardingitem)

## Definition

```
"""
An onboarding item that has something for the client to complete
"""
type OnboardingItem {
  """
  The URL to go to to edit the attached object
  """
  attached_object_edit_url: String


  """
  Custom text above the billing info screen
  """
  billing_disclaimer: String


  """
  Return the ID of the associated completed form_answer_group
  """
  completed_form_id: String


  """
  The completed onboarding item for the given user id (from args)
  """
  completed_onboarding_item: CompletedOnboardingItem


  """
  The relevant date to show
  """
  date_to_show: ISO8601DateTime


  """
  The display name for the onboarding item (based off the attached object)
  """
  display_name: String


  """
  Onboarding item has matrix field
  """
  has_matrix_field: Boolean


  """
  The unique identifier of the onboarding item
  """
  id: ID!


  """
  Return the ID of the incomplete form
  """
  incomplete_form_id: String


  """
  Show if it the last item in related onboarding flow
  """
  is_last_item(
    """
    Show if it the last item in related onboarding flow
    """
    custom_module_forms_only: Boolean = false
  ): Boolean


  """
  Whether the user can skip this onboarding item
  """
  is_skippable: Boolean!


  """
  The ID of the associated item
  """
  item_id: String


  """
  The type of item attached to this onboarding item
  """
  item_type: String


  """
  The user group this onboarding flow is assigned to
  """
  onboarding_flow: OnboardingFlow


  """
  ID of the onboarding flow
  """
  onboarding_flow_id: ID


  """
  Custom text above the photo ID screen
  """
  photo_id_disclaimer: String


  """
  Custom text above the insurance policy screen
  """
  policy_disclaimer: String


  """
  Owner of this onboarding item
  """
  user: User


  """
  The URL to view the onboarding item
  """
  view_url: String


  """
  Custom text for the welcome screen
  """
  welcome_text: String
}
```
