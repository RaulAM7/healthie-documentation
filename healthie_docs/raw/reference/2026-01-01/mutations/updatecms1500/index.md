---
title: updateCms1500 | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecms1500/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecms1500/index.md
---

update CMS1500

## Arguments

[`input` ](#argument-input)· [`updateCms1500Input` ](/reference/2026-01-01/input-objects/updatecms1500input)· Parameters for updateCms1500

## Returns

[`updateCms1500Payload`](/reference/2026-01-01/objects/updatecms1500payload)

## Example

```
mutation updateCms1500($input: updateCms1500Input) {
  updateCms1500(input: $input) {
    cms1500
    messages
  }
}
```
