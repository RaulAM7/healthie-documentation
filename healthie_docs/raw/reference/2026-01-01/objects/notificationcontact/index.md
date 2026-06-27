---
title: NotificationContact | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/notificationcontact/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/notificationcontact/index.md
---

A notification contact

## Fields

[`client_portal_access` ](#field-client-portal-access)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Has personal client portal access

[`client_portal_setting` ](#field-client-portal-setting)· [`ClientPortalSetting` ](/reference/2026-01-01/objects/clientportalsetting)· Client portal settings

[`contact_type` ](#field-contact-type)· [`String` ](/reference/2026-01-01/scalars/string)· contact type

[`copy_notifications` ](#field-copy-notifications)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · should a notifications of user be copied to contact

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· contact email

[`emergency` ](#field-emergency)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · is emergency contact

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· first name of a contact

[`full_legal_name_with_preferred` ](#field-full-legal-name-with-preferred)· [`String` ](/reference/2026-01-01/scalars/string)· full legal name with preferred

[`full_name` ](#field-full-name)· [`String` ](/reference/2026-01-01/scalars/string)· full name of a contact

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the contact

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· last name of a contact

[`linked_client` ](#field-linked-client)· [`User` ](/reference/2026-01-01/objects/user)· Linked user to notification contact

[`linked_client_id` ](#field-linked-client-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the linked user account

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· contact phone number

[`relationship` ](#field-relationship)· [`String` ](/reference/2026-01-01/scalars/string)· relationship between contact and user

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date notification contact was last updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this notification contact

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· user id

## Used By

[`User.linked_relatives`](/reference/2026-01-01/objects/user)

[`User.notification_contacts`](/reference/2026-01-01/objects/user)

[`createNotificationContactPayload.notificationContact`](/reference/2026-01-01/objects/createnotificationcontactpayload)

[`deleteNotificationContactPayload.notificationContact`](/reference/2026-01-01/objects/deletenotificationcontactpayload)

[`updateNotificationContactPayload.notificationContact`](/reference/2026-01-01/objects/updatenotificationcontactpayload)

## Definition

```
"""
A notification contact
"""
type NotificationContact {
  """
  Has personal client portal access
  """
  client_portal_access: Boolean!


  """
  Client portal settings
  """
  client_portal_setting: ClientPortalSetting


  """
  contact type
  """
  contact_type: String


  """
  should a notifications of user be copied to contact
  """
  copy_notifications: Boolean!


  """
  contact email
  """
  email: String


  """
  is emergency contact
  """
  emergency: Boolean!


  """
  first name of a contact
  """
  first_name: String


  """
  full legal name with preferred
  """
  full_legal_name_with_preferred: String


  """
  full name of a contact
  """
  full_name: String


  """
  The unique identifier of the contact
  """
  id: ID!


  """
  last name of a contact
  """
  last_name: String


  """
  Linked user to notification contact
  """
  linked_client: User


  """
  ID of the linked user account
  """
  linked_client_id: String


  """
  contact phone number
  """
  phone_number: String


  """
  relationship between contact and user
  """
  relationship: String


  """
  Date notification contact was last updated
  """
  updated_at: ISO8601DateTime!


  """
  Owner of this notification contact
  """
  user: User


  """
  user id
  """
  user_id: ID
}
```
