---
title: createMessageBlast | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmessageblast/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmessageblast/index.md
---

create Message Blast

## Arguments

[`input` ](#argument-input)· [`createMessageBlastInput` ](/reference/2026-01-01/input-objects/createmessageblastinput)· Parameters for createMessageBlast

## Returns

[`createMessageBlastPayload`](/reference/2026-01-01/objects/createmessageblastpayload)

## Example

```
mutation createMessageBlast($input: createMessageBlastInput) {
  createMessageBlast(input: $input) {
    message
    messages
  }
}
```
