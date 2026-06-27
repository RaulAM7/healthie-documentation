---
title: waterIntakeEntry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/waterintakeentry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/waterintakeentry/index.md
---

## Arguments

[`created_at` ](#argument-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date entry was posted

[`entry_id` ](#argument-entry-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Entry to query daily intake total if present.

## Returns

[`Entry`](/reference/2026-01-01/objects/entry)

## Example

```
query waterIntakeEntry($created_at: ISO8601DateTime, $entry_id: ID) {
  waterIntakeEntry(created_at: $created_at, entry_id: $entry_id) {
    added_by_user
    added_by_user_id
    category
    comments
    created_at
    default_water_intake_for_entry_user
    description
    ed_posthunger
    ed_posthunger_string
    ed_prehunger
    ed_prehunger_string
    emotions
    emotions_string
    entries_in_average
    external_id
    external_id_type
    has_subentries
    healthiness_info_hex_value
    hide_from_main_feed
    id
    image
    image_url
    linked_to_autoscored_form
    meals
    metric_stat
    metric_stat_string
    name
    other_symptom
    percieved_hungriness
    poster
    previous_water_intake_stat
    record_created_at
    reflection
    source
    subentries
    symptom_names
    symptoms
    third_party_source
    type
    updated_at
    viewed
  }
}
```
