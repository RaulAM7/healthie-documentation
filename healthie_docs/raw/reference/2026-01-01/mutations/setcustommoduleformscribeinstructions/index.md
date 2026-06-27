---
title: setCustomModuleFormScribeInstructions | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/setcustommoduleformscribeinstructions/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/setcustommoduleformscribeinstructions/index.md
---

Set or clear form-level AI Scribe instructions on a charting CustomModuleForm.

## Arguments

[`input` ](#argument-input)· [`SetCustomModuleFormScribeInstructionsInput!` ](/reference/2026-01-01/input-objects/setcustommoduleformscribeinstructionsinput)· required · Parameters for SetCustomModuleFormScribeInstructions

## Returns

[`SetCustomModuleFormScribeInstructionsPayload`](/reference/2026-01-01/objects/setcustommoduleformscribeinstructionspayload)

## Example

```
mutation setCustomModuleFormScribeInstructions(
  $input: SetCustomModuleFormScribeInstructionsInput!
) {
  setCustomModuleFormScribeInstructions(input: $input) {
    customModuleForm
    messages
  }
}
```
