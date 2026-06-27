---
title: createAnnouncement | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createannouncement/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createannouncement/index.md
---

Create Announcement

## Arguments

[`input` ](#argument-input)· [`createAnnouncementInput` ](/reference/2026-01-01/input-objects/createannouncementinput)· Parameters for createAnnouncement

## Returns

[`createAnnouncementPayload`](/reference/2026-01-01/objects/createannouncementpayload)

## Example

```
mutation createAnnouncement($input: createAnnouncementInput) {
  createAnnouncement(input: $input) {
    announcement
    messages
  }
}
```
