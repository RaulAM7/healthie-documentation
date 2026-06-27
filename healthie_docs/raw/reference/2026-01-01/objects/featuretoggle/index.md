---
title: FeatureToggle | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/featuretoggle/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/featuretoggle/index.md
---

An object containing details about what the client can and can't do

## Fields

[`activity_level` ](#field-activity-level)· [`String` ](/reference/2026-01-01/scalars/string)· Activity level of the user

[`allow_apple_health_sync` ](#field-allow-apple-health-sync)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow clients to sync with Apple Health

[`allow_clearstep_sync` ](#field-allow-clearstep-sync)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow clients to sync with Clearstep

[`allow_community_chat` ](#field-allow-community-chat)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow send messages to community chat

[`allow_dexcom_sync` ](#field-allow-dexcom-sync)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Allow clients to sync with Dexcom

[`allow_direct_chat` ](#field-allow-direct-chat)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow send messages to direct chat

[`allow_fitbit_sync` ](#field-allow-fitbit-sync)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow clients to sync with Fitbit

[`allow_google_fit_sync` ](#field-allow-google-fit-sync)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow clients to sync with Google Fit

[`allow_google_health_connect_sync` ](#field-allow-google-health-connect-sync)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow clients to sync with Google Health Connect

[`allow_shapa_sync` ](#field-allow-shapa-sync)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow clients to sync with Shapa

[`allow_withings_sync` ](#field-allow-withings-sync)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Allow clients to sync with Withings

[`apply_eating_disorder_default` ](#field-apply-eating-disorder-default)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · whether or not the eating disorder defaults are applied

[`can_schedule_appointments` ](#field-can-schedule-appointments)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view and schedule appointments

[`can_track_poop` ](#field-can-track-poop)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not clients can track poop in their journal entries

[`can_track_symptoms` ](#field-can-track-symptoms)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not the client can track symptoms

[`can_track_water_intake` ](#field-can-track-water-intake)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not clients can track water intake in their journal entries

[`can_view_care_plan` ](#field-can-view-care-plan)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view care plan

[`can_view_documents` ](#field-can-view-documents)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view and upload documents

[`can_view_forms` ](#field-can-view-forms)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view and complete intake forms

[`can_view_goals` ](#field-can-view-goals)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view and create goals

[`can_view_journal_entries` ](#field-can-view-journal-entries)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view and create journal entries

[`can_view_packages` ](#field-can-view-packages)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view and purchase packages

[`can_view_payments` ](#field-can-view-payments)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view and make payments

[`can_view_programs` ](#field-can-view-programs)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The status of whether the linked user can view and complete programs

[`care_plan` ](#field-care-plan)· [`CarePlan` ](/reference/2026-01-01/objects/careplan)· The care plan associated with this feature toggle

[`care_plan_id` ](#field-care-plan-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the care plan associated with this feature toggle

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time the entry was done

[`custom_metrics` ](#field-custom-metrics)· [`[CustomMetric!]` ](/reference/2026-01-01/objects/custommetric)· Custom Metrics for this toggle

[`date_range_preference` ](#field-date-range-preference)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Default date range selector when provider opens date picker in metrics tab

[`default_water_intake` ](#field-default-water-intake)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Default water intake set by provider

[`do_not_auto_submit_cms1500` ](#field-do-not-auto-submit-cms1500)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, it will not auto submit the CMS1500 to the clearing house

[`email_notification_frequency` ](#field-email-notification-frequency)· [`String` ](/reference/2026-01-01/scalars/string)· The frequency with which clients get email notifications about their goals

[`food_categories` ](#field-food-categories)· [`[String!]!` ](/reference/2026-01-01/scalars/string)· required · Food categories

[`has_any_entry_types` ](#field-has-any-entry-types)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, user has at least one entry type to track

[`has_ccda` ](#field-has-ccda)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· CCDA is available if true

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the feature toggle

[`initial_custom_metric_overrides` ](#field-initial-custom-metric-overrides)· [`[CustomMetricOverride!]` ](/reference/2026-01-01/objects/custommetricoverride)· Food categories

[`last_journal_date_range_preference` ](#field-last-journal-date-range-preference)· [`String` ](/reference/2026-01-01/scalars/string)· Default date range when provider opens date picker in journal tab

[`last_journal_from_date` ](#field-last-journal-from-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Default from\_date when provider opens date picker in journal tab

[`last_journal_to_date` ](#field-last-journal-to-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Default to\_date when provider opens date picker in journal tab

[`line_graph_metric_categories` ](#field-line-graph-metric-categories)· [`[String]` ](/reference/2026-01-01/scalars/string)· Metric Graphs to show in line graph form

[`line_graph_sleep_categories` ](#field-line-graph-sleep-categories)· [`[String]` ](/reference/2026-01-01/scalars/string)· Sleep Graphs to show in line graph form

[`metric_categories` ](#field-metric-categories)· [`[String!]!` ](/reference/2026-01-01/scalars/string)· required · Metric categories based on users toggle features

[`metric_category_objects` ](#field-metric-category-objects)· [`[CustomMetric!]` ](/reference/2026-01-01/objects/custommetric)· Metric category objects (including defaults) based on users toggle features

[`mirror_categories` ](#field-mirror-categories)· [`[String!]!` ](/reference/2026-01-01/scalars/string)· required · Mirror categories

[`prevent_inactive_access` ](#field-prevent-inactive-access)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, locks inactive clients from login and outbound emails

[`push_notification_frequency` ](#field-push-notification-frequency)· [`String` ](/reference/2026-01-01/scalars/string)· The frequency with which clients get push notifications about their goals

[`returned_custom_metrics` ](#field-returned-custom-metrics)· [`[String!]!` ](/reference/2026-01-01/scalars/string)· required · Metrics that should be on for this feature toggle

[`send_unpaid_invoice_reminder` ](#field-send-unpaid-invoice-reminder)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send unpaid invoice reminder

[`separate_provider_metric_from_client` ](#field-separate-provider-metric-from-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether entries on graphs are separated by the poster

[`seperate_provider_metric_from_client` ](#field-seperate-provider-metric-from-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether entries on graphs are separated by the poster

deprecated

Use \`separate\_provider\_metric\_from\_client\` instead

[`show_a1c_metric` ](#field-show-a1c-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the A1C of the client

[`show_bf_percent_metric` ](#field-show-bf-percent-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can view and track the client's body fat percentage

[`show_blood_pressure_metric` ](#field-show-blood-pressure-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can view and track the client's blood pressure

[`show_blood_sugar_metric` ](#field-show-blood-sugar-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the blood sugar metrics of the client

[`show_bmi_graph` ](#field-show-bmi-graph)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the calculated BMI of the client

[`show_bmi_growth_chart` ](#field-show-bmi-growth-chart)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the bmi-growth chart of the client

[`show_bmr_metric` ](#field-show-bmr-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the calculated BMR (using MFJ) of the client

[`show_body_temperature_metric` ](#field-show-body-temperature-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the body temperature entries of the client

[`show_client_a1c_metric` ](#field-show-client-a1c-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see A1C metrics of the client

[`show_client_bf_percent_metric` ](#field-show-client-bf-percent-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can view and track the client's body fat percentage

[`show_client_blood_pressure_metric` ](#field-show-client-blood-pressure-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can view and track the client's blood pressure

[`show_client_blood_sugar_metric` ](#field-show-client-blood-sugar-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see the blood sugar metrics of the client

[`show_client_bmi_graph` ](#field-show-client-bmi-graph)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see the calculated BMI of the client

[`show_client_bmi_growth_chart` ](#field-show-client-bmi-growth-chart)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see the bmi-growth chart of the client

[`show_client_bmr_metric` ](#field-show-client-bmr-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see the calculated BMR (using MFJ) of the client

[`show_client_body_temperature_metric` ](#field-show-client-body-temperature-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see the body temperature entries of the client

[`show_client_harris_benedict` ](#field-show-client-harris-benedict)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see the calculated BMR (using HB) of the client

[`show_client_height_graph` ](#field-show-client-height-graph)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can view and track the client's height

[`show_client_height_growth_chart` ](#field-show-client-height-growth-chart)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see the height-growth chart of the client

[`show_client_ox_sat_metric` ](#field-show-client-ox-sat-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see oxygen saturation metrics of the client

[`show_client_waist_circumference_metric` ](#field-show-client-waist-circumference-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can view and track the client's waist circumference

[`show_client_weight_growth_chart` ](#field-show-client-weight-growth-chart)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can see the weight-growth chart of the client

[`show_client_weight_metric` ](#field-show-client-weight-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can view and track the client's weight

[`show_ed_posthunger` ](#field-show-ed-posthunger)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client is asked to track expanded (1-10) postmeal hunger level

[`show_ed_prehunger` ](#field-show-ed-prehunger)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client is asked to track expanded (1-10) premeal hunger level

[`show_food` ](#field-show-food)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can post food entries

[`show_food_category` ](#field-show-food-category)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client is asked to track the category (meal or snack) of the food

[`show_food_emotion` ](#field-show-food-emotion)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client is asked to track (1-10) emotion towards the food

[`show_food_reflection` ](#field-show-food-reflection)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client is asked to post a (text) reflection towards the food

[`show_harris_benedict` ](#field-show-harris-benedict)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the calculated BMR (using HB) of the client

[`show_healthiness` ](#field-show-healthiness)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client is asked to track perceived healthiness

[`show_height_graph` ](#field-show-height-graph)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the height graph of the client

[`show_height_growth_chart` ](#field-show-height-growth-chart)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the height-growth chart of the client

[`show_metric` ](#field-show-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can post metric entries

[`show_mirror` ](#field-show-mirror)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can post selfie entries

[`show_normal_hunger` ](#field-show-normal-hunger)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client is asked to track normal (1-3) hunger level

[`show_note` ](#field-show-note)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can post note entries

[`show_note_emotion` ](#field-show-note-emotion)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client is asked to track (1-10) emotion towards the note

[`show_nutrients_tracking` ](#field-show-nutrients-tracking)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can include macro and micro nutrients for the food they track

[`show_ox_sat_metric` ](#field-show-ox-sat-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the oxygen saturation of the client

[`show_sleep` ](#field-show-sleep)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can post sleep entries

[`show_waist_circumference_metric` ](#field-show-waist-circumference-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can view and track the client's waist circumference

[`show_weight_growth_chart` ](#field-show-weight-growth-chart)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can see the weight-growth chart of the client

[`show_weight_metric` ](#field-show-weight-metric)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the provider can view and track the client's weight

[`show_workout` ](#field-show-workout)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client can post workout entries

[`symptom_options` ](#field-symptom-options)· [`[SymptomOption!]!` ](/reference/2026-01-01/objects/symptomoption)· required · Symptom options for symptom entry type

[`use_metric_system` ](#field-use-metric-system)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the client uses the metric system (versus imperial)

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Associated user

[`user_group` ](#field-user-group)· [`UserGroup` ](/reference/2026-01-01/objects/usergroup)· The user group associated with this feature toggle

[`user_group_id` ](#field-user-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The user group associated with this feature toggle

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The user associated with this feature toggle

[`uses_feature_toggle_from_care_plan` ](#field-uses-feature-toggle-from-care-plan)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user has active\_care\_plan

[`view_medications` ](#field-view-medications)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the client can view medications and prescriptions

[`view_not_track` ](#field-view-not-track)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When enabled, let's providers choose to have metrics that clients can view, but not enter

[`workout_categories` ](#field-workout-categories)· [`[String!]!` ](/reference/2026-01-01/scalars/string)· required · Workout categories

## Used By

[`CarePlan.feature_toggle`](/reference/2026-01-01/objects/careplan)

[`User.feature_toggle`](/reference/2026-01-01/objects/user)

[`createFeatureTogglePayload.feature_toggle`](/reference/2026-01-01/objects/createfeaturetogglepayload)

[`updateFeatureTogglePayload.feature_toggle`](/reference/2026-01-01/objects/updatefeaturetogglepayload)

[`Query.featureToggle`](/reference/2026-01-01/queries/featuretoggle)

[`Query.featureToggleForEditing`](/reference/2026-01-01/queries/featuretoggleforediting)

## Definition

```
"""
An object containing details about what the client can and can't do
"""
type FeatureToggle {
  """
  Activity level of the user
  """
  activity_level: String


  """
  Allow clients to sync with Apple Health
  """
  allow_apple_health_sync: Boolean!


  """
  Allow clients to sync with Clearstep
  """
  allow_clearstep_sync: Boolean!


  """
  Allow send messages to community chat
  """
  allow_community_chat: Boolean!


  """
  Allow clients to sync with Dexcom
  """
  allow_dexcom_sync: Boolean


  """
  Allow send messages to direct chat
  """
  allow_direct_chat: Boolean!


  """
  Allow clients to sync with Fitbit
  """
  allow_fitbit_sync: Boolean!


  """
  Allow clients to sync with Google Fit
  """
  allow_google_fit_sync: Boolean!


  """
  Allow clients to sync with Google Health Connect
  """
  allow_google_health_connect_sync: Boolean!


  """
  Allow clients to sync with Shapa
  """
  allow_shapa_sync: Boolean!


  """
  Allow clients to sync with Withings
  """
  allow_withings_sync: Boolean!


  """
  whether or not the eating disorder defaults are applied
  """
  apply_eating_disorder_default: Boolean!


  """
  The status of whether the linked user can view and schedule appointments
  """
  can_schedule_appointments: Boolean!


  """
  Whether or not clients can track poop in their journal entries
  """
  can_track_poop: Boolean!


  """
  Whether or not the client can track symptoms
  """
  can_track_symptoms: Boolean!


  """
  Whether or not clients can track water intake in their journal entries
  """
  can_track_water_intake: Boolean!


  """
  The status of whether the linked user can view care plan
  """
  can_view_care_plan: Boolean!


  """
  The status of whether the linked user can view and upload documents
  """
  can_view_documents: Boolean!


  """
  The status of whether the linked user can view and complete intake forms
  """
  can_view_forms: Boolean!


  """
  The status of whether the linked user can view and create goals
  """
  can_view_goals: Boolean!


  """
  The status of whether the linked user can view and create journal entries
  """
  can_view_journal_entries: Boolean!


  """
  The status of whether the linked user can view and purchase packages
  """
  can_view_packages: Boolean!


  """
  The status of whether the linked user can view and make payments
  """
  can_view_payments: Boolean!


  """
  The status of whether the linked user can view and complete programs
  """
  can_view_programs: Boolean!


  """
  The care plan associated with this feature toggle
  """
  care_plan: CarePlan


  """
  The id of the care plan associated with this feature toggle
  """
  care_plan_id: ID


  """
  The date and time the entry was done
  """
  created_at: ISO8601DateTime!


  """
  Custom Metrics for this toggle
  """
  custom_metrics: [CustomMetric!]


  """
  Default date range selector when provider opens date picker in metrics tab
  """
  date_range_preference: String!


  """
  Default water intake set by provider
  """
  default_water_intake: String!


  """
  When true, it will not auto submit the CMS1500 to the clearing house
  """
  do_not_auto_submit_cms1500: Boolean!


  """
  The frequency with which clients get email notifications about their goals
  """
  email_notification_frequency: String


  """
  Food categories
  """
  food_categories: [String!]!


  """
  If true, user has at least one entry type to track
  """
  has_any_entry_types: Boolean


  """
  CCDA is available if true
  """
  has_ccda: Boolean


  """
  The unique identifier of the feature toggle
  """
  id: ID


  """
  Food categories
  """
  initial_custom_metric_overrides: [CustomMetricOverride!]


  """
  Default date range when provider opens date picker in journal tab
  """
  last_journal_date_range_preference: String


  """
  Default from_date when provider opens date picker in journal tab
  """
  last_journal_from_date: ISO8601Date


  """
  Default to_date when provider opens date picker in journal tab
  """
  last_journal_to_date: ISO8601Date


  """
  Metric Graphs to show in line graph form
  """
  line_graph_metric_categories(
    """
    The id of the user to get the line graph metric categories for
    """
    user_id: ID
  ): [String]


  """
  Sleep Graphs to show in line graph form
  """
  line_graph_sleep_categories(
    """
    The id of the user to get the line graph sleep categories for
    """
    user_id: ID
  ): [String]


  """
  Metric categories based on users toggle features
  """
  metric_categories(
    """
    The id of the user to get the metric categories for
    """
    user_id: ID
  ): [String!]!


  """
  Metric category objects (including defaults) based on users toggle features
  """
  metric_category_objects(
    """
    Self-descriptive
    """
    user_id: ID
  ): [CustomMetric!]


  """
  Mirror categories
  """
  mirror_categories: [String!]!


  """
  When true, locks inactive clients from login and outbound emails
  """
  prevent_inactive_access: Boolean!


  """
  The frequency with which clients get push notifications about their goals
  """
  push_notification_frequency: String


  """
  Metrics that should be on for this feature toggle
  """
  returned_custom_metrics: [String!]!


  """
  Send unpaid invoice reminder
  """
  send_unpaid_invoice_reminder: Boolean


  """
  The status of whether entries on graphs are separated by the poster
  """
  separate_provider_metric_from_client: Boolean


  """
  The status of whether entries on graphs are separated by the poster
  """
  seperate_provider_metric_from_client: Boolean
    @deprecated(reason: "Use `separate_provider_metric_from_client` instead")


  """
  The status of whether the provider can see the A1C of the client
  """
  show_a1c_metric: Boolean


  """
  The status of whether the provider can view and track the client's body fat percentage
  """
  show_bf_percent_metric: Boolean


  """
  The status of whether the provider can view and track the client's blood pressure
  """
  show_blood_pressure_metric: Boolean


  """
  The status of whether the provider can see the blood sugar metrics of the client
  """
  show_blood_sugar_metric: Boolean


  """
  The status of whether the provider can see the calculated BMI of the client
  """
  show_bmi_graph: Boolean


  """
  The status of whether the provider can see the bmi-growth chart of the client
  """
  show_bmi_growth_chart: Boolean


  """
  The status of whether the provider can see the calculated BMR (using MFJ) of the client
  """
  show_bmr_metric: Boolean


  """
  The status of whether the provider can see the body temperature entries of the client
  """
  show_body_temperature_metric: Boolean


  """
  The status of whether the client can see A1C metrics of the client
  """
  show_client_a1c_metric: Boolean


  """
  The status of whether the client can view and track the client's body fat percentage
  """
  show_client_bf_percent_metric: Boolean


  """
  The status of whether the client can view and track the client's blood pressure
  """
  show_client_blood_pressure_metric: Boolean


  """
  The status of whether the client can see the blood sugar metrics of the client
  """
  show_client_blood_sugar_metric: Boolean


  """
  The status of whether the client can see the calculated BMI of the client
  """
  show_client_bmi_graph: Boolean


  """
  The status of whether the client can see the bmi-growth chart of the client
  """
  show_client_bmi_growth_chart: Boolean


  """
  The status of whether the client can see the calculated BMR (using MFJ) of the client
  """
  show_client_bmr_metric: Boolean


  """
  The status of whether the client can see the body temperature entries of the client
  """
  show_client_body_temperature_metric: Boolean


  """
  The status of whether the client can see the calculated BMR (using HB) of the client
  """
  show_client_harris_benedict: Boolean


  """
  The status of whether the client can view and track the client's height
  """
  show_client_height_graph: Boolean


  """
  The status of whether the client can see the height-growth chart of the client
  """
  show_client_height_growth_chart: Boolean


  """
  The status of whether the client can see oxygen saturation metrics of the client
  """
  show_client_ox_sat_metric: Boolean


  """
  The status of whether the client can view and track the client's waist circumference
  """
  show_client_waist_circumference_metric: Boolean


  """
  The status of whether the client can see the weight-growth chart of the client
  """
  show_client_weight_growth_chart: Boolean


  """
  The status of whether the client can view and track the client's weight
  """
  show_client_weight_metric: Boolean


  """
  The status of whether the client is asked to track expanded (1-10) postmeal hunger level
  """
  show_ed_posthunger: Boolean


  """
  The status of whether the client is asked to track expanded (1-10) premeal hunger level
  """
  show_ed_prehunger: Boolean


  """
  The status of whether the client can post food entries
  """
  show_food: Boolean


  """
  The status of whether the client is asked to track the category (meal or snack) of the food
  """
  show_food_category: Boolean


  """
  The status of whether the client is asked to track (1-10) emotion towards the food
  """
  show_food_emotion: Boolean


  """
  The status of whether the client is asked to post a (text) reflection towards the food
  """
  show_food_reflection: Boolean


  """
  The status of whether the provider can see the calculated BMR (using HB) of the client
  """
  show_harris_benedict: Boolean


  """
  The status of whether the client is asked to track perceived healthiness
  """
  show_healthiness: Boolean


  """
  The status of whether the provider can see the height graph of the client
  """
  show_height_graph: Boolean


  """
  The status of whether the provider can see the height-growth chart of the client
  """
  show_height_growth_chart: Boolean


  """
  The status of whether the client can post metric entries
  """
  show_metric: Boolean


  """
  The status of whether the client can post selfie entries
  """
  show_mirror: Boolean


  """
  The status of whether the client is asked to track normal (1-3) hunger level
  """
  show_normal_hunger: Boolean


  """
  The status of whether the client can post note entries
  """
  show_note: Boolean


  """
  The status of whether the client is asked to track (1-10) emotion towards the note
  """
  show_note_emotion: Boolean


  """
  The status of whether the client can include macro and micro nutrients for the food they track
  """
  show_nutrients_tracking: Boolean


  """
  The status of whether the provider can see the oxygen saturation of the client
  """
  show_ox_sat_metric: Boolean


  """
  The status of whether the client can post sleep entries
  """
  show_sleep: Boolean


  """
  The status of whether the provider can view and track the client's waist circumference
  """
  show_waist_circumference_metric: Boolean


  """
  The status of whether the provider can see the weight-growth chart of the client
  """
  show_weight_growth_chart: Boolean


  """
  The status of whether the provider can view and track the client's weight
  """
  show_weight_metric: Boolean


  """
  The status of whether the client can post workout entries
  """
  show_workout: Boolean


  """
  Symptom options for symptom entry type
  """
  symptom_options: [SymptomOption!]!


  """
  The status of whether the client uses the metric system (versus imperial)
  """
  use_metric_system: Boolean


  """
  Associated user
  """
  user: User


  """
  The user group associated with this feature toggle
  """
  user_group: UserGroup


  """
  The user group associated with this feature toggle
  """
  user_group_id: ID


  """
  The user associated with this feature toggle
  """
  user_id: ID


  """
  If true, the user has active_care_plan
  """
  uses_feature_toggle_from_care_plan: Boolean


  """
  Whether the client can view medications and prescriptions
  """
  view_medications: Boolean


  """
  When enabled, let's providers choose to have metrics that clients can view, but not enter
  """
  view_not_track: Boolean


  """
  Workout categories
  """
  workout_categories: [String!]!
}
```
