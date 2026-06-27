---
title: organization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/organization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/organization/index.md
---

Fetch an organization by id, by provider id, or by the current\_user, demographic org info is (considered public)

## Arguments

[`email` ](#argument-email)· [`String` ](/reference/2026-01-01/scalars/string)· The email address of a user to look up their associated organization.

[`for_client` ](#argument-for-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns the organization of the current patient's assigned provider.

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the organization to fetch.

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of a provider whose organization should be returned.

[`provider_ids` ](#argument-provider-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`state_licenses` ](#argument-state-licenses)· [`[String]`](/reference/2026-01-01/scalars/string)

## Returns

[`Organization`](/reference/2026-01-01/objects/organization)

## Example

```
query organization(
  $email: String
  $for_client: Boolean
  $id: ID
  $provider_id: ID
  $provider_ids: [ID]
  $state_licenses: [String]
) {
  organization(
    email: $email
    for_client: $for_client
    id: $id
    provider_id: $provider_id
    provider_ids: $provider_ids
    state_licenses: $state_licenses
  ) {
    accepted_insurance_plans
    active_care_team_members
    active_members_for_conversation
    appointment_locations
    automated_insurance_billing_setting
    billing_configuration
    can_have_suborgs
    can_link_labs_to_chart_notes
    can_link_prescriptions_to_chart_notes
    cancellation_reasons
    care_plan_recommendation_categories
    created_at
    default_pdf_letterhead_template
    e_labs_settings
    id
    insurance_plans_used_by_organization_providers
    is_active
    is_using_system_default_pdf_letterhead_template
    location
    name
    npi
    num_users
    onboarding_flow_id
    only_active_organization_memberships
    only_active_providers
    only_active_providers_count
    only_active_standard
    only_active_standard_count
    only_active_support
    only_active_support_count
    org_roles
    organization_cpt_codes
    organization_email
    organization_info
    organization_infos
    organization_memberships
    other_id
    other_id_qual
    owner
    owner_id
    owner_subscription
    paginated_users
    parent_organization
    parent_organization_id
    payout_accounts_enabled
    pdf_letterhead_templates
    permission_templates
    phone_number
    provider_insurance_plans
    providers
    require_insurance_card_upload
    rupa_health_members
    state_licenses
    suborganizations
    tags
    tax_id
    tax_id_type
    user_groups
    users
    zus_builder_id
  }
}
```
