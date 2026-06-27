---
title: include | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/directives/include/index
  md: https://docs.gethealthie.com/reference/2026-01-01/directives/include/index.md
---

Directs the executor to include this field or fragment only when the \`if\` argument is true.

## Arguments

[`if` ](#argument-if)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Included when true.

## Definition

```
directive @include(if: Boolean!) on FIELD | FRAGMENT_SPREAD | INLINE_FRAGMENT
```
