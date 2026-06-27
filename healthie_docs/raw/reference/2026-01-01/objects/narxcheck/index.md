---
title: NarxCheck | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/narxcheck/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/narxcheck/index.md
---

A record of a DoseSpot Narx check

## Fields

[`provider` ](#field-provider)· [`User!` ](/reference/2026-01-01/objects/user)· required · The provider who initiated the Narx check retrieval

[`timestamp` ](#field-timestamp)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the Narx check was performed

## Used By

[`FormAnswerGroup.narx_checks`](/reference/2026-01-01/objects/formanswergroup)

## Definition

```
"""
A record of a DoseSpot Narx check
"""
type NarxCheck {
  """
  The provider who initiated the Narx check retrieval
  """
  provider: User!


  """
  When the Narx check was performed
  """
  timestamp: ISO8601DateTime!
}
```
