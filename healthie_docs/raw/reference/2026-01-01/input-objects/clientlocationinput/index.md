---
title: ClientLocationInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/clientlocationinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/clientlocationinput/index.md
---

Payload for a deletable location

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the location will be deleted

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· The country code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the location

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· The first line of the address

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· The second line of the address

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the location

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state

[`zip` ](#field-zip)· [`String` ](/reference/2026-01-01/scalars/string)· The zip code

## Used By

[`ClientPolicyInput.holder_location`](/reference/2026-01-01/input-objects/clientpolicyinput)

[`ClientPolicyInput.payer_location`](/reference/2026-01-01/input-objects/clientpolicyinput)

[`ReferringPhysicianInput.location`](/reference/2026-01-01/input-objects/referringphysicianinput)

[`UserPolicyInput.holder_location`](/reference/2026-01-01/input-objects/userpolicyinput)

[`UserPolicyInput.payer_location`](/reference/2026-01-01/input-objects/userpolicyinput)

[`updateClientInput.location`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateClientInput.locations`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateStripeVerificationDetailsInput.location`](/reference/2026-01-01/input-objects/updatestripeverificationdetailsinput)

[`updateStripeVerificationDetailsInput.personal_address`](/reference/2026-01-01/input-objects/updatestripeverificationdetailsinput)

[`updateUserInput.locations`](/reference/2026-01-01/input-objects/updateuserinput)

## Definition

```
"""
Payload for a deletable location
"""
input ClientLocationInput {
  """
  If true, the location will be deleted
  """
  _destroy: Boolean


  """
  The city
  """
  city: String


  """
  The country code
  """
  country: String


  """
  The ID of the location
  """
  id: ID


  """
  The first line of the address
  """
  line1: String


  """
  The second line of the address
  """
  line2: String


  """
  The graphql_name of the location
  """
  name: String


  """
  The state
  """
  state: String


  """
  The zip code
  """
  zip: String
}
```
