---
title: brandFromCustomSignInPath | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/brandfromcustomsigninpath/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/brandfromcustomsigninpath/index.md
---

fetch a Brand by custom sign in path (considered public)

## Arguments

[`custom_sign_in_path` ](#argument-custom-sign-in-path)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`Brand`](/reference/2026-01-01/objects/brand)

## Example

```
query brandFromCustomSignInPath($custom_sign_in_path: String) {
  brandFromCustomSignInPath(custom_sign_in_path: $custom_sign_in_path) {
    about_description
    bg_color
    brand_email
    brand_name
    brand_owner
    brand_owner_has_practice_plus
    brand_owner_has_whitelabel
    brand_phone
    contact_description
    custom_sign_in_path
    display_embed_title
    display_name
    display_package_image
    email_background_color
    embed_primary_color
    embeddable_layout_css_url
    facebook
    font_color
    ga_id
    gtm_id
    id
    instagram
    intake_completed_html
    logo
    logo_file_name
    logo_url
    main_layout_css_url
    selected_color
    slogan
    tab_accent_color
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
    titles
    twitter
    user_id
    website
  }
}
```
