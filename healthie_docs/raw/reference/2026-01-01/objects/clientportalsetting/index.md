---
title: ClientPortalSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/clientportalsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/clientportalsetting/index.md
---

A client portal setting

## Fields

[`chat_with_provider` ](#field-chat-with-provider)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can chat with the provider

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the setting

[`schedule_appointments` ](#field-schedule-appointments)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can schedule appointments

[`view_and_complete_forms` ](#field-view-and-complete-forms)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can view and complete forms

[`view_and_create_goals` ](#field-view-and-create-goals)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can view and create goals

[`view_and_create_journal_entries` ](#field-view-and-create-journal-entries)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can view and create journal entries

[`view_and_pay_bills` ](#field-view-and-pay-bills)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can view and pay bills

[`view_and_purchase_packages` ](#field-view-and-purchase-packages)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can view and purchase packages

[`view_and_upload_documents` ](#field-view-and-upload-documents)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can view and upload documents

## Used By

[`NotificationContact.client_portal_setting`](/reference/2026-01-01/objects/notificationcontact)

## Definition

```
"""
A client portal setting
"""
type ClientPortalSetting {
  """
  Whether the client can chat with the provider
  """
  chat_with_provider: Boolean!


  """
  The unique identifier of the setting
  """
  id: ID!


  """
  Whether the client can schedule appointments
  """
  schedule_appointments: Boolean!


  """
  Whether the client can view and complete forms
  """
  view_and_complete_forms: Boolean!


  """
  Whether the client can view and create goals
  """
  view_and_create_goals: Boolean!


  """
  Whether the client can view and create journal entries
  """
  view_and_create_journal_entries: Boolean!


  """
  Whether the client can view and pay bills
  """
  view_and_pay_bills: Boolean!


  """
  Whether the client can view and purchase packages
  """
  view_and_purchase_packages: Boolean!


  """
  Whether the client can view and upload documents
  """
  view_and_upload_documents: Boolean!
}
```
