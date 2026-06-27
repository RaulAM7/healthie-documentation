---
title: Organization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organization/index.md
---

An organization, that is an umbrella group for multiple providers

## Fields

[`accepted_insurance_plans` ](#field-accepted-insurance-plans)· [`AcceptedInsurancePlanConnection` ](/reference/2026-01-01/objects/acceptedinsuranceplanconnection)· The insurance plans the organization accepts, sorted by payer name ascending.

[`active_care_team_members` ](#field-active-care-team-members)· [`[User!]` ](/reference/2026-01-01/objects/user)· The active potential care team members of the organization

[`active_members_for_conversation` ](#field-active-members-for-conversation)· [`[User!]` ](/reference/2026-01-01/objects/user)· The active users of the organization used for starting new conversations

[`appointment_locations` ](#field-appointment-locations)· [`[AppointmentLocation!]` ](/reference/2026-01-01/objects/appointmentlocation)· Returns organization appointment locations

[`automated_insurance_billing_setting` ](#field-automated-insurance-billing-setting)· [`AutomatedInsuranceBillingSetting` ](/reference/2026-01-01/objects/automatedinsurancebillingsetting)· The automated insurance billing settings for the organization

[`billing_configuration` ](#field-billing-configuration)· [`BillingConfiguration` ](/reference/2026-01-01/objects/billingconfiguration)· Billing configuration settings for this organization

[`can_have_suborgs` ](#field-can-have-suborgs)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Can have suborgs for this org

[`can_link_labs_to_chart_notes` ](#field-can-link-labs-to-chart-notes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the organization can link lab orders to chart notes

[`can_link_prescriptions_to_chart_notes` ](#field-can-link-prescriptions-to-chart-notes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the organization can link E-Rx prescriptions to chart notes

[`cancellation_reasons` ](#field-cancellation-reasons)· [`[CancellationReason!]!` ](/reference/2026-01-01/objects/cancellationreason)· required · Returns general cancellation reasons

[`care_plan_recommendation_categories` ](#field-care-plan-recommendation-categories)· [`[CarePlanRecommendationCategory!]!` ](/reference/2026-01-01/objects/careplanrecommendationcategory)· required · Fetch paginated Care Plan Recommendation Categories collection

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The creation date of the organization

[`default_pdf_letterhead_template` ](#field-default-pdf-letterhead-template)· [`PdfLetterheadTemplate` ](/reference/2026-01-01/objects/pdfletterheadtemplate)· The default \`PdfLetterheadTemplate\` for this organization

[`e_labs_settings` ](#field-e-labs-settings)· [`ELabsSettings` ](/reference/2026-01-01/objects/elabssettings)· If enabled for organization, settings for E-Labs

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the organization

[`insurance_plans_used_by_organization_providers` ](#field-insurance-plans-used-by-organization-providers)· [`[InsurancePlan!]!` ](/reference/2026-01-01/objects/insuranceplan)· required · Returns the first 20 distinct insurance plans used by providers in an organization, filtered by payer name if provided (considered public)

[`is_active` ](#field-is-active)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the organization is active. Inactive orgs are blocked from adding clients or creating appointments.

[`is_using_system_default_pdf_letterhead_template` ](#field-is-using-system-default-pdf-letterhead-template)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The system default PDF Letterhead Template is used if true

[`location` ](#field-location)· [`Location` ](/reference/2026-01-01/objects/location)· The location of the organization

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the organization

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the organization

[`num_users` ](#field-num-users)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of users in the organization

[`onboarding_flow_id` ](#field-onboarding-flow-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the onboarding flow for org providers

[`only_active_organization_memberships` ](#field-only-active-organization-memberships)· [`[OrganizationMembership!]` ](/reference/2026-01-01/objects/organizationmembership)· The active organization memberships of the organization

[`only_active_providers` ](#field-only-active-providers)· [`[User!]` ](/reference/2026-01-01/objects/user)· The active providers of the organization

[`only_active_providers_count` ](#field-only-active-providers-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of active providers of the organization

[`only_active_standard` ](#field-only-active-standard)· [`[User!]` ](/reference/2026-01-01/objects/user)· The active standard users of the organization

[`only_active_standard_count` ](#field-only-active-standard-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of active standard user of the organization

[`only_active_support` ](#field-only-active-support)· [`[User!]` ](/reference/2026-01-01/objects/user)· The active support users of the organization

[`only_active_support_count` ](#field-only-active-support-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of active support user of the organization

[`org_roles` ](#field-org-roles)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Potential Organization Roles for this Organization

[`organization_cpt_codes` ](#field-organization-cpt-codes)· [`[OrganizationCptCodeType!]` ](/reference/2026-01-01/objects/organizationcptcodetype)· Returns organization cpt codes

[`organization_email` ](#field-organization-email)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The email of organization

[`organization_info` ](#field-organization-info)· [`OrganizationInfo` ](/reference/2026-01-01/objects/organizationinfo)· The first organization info of the organization

[`organization_infos` ](#field-organization-infos)· [`OrganizationInfoPaginationConnection` ](/reference/2026-01-01/objects/organizationinfopaginationconnection)· The organization infos of the organization

[`organization_memberships` ](#field-organization-memberships)· [`OrganizationMembershipPaginationConnection` ](/reference/2026-01-01/objects/organizationmembershippaginationconnection)· The organization memberships of the organization

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other id

[`other_id_qual` ](#field-other-id-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID qualifier (what type of ID it is)

[`owner` ](#field-owner)· [`User` ](/reference/2026-01-01/objects/user)· The owner of the organization

[`owner_id` ](#field-owner-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the org owner

[`owner_subscription` ](#field-owner-subscription)· [`SubscriptionInstance` ](/reference/2026-01-01/objects/subscriptioninstance)· The owner of the org's subscription

[`paginated_users` ](#field-paginated-users)· [`UserConnection` ](/reference/2026-01-01/objects/userconnection)· The users associated with the organization

[`parent_organization` ](#field-parent-organization)· [`Organization` ](/reference/2026-01-01/objects/organization)· Parent organization for this org

[`parent_organization_id` ](#field-parent-organization-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the parent organization

[`payout_accounts_enabled` ](#field-payout-accounts-enabled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the organization has the payout accounts feature enabled

[`pdf_letterhead_templates` ](#field-pdf-letterhead-templates)· [`[PdfLetterheadTemplate!]` ](/reference/2026-01-01/objects/pdfletterheadtemplate)· The list of available \`PdfLetterheadTemplate\`s

[`permission_templates` ](#field-permission-templates)· [`[PermissionTemplateType!]` ](/reference/2026-01-01/objects/permissiontemplatetype)· Permission templates for this org

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the organization

[`provider_insurance_plans` ](#field-provider-insurance-plans)· [`InsurancePlanPaginationConnection!` ](/reference/2026-01-01/objects/insuranceplanpaginationconnection)· required · Distinct insurance plans used by providers in an organization, filtered by payer name if provided (considered public). Uses cursor-based pagination (connections).

[`providers` ](#field-providers)· [`UserConnection` ](/reference/2026-01-01/objects/userconnection)· The providers of the organization

[`require_insurance_card_upload` ](#field-require-insurance-card-upload)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Require patients to upload their insurance card via the Insurance Form

[`rupa_health_members` ](#field-rupa-health-members)· [`[User!]` ](/reference/2026-01-01/objects/user)· The number of users in the organization connected their rupa health account

[`state_licenses` ](#field-state-licenses)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Returns organization state licenses

[`suborganizations` ](#field-suborganizations)· [`[Organization!]` ](/reference/2026-01-01/objects/organization)· Suborganizations for this org

[`tags` ](#field-tags)· [`[Tag!]` ](/reference/2026-01-01/objects/tag)· Returns organization tags

[`tax_id` ](#field-tax-id)· [`String` ](/reference/2026-01-01/scalars/string)· Tax ID of organization

[`tax_id_type` ](#field-tax-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· The tax is of the organization

[`user_groups` ](#field-user-groups)· [`[UserGroup!]` ](/reference/2026-01-01/objects/usergroup)· User groups that are in the organization

[`users` ](#field-users)· [`[User!]` ](/reference/2026-01-01/objects/user)· The users of the organization

[`zus_builder_id` ](#field-zus-builder-id)· [`String` ](/reference/2026-01-01/scalars/string)· Builder ID for the Zus token

## Used By

[`CarePlanRecommendationCategory.organization`](/reference/2026-01-01/objects/careplanrecommendationcategory)

[`Cms1500.billing_provider`](/reference/2026-01-01/objects/cms1500)

[`Organization.parent_organization`](/reference/2026-01-01/objects/organization)

[`Organization.suborganizations`](/reference/2026-01-01/objects/organization)

[`OrganizationInfo.organization`](/reference/2026-01-01/objects/organizationinfo)

[`OrganizationMembership.organization`](/reference/2026-01-01/objects/organizationmembership)

[`OtherIdNumber.organization`](/reference/2026-01-01/objects/otheridnumber)

[`PdfLetterheadTemplate.organization`](/reference/2026-01-01/objects/pdfletterheadtemplate)

[`ProviderAcceptedInsurancePlanType.organization`](/reference/2026-01-01/objects/provideracceptedinsuranceplantype)

[`UpdateUiConfigurationPayload.organization`](/reference/2026-01-01/objects/updateuiconfigurationpayload)

[`User.organization`](/reference/2026-01-01/objects/user)

[`createCarePlanRecommendationCategoryPayload.organization`](/reference/2026-01-01/objects/createcareplanrecommendationcategorypayload)

[`createOrganizationPayload.organization`](/reference/2026-01-01/objects/createorganizationpayload)

[`createPdfLetterheadTemplatePayload.organization`](/reference/2026-01-01/objects/createpdfletterheadtemplatepayload)

[`deleteCarePlanRecommendationCategoryPayload.organization`](/reference/2026-01-01/objects/deletecareplanrecommendationcategorypayload)

[`destroyPdfLetterheadTemplatePayload.organization`](/reference/2026-01-01/objects/destroypdfletterheadtemplatepayload)

[`resetDefaultPdfLetterheadTemplatePayload.organization`](/reference/2026-01-01/objects/resetdefaultpdfletterheadtemplatepayload)

[`setDefaultPdfLetterheadTemplatePayload.organization`](/reference/2026-01-01/objects/setdefaultpdfletterheadtemplatepayload)

[`updateCarePlanRecommendationCategoryPayload.organization`](/reference/2026-01-01/objects/updatecareplanrecommendationcategorypayload)

[`updateOrganizationPayload.organization`](/reference/2026-01-01/objects/updateorganizationpayload)

[`updatePdfLetterheadTemplatePayload.organization`](/reference/2026-01-01/objects/updatepdfletterheadtemplatepayload)

[`Query.organization`](/reference/2026-01-01/queries/organization)

## Definition

```
"""
An organization, that is an umbrella group for multiple providers
"""
type Organization {
  """
  The insurance plans the organization accepts, sorted by payer name ascending.
  """
  accepted_insurance_plans(
    """
    Search insurance plans by payer name or ID
    """
    keywords: String


    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): AcceptedInsurancePlanConnection


  """
  The active potential care team members of the organization
  """
  active_care_team_members(
    """
    The list of IDs of interested providers
    """
    provider_ids: [ID]


    """
    Filters the provider list to only include users who have ALL of the specified tags applied. Ignored if org_level is not true
    """
    tag_ids: [ID]


    """
    An array of provider record identifiers. When passed in, only providers with these matching record identifiers are returned.
    """
    record_identifiers: [String]
    state_licenses: [String]


    """
    Filter providers by the selected insurance plan
    """
    selected_insurance_plan_id: ID
    order_by: ActiveCareTeamMemberOrderKeys
  ): [User!]


  """
  The active users of the organization used for starting new conversations
  """
  active_members_for_conversation(
    exclude_sub_org_members: Boolean = false
    keywords: String = null
  ): [User!]


  """
  Returns organization appointment locations
  """
  appointment_locations: [AppointmentLocation!]


  """
  The automated insurance billing settings for the organization
  """
  automated_insurance_billing_setting: AutomatedInsuranceBillingSetting


  """
  Billing configuration settings for this organization
  """
  billing_configuration: BillingConfiguration


  """
  Can have suborgs for this org
  """
  can_have_suborgs: Boolean


  """
  When true, the organization can link lab orders to chart notes
  """
  can_link_labs_to_chart_notes: Boolean


  """
  Whether the organization can link E-Rx prescriptions to chart notes
  """
  can_link_prescriptions_to_chart_notes: Boolean


  """
  Returns general cancellation reasons
  """
  cancellation_reasons(
    """
    Filter by reason type. Defaults to client for backwards compatibility. Use all to return all types.
    """
    reason_type: CancellationReasonTypeEnum = client
  ): [CancellationReason!]!


  """
  Fetch paginated Care Plan Recommendation Categories collection
  """
  care_plan_recommendation_categories(
    """
    When true, only return active categories
    """
    active: Boolean = false


    """
    (Deprecated in favor of `active`)
    """
    only_active: Boolean = false
  ): [CarePlanRecommendationCategory!]!


  """
  The creation date of the organization
  """
  created_at: ISO8601DateTime!


  """
  The default `PdfLetterheadTemplate` for this organization
  """
  default_pdf_letterhead_template: PdfLetterheadTemplate


  """
  If enabled for organization, settings for E-Labs
  """
  e_labs_settings: ELabsSettings


  """
  The unique identifier of the organization
  """
  id: ID!


  """
  Returns the first 20 distinct insurance plans used by providers in an organization, filtered by payer name if provided (considered public)
  """
  insurance_plans_used_by_organization_providers(
    keywords: String
  ): [InsurancePlan!]!


  """
  Whether the organization is active. Inactive orgs are blocked from adding clients or creating appointments.
  """
  is_active: Boolean!


  """
  The system default PDF Letterhead Template is used if true
  """
  is_using_system_default_pdf_letterhead_template: Boolean


  """
  The location of the organization
  """
  location: Location


  """
  The name of the organization
  """
  name: String


  """
  The NPI of the organization
  """
  npi: String


  """
  The number of users in the organization
  """
  num_users: Int


  """
  The ID of the onboarding flow for org providers
  """
  onboarding_flow_id: String


  """
  The active organization memberships of the organization
  """
  only_active_organization_memberships: [OrganizationMembership!]


  """
  The active providers of the organization
  """
  only_active_providers(
    """
    If false return only active providers of current org
    """
    include_suborg_providers: Boolean


    """
    Customize IDs of interested providers
    """
    provider_ids: [ID]
  ): [User!]


  """
  The number of active providers of the organization
  """
  only_active_providers_count(
    """
    Customize IDs of interested providers
    """
    provider_ids: [ID]
  ): Int


  """
  The active standard users of the organization
  """
  only_active_standard: [User!]


  """
  The number of active standard user of the organization
  """
  only_active_standard_count: Int


  """
  The active support users of the organization
  """
  only_active_support: [User!]


  """
  The number of active support user of the organization
  """
  only_active_support_count: Int


  """
  Potential Organization Roles for this Organization
  """
  org_roles: [String!]


  """
  Returns organization cpt codes
  """
  organization_cpt_codes: [OrganizationCptCodeType!]


  """
  The email of organization
  """
  organization_email: String!


  """
  The first organization info of the organization
  """
  organization_info: OrganizationInfo


  """
  The organization infos of the organization
  """
  organization_infos(
    id: ID
    keywords: String


    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): OrganizationInfoPaginationConnection


  """
  The organization memberships of the organization
  """
  organization_memberships(
    """
    If set, return only memberships with active/inactive users
    """
    active: Boolean


    """
    Org IDs to exclude from results
    """
    exclude_org_ids: [ID!] = []
    keywords: String
    use_filters: Boolean = false


    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): OrganizationMembershipPaginationConnection


  """
  The other id
  """
  other_id: String


  """
  The other ID qualifier (what type of ID it is)
  """
  other_id_qual: String


  """
  The owner of the organization
  """
  owner: User


  """
  The ID of the org owner
  """
  owner_id: ID


  """
  The owner of the org's subscription
  """
  owner_subscription: SubscriptionInstance


  """
  The users associated with the organization
  """
  paginated_users(
    keywords: String


    """
    Filter by exact email (case-insensitive)
    """
    email: String


    """
    Options are one of [active, archived]
    """
    active_status: String


    """
    Whether to include users in suborganizations
    """
    include_suborgs: Boolean = false


    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): UserConnection


  """
  Parent organization for this org
  """
  parent_organization: Organization


  """
  ID of the parent organization
  """
  parent_organization_id: ID


  """
  Whether the organization has the payout accounts feature enabled
  """
  payout_accounts_enabled: Boolean!


  """
  The list of available `PdfLetterheadTemplate`s
  """
  pdf_letterhead_templates: [PdfLetterheadTemplate!]


  """
  Permission templates for this org
  """
  permission_templates: [PermissionTemplateType!]


  """
  The phone number of the organization
  """
  phone_number: String


  """
  Distinct insurance plans used by providers in an organization, filtered by payer name if provided (considered public). Uses cursor-based pagination (connections).
  """
  provider_insurance_plans(
    keywords: String


    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): InsurancePlanPaginationConnection!


  """
  The providers of the organization
  """
  providers(
    keywords: String


    """
    Provider IDs to exclude from results
    """
    exclude_ids: [ID!] = []


    """
    Options are one of [active, archived]
    """
    active_status: String


    """
    Two letter state abbreviation (e.g. "CA", "NY")
    """
    licensed_in_state: String
    provider_ids: [ID] = []
    with_private_notes_for_id: ID


    """
    When passed in, only providers with at least ONE of the passed-in tags will be returned.
    """
    with_tag_ids: [ID]


    """
    If false return only active providers of current org
    """
    include_suborg_providers: Boolean
    order_by: UserOrderKeys


    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): UserConnection


  """
  Require patients to upload their insurance card via the Insurance Form
  """
  require_insurance_card_upload: Boolean


  """
  The number of users in the organization connected their rupa health account
  """
  rupa_health_members: [User!]


  """
  Returns organization state licenses
  """
  state_licenses: [String!]


  """
  Suborganizations for this org
  """
  suborganizations: [Organization!]


  """
  Returns organization tags
  """
  tags: [Tag!]


  """
  Tax ID of organization
  """
  tax_id: String


  """
  The tax is of the organization
  """
  tax_id_type: String


  """
  User groups that are in the organization
  """
  user_groups: [UserGroup!]


  """
  The users of the organization
  """
  users(
    """
    Options are one of [active, archived]
    """
    active_status: String
    keywords: String
    show_all_by_default: Boolean = false
  ): [User!]


  """
  Builder ID for the Zus token
  """
  zus_builder_id: String
}
```
