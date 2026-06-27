---
title: Versioning | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/versioning/index
  md: https://docs.gethealthie.com/guides/api-concepts/versioning/index.md
---

At Healthie, we’re committed to providing a stable and reliable API for all our integrations. Our versioning strategy allows us to continuously improve our API while ensuring your existing integrations remain functional.

## How We Release Changes

We release two types of changes to the Healthie API:

### Breaking Changes (Require Version Upgrade)

When we make breaking changes, we release a new API version. You must update your `Healthie-GraphQL-API-Version` header to access these changes. This gives you complete control over when to adopt breaking changes, ensuring they never affect your integration unexpectedly.

### Non-Breaking Changes (Automatic)

We continuously add new fields, queries, mutations, and optional arguments through accretion. These changes are immediately available in **all API versions**, including your current version, without any action required. You don’t need to update your version header to access these improvements.

Track Non-Breaking Changes

All non-breaking additions to the schema are documented in the **[Changelog](/guides/api-concepts/changelog)**. Check it regularly to discover new fields and capabilities added to the API.

## Understanding Breaking Changes

A breaking change is any modification that could cause existing API calls to fail or return different results without any changes to your account data. We take breaking changes seriously and use versioning to ensure they never affect your integration unexpectedly.

**Examples of breaking changes (which require a new version):**

* Removing a field
* Changing the return type of a field
* Changing an input argument default (e.g changing a query to be default unpaginated versus paginated)
* Making a field nullable when it was previously non-nullable (e.g. `user: User!` -> `user: User`)
* Making an input argument non-nullable when it was previously nullable (e.g. `id: ID` -> `id: ID!`)

**Examples of non-breaking changes (which we can make without a new version):**

* Adding new queries, mutations, or fields
* Adding an optional new input argument to an existing mutation
* Adding a new filter or sort\_by option to an existing field
* Adding new and updated data to Healthie-provided resource queries (e.g Insurance Plans or Icd Codes)
* Fixing an internal server error (e.g a 500)

When we need to make breaking changes, we release a new API version. This allows you to continue using your current version while giving you the option to adopt the new changes when you’re ready.

## What is API Versioning?

API versioning is a strategy that allows us to make significant improvements to our API while protecting your existing integrations. Different versions of our API can exist simultaneously, giving you control over when to adopt new changes. This approach ensures we can continue evolving our API while maintaining stability for all our users.

## When will Healthie release a new version?

When we make updates to the GraphQL API that may result in a breaking change, a new version is created. Each version is carefully documented and includes all the modifications made since the last version. By opting into a specific version, you can control when and how you adopt new features and changes, eliminating the risk of breaking your existing integration.

All API versions are **cumulative**, which means that changes in version `N+1` will include all changes from version `N`. Customers that request the latest version will need to update their API clients as we release new versions.

We seek to avoid breaking changes and will continue to make non-breaking updates and improvements through accretion. This means you won't need to opt-in to use these changes, as they will be available in all versions, including the baseline.

## Specifying an API Version

Terminal window

```
curl \
-H "Healthie-GraphQL-API-Version: 2026-01-01" \
-H 'AuthorizationSource: API' \
-H 'Authorization: Bearer ...' \
-d '{...}' https://api.gethealthie.com/graphql
```

You should use the `Healthie-GraphQL-API-Version` header to specify an API version, as shown in the example above.

Requests without the `Healthie-GraphQL-API-Version` header currently default to the `2024-06-01` baseline version. **This fallback will be removed on 2027-01-31** — see [Transition Timeline](#transition-timeline).

The header value must match a published Healthie release date exactly. Arbitrary date strings (e.g. `2025-06-15`) are not valid and will be rejected with `UNSUPPORTED_API_VERSION`.

## How to adopt a new version

1. **Review Changes**: Check the version history below for updates in the new version. Use the GraphQL Explorer and check our [Schema Reference](/reference/2026-01-01) to find the latest schema definitions for the version you are adopting.
2. **Test**: Try the new version in your development environment to ensure compatibility
3. **Update**: Change your API requests to use the new version header
4. **Deploy**: Roll out your updated integration with confidence

## Version Lifecycle

Note

The version lifecycle policy described in this section takes effect on **2026-07-01**. See [Transition Timeline](#transition-timeline) for how existing integrations are affected.

Each API version moves through three phases:

| Phase          | Description                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Active**     | Fully supported. No restrictions on use.                                                                                                                                                                  |
| **Deprecated** | Still functional, but the version has a sunset date. Every response on a deprecated version includes an `API_VERSION_SUNSET_WARNING` in `extensions.warnings`. You have until the sunset date to upgrade. |
| **Sunset**     | No longer accepted. Requests using a sunset version are rejected with `UNSUPPORTED_API_VERSION`.                                                                                                          |

When a new version ships, the previous version enters a **6-month deprecation window**, after which it is sunset.

## Transition Timeline

We are introducing a formal version lifecycle with deprecation windows and sunset enforcement. The timeline below describes what changes, and when.

| Date           | What happens                                                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2026-07-01** | Deprecation warnings begin. All existing API versions enter deprecation — requests still succeed, but every response will include an `API_VERSION_SUNSET_WARNING` in `extensions.warnings`. Requests without the `Healthie-GraphQL-API-Version` header will additionally receive a `MISSING_API_VERSION_HEADER` warning (the request still succeeds via the baseline fallback). |
| **2027-01-31** | Enforcement goes live. All versions prior to `2026-07-01` are sunset and requests on those versions will be rejected. The `Healthie-GraphQL-API-Version` header becomes required — requests without it will be rejected.                                                                                                                                                        |

**Action required:**

* **Now:** Add the `Healthie-GraphQL-API-Version` header to all requests. Upgrade to the latest supported version (`2026-01-01`) if you haven’t already.
* **By 2027-01-31:** Be on `2026-07-01` or later. This version will be available from 2026-07-01.

Versions released on or after `2026-07-01` follow the standard 6-month deprecation window and are not affected by the transition sunset date.

## Deprecation Warnings

Once the version lifecycle policy is active, any response on a deprecated version — or any response where the `Healthie-GraphQL-API-Version` header is missing — will include a `warnings` array in the `extensions` field. These warnings fire on **every response** they apply to — they are not sampled or rate-limited.

### `API_VERSION_SUNSET_WARNING`

Returned when the requested version has entered its deprecation window:

```
{
  "data": {},
  "extensions": {
    "warnings": [
      {
        "code": "API_VERSION_SUNSET_WARNING",
        "message": "API version 2025-10-15 is deprecated and will be sunset on 2027-01-31. Please upgrade to a supported version.",
        "requested_version": "2025-10-15",
        "sunset_date": "2027-01-31",
        "latest_version": "2026-07-01"
      }
    ]
  }
}
```

### `MISSING_API_VERSION_HEADER`

Returned when no `Healthie-GraphQL-API-Version` header is present. Since the request falls back to the baseline version (`2024-06-01`), which is itself deprecated, both warnings will appear together:

```
{
  "data": {},
  "extensions": {
    "warnings": [
      {
        "code": "MISSING_API_VERSION_HEADER",
        "message": "No Healthie-GraphQL-API-Version header was sent. Defaulting to baseline version 2024-06-01. This fallback will be removed on 2027-01-31; please include the header in all requests.",
        "latest_version": "2026-07-01"
      },
      {
        "code": "API_VERSION_SUNSET_WARNING",
        "message": "API version 2024-06-01 is deprecated and will be sunset on 2027-01-31. Please upgrade to a supported version.",
        "requested_version": "2024-06-01",
        "sunset_date": "2027-01-31",
        "latest_version": "2026-07-01"
      }
    ]
  }
}
```

## Version Enforcement

Once enforcement is active (see [Transition Timeline](#transition-timeline)), requests using an unsupported version, an unrecognized version date, or a missing header will be rejected rather than served.

### `UNSUPPORTED_API_VERSION`

Returned when the requested version is sunset or is not a recognized Healthie release date:

```
{
  "errors": [
    {
      "message": "API version '2025-10-15' is no longer supported. Please upgrade to a supported version.",
      "extensions": {
        "code": "UNSUPPORTED_API_VERSION",
        "requested_version": "2025-10-15",
        "minimum_supported_version": "2026-07-01",
        "latest_version": "2026-07-01"
      }
    }
  ]
}
```

### `MISSING_API_VERSION_HEADER`

Returned once the baseline fallback is removed and the header is required on every request:

```
{
  "errors": [
    {
      "message": "Missing required header: Healthie-GraphQL-API-Version. All API requests must include a version header.",
      "extensions": {
        "code": "MISSING_API_VERSION_HEADER",
        "latest_version": "2026-07-01"
      }
    }
  ]
}
```

## Version History (Breaking Changes)

These changes require opting into a specific API version using the `Healthie-GraphQL-API-Version` header.

Related Documentation

* **[Changelog](/guides/api-concepts/changelog)** - Granular tracking of non-breaking schema additions available in all versions
* **[API Deprecations](/guides/api-concepts/deprecations)** - Types and operations scheduled for removal

***

### 2026-01-01

* Migrated additional query fields to Connection Type pagination

### 2025-11-30

* Improved the `surescriptsReportedMedicationHistory` query.

  * This now returns a `MedicationHistoryType` that is a direct representation of all information available from DoseSpot.
  * This query now uses cursor pagination
  * Improved error handling will return more specific error messages when issues occur.
  * Supports the use of an ‘Organization Level Prescriber’ if one is configured for the organization.
  * Defaults to returning the last 6 months of medication history if no date range is specified.
  * `patient_id` is now a required argument.

### 2025-10-15

* Removed `clientMutationId` from all mutations
* Migrated additional query fields to Connection Type pagination

### 2025-07-31

* Standardized field types: converted string fields to enums and integers for improved type safety

### 2025-05-15

* Added validation to `createAppointment` to allow only a single attendee for individual appointments when specified via `attendee_ids` (`user_id` is still preferred for individual appointments)

### 2025-04-01

* Converted fields and arguments to enums for improved type safety
* Added validation to require `appointment_location_id` when scheduling an in-person appointment via `createAppointment`

### 2025-01-01

* Migrated fields to Connection Type pagination

### 2024-11-01

* Added validation and updated field nullability for common mutations
* Fixed spelling issues across the API

### 2024-10-20

* Updated `ISO8601Date` and `ISO8601DateTime` type implementations

### 2024-10-01

* Added pagination to the `pharmacies` query field

### 2024-07-01

* Standardized datetime fields to `ISO8601DateTime` type (previously `String`)
* Standardized ID fields to `ID` type (previously `String` and `Int`)
