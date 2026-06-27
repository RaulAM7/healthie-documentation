---
title: createApiKey | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createapikey/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createapikey/index.md
---

create API Key. This capability needs to be turned on for your account first

## Arguments

[`input` ](#argument-input)· [`createApiKeyInput` ](/reference/2026-01-01/input-objects/createapikeyinput)· Parameters for createApiKey

## Returns

[`createApiKeyPayload`](/reference/2026-01-01/objects/createapikeypayload)

## Example

```
mutation createApiKey($input: createApiKeyInput) {
  createApiKey(input: $input) {
    api_key
    api_key_object
    messages
  }
}
```
