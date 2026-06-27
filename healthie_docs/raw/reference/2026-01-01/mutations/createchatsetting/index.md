---
title: createChatSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createchatsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createchatsetting/index.md
---

create an Chat Setting

## Arguments

[`input` ](#argument-input)· [`createChatSettingInput` ](/reference/2026-01-01/input-objects/createchatsettinginput)· Parameters for createChatSetting

## Returns

[`createChatSettingPayload`](/reference/2026-01-01/objects/createchatsettingpayload)

## Example

```
mutation createChatSetting($input: createChatSettingInput) {
  createChatSetting(input: $input) {
    chatSetting
    messages
  }
}
```
