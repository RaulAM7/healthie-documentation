---
title: createGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/creategroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/creategroup/index.md
---

Create a Group

## Arguments

[`input` ](#argument-input)· [`createGroupInput` ](/reference/2026-01-01/input-objects/creategroupinput)· Parameters for createGroup

## Returns

[`createGroupPayload`](/reference/2026-01-01/objects/creategrouppayload)

## Example

```
mutation createGroup($input: createGroupInput) {
  createGroup(input: $input) {
    messages
    user_group
  }
}
```
