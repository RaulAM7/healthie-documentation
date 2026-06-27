---
title: BulkEntryInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/bulkentryinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/bulkentryinput/index.md
---

Payload for a new entry

## Fields

[`add_to_avg_heart_rate` ](#field-add-to-avg-heart-rate)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Check and either add to pre-existing average heart rate entry or create a new one

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of the entry

[`check_duplicates` ](#field-check-duplicates)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Check for duplicates, currently only supported if third\_party\_source is apple\_health

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time the entry was created

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the entry

[`ed_posthunger` ](#field-ed-posthunger)· [`String` ](/reference/2026-01-01/scalars/string)· ED Post Hunger

[`ed_prehunger` ](#field-ed-prehunger)· [`String` ](/reference/2026-01-01/scalars/string)· ED Pre Hunger

[`emotions` ](#field-emotions)· [`String` ](/reference/2026-01-01/scalars/string)· The comma separated list of emotions

[`entries_in_average` ](#field-entries-in-average)· [`String` ](/reference/2026-01-01/scalars/string)· If average of any type, value indicates amount of entries already included in average

[`external_id` ](#field-external-id)· [`String` ](/reference/2026-01-01/scalars/string)· Third party external ID associated with this entry

[`external_id_type` ](#field-external-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· Third party associated with the external ID on this entry. Option currently supported is 'AppleHealth'

[`image` ](#field-image)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The image associated with the entry

[`image_string` ](#field-image-string)· [`String` ](/reference/2026-01-01/scalars/string)· The base64 encoded image string

[`metric_stat` ](#field-metric-stat)· [`String` ](/reference/2026-01-01/scalars/string)· The statistic associated with the metric entry

[`notify_provider` ](#field-notify-provider)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, will trigger a notification to the provider based on the provider settings. If nil or false will trigger a notification to the provider if the poster is a patient.

[`percieved_hungriness` ](#field-percieved-hungriness)· [`String` ](/reference/2026-01-01/scalars/string)· The percieved hungriness

[`reflection` ](#field-reflection)· [`String` ](/reference/2026-01-01/scalars/string)· The reflection on the entry

[`subentries` ](#field-subentries)· [`[SubentryInput]` ](/reference/2026-01-01/input-objects/subentryinput)· The list of subentries associated with this entry

[`third_party_source` ](#field-third-party-source)· [`String` ](/reference/2026-01-01/scalars/string)· Options are apple\_health, google\_fit, or fitbit

[`type` ](#field-type)· [`String` ](/reference/2026-01-01/scalars/string)· One of MetricEntry, FoodEntry, WorkoutEntry, MirrorEntry, SleepEntry, NoteEntry, WaterIntakeEntry, PoopEntry, SymptomEntry

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user that created the entry

## Used By

[`bulkCreateEntriesInput.entries`](/reference/2026-01-01/input-objects/bulkcreateentriesinput)

## Definition

```
"""
Payload for a new entry
"""
input BulkEntryInput {
  """
  Check and either add to pre-existing average heart rate entry or create a new one
  """
  add_to_avg_heart_rate: Boolean


  """
  The category of the entry
  """
  category: String


  """
  Check for duplicates, currently only supported if third_party_source is apple_health
  """
  check_duplicates: Boolean


  """
  The time the entry was created
  """
  created_at: ISO8601DateTime


  """
  The description of the entry
  """
  description: String


  """
  ED Post Hunger
  """
  ed_posthunger: String


  """
  ED Pre Hunger
  """
  ed_prehunger: String


  """
  The comma separated list of emotions
  """
  emotions: String


  """
  If average of any type, value indicates amount of entries already included in average
  """
  entries_in_average: String


  """
  Third party external ID associated with this entry
  """
  external_id: String


  """
  Third party associated with the external ID on this entry. Option currently supported is 'AppleHealth'
  """
  external_id_type: String


  """
  The image associated with the entry
  """
  image: Upload


  """
  The base64 encoded image string
  """
  image_string: String


  """
  The statistic associated with the metric entry
  """
  metric_stat: String


  """
  If true, will trigger a notification to the provider based on the provider settings. If nil or false will trigger a notification to the provider if the poster is a patient.
  """
  notify_provider: Boolean


  """
  The percieved hungriness
  """
  percieved_hungriness: String


  """
  The reflection on the entry
  """
  reflection: String


  """
  The list of subentries associated with this entry
  """
  subentries: [SubentryInput]


  """
  Options are apple_health, google_fit, or fitbit
  """
  third_party_source: String


  """
  One of MetricEntry, FoodEntry, WorkoutEntry, MirrorEntry, SleepEntry, NoteEntry, WaterIntakeEntry, PoopEntry, SymptomEntry
  """
  type: String


  """
  The ID of the user that created the entry
  """
  user_id: String
}
```
