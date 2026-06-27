---
title: entry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/entry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/entry/index.md
---

fetch an entry by id

## Arguments

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`type` ](#argument-type)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`Entry`](/reference/2026-01-01/objects/entry)

## Example

```
query entry($client_id: ID, $id: ID, $type: String) {
  entry(client_id: $client_id, id: $id, type: $type) {
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
