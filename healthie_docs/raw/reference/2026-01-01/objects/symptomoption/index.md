---
title: SymptomOption | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/symptomoption/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/symptomoption/index.md
---

A Symptom Option

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Custom Symptoms use numeric IDs. Standard symptoms just use the symptom name

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The symptom name

[`value` ](#field-value)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · The symptom value

## Used By

[`FeatureToggle.symptom_options`](/reference/2026-01-01/objects/featuretoggle)

## Definition

```
"""
A Symptom Option
"""
type SymptomOption {
  """
  Custom Symptoms use numeric IDs. Standard symptoms just use the symptom name
  """
  id: ID!


  """
  The symptom name
  """
  name: String!


  """
  The symptom value
  """
  value: Int!
}
```
