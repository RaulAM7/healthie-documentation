---
title: AssumedBrand | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/assumedbrand/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/assumedbrand/index.md
---

Assumed brand information

## Fields

[`alt_branded_logo_url` ](#field-alt-branded-logo-url)· [`String` ](/reference/2026-01-01/scalars/string)· The dark logo url for the brand

[`branded_favicon_url` ](#field-branded-favicon-url)· [`String` ](/reference/2026-01-01/scalars/string)· The favicon url for the brand

[`branded_logo_url` ](#field-branded-logo-url)· [`String` ](/reference/2026-01-01/scalars/string)· The branded logo url for the brand

[`branded_name` ](#field-branded-name)· [`String` ](/reference/2026-01-01/scalars/string)· The branded name for the brand

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

[`theme_accent_primary` ](#field-theme-accent-primary)· [`String` ](/reference/2026-01-01/scalars/string)· theme\_accent\_primary

[`theme_accent_primary_hover` ](#field-theme-accent-primary-hover)· [`String` ](/reference/2026-01-01/scalars/string)· theme\_accent\_primary\_hover

[`theme_background_hover` ](#field-theme-background-hover)· [`String` ](/reference/2026-01-01/scalars/string)· theme\_background\_hover

[`theme_background_input` ](#field-theme-background-input)· [`String` ](/reference/2026-01-01/scalars/string)· theme\_background\_input

[`theme_background_primary` ](#field-theme-background-primary)· [`String` ](/reference/2026-01-01/scalars/string)· theme\_background\_primary

[`theme_background_secondary` ](#field-theme-background-secondary)· [`String` ](/reference/2026-01-01/scalars/string)· theme\_background\_secondary

[`theme_background_sidebar` ](#field-theme-background-sidebar)· [`String` ](/reference/2026-01-01/scalars/string)· bg\_color

[`theme_border_input` ](#field-theme-border-input)· [`String` ](/reference/2026-01-01/scalars/string)· theme\_border\_input

[`theme_border_primary` ](#field-theme-border-primary)· [`String` ](/reference/2026-01-01/scalars/string)· theme\_border\_primary

[`theme_text_sidebar` ](#field-theme-text-sidebar)· [`String` ](/reference/2026-01-01/scalars/string)· font\_color

[`theme_text_sidebar_active` ](#field-theme-text-sidebar-active)· [`String` ](/reference/2026-01-01/scalars/string)· selected\_color

[`theme_text_sidebar_tab_bar` ](#field-theme-text-sidebar-tab-bar)· [`String` ](/reference/2026-01-01/scalars/string)· tab\_accent\_color

## Used By

[`Query.assumedBrand`](/reference/2026-01-01/queries/assumedbrand)

## Definition

```
"""
Assumed brand information
"""
type AssumedBrand {
  """
  The dark logo url for the brand
  """
  alt_branded_logo_url: String


  """
  The favicon url for the brand
  """
  branded_favicon_url: String


  """
  The branded logo url for the brand
  """
  branded_logo_url: String


  """
  The branded name for the brand
  """
  branded_name: String
  id: ID!


  """
  theme_accent_primary
  """
  theme_accent_primary: String


  """
  theme_accent_primary_hover
  """
  theme_accent_primary_hover: String


  """
  theme_background_hover
  """
  theme_background_hover: String


  """
  theme_background_input
  """
  theme_background_input: String


  """
  theme_background_primary
  """
  theme_background_primary: String


  """
  theme_background_secondary
  """
  theme_background_secondary: String


  """
  bg_color
  """
  theme_background_sidebar: String


  """
  theme_border_input
  """
  theme_border_input: String


  """
  theme_border_primary
  """
  theme_border_primary: String


  """
  font_color
  """
  theme_text_sidebar: String


  """
  selected_color
  """
  theme_text_sidebar_active: String


  """
  tab_accent_color
  """
  theme_text_sidebar_tab_bar: String
}
```
