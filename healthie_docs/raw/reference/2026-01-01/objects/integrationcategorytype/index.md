---
title: IntegrationCategoryType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationcategorytype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationcategorytype/index.md
---

Integration Category

## Fields

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the integration category

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the category

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the integration category

[`options` ](#field-options)· [`[IntegrationOptionType!]` ](/reference/2026-01-01/objects/integrationoptiontype)· The list of category options

## Used By

[`IntegrationCategoryTypeEdge.node`](/reference/2026-01-01/objects/integrationcategorytypeedge)

[`IntegrationCategoryTypePaginationConnection.nodes`](/reference/2026-01-01/objects/integrationcategorytypepaginationconnection)

## Definition

```
"""
Integration Category
"""
type IntegrationCategoryType {
  """
  The description of the integration category
  """
  description: String


  """
  The unique identifier of the category
  """
  id: ID!


  """
  The name of the integration category
  """
  name: String


  """
  The list of category options
  """
  options: [IntegrationOptionType!]
}
```
