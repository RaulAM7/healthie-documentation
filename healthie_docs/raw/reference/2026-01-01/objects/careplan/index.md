---
title: CarePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/careplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/careplan/index.md
---

A Care Plan

## Fields

[`assigned_to` ](#field-assigned-to)· [`String` ](/reference/2026-01-01/scalars/string)· The name of a user group or a patient the care plan has been assigned to

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date of creation

[`creator` ](#field-creator)· [`User` ](/reference/2026-01-01/objects/user)· Provider who created care plan

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The care plan description

[`documents` ](#field-documents)· [`[Document!]!` ](/reference/2026-01-01/objects/document)· required · Associated documents

[`feature_toggle` ](#field-feature-toggle)· [`FeatureToggle` ](/reference/2026-01-01/objects/featuretoggle)· Feature Toggle of the care plan

[`goals` ](#field-goals)· [`[Goal!]!` ](/reference/2026-01-01/objects/goal)· required · Associated goals

[`group_plan_is_active_for_given_user` ](#field-group-plan-is-active-for-given-user)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Shows whether a group care plan(or a single one, if patient\_id argument is not passed) is active for a given user. Make sure to pass patient\_id argument if you need to check the status of a group care\_plan for the given user

[`has_users_with_real_emails` ](#field-has-users-with-real-emails)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Shows whether the patient or at least one user from the related group has not skipped email. We don't want to call care\_plan\_mailer if all of related users have skipped\_email == true

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the plan

[`is_active` ](#field-is-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Care plan is active for the associated patient

[`is_group` ](#field-is-group)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicates whether a care plan is for a group

[`is_hidden` ](#field-is-hidden)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Care plan status

[`is_template` ](#field-is-template)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Indicates if care plan can be used as a template and can be assigned on other users

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of care plan

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· A user the care plan has been assigned to

[`recommendations` ](#field-recommendations)· [`[Recommendation!]!` ](/reference/2026-01-01/objects/recommendation)· required · Ordered (Ascending) associated recommendations

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date when record was last updated

[`user_group` ](#field-user-group)· [`UserGroup` ](/reference/2026-01-01/objects/usergroup)· A user group the care plan has been assigned to

## Used By

[`CarePlanEdge.node`](/reference/2026-01-01/objects/careplanedge)

[`CarePlanPaginationConnection.nodes`](/reference/2026-01-01/objects/careplanpaginationconnection)

[`FeatureToggle.care_plan`](/reference/2026-01-01/objects/featuretoggle)

[`User.active_care_plan`](/reference/2026-01-01/objects/user)

[`User.active_group_care_plan`](/reference/2026-01-01/objects/user)

[`bulkApplyCarePlanTemplatePayload.carePlans`](/reference/2026-01-01/objects/bulkapplycareplantemplatepayload)

[`bulkUpdateCarePlanUsersPayload.carePlans`](/reference/2026-01-01/objects/bulkupdatecareplanuserspayload)

[`createCarePlanPayload.carePlan`](/reference/2026-01-01/objects/createcareplanpayload)

[`deleteCarePlanPayload.carePlan`](/reference/2026-01-01/objects/deletecareplanpayload)

[`exportToTemplatePayload.carePlan`](/reference/2026-01-01/objects/exporttotemplatepayload)

[`sendCarePlanEmailPayload.carePlan`](/reference/2026-01-01/objects/sendcareplanemailpayload)

[`toggleCarePlanStatusForSpecificUserPayload.carePlan`](/reference/2026-01-01/objects/togglecareplanstatusforspecificuserpayload)

[`updateCarePlanPayload.carePlan`](/reference/2026-01-01/objects/updatecareplanpayload)

[`updateGroupCarePlanPayload.carePlan`](/reference/2026-01-01/objects/updategroupcareplanpayload)

[`Query.carePlan`](/reference/2026-01-01/queries/careplan)

## Definition

```
"""
A Care Plan
"""
type CarePlan {
  """
  The name of a user group or a patient the care plan has been assigned to
  """
  assigned_to: String


  """
  Date of creation
  """
  created_at: ISO8601DateTime!


  """
  Provider who created care plan
  """
  creator: User


  """
  The care plan description
  """
  description: String


  """
  Associated documents
  """
  documents: [Document!]!


  """
  Feature Toggle of the care plan
  """
  feature_toggle: FeatureToggle


  """
  Associated goals
  """
  goals: [Goal!]!


  """
  Shows whether a group care plan(or a single one, if patient_id argument is not passed) is active for a given user. Make sure to pass patient_id argument if you need to check the status of a group care_plan for the given user
  """
  group_plan_is_active_for_given_user(
    """
    The ID of a patient to check
    """
    patient_id: ID
  ): Boolean


  """
  Shows whether the patient or at least one user from the related group has not skipped email. We don't want to call care_plan_mailer if all of related users have skipped_email == true
  """
  has_users_with_real_emails: Boolean


  """
  The unique identifier of the plan
  """
  id: ID!


  """
  Care plan is active for the associated patient
  """
  is_active: Boolean


  """
  Indicates whether a care plan is for a group
  """
  is_group: Boolean


  """
  Care plan status
  """
  is_hidden: Boolean!


  """
  Indicates if care plan can be used as a template and can be assigned on other users
  """
  is_template: Boolean!


  """
  The name of care plan
  """
  name: String


  """
  A user the care plan has been assigned to
  """
  patient: User


  """
  Ordered (Ascending) associated recommendations
  """
  recommendations: [Recommendation!]!


  """
  Date when record was last updated
  """
  updated_at: ISO8601DateTime!


  """
  A user group the care plan has been assigned to
  """
  user_group: UserGroup
}
```
