---
title: uploadCms1500sToIntegrations | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/uploadcms1500stointegrations/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/uploadcms1500stointegrations/index.md
---

Upload a CMS1500 to integrations: ChangeHealth, OfficeAlly, CandidHealth

## Arguments

[`input` ](#argument-input)· [`uploadToIntegrationsInput` ](/reference/2026-01-01/input-objects/uploadtointegrationsinput)· Parameters for uploadToIntegrations

## Returns

[`uploadToIntegrationsPayload`](/reference/2026-01-01/objects/uploadtointegrationspayload)

## Example

```
mutation uploadCms1500sToIntegrations($input: uploadToIntegrationsInput) {
  uploadCms1500sToIntegrations(input: $input) {
    cms1500s
    messages
    success_message
  }
}
```
