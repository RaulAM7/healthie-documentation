---
title: deleteApiKey | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteapikey/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteapikey/index.md
---

Destroy API Key

## Arguments

[`input` ](#argument-input)· [`deleteApiKeyInput` ](/reference/2026-01-01/input-objects/deleteapikeyinput)· Parameters for deleteApiKey

## Returns

[`deleteApiKeyPayload`](/reference/2026-01-01/objects/deleteapikeypayload)

## Example

```
mutation deleteApiKey($input: deleteApiKeyInput) {
  deleteApiKey(input: $input) {
    api_key
    messages
  }
}
```
