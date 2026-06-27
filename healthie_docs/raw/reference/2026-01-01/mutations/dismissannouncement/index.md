---
title: dismissAnnouncement | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/dismissannouncement/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/dismissannouncement/index.md
---

Dismiss Announcement

## Arguments

[`input` ](#argument-input)· [`dismissAnnouncementInput` ](/reference/2026-01-01/input-objects/dismissannouncementinput)· Parameters for dismissAnnouncement

## Returns

[`dismissAnnouncementPayload`](/reference/2026-01-01/objects/dismissannouncementpayload)

## Example

```
mutation dismissAnnouncement($input: dismissAnnouncementInput) {
  dismissAnnouncement(input: $input) {
    announcement
    messages
  }
}
```
