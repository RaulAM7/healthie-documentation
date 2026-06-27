---
title: createClientRestrictionAuthorization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createclientrestrictionauthorization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createclientrestrictionauthorization/index.md
---

Create client restriction authorization

## Arguments

[`input` ](#argument-input)· [`createClientRestrictionAuthorizationInput` ](/reference/2026-01-01/input-objects/createclientrestrictionauthorizationinput)· Parameters for createClientRestrictionAuthorization

## Returns

[`createClientRestrictionAuthorizationPayload`](/reference/2026-01-01/objects/createclientrestrictionauthorizationpayload)

## Example

```
mutation createClientRestrictionAuthorization(
  $input: createClientRestrictionAuthorizationInput
) {
  createClientRestrictionAuthorization(input: $input) {
    client_restriction_authorization
    messages
  }
}
```
