---
title: dismissAllAnnouncements | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/dismissallannouncements/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/dismissallannouncements/index.md
---

Dismiss All Announcements For A User

## Arguments

[`input` ](#argument-input)· [`dismissAllAnnouncementsInput` ](/reference/2026-01-01/input-objects/dismissallannouncementsinput)· Parameters for dismissAllAnnouncements

## Returns

[`dismissAllAnnouncementsPayload`](/reference/2026-01-01/objects/dismissallannouncementspayload)

## Example

```
mutation dismissAllAnnouncements($input: dismissAllAnnouncementsInput) {
  dismissAllAnnouncements(input: $input) {
    announcements
    messages
  }
}
```
