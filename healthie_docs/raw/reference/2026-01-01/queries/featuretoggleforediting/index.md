---
title: featureToggleForEditing | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/featuretoggleforediting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/featuretoggleforediting/index.md
---

fetch a featureToggle by id

## Arguments

[`care_plan_id` ](#argument-care-plan-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_group_id` ](#argument-user-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`FeatureToggle`](/reference/2026-01-01/objects/featuretoggle)

## Example

```
query featureToggleForEditing(
  $care_plan_id: ID
  $id: ID
  $user_group_id: ID
  $user_id: ID
) {
  featureToggleForEditing(
    care_plan_id: $care_plan_id
    id: $id
    user_group_id: $user_group_id
    user_id: $user_id
  ) {
    activity_level
    allow_apple_health_sync
    allow_clearstep_sync
    allow_community_chat
    allow_dexcom_sync
    allow_direct_chat
    allow_fitbit_sync
    allow_google_fit_sync
    allow_google_health_connect_sync
    allow_shapa_sync
    allow_withings_sync
    apply_eating_disorder_default
    can_schedule_appointments
    can_track_poop
    can_track_symptoms
    can_track_water_intake
    can_view_care_plan
    can_view_documents
    can_view_forms
    can_view_goals
    can_view_journal_entries
    can_view_packages
    can_view_payments
    can_view_programs
    care_plan
    care_plan_id
    created_at
    custom_metrics
    date_range_preference
    default_water_intake
    do_not_auto_submit_cms1500
    email_notification_frequency
    food_categories
    has_any_entry_types
    has_ccda
    id
    initial_custom_metric_overrides
    last_journal_date_range_preference
    last_journal_from_date
    last_journal_to_date
    line_graph_metric_categories
    line_graph_sleep_categories
    metric_categories
    metric_category_objects
    mirror_categories
    prevent_inactive_access
    push_notification_frequency
    returned_custom_metrics
    send_unpaid_invoice_reminder
    separate_provider_metric_from_client
    show_a1c_metric
    show_bf_percent_metric
    show_blood_pressure_metric
    show_blood_sugar_metric
    show_bmi_graph
    show_bmi_growth_chart
    show_bmr_metric
    show_body_temperature_metric
    show_client_a1c_metric
    show_client_bf_percent_metric
    show_client_blood_pressure_metric
    show_client_blood_sugar_metric
    show_client_bmi_graph
    show_client_bmi_growth_chart
    show_client_bmr_metric
    show_client_body_temperature_metric
    show_client_harris_benedict
    show_client_height_graph
    show_client_height_growth_chart
    show_client_ox_sat_metric
    show_client_waist_circumference_metric
    show_client_weight_growth_chart
    show_client_weight_metric
    show_ed_posthunger
    show_ed_prehunger
    show_food
    show_food_category
    show_food_emotion
    show_food_reflection
    show_harris_benedict
    show_healthiness
    show_height_graph
    show_height_growth_chart
    show_metric
    show_mirror
    show_normal_hunger
    show_note
    show_note_emotion
    show_nutrients_tracking
    show_ox_sat_metric
    show_sleep
    show_waist_circumference_metric
    show_weight_growth_chart
    show_weight_metric
    show_workout
    symptom_options
    use_metric_system
    user
    user_group
    user_group_id
    user_id
    uses_feature_toggle_from_care_plan
    view_medications
    view_not_track
    workout_categories
  }
}
```
