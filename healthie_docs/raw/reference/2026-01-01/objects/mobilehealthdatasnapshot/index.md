---
title: MobileHealthDataSnapshot | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/mobilehealthdatasnapshot/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/mobilehealthdatasnapshot/index.md
---

Mobile health data snapshot

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the snapshot was created

[`current_status` ](#field-current-status)· [`MobileHealthDataSnapshotStatus!` ](/reference/2026-01-01/enums/mobilehealthdatasnapshotstatus)· required · Current status of the snapshot

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · ID of the snapshot

[`integration_type` ](#field-integration-type)· [`MobileHealthDataSnapshotIntegrationType!` ](/reference/2026-01-01/enums/mobilehealthdatasnapshotintegrationtype)· required · Type of integration

[`organization_id` ](#field-organization-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · ID of the organization

[`parent_organization_id` ](#field-parent-organization-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · ID of the parent organization

[`patient_id` ](#field-patient-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · ID of the patient

[`s3_object_expiring_url` ](#field-s3-object-expiring-url)· [`String` ](/reference/2026-01-01/scalars/string)· Presigned S3 URL for uploading snapshot data

[`s3_object_key` ](#field-s3-object-key)· [`String!` ](/reference/2026-01-01/scalars/string)· required · S3 object key for the snapshot data

[`sync_ended_at` ](#field-sync-ended-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the sync ended

[`sync_started_at` ](#field-sync-started-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the sync started

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the snapshot was last updated

## Used By

[`CancelMobileHealthDataSnapshotPayload.snapshot`](/reference/2026-01-01/objects/cancelmobilehealthdatasnapshotpayload)

[`CreateMobileHealthDataSnapshotPayload.snapshot`](/reference/2026-01-01/objects/createmobilehealthdatasnapshotpayload)

[`ProcessMobileHealthDataSnapshotPayload.snapshot`](/reference/2026-01-01/objects/processmobilehealthdatasnapshotpayload)

## Definition

```
"""
Mobile health data snapshot
"""
type MobileHealthDataSnapshot {
  """
  When the snapshot was created
  """
  created_at: ISO8601DateTime!


  """
  Current status of the snapshot
  """
  current_status: MobileHealthDataSnapshotStatus!


  """
  ID of the snapshot
  """
  id: ID!


  """
  Type of integration
  """
  integration_type: MobileHealthDataSnapshotIntegrationType!


  """
  ID of the organization
  """
  organization_id: ID!


  """
  ID of the parent organization
  """
  parent_organization_id: ID!


  """
  ID of the patient
  """
  patient_id: ID!


  """
  Presigned S3 URL for uploading snapshot data
  """
  s3_object_expiring_url: String


  """
  S3 object key for the snapshot data
  """
  s3_object_key: String!


  """
  When the sync ended
  """
  sync_ended_at: ISO8601DateTime!


  """
  When the sync started
  """
  sync_started_at: ISO8601DateTime!


  """
  When the snapshot was last updated
  """
  updated_at: ISO8601DateTime!
}
```
