---
title: PdfLetterheadTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/pdfletterheadtemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/pdfletterheadtemplate/index.md
---

Base class for types

## Fields

[`address_source` ](#field-address-source)· [`PdfLetterheadTemplateAddressSource!` ](/reference/2026-01-01/enums/pdfletterheadtemplateaddresssource)· required · The source the address should be taken from

[`brand_logo_source` ](#field-brand-logo-source)· [`PdfLetterheadTemplateBrandLogoSource!` ](/reference/2026-01-01/enums/pdfletterheadtemplatebrandlogosource)· required · The source the brand logo should be taken from

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required

[`email_source` ](#field-email-source)· [`PdfLetterheadTemplateEmailSource!` ](/reference/2026-01-01/enums/pdfletterheadtemplateemailsource)· required · The source the email address should be taken from

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

[`include_address` ](#field-include-address)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the address should be shown in PDF

[`include_appointment_details` ](#field-include-appointment-details)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the appointment details should be shown in PDF

[`include_brand_logo` ](#field-include-brand-logo)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the brand logo should be shown in PDF

[`include_email` ](#field-include-email)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the email address should be shown in PDF

[`include_organization_name` ](#field-include-organization-name)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the name of the organization should be shown in PDF

[`include_phone_number` ](#field-include-phone-number)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the phone number should be shown in PDF

[`include_team_member_name` ](#field-include-team-member-name)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the name of the team member should be shown in PDF

[`include_team_member_npi` ](#field-include-team-member-npi)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether provider's NPI should be shown in PDF

[`include_team_member_qualifications` ](#field-include-team-member-qualifications)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether provider's qualifications should be shown in PDF

[`is_default` ](#field-is-default)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether this template is default for the organization

[`organization` ](#field-organization)· [`Organization!` ](/reference/2026-01-01/objects/organization)· required

[`other_email` ](#field-other-email)· [`String` ](/reference/2026-01-01/scalars/string)· Custom email address to use in PDF

[`other_phone_number` ](#field-other-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· Custom phone number to use in PDF

[`phone_number_source` ](#field-phone-number-source)· [`PdfLetterheadTemplatePhoneNumberSource!` ](/reference/2026-01-01/enums/pdfletterheadtemplatephonenumbersource)· required · The source the phone number should be taken from

[`team_member_name_source` ](#field-team-member-name-source)· [`PdfLetterheadTemplateTeamMemberNameSource!` ](/reference/2026-01-01/enums/pdfletterheadtemplateteammembernamesource)· required · The source the team member's name should be taken from

[`title` ](#field-title)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The title for the PDF Letterhead Template

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required

## Used By

[`Organization.default_pdf_letterhead_template`](/reference/2026-01-01/objects/organization)

[`Organization.pdf_letterhead_templates`](/reference/2026-01-01/objects/organization)

[`createPdfLetterheadTemplatePayload.pdf_letterhead_template`](/reference/2026-01-01/objects/createpdfletterheadtemplatepayload)

[`destroyPdfLetterheadTemplatePayload.pdf_letterhead_template`](/reference/2026-01-01/objects/destroypdfletterheadtemplatepayload)

[`setDefaultPdfLetterheadTemplatePayload.pdf_letterhead_template`](/reference/2026-01-01/objects/setdefaultpdfletterheadtemplatepayload)

[`updatePdfLetterheadTemplatePayload.pdf_letterhead_template`](/reference/2026-01-01/objects/updatepdfletterheadtemplatepayload)

[`Query.pdfLetterheadTemplate`](/reference/2026-01-01/queries/pdfletterheadtemplate)

## Definition

```
"""
Base class for types
"""
type PdfLetterheadTemplate {
  """
  The source the address should be taken from
  """
  address_source: PdfLetterheadTemplateAddressSource!


  """
  The source the brand logo should be taken from
  """
  brand_logo_source: PdfLetterheadTemplateBrandLogoSource!
  created_at: ISO8601DateTime!


  """
  The source the email address should be taken from
  """
  email_source: PdfLetterheadTemplateEmailSource!
  id: ID!


  """
  Whether the address should be shown in PDF
  """
  include_address: Boolean!


  """
  Whether the appointment details should be shown in PDF
  """
  include_appointment_details: Boolean!


  """
  Whether the brand logo should be shown in PDF
  """
  include_brand_logo: Boolean!


  """
  Whether the email address should be shown in PDF
  """
  include_email: Boolean!


  """
  Whether the name of the organization should be shown in PDF
  """
  include_organization_name: Boolean!


  """
  Whether the phone number should be shown in PDF
  """
  include_phone_number: Boolean!


  """
  Whether the name of the team member should be shown in PDF
  """
  include_team_member_name: Boolean!


  """
  Whether provider's NPI should be shown in PDF
  """
  include_team_member_npi: Boolean!


  """
  Whether provider's qualifications should be shown in PDF
  """
  include_team_member_qualifications: Boolean!


  """
  Whether this template is default for the organization
  """
  is_default: Boolean!
  organization: Organization!


  """
  Custom email address to use in PDF
  """
  other_email: String


  """
  Custom phone number to use in PDF
  """
  other_phone_number: String


  """
  The source the phone number should be taken from
  """
  phone_number_source: PdfLetterheadTemplatePhoneNumberSource!


  """
  The source the team member's name should be taken from
  """
  team_member_name_source: PdfLetterheadTemplateTeamMemberNameSource!


  """
  The title for the PDF Letterhead Template
  """
  title: String!
  updated_at: ISO8601DateTime!
}
```
