---
title: CourseTypeFilter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/coursetypefilter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/coursetypefilter/index.md
---

The type of course to filter by

## Used By

[`Query.courses`](/reference/2026-01-01/queries/courses)

## Definition

```
"""
The type of course to filter by
"""
enum CourseTypeFilter {
  """
  All courses
  """
  ALL
  ROLLING
  FIXED
}
```
