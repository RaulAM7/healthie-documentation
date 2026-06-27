---
title: skip | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/directives/skip/index
  md: https://docs.gethealthie.com/reference/2026-01-01/directives/skip/index.md
---

Directs the executor to skip this field or fragment when the \`if\` argument is true.

## Arguments

[`if` ](#argument-if)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Skipped when true.

## Definition

```
directive @skip(if: Boolean!) on FIELD | FRAGMENT_SPREAD | INLINE_FRAGMENT
```
