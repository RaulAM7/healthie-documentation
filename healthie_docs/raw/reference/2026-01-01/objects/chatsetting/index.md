---
title: ChatSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chatsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chatsetting/index.md
---

Chat settings for a user

## Fields

[`auto_welcome_text` ](#field-auto-welcome-text)· [`String` ](/reference/2026-01-01/scalars/string)· The text of the auto welcome message

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· The text of the setting

[`end_date` ](#field-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The end of scheduled autoreply period

[`hide_close_confirmation` ](#field-hide-close-confirmation)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether a user should be prompted to confirm closing a chat

[`hide_org_chat_confirmation` ](#field-hide-org-chat-confirmation)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether a user should be prompted to confirm opening an org chat

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the chat setting

[`is_active` ](#field-is-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the setting is active

[`is_recurring_active` ](#field-is-recurring-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the setting is within recurring messaging period

[`no_end_date` ](#field-no-end-date)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Allow users to no add an end date

[`receive_notifications` ](#field-receive-notifications)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether user should receive notifications from chat while is\_active is true

[`receive_notifications_recurring` ](#field-receive-notifications-recurring)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether a user should receive notifications from chat while is\_recurring\_active is true

[`recurring_all_day` ](#field-recurring-all-day)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not the recurring messages should be all day or for a time range

[`recurring_content` ](#field-recurring-content)· [`String` ](/reference/2026-01-01/scalars/string)· The content for recurring autoreplies

[`recurring_days_data` ](#field-recurring-days-data)· [`RecurringDaysData` ](/reference/2026-01-01/objects/recurringdaysdata)· Front-end friendly version of recurring days

[`recurring_end_time` ](#field-recurring-end-time)· [`String` ](/reference/2026-01-01/scalars/string)· The end of time range for recurring messages

[`recurring_friday` ](#field-recurring-friday)· [`String` ](/reference/2026-01-01/scalars/string)· Either nil, all\_day, or a string representation of a time range

[`recurring_monday` ](#field-recurring-monday)· [`String` ](/reference/2026-01-01/scalars/string)· Either nil, all\_day, or a string representation of a time range

[`recurring_saturday` ](#field-recurring-saturday)· [`String` ](/reference/2026-01-01/scalars/string)· Either nil, all\_day, or a string representation of a time range

[`recurring_start_time` ](#field-recurring-start-time)· [`String` ](/reference/2026-01-01/scalars/string)· The start of time range for recurring messages

[`recurring_sunday` ](#field-recurring-sunday)· [`String` ](/reference/2026-01-01/scalars/string)· Either nil, all\_day, or a string representation of a time range

[`recurring_thursday` ](#field-recurring-thursday)· [`String` ](/reference/2026-01-01/scalars/string)· Either nil, all\_day, or a string representation of a time range

[`recurring_tuesday` ](#field-recurring-tuesday)· [`String` ](/reference/2026-01-01/scalars/string)· Either nil, all\_day, or a string representation of a time range

[`recurring_turned_on` ](#field-recurring-turned-on)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicates whether or not recurring messaging has been set up

[`recurring_wednesday` ](#field-recurring-wednesday)· [`String` ](/reference/2026-01-01/scalars/string)· Either nil, all\_day, or a string representation of a time range

[`scheduled_turned_on` ](#field-scheduled-turned-on)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not a schedule message is set up

[`send_auto_welcome` ](#field-send-auto-welcome)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to send an auto welcome message

[`start_date` ](#field-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The beginning of scheduled autoreply period

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the setting owner

## Used By

[`Query.chatSetting`](/reference/2026-01-01/queries/chatsetting)

[`createChatSettingPayload.chatSetting`](/reference/2026-01-01/objects/createchatsettingpayload)

[`updateChatSettingPayload.chatSetting`](/reference/2026-01-01/objects/updatechatsettingpayload)

## Definition

```
"""
Chat settings for a user
"""
type ChatSetting {
  """
  The text of the auto welcome message
  """
  auto_welcome_text: String


  """
  The text of the setting
  """
  content: String


  """
  The end of scheduled autoreply period
  """
  end_date: ISO8601DateTime


  """
  Whether a user should be prompted to confirm closing a chat
  """
  hide_close_confirmation: Boolean


  """
  Whether a user should be prompted to confirm opening an org chat
  """
  hide_org_chat_confirmation: Boolean


  """
  The unique identifier of the chat setting
  """
  id: ID!


  """
  Whether the setting is active
  """
  is_active: Boolean


  """
  Whether the setting is within recurring messaging period
  """
  is_recurring_active: Boolean


  """
  Allow users to no add an end date
  """
  no_end_date: Boolean


  """
  Whether user should receive notifications from chat while is_active is true
  """
  receive_notifications: Boolean


  """
  Whether a user should receive notifications from chat while is_recurring_active is true
  """
  receive_notifications_recurring: Boolean


  """
  Whether or not the recurring messages should be all day or for a time range
  """
  recurring_all_day: Boolean


  """
  The content for recurring autoreplies
  """
  recurring_content: String


  """
  Front-end friendly version of recurring days
  """
  recurring_days_data: RecurringDaysData


  """
  The end of time range for recurring messages
  """
  recurring_end_time: String


  """
  Either nil, all_day, or a string representation of a time range
  """
  recurring_friday: String


  """
  Either nil, all_day, or a string representation of a time range
  """
  recurring_monday: String


  """
  Either nil, all_day, or a string representation of a time range
  """
  recurring_saturday: String


  """
  The start of time range for recurring messages
  """
  recurring_start_time: String


  """
  Either nil, all_day, or a string representation of a time range
  """
  recurring_sunday: String


  """
  Either nil, all_day, or a string representation of a time range
  """
  recurring_thursday: String


  """
  Either nil, all_day, or a string representation of a time range
  """
  recurring_tuesday: String


  """
  Indicates whether or not recurring messaging has been set up
  """
  recurring_turned_on: Boolean


  """
  Either nil, all_day, or a string representation of a time range
  """
  recurring_wednesday: String


  """
  Whether or not a schedule message is set up
  """
  scheduled_turned_on: Boolean


  """
  Whether to send an auto welcome message
  """
  send_auto_welcome: Boolean


  """
  The beginning of scheduled autoreply period
  """
  start_date: ISO8601DateTime


  """
  The ID of the setting owner
  """
  user_id: ID
}
```
