---
title: updateAnnouncement | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateannouncement/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateannouncement/index.md
---

Update Announcement

## Arguments

[`input` ](#argument-input)· [`updateAnnouncementInput` ](/reference/2026-01-01/input-objects/updateannouncementinput)· Parameters for updateAnnouncement

## Returns

[`updateAnnouncementPayload`](/reference/2026-01-01/objects/updateannouncementpayload)

## Example

```
mutation updateAnnouncement($input: updateAnnouncementInput) {
  updateAnnouncement(input: $input) {
    announcement
    messages
  }
}
```
