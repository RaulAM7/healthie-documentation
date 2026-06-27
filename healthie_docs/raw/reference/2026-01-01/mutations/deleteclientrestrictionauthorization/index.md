---
title: deleteClientRestrictionAuthorization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteclientrestrictionauthorization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteclientrestrictionauthorization/index.md
---

Delete client restriction authorization

## Arguments

[`input` ](#argument-input)· [`deleteClientRestrictionAuthorizationInput` ](/reference/2026-01-01/input-objects/deleteclientrestrictionauthorizationinput)· Parameters for deleteClientRestrictionAuthorization

## Returns

[`deleteClientRestrictionAuthorizationPayload`](/reference/2026-01-01/objects/deleteclientrestrictionauthorizationpayload)

## Example

```
mutation deleteClientRestrictionAuthorization(
  $input: deleteClientRestrictionAuthorizationInput
) {
  deleteClientRestrictionAuthorization(input: $input) {
    client_restriction_authorization
    messages
  }
}
```
