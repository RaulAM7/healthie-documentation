---
title: pdfLetterheadTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/pdfletterheadtemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/pdfletterheadtemplate/index.md
---

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

## Returns

[`PdfLetterheadTemplate`](/reference/2026-01-01/objects/pdfletterheadtemplate)

## Example

```
query pdfLetterheadTemplate($id: ID!) {
  pdfLetterheadTemplate(id: $id) {
    address_source
    brand_logo_source
    created_at
    email_source
    id
    include_address
    include_appointment_details
    include_brand_logo
    include_email
    include_organization_name
    include_phone_number
    include_team_member_name
    include_team_member_npi
    include_team_member_qualifications
    is_default
    organization
    other_email
    other_phone_number
    phone_number_source
    team_member_name_source
    title
    updated_at
  }
}
```
