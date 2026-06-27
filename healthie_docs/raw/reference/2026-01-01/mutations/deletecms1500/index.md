---
title: deleteCms1500 | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecms1500/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecms1500/index.md
---

Destroy a Cms1500

## Arguments

[`input` ](#argument-input)· [`deleteCms1500Input` ](/reference/2026-01-01/input-objects/deletecms1500input)· Parameters for deleteCms1500

## Returns

[`deleteCms1500Payload`](/reference/2026-01-01/objects/deletecms1500payload)

## Example

```
mutation deleteCms1500($input: deleteCms1500Input) {
  deleteCms1500(input: $input) {
    cms1500
    messages
  }
}
```
