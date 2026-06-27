---
title: EntryImageStyleEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/entryimagestyleenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/entryimagestyleenum/index.md
---

Paperclip style variants available for an entry image

## Used By

[`Entry.image_url`](/reference/2026-01-01/objects/entry)

## Definition

```
"""
Paperclip style variants available for an entry image
"""
enum EntryImageStyleEnum {
  """
  Thumbnail variant (100x100).
  """
  THUMB


  """
  Medium variant (300x300).
  """
  MEDIUM


  """
  Large variant (500x500).
  """
  LARGE
}
```
