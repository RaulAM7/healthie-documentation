---
title: Audit Logs API Guide | Healthie API Docs
description: Learn how to access and use Healthie's audit logs via the GraphQL API.
source_url:
  html: https://docs.gethealthie.com/guides/audit-logs/audit-logs/index
  md: https://docs.gethealthie.com/guides/audit-logs/audit-logs/index.md
---

# Healthie Audit Logs API Guide

## Overview

Healthie provides detailed audit logs to help organizations monitor key events and actions within the platform. These logs are essential for tracking activities such as appointment scheduling, billing updates, form submissions, and user modifications. Access to audit logs is currently available through Healthie’s GraphQL API for Enterprise organizations.

> **Note:** As of October 2024, Healthie has been logging data for API audit logs. The API supports retrieving data from the last four months. For access to older data, contact <hello@gethealthie.com>.

## Prerequisites

* **Enterprise Plan:** Audit log access is available to organizations on Healthie’s Enterprise plan.
* **API Access:** Ensure your organization has API access enabled.
* **Permissions:** Users must have the `can_view_audit_log` permission enabled. This permission is managed through the API and not via the standard permissions UI.

## Supported Audit Events

The API tracks audit events for the following resource types:

* API\_KEY
* APPOINTMENT
* APPOINTMENT\_INCLUSION
* APPOINTMENT\_LOCATION
* APPOINTMENT\_SETTING
* AVAILABILITY
* BILLING\_ITEM
* CARE\_PLAN
* CMS1500
* CMS1500\_POLICY
* CPT\_CODES\_CMS1500
* DIAGNOSIS
* FEATURE\_TOGGLE
* FORM\_ANSWER\_GROUP
* FORM\_ANSWER
* GOAL
* LOCATION
* ORGANIZATION
* ORGANIZATION\_INFO
* ORGANIZATION\_MEMBERSHIP
* POLICY
* USER

## Event Types

Audit logs track three types of events for each resource:

* **CREATE**: When a new resource is created
* **UPDATE**: When an existing resource is modified
* **DESTROY**: When a resource is deleted

Each event includes detailed information about what changed, including the field name, the previous value, and the new value.

## Accessing Audit Logs via GraphQL API

To retrieve audit logs, utilize the `auditLog` query in Healthie’s GraphQL API. For detailed query examples and implementation guidance, see the [Querying the Audit Log](/guides/audit-logs/audit-log-query) guide.

## Additional Information

* **Sub-Organizations:** For organizations with multiple sub-organizations, the parent organization’s audit log includes events from all subsidiaries, offering a consolidated view.

* **Future Enhancements:** Healthie plans to expand audit logging capabilities, including:

  * Additional models
  * New event types (e.g., data views, document prints)
  * Custom event definitions via the API
  * UI-based access to audit logs

## Getting Started

To enable audit log access or for assistance with permissions, reach out to <hello@gethealthie.com>.

***
