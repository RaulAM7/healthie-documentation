---
title: HealthAssessmentRecommendation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/healthassessmentrecommendation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/healthassessmentrecommendation/index.md
---

Health Assessment Recommendation is a sub category of a HealthAssessment

## Fields

[`cal_deficit` ](#field-cal-deficit)· [`String` ](/reference/2026-01-01/scalars/string)· cal\_deficit of user

[`carbs_cal` ](#field-carbs-cal)· [`String` ](/reference/2026-01-01/scalars/string)· carbs\_cal of user

[`carbs_grams` ](#field-carbs-grams)· [`String` ](/reference/2026-01-01/scalars/string)· carbs\_grams of user

[`carbs_percent` ](#field-carbs-percent)· [`String` ](/reference/2026-01-01/scalars/string)· Carbs percent

[`current_body_fat` ](#field-current-body-fat)· [`String` ](/reference/2026-01-01/scalars/string)· current\_body\_fat of user

[`current_body_weight` ](#field-current-body-weight)· [`String` ](/reference/2026-01-01/scalars/string)· current\_body\_weight of user

[`current_daily_caloric_intake` ](#field-current-daily-caloric-intake)· [`String` ](/reference/2026-01-01/scalars/string)· current\_daily\_caloric\_intake of user

[`current_time_to_goal` ](#field-current-time-to-goal)· [`String` ](/reference/2026-01-01/scalars/string)· current\_time\_to\_goal of user

[`fat_cal` ](#field-fat-cal)· [`String` ](/reference/2026-01-01/scalars/string)· fat\_cal of user

[`fat_grams` ](#field-fat-grams)· [`String` ](/reference/2026-01-01/scalars/string)· fat\_grams of user

[`fat_percent` ](#field-fat-percent)· [`String` ](/reference/2026-01-01/scalars/string)· Fat Percent

[`high_end_caloric_intake` ](#field-high-end-caloric-intake)· [`String` ](/reference/2026-01-01/scalars/string)· high\_end\_caloric\_intake of user

[`ideal_body_fat` ](#field-ideal-body-fat)· [`String` ](/reference/2026-01-01/scalars/string)· Ideal body fat of user

[`ideal_body_weight` ](#field-ideal-body-weight)· [`String` ](/reference/2026-01-01/scalars/string)· ideal\_body\_weight of user

[`ideal_daily_caloric_intake` ](#field-ideal-daily-caloric-intake)· [`String` ](/reference/2026-01-01/scalars/string)· ideal\_daily\_caloric\_intake of user

[`ideal_time_to_goal` ](#field-ideal-time-to-goal)· [`String` ](/reference/2026-01-01/scalars/string)· ideal\_time\_to\_goal of user

[`low_end_caloric_intake` ](#field-low-end-caloric-intake)· [`String` ](/reference/2026-01-01/scalars/string)· low\_end\_caloric\_intake of user

[`protein_cal` ](#field-protein-cal)· [`String` ](/reference/2026-01-01/scalars/string)· protein\_cal of user

[`protein_grams` ](#field-protein-grams)· [`String` ](/reference/2026-01-01/scalars/string)· protein\_grams of user

[`protein_percent` ](#field-protein-percent)· [`String` ](/reference/2026-01-01/scalars/string)· Protein Percent

## Used By

[`HealthAssessment.recommendation`](/reference/2026-01-01/objects/healthassessment)

## Definition

```
"""
Health Assessment Recommendation is a sub category of a HealthAssessment
"""
type HealthAssessmentRecommendation {
  """
  cal_deficit of user
  """
  cal_deficit: String


  """
  carbs_cal of user
  """
  carbs_cal: String


  """
  carbs_grams of user
  """
  carbs_grams: String


  """
  Carbs percent
  """
  carbs_percent: String


  """
  current_body_fat of user
  """
  current_body_fat: String


  """
  current_body_weight of user
  """
  current_body_weight: String


  """
  current_daily_caloric_intake of user
  """
  current_daily_caloric_intake: String


  """
  current_time_to_goal of user
  """
  current_time_to_goal: String


  """
  fat_cal of user
  """
  fat_cal: String


  """
  fat_grams of user
  """
  fat_grams: String


  """
  Fat Percent
  """
  fat_percent: String


  """
  high_end_caloric_intake of user
  """
  high_end_caloric_intake: String


  """
  Ideal body fat of user
  """
  ideal_body_fat: String


  """
  ideal_body_weight of user
  """
  ideal_body_weight: String


  """
  ideal_daily_caloric_intake of user
  """
  ideal_daily_caloric_intake: String


  """
  ideal_time_to_goal of user
  """
  ideal_time_to_goal: String


  """
  low_end_caloric_intake of user
  """
  low_end_caloric_intake: String


  """
  protein_cal of user
  """
  protein_cal: String


  """
  protein_grams of user
  """
  protein_grams: String


  """
  Protein Percent
  """
  protein_percent: String
}
```
