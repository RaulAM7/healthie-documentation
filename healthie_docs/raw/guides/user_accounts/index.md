---
title: User Accounts | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/user_accounts/index
  md: https://docs.gethealthie.com/guides/user_accounts/index.md
---

# User Accounts

There are two primary types of accounts in Healthie: Patients and providers. If a user in Healthie is a patient, that means the user is not a provider and vice versa (the types are mutually exclusive). On the `User` type, the field `is_patient` signifies whether a user is a patient.

## Organizations

When using the Healthie API, your company will have an organization (`Organization` type) and potentially sub-organizations associated with it. Every provider in Healthie is associated with one organization, but patients are *not* associated with an organization directly in the data model. Instead, patients are associated with one or more providers.

If a provider works for multiple organizations or sub-organizations, the provider will have multiple user accounts (one per organization).

## Account uniqueness

Account uniqueness in Healthie is based on several factors:

* Every user account is associated with a `namespace` in Healthie. A `namespace` is essentially your organization’s authentication space within Healthie. There can only be one patient account with the same combination of `namespace`, `email`, `first_name` and `last_name` values. This means two user accounts can have the same `namespace` and `email` if `first_name` and/or `last_name` differ between them.
* Every user account is also associated with a specific `human` in Healthie. A `human` is meant to signify an actual person using Healthie. Each `human` can have one or more Healthie accounts associated with them. Within a single `namespace` in Healthie, if multiple accounts exist with the same `email`, those accounts will typically be associated with the same `human`. The person using those accounts will be able to switch between them in the Healthie portal UI.

To avoid creating duplicate accounts in Healthie by accident, we typically recommend querying the Healthie API first to check for any users with the email specified by a person booking an appointment or signing up for your service.

## Developer and owner permissions

There are no separate “developer” or “owner” account types in Healthie. Instead, these are both permission types controlled by settings on a provider account.

Developer permissions can be changed with the `updateOrganizationMembership` mutation using the `is_developer` parameter. (Every provider account in an organization has an associated `OrganizationMembership`.) The `is_owner` field on the `User` type shows if a given provider account is the organization owner.
