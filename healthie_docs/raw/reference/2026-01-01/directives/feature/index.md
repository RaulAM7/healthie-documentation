---
title: feature | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/directives/feature/index
  md: https://docs.gethealthie.com/reference/2026-01-01/directives/feature/index.md
---

Directs the executor to run this only based on the state of a server-side feature flag.

## Arguments

[`if` ](#argument-if)· [`String` ](/reference/2026-01-01/scalars/string)· Include the element if the feature flag is enabled.

[`unless` ](#argument-unless)· [`String` ](/reference/2026-01-01/scalars/string)· Include the element if the feature flag is disabled.

## Definition

```
directive @feature(
  if: String
  unless: String
) on FIELD | FRAGMENT_SPREAD | INLINE_FRAGMENT
```
