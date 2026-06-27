---
title: Entry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/entry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/entry/index.md
---

A post about a client, with different category options

## Fields

[`added_by_user` ](#field-added-by-user)· [`User` ](/reference/2026-01-01/objects/user)· User who added the entry

[`added_by_user_id` ](#field-added-by-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· the user who actually put in the entry (not always the user who the entry is about)

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of this entry

[`comments` ](#field-comments)· [`[Comment!]!` ](/reference/2026-01-01/objects/comment)· required · All comments association with this entry.

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time at which this entry was created

[`default_water_intake_for_entry_user` ](#field-default-water-intake-for-entry-user)· [`Int` ](/reference/2026-01-01/scalars/int)· Default water intake for this entry user

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description for the entry

[`ed_posthunger` ](#field-ed-posthunger)· [`String` ](/reference/2026-01-01/scalars/string)· A more granular 1-10 scale of how hungry the user thought they were after eating

[`ed_posthunger_string` ](#field-ed-posthunger-string)· [`String` ](/reference/2026-01-01/scalars/string)· A more granular 1-10 scale of how hungry the user thought they were after eating

[`ed_prehunger` ](#field-ed-prehunger)· [`String` ](/reference/2026-01-01/scalars/string)· A more granular 1-10 scale of how hungry the user thought they were before eating

[`ed_prehunger_string` ](#field-ed-prehunger-string)· [`String` ](/reference/2026-01-01/scalars/string)· A more granular 1-10 scale of how hungry the user thought they were before eating

[`emotions` ](#field-emotions)· [`String` ](/reference/2026-01-01/scalars/string)· The users emotions towards the meal as a numerical value

[`emotions_string` ](#field-emotions-string)· [`String` ](/reference/2026-01-01/scalars/string)· A descriptive string of the users emotions towards the meal based on the emotions value. Comes from the mapping: \['Stressed', 1], \['Anxious', 2], \['Tired', 3], \['Bored', 4], \['Confident', 5], \['Happy', 6], \['Sad', 7 or 0], \['Angry', 8]

[`entries_in_average` ](#field-entries-in-average)· [`Int` ](/reference/2026-01-01/scalars/int)· If average of any type, value indicates amount of entries already included in average calculation

[`external_id` ](#field-external-id)· [`String` ](/reference/2026-01-01/scalars/string)· Third party external ID associated with this entry

[`external_id_type` ](#field-external-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· Third party associated with the external ID on this entry. One option currently supported is 'AppleHealth'

[`has_subentries` ](#field-has-subentries)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the entry has subentries

[`healthiness_info_hex_value` ](#field-healthiness-info-hex-value)· [`String` ](/reference/2026-01-01/scalars/string)· A hexadecimal value corresponding to the metric stat of a food entry

[`hide_from_main_feed` ](#field-hide-from-main-feed)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · A boolean to check if the entry should be hidden from the main client feed

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the entry

[`image` ](#field-image)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The associated image of the entry

[`image_url` ](#field-image-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL of the entry's associated image

[`linked_to_autoscored_form` ](#field-linked-to-autoscored-form)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the custom metric is linked to an auto-scored form template

[`meals` ](#field-meals)· [`[Meal!]` ](/reference/2026-01-01/objects/meal)· Meal entries of FoodEntry

[`metric_stat` ](#field-metric-stat)· [`Float` ](/reference/2026-01-01/scalars/float)· The value of the metric for the entry

[`metric_stat_string` ](#field-metric-stat-string)· [`String` ](/reference/2026-01-01/scalars/string)· Metric stat as a string

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name for this entry

[`other_symptom` ](#field-other-symptom)· [`String` ](/reference/2026-01-01/scalars/string)· Other symptom typed by the client

[`percieved_hungriness` ](#field-percieved-hungriness)· [`Float` ](/reference/2026-01-01/scalars/float)· How hungry the poster thinks they were before eating

[`poster` ](#field-poster)· [`User` ](/reference/2026-01-01/objects/user)· User who the entry is about

[`previous_water_intake_stat` ](#field-previous-water-intake-stat)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · The water intake previously added

[`record_created_at` ](#field-record-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time at which this entry was created. Cannot be updated

[`reflection` ](#field-reflection)· [`String` ](/reference/2026-01-01/scalars/string)· The user's free-text reflection or notes about the meal

[`source` ](#field-source)· [`String` ](/reference/2026-01-01/scalars/string)· A name of third party source or full name of user who have created the entry

[`subentries` ](#field-subentries)· [`[Entry!]` ](/reference/2026-01-01/objects/entry)· subentries of the Entry

[`symptom_names` ](#field-symptom-names)· [`String` ](/reference/2026-01-01/scalars/string)· Comma-separated list of symptom names

[`symptoms` ](#field-symptoms)· [`String` ](/reference/2026-01-01/scalars/string)· Comma-separated list of symptom IDs selected by the client for this entry

[`third_party_source` ](#field-third-party-source)· [`String` ](/reference/2026-01-01/scalars/string)· A name of third party source which actually created the entry

[`type` ](#field-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type for this entry, options are - FoodEntry, WorkoutEntry, MirrorEntry, SleepEntry, NoteEntry, WaterIntakeEntry, PoopEntry', null: false

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The last date and time that the entry was updated

[`viewed` ](#field-viewed)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · A check to see if the entry has been viewed or not

## Used By

[`Entry.subentries`](/reference/2026-01-01/objects/entry)

[`EntryEdge.node`](/reference/2026-01-01/objects/entryedge)

[`EntryPaginationConnection.nodes`](/reference/2026-01-01/objects/entrypaginationconnection)

[`Notification.associated_entry`](/reference/2026-01-01/objects/notification)

[`bulkCreateEntriesPayload.entries`](/reference/2026-01-01/objects/bulkcreateentriespayload)

[`createEntryPayload.entry`](/reference/2026-01-01/objects/createentrypayload)

[`createOrAddToWaterIntakeEntryPayload.entry`](/reference/2026-01-01/objects/createoraddtowaterintakeentrypayload)

[`deleteEntryPayload.entry`](/reference/2026-01-01/objects/deleteentrypayload)

[`updateEntryPayload.entry`](/reference/2026-01-01/objects/updateentrypayload)

[`Query.entry`](/reference/2026-01-01/queries/entry)

[`Query.waterIntakeEntry`](/reference/2026-01-01/queries/waterintakeentry)

## Definition

```
"""
A post about a client, with different category options
"""
type Entry {
  """
  User who added the entry
  """
  added_by_user: User


  """
  the user who actually put in the entry (not always the user who the entry is about)
  """
  added_by_user_id: ID


  """
  The category of this entry
  """
  category: String


  """
  All comments association with this entry.
  """
  comments: [Comment!]!


  """
  The time at which this entry was created
  """
  created_at: ISO8601DateTime!


  """
  Default water intake for this entry user
  """
  default_water_intake_for_entry_user: Int


  """
  The description for the entry
  """
  description: String


  """
  A more granular 1-10 scale of how hungry the user thought they were after eating
  """
  ed_posthunger: String


  """
  A more granular 1-10 scale of how hungry the user thought they were after eating
  """
  ed_posthunger_string: String


  """
  A more granular 1-10 scale of how hungry the user thought they were before eating
  """
  ed_prehunger: String


  """
  A more granular 1-10 scale of how hungry the user thought they were before eating
  """
  ed_prehunger_string: String


  """
  The users emotions towards the meal as a numerical value
  """
  emotions: String


  """
  A descriptive string of the users emotions towards the meal based on the emotions value. Comes from the mapping: ['Stressed', 1], ['Anxious', 2], ['Tired', 3], ['Bored', 4], ['Confident', 5], ['Happy', 6], ['Sad', 7 or 0], ['Angry', 8]
  """
  emotions_string: String


  """
  If average of any type, value indicates amount of entries already included in average calculation
  """
  entries_in_average: Int


  """
  Third party external ID associated with this entry
  """
  external_id: String


  """
  Third party associated with the external ID on this entry. One option currently supported is 'AppleHealth'
  """
  external_id_type: String


  """
  True if the entry has subentries
  """
  has_subentries: Boolean


  """
  A hexadecimal value corresponding to the metric stat of a food entry
  """
  healthiness_info_hex_value: String


  """
  A boolean to check if the entry should be hidden from the main client feed
  """
  hide_from_main_feed: Boolean!


  """
  The unique identifier of the entry
  """
  id: ID!


  """
  The associated image of the entry
  """
  image: Upload


  """
  The URL of the entry's associated image
  """
  image_url(
    """
    Image size variant to return. If omitted, returns the original uploaded image (or the medium variant for entries created before 2019-09-21).
    """
    style: EntryImageStyleEnum
  ): String


  """
  True if the custom metric is linked to an auto-scored form template
  """
  linked_to_autoscored_form: Boolean


  """
  Meal entries of FoodEntry
  """
  meals: [Meal!]


  """
  The value of the metric for the entry
  """
  metric_stat: Float


  """
  Metric stat as a string
  """
  metric_stat_string: String


  """
  The name for this entry
  """
  name: String


  """
  Other symptom typed by the client
  """
  other_symptom: String


  """
  How hungry the poster thinks they were before eating
  """
  percieved_hungriness: Float


  """
  User who the entry is about
  """
  poster: User


  """
  The water intake previously added
  """
  previous_water_intake_stat: Int!


  """
  The time at which this entry was created. Cannot be updated
  """
  record_created_at: ISO8601DateTime!


  """
  The user's free-text reflection or notes about the meal
  """
  reflection: String


  """
  A name of third party source or full name of user who have created the entry
  """
  source: String


  """
  subentries of the Entry
  """
  subentries: [Entry!]


  """
  Comma-separated list of symptom names
  """
  symptom_names: String


  """
  Comma-separated list of symptom IDs selected by the client for this entry
  """
  symptoms: String


  """
  A name of third party source which actually created the entry
  """
  third_party_source: String


  """
  The type for this entry, options are - FoodEntry, WorkoutEntry, MirrorEntry, SleepEntry, NoteEntry, WaterIntakeEntry, PoopEntry', null: false
  """
  type: String


  """
  The last date and time that the entry was updated
  """
  updated_at: ISO8601DateTime!


  """
  A check to see if the entry has been viewed or not
  """
  viewed: Boolean!
}
```
