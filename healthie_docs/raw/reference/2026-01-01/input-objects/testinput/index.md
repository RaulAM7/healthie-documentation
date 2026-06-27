---
title: TestInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/testinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/testinput/index.md
---

DEPRECATED. A test that can be ordered

## Fields

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Human readable description of the test

[`provider_identifier` ](#field-provider-identifier)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier for the test

## Used By

[`SubmissionInput.tests`](/reference/2026-01-01/input-objects/submissioninput)

## Definition

```
"""
DEPRECATED. A test that can be ordered
"""
input TestInput {
  """
  Human readable description of the test
  """
  name: String


  """
  The unique identifier for the test
  """
  provider_identifier: ID!
}
```
