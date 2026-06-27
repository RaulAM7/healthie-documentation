---
title: ImportDataRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/importdatarequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/importdatarequest/index.md
---

An object containing info about the import data request

## Fields

[`clients_template` ](#field-clients-template)· [`String` ](/reference/2026-01-01/scalars/string)· The file type of import

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time that the import data request was created

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The file name

[`extension` ](#field-extension)· [`String` ](/reference/2026-01-01/scalars/string)· The file extension

[`optional_comment` ](#field-optional-comment)· [`String` ](/reference/2026-01-01/scalars/string)· The optional comment of import

[`request_type` ](#field-request-type)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The request type

## Used By

[`Query.importDataRequest`](/reference/2026-01-01/queries/importdatarequest)

[`createImportDataRequestPayload.importDataRequest`](/reference/2026-01-01/objects/createimportdatarequestpayload)

## Definition

```
"""
An object containing info about the import data request
"""
type ImportDataRequest {
  """
  The file type of import
  """
  clients_template: String


  """
  The date and time that the import data request was created
  """
  created_at: ISO8601DateTime!


  """
  The file name
  """
  display_name: String


  """
  The file extension
  """
  extension: String


  """
  The optional comment of import
  """
  optional_comment: String


  """
  The request type
  """
  request_type: String!
}
```
