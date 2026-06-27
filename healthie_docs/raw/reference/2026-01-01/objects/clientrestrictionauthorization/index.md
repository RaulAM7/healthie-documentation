---
title: ClientRestrictionAuthorization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/clientrestrictionauthorization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/clientrestrictionauthorization/index.md
---

A client restriction authorization must be created for users to access restricted patients

## Fields

[`client` ](#field-client)· [`User!` ](/reference/2026-01-01/objects/user)· required · The client to whom the restriction authorization applies

[`created_at` ](#field-created-at)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the authorization

[`provider` ](#field-provider)· [`User!` ](/reference/2026-01-01/objects/user)· required · The user who was granted access

[`reason` ](#field-reason)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Optional reason for this authorization

## Used By

[`User.client_restriction_authorizations`](/reference/2026-01-01/objects/user)

[`User.provider_restriction_authorizations`](/reference/2026-01-01/objects/user)

[`createClientRestrictionAuthorizationPayload.client_restriction_authorization`](/reference/2026-01-01/objects/createclientrestrictionauthorizationpayload)

[`deleteClientRestrictionAuthorizationPayload.client_restriction_authorization`](/reference/2026-01-01/objects/deleteclientrestrictionauthorizationpayload)

## Definition

```
"""
A client restriction authorization must be created for users to access restricted patients
"""
type ClientRestrictionAuthorization {
  """
  The client to whom the restriction authorization applies
  """
  client: User!
  created_at: ISO8601DateTime


  """
  The unique identifier of the authorization
  """
  id: ID!


  """
  The user who was granted access
  """
  provider: User!


  """
  Optional reason for this authorization
  """
  reason: String!
}
```
