---
title: createCms1500 | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcms1500/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcms1500/index.md
---

create CMS1500

## Arguments

[`input` ](#argument-input)· [`createCms1500Input` ](/reference/2026-01-01/input-objects/createcms1500input)· Parameters for createCms1500

## Returns

[`createCms1500Payload`](/reference/2026-01-01/objects/createcms1500payload)

## Example

```
mutation createCms1500($input: createCms1500Input) {
  createCms1500(input: $input) {
    cms1500
    messages
  }
}
```
