---
title: CustomSidebarOverride | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/customsidebaroverride/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/customsidebaroverride/index.md
---

A custom sidebar override

## Fields

[`append_current_user_id` ](#field-append-current-user-id)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the current user ID will be appended to the URL

[`icon` ](#field-icon)· [`String` ](/reference/2026-01-01/scalars/string)· The icon of the image that will be display on the sidebar

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the override

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label of the sidebar item that will be shown or hidden

[`open_in_iframe` ](#field-open-in-iframe)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the sidebar item will be open in an iframe within the Healthie UI

[`show` ](#field-show)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the sidebar item will be displayed

[`svg_url` ](#field-svg-url)· [`String` ](/reference/2026-01-01/scalars/string)· The link to the custom icon that will be displayed on the sidebar

[`target` ](#field-target)· [`String` ](/reference/2026-01-01/scalars/string)· Where the link will open if clicked

[`url` ](#field-url)· [`String` ](/reference/2026-01-01/scalars/string)· The link that the sidebar item will direct to

## Used By

[`User.additional_client_profile_items`](/reference/2026-01-01/objects/user)

[`User.additional_header_dropdown_items`](/reference/2026-01-01/objects/user)

[`User.additional_quick_profile_items`](/reference/2026-01-01/objects/user)

[`User.additional_sidebar_items`](/reference/2026-01-01/objects/user)

## Definition

```
"""
A custom sidebar override
"""
type CustomSidebarOverride {
  """
  If true, the current user ID will be appended to the URL
  """
  append_current_user_id: Boolean


  """
  The icon of the image that will be display on the sidebar
  """
  icon: String


  """
  The unique identifier of the override
  """
  id: ID!


  """
  The label of the sidebar item that will be shown or hidden
  """
  label: String


  """
  If true, the sidebar item will be open in an iframe within the Healthie UI
  """
  open_in_iframe: Boolean


  """
  If true, the sidebar item will be displayed
  """
  show: Boolean


  """
  The link to the custom icon that will be displayed on the sidebar
  """
  svg_url: String


  """
  Where the link will open if clicked
  """
  target: String


  """
  The link that the sidebar item will direct to
  """
  url: String
}
```
