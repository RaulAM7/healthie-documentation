---
title: updateNotificationRecords | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotificationrecords/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotificationrecords/index.md
---

Update multiple notification records at once

## Arguments

[`input` ](#argument-input)· [`bulkUpdateNotificationRecordsInput` ](/reference/2026-01-01/input-objects/bulkupdatenotificationrecordsinput)· Parameters for bulkUpdateNotificationRecords

## Returns

[`bulkUpdateNotificationRecordsPayload`](/reference/2026-01-01/objects/bulkupdatenotificationrecordspayload)

## Example

```
mutation updateNotificationRecords($input: bulkUpdateNotificationRecordsInput) {
  updateNotificationRecords(input: $input) {
    messages
    success_string
  }
}
```
