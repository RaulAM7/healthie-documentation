---
title: CompletedOnboardingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/completedonboardingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/completedonboardingitem/index.md
---

An object with information about how an onboarding item was completed

## Fields

[`attached_object_edit_url` ](#field-attached-object-edit-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL to go to to edit the attached object

[`date_to_show` ](#field-date-to-show)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The most relevant date to display

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the item

[`item_id` ](#field-item-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the object that completed the onboarding item

[`item_type` ](#field-item-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of item that was completed

[`onboarding_item` ](#field-onboarding-item)· [`OnboardingItem` ](/reference/2026-01-01/objects/onboardingitem)· The onboarding item that was completed

[`onboarding_item_id` ](#field-onboarding-item-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the onboarding item

[`skipped` ](#field-skipped)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Set to true if the user skipped this

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The completed (client)

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the completer (client)

[`view_url` ](#field-view-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL to view

## Used By

[`CompletedOnboardingItemEdge.node`](/reference/2026-01-01/objects/completedonboardingitemedge)

[`CompletedOnboardingItemPaginationConnection.nodes`](/reference/2026-01-01/objects/completedonboardingitempaginationconnection)

[`IntakeFlowItem.completed_onboarding_item`](/reference/2026-01-01/objects/intakeflowitem)

[`OnboardingItem.completed_onboarding_item`](/reference/2026-01-01/objects/onboardingitem)

[`createCompletedOnboardingItemPayload.completed_onboarding_item`](/reference/2026-01-01/objects/createcompletedonboardingitempayload)

[`Query.completedOnboardingItem`](/reference/2026-01-01/queries/completedonboardingitem)

## Definition

```
"""
An object with information about how an onboarding item was completed
"""
type CompletedOnboardingItem {
  """
  The URL to go to to edit the attached object
  """
  attached_object_edit_url: String


  """
  The most relevant date to display
  """
  date_to_show: ISO8601DateTime


  """
  The unique identifier of the item
  """
  id: ID!


  """
  The id of the object that completed the onboarding item
  """
  item_id: String


  """
  The type of item that was completed
  """
  item_type: String


  """
  The onboarding item that was completed
  """
  onboarding_item: OnboardingItem


  """
  The ID of the onboarding item
  """
  onboarding_item_id: String


  """
  Set to true if the user skipped this
  """
  skipped: Boolean!


  """
  The completed (client)
  """
  user: User


  """
  The ID of the completer (client)
  """
  user_id: String


  """
  The URL to view
  """
  view_url: String
}
```
