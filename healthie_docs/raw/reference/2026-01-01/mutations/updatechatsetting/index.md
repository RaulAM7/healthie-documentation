---
title: updateChatSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatechatsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatechatsetting/index.md
---

update Chat Setting

## Arguments

[`input` ](#argument-input)· [`updateChatSettingInput` ](/reference/2026-01-01/input-objects/updatechatsettinginput)· Parameters for updateChatSetting

## Returns

[`updateChatSettingPayload`](/reference/2026-01-01/objects/updatechatsettingpayload)

## Example

```
mutation updateChatSetting($input: updateChatSettingInput) {
  updateChatSetting(input: $input) {
    chatSetting
    messages
  }
}
```
