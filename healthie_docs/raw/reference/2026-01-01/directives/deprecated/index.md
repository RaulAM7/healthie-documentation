---
title: deprecated | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/directives/deprecated/index
  md: https://docs.gethealthie.com/reference/2026-01-01/directives/deprecated/index.md
---

Marks an element of a GraphQL schema as no longer supported.

## Arguments

[`reason` ](#argument-reason)· [`String` ](/reference/2026-01-01/scalars/string)· Explains why this element was deprecated, usually also including a suggestion for how to access supported similar data. Formatted in \[Markdown]\(https\://daringfireball.net/projects/markdown/).

## Definition

```
directive @deprecated(
  reason: String
) on FIELD_DEFINITION | ENUM_VALUE | ARGUMENT_DEFINITION | INPUT_FIELD_DEFINITION
```
