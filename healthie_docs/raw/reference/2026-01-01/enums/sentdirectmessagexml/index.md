---
title: SentDirectMessageXml | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/sentdirectmessagexml/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/sentdirectmessagexml/index.md
---

Options of what patient XML formats to include in the message

## Used By

[`createSentDirectMessageInput.include_patient_xml`](/reference/2026-01-01/input-objects/createsentdirectmessageinput)

## Definition

```
"""
Options of what patient XML formats to include in the message
"""
enum SentDirectMessageXml {
  cda
  referral_note
}
```
