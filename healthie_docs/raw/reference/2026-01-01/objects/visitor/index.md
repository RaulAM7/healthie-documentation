---
title: Visitor | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/visitor/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/visitor/index.md
---

Info about a visitor to the site

## Fields

[`about_me` ](#field-about-me)· [`String` ](/reference/2026-01-01/scalars/string)· Message from visitor

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· Email of the visitor

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· First name of visitor

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the visitor

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· Last name of visitor

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· Phone number of visitor

## Used By

[`createContactPayload.visitor`](/reference/2026-01-01/objects/createcontactpayload)

[`createEbookPayload.visitor`](/reference/2026-01-01/objects/createebookpayload)

[`createPartnerPayload.visitor`](/reference/2026-01-01/objects/createpartnerpayload)

[`createVisitorPayload.visitor`](/reference/2026-01-01/objects/createvisitorpayload)

## Definition

```
"""
Info about a visitor to the site
"""
type Visitor {
  """
  Message from visitor
  """
  about_me: String


  """
  Email of the visitor
  """
  email: String


  """
  First name of visitor
  """
  first_name: String


  """
  The unique identifier of the visitor
  """
  id: ID!


  """
  Last name of visitor
  """
  last_name: String


  """
  Phone number of visitor
  """
  phone_number: String
}
```
