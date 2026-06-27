---
title: BrandInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/brandinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/brandinfo/index.md
---

Info for authentication pages for either a dietitian or partner

## Fields

[`image_url` ](#field-image-url)· [`String` ](/reference/2026-01-01/scalars/string)· Brand Owner's logo

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the partner

[`partner_brand` ](#field-partner-brand)· [`Brand` ](/reference/2026-01-01/objects/brand)· The brand associated with provider/partner

[`show_client_tab` ](#field-show-client-tab)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· if false the client signup tab is not shown

[`show_provider_tab` ](#field-show-provider-tab)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· if false the client signup tab is not shown

[`sign_up_header` ](#field-sign-up-header)· [`String` ](/reference/2026-01-01/scalars/string)· Header for the sign up page

[`sign_up_text` ](#field-sign-up-text)· [`String` ](/reference/2026-01-01/scalars/string)· Header for the sign up page

[`signup_footer` ](#field-signup-footer)· [`String` ](/reference/2026-01-01/scalars/string)· Custom HTML to be placed at the bottom of signup

[`unique_code` ](#field-unique-code)· [`String` ](/reference/2026-01-01/scalars/string)· Unique code of the brand or provider

[`uses_username` ](#field-uses-username)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the partner's users can use a username to sign in (defaults to false)

## Used By

[`Query.brandInfo`](/reference/2026-01-01/queries/brandinfo)

## Definition

```
"""
Info for authentication pages for either a dietitian or partner
"""
type BrandInfo {
  """
  Brand Owner's logo
  """
  image_url: String


  """
  Name of the partner
  """
  name: String


  """
  The brand associated with provider/partner
  """
  partner_brand: Brand


  """
  if false the client signup tab is not shown
  """
  show_client_tab: Boolean


  """
  if false the client signup tab is not shown
  """
  show_provider_tab: Boolean


  """
  Header for the sign up page
  """
  sign_up_header: String


  """
  Header for the sign up page
  """
  sign_up_text: String


  """
  Custom HTML to be placed at the bottom of signup
  """
  signup_footer: String


  """
  Unique code of the brand or provider
  """
  unique_code: String


  """
  Whether the partner's users can use a username to sign in (defaults to false)
  """
  uses_username: Boolean
}
```
