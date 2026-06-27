---
title: OfferingImageUpload | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/offeringimageupload/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/offeringimageupload/index.md
---

Offering image upload

## Fields

[`image` ](#field-image)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The image for upload

## Used By

[`createOfferingInput.offering_image`](/reference/2026-01-01/input-objects/createofferinginput)

[`updateOfferingInput.offering_image`](/reference/2026-01-01/input-objects/updateofferinginput)

## Definition

```
"""
Offering image upload
"""
input OfferingImageUpload {
  """
  The image for upload
  """
  image: Upload
}
```
