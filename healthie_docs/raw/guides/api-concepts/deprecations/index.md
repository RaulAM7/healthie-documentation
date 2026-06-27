---
title: API Deprecations | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/deprecations/index
  md: https://docs.gethealthie.com/guides/api-concepts/deprecations/index.md
---

## Introduction

Our API evolves over time to add new features, improve functionality, and maintain security. When certain features or practices become outdated, they will be deprecated, meaning they are scheduled to be removed or replaced by a newer alternative. Remember, deprecation does not mean immediate removal but indicates that the feature should be avoided and planned for replacement in the future.

This page is designed to provide you with the latest information about deprecated features within our API. We understand that changes to the API can impact your development process and we are committed to ensuring a smooth transition for all users.

Our API leverages the GraphQL `@deprecated` directive to flag deprecated fields and enum values. This feature enables you to see warnings within your development environment or GraphQL Explorer when you are using a deprecated feature.

Note

For any changes, please keep an eye on this document as it will be updated regularly to reflect any new deprecations.

## Deprecation Policy

Our deprecation policy is designed to give developers a clear and predictable path for transitioning from old features and functionality to new ones. When a feature is deprecated:

* We will provide a minimum of 6 months notice before any deprecated feature is removed.
* We will provide migration instructions for deprecated features.

### List of Deprecated Features

Below is a list of features that are currently deprecated within our GraphQL API.

#### String-based `sort_by` query arguments

* **Deprecation date:** November 6, 2023
* **Expected removal date:** August 6, 2024
* **Recommendation:** All API clients should use the enum-based `order_by` arguments.

## Migration Support

If you have any questions or concerns about migrating from deprecated features, please reach out to our support team at [hello@gethealthie.com](mailto:hello@gethealthie.com?subject=API%20Deprecation%20Question).

We appreciate your understanding and cooperation as we continue to improve our GraphQL API to serve you better.
