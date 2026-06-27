---
title: assumedBrand | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/assumedbrand/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/assumedbrand/index.md
---

Get the assumed brand for the current user

## Arguments

[`brand_id` ](#argument-brand-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`branded_url` ](#argument-branded-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL from which the brand is assumed

[`custom_sign_in_path` ](#argument-custom-sign-in-path)· [`String` ](/reference/2026-01-01/scalars/string)· The custom sign in path for the brand

[`partner_name` ](#argument-partner-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the partner brand

## Returns

[`AssumedBrand`](/reference/2026-01-01/objects/assumedbrand)

## Example

```
query assumedBrand(
  $brand_id: ID
  $branded_url: String
  $custom_sign_in_path: String
  $partner_name: String
) {
  assumedBrand(
    brand_id: $brand_id
    branded_url: $branded_url
    custom_sign_in_path: $custom_sign_in_path
    partner_name: $partner_name
  ) {
    alt_branded_logo_url
    branded_favicon_url
    branded_logo_url
    branded_name
    id
    theme_accent_primary
    theme_accent_primary_hover
    theme_background_hover
    theme_background_input
    theme_background_primary
    theme_background_secondary
    theme_background_sidebar
    theme_border_input
    theme_border_primary
    theme_text_sidebar
    theme_text_sidebar_active
    theme_text_sidebar_tab_bar
  }
}
```
