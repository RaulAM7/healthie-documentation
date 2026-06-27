---
title: LabFiltersDataType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/labfiltersdatatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/labfiltersdatatype/index.md
---

Options for lab filters

## Fields

[`clients` ](#field-clients)· [`[User!]` ](/reference/2026-01-01/objects/user)· The list of the data clients

[`labs` ](#field-labs)· [`[String]` ](/reference/2026-01-01/scalars/string)· The list of the labs

[`normalized_statuses` ](#field-normalized-statuses)· [`[String]` ](/reference/2026-01-01/scalars/string)· The list of the normalized statuses

[`providers` ](#field-providers)· [`[User!]` ](/reference/2026-01-01/objects/user)· The list of the ordering providers

[`reviewing_providers` ](#field-reviewing-providers)· [`[User!]` ](/reference/2026-01-01/objects/user)· The list of the reviewing providers

[`statuses` ](#field-statuses)· [`[String]` ](/reference/2026-01-01/scalars/string)· The list of the statuses

## Used By

[`Query.labFiltersData`](/reference/2026-01-01/queries/labfiltersdata)

## Definition

```
"""
Options for lab filters
"""
type LabFiltersDataType {
  """
  The list of the data clients
  """
  clients: [User!]


  """
  The list of the labs
  """
  labs: [String]


  """
  The list of the normalized statuses
  """
  normalized_statuses: [String]


  """
  The list of the ordering providers
  """
  providers: [User!]


  """
  The list of the reviewing providers
  """
  reviewing_providers: [User!]


  """
  The list of the statuses
  """
  statuses: [String]
}
```
