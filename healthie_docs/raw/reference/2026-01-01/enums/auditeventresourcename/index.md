---
title: AuditEventResourceName | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/auditeventresourcename/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/auditeventresourcename/index.md
---

The types of resources that audit events can be associated with.

## Used By

[`AuditEvent.resource_name`](/reference/2026-01-01/objects/auditevent)

[`Query.auditLog`](/reference/2026-01-01/queries/auditlog)

## Definition

```
"""
The types of resources that audit events can be associated with.
"""
enum AuditEventResourceName {
  API_KEY
  APPOINTMENT
  APPOINTMENT_INCLUSION
  APPOINTMENT_LOCATION
  APPOINTMENT_SETTING
  AVAILABILITY
  BILLING_ITEM
  CARE_PLAN
  CMS1500
  CMS1500_POLICY
  CPT_CODES_CMS1500
  DIAGNOSIS
  FEATURE_TOGGLE
  FORM_ANSWER_GROUP
  FORM_ANSWER
  GOAL
  LOCATION
  ORGANIZATION
  ORGANIZATION_INFO
  ORGANIZATION_MEMBERSHIP
  POLICY
  TASK
  USER
}
```
