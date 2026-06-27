---
title: AnnouncementImageUpload | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/announcementimageupload/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/announcementimageupload/index.md
---

Announcement image upload

## Fields

[`image` ](#field-image)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The announcement image

## Used By

[`createAnnouncementInput.announcement_image`](/reference/2026-01-01/input-objects/createannouncementinput)

[`updateAnnouncementInput.announcement_image`](/reference/2026-01-01/input-objects/updateannouncementinput)

## Definition

```
"""
Announcement image upload
"""
input AnnouncementImageUpload {
  """
  The announcement image
  """
  image: Upload
}
```
