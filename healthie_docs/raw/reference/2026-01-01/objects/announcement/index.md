---
title: Announcement | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/announcement/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/announcement/index.md
---

Announcements created by providers for client consumption

## Fields

[`active` ](#field-active)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, announcement is active

[`announcement_image_name` ](#field-announcement-image-name)· [`String` ](/reference/2026-01-01/scalars/string)· file name of associated image

[`announcement_image_url` ](#field-announcement-image-url)· [`String` ](/reference/2026-01-01/scalars/string)· URL of image associated with announcement

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· Announcement content(viewable by client)

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique identifier of the announcement

[`last_toggled_at` ](#field-last-toggled-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date and time announcement active status was changed

[`last_toggled_by` ](#field-last-toggled-by)· [`User` ](/reference/2026-01-01/objects/user)· User that updated active status of this announcement most recently

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of announcement(only viewable by provider)

[`title` ](#field-title)· [`String` ](/reference/2026-01-01/scalars/string)· Title of announcement(viewable by client)

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· User that created this announcement

[`user_group_ids` ](#field-user-group-ids)· [`String` ](/reference/2026-01-01/scalars/string)· Comma separated list of user group ids associated with this announcement

[`user_group_names` ](#field-user-group-names)· [`String` ](/reference/2026-01-01/scalars/string)· Comma separated list of user group names associated with this announcement

## Used By

[`AnnouncementEdge.node`](/reference/2026-01-01/objects/announcementedge)

[`AnnouncementPaginationConnection.nodes`](/reference/2026-01-01/objects/announcementpaginationconnection)

[`User.announcements`](/reference/2026-01-01/objects/user)

[`createAnnouncementPayload.announcement`](/reference/2026-01-01/objects/createannouncementpayload)

[`destroyAnnouncementPayload.announcement`](/reference/2026-01-01/objects/destroyannouncementpayload)

[`dismissAllAnnouncementsPayload.announcements`](/reference/2026-01-01/objects/dismissallannouncementspayload)

[`dismissAnnouncementPayload.announcement`](/reference/2026-01-01/objects/dismissannouncementpayload)

[`updateAnnouncementPayload.announcement`](/reference/2026-01-01/objects/updateannouncementpayload)

[`Query.announcement`](/reference/2026-01-01/queries/announcement)

## Definition

```
"""
Announcements created by providers for client consumption
"""
type Announcement {
  """
  If true, announcement is active
  """
  active: Boolean!


  """
  file name of associated image
  """
  announcement_image_name: String


  """
  URL of image associated with announcement
  """
  announcement_image_url: String


  """
  Announcement content(viewable by client)
  """
  description: String


  """
  Unique identifier of the announcement
  """
  id: ID!


  """
  Date and time announcement active status was changed
  """
  last_toggled_at: ISO8601DateTime


  """
  User that updated active status of this announcement most recently
  """
  last_toggled_by: User


  """
  Name of announcement(only viewable by provider)
  """
  name: String


  """
  Title of announcement(viewable by client)
  """
  title: String


  """
  User that created this announcement
  """
  user: User


  """
  Comma separated list of user group ids associated with this announcement
  """
  user_group_ids: String


  """
  Comma separated list of user group names associated with this announcement
  """
  user_group_names: String
}
```
