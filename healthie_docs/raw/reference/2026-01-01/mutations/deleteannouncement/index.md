---
title: deleteAnnouncement | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteannouncement/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteannouncement/index.md
---

Destroy Announcement

## Arguments

[`input` ](#argument-input)· [`destroyAnnouncementInput` ](/reference/2026-01-01/input-objects/destroyannouncementinput)· Parameters for destroyAnnouncement

## Returns

[`destroyAnnouncementPayload`](/reference/2026-01-01/objects/destroyannouncementpayload)

## Example

```
mutation deleteAnnouncement($input: destroyAnnouncementInput) {
  deleteAnnouncement(input: $input) {
    announcement
    messages
  }
}
```
