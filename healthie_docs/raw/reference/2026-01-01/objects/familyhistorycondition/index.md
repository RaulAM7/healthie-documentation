---
title: FamilyHistoryCondition | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/familyhistorycondition/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/familyhistorycondition/index.md
---

A family history condition record for a client

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the family history condition

[`relationships` ](#field-relationships)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Enum field for family relationships

[`snomed_term` ](#field-snomed-term)· [`SnomedTerm` ](/reference/2026-01-01/objects/snomedterm)· snomed term associated with the condition

## Used By

[`User.family_history_conditions`](/reference/2026-01-01/objects/user)

[`createFamilyHistoryPayload.duplicate_family_history_condition`](/reference/2026-01-01/objects/createfamilyhistorypayload)

[`createFamilyHistoryPayload.family_history_condition`](/reference/2026-01-01/objects/createfamilyhistorypayload)

[`deleteFamilyHistoryPayload.family_history_condition`](/reference/2026-01-01/objects/deletefamilyhistorypayload)

[`updateFamilyHistoryPayload.duplicate_family_history_condition`](/reference/2026-01-01/objects/updatefamilyhistorypayload)

[`updateFamilyHistoryPayload.family_history_condition`](/reference/2026-01-01/objects/updatefamilyhistorypayload)

## Definition

```
"""
A family history condition record for a client
"""
type FamilyHistoryCondition {
  """
  The unique identifier of the family history condition
  """
  id: ID!


  """
  Enum field for family relationships
  """
  relationships: [String!]


  """
  snomed term associated with the condition
  """
  snomed_term: SnomedTerm
}
```
