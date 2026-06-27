---
title: FormTypesToRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formtypestorequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formtypestorequest/index.md
---

types of forms that can be requested

## Fields

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the object

[`is_video` ](#field-is-video)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the form contains only one custom\_module with mod\_type 'video' and was created as part of a program

[`item_type` ](#field-item-type)· [`String` ](/reference/2026-01-01/scalars/string)· Type of form to request

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The given name of the template

## Used By

[`Query.formTypesToRequest`](/reference/2026-01-01/queries/formtypestorequest)

## Definition

```
"""
types of forms that can be requested
"""
type FormTypesToRequest {
  """
  The unique identifier of the object
  """
  id: String!


  """
  Whether the form contains only one custom_module with mod_type 'video' and was created as part of a program
  """
  is_video: Boolean


  """
  Type of form to request
  """
  item_type: String


  """
  The given name of the template
  """
  name: String
}
```
