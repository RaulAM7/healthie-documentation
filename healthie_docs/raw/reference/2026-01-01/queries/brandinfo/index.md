---
title: brandInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/brandinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/brandinfo/index.md
---

get info used on authentication pages for either a dietitian or partner

## Arguments

[`code` ](#argument-code)· [`String`](/reference/2026-01-01/scalars/string)

[`dietitian_id` ](#argument-dietitian-id)· [`String`](/reference/2026-01-01/scalars/string)

[`invite_code` ](#argument-invite-code)· [`String`](/reference/2026-01-01/scalars/string)

[`partner_name` ](#argument-partner-name)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`BrandInfo`](/reference/2026-01-01/objects/brandinfo)

## Example

```
query brandInfo(
  $code: String
  $dietitian_id: String
  $invite_code: String
  $partner_name: String
) {
  brandInfo(
    code: $code
    dietitian_id: $dietitian_id
    invite_code: $invite_code
    partner_name: $partner_name
  ) {
    image_url
    name
    partner_brand
    show_client_tab
    show_provider_tab
    sign_up_header
    sign_up_text
    signup_footer
    unique_code
    uses_username
  }
}
```
