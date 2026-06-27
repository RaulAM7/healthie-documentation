---
title: GeneratedFormAnswerGroupRejectionReasonEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/generatedformanswergrouprejectionreasonenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/generatedformanswergrouprejectionreasonenum/index.md
---

The reason for rejecting an AI-generated form answer group

## Used By

[`rejectGeneratedFormAnswerGroupInput.rejection_reason`](/reference/2026-01-01/input-objects/rejectgeneratedformanswergroupinput)

## Definition

```
"""
The reason for rejecting an AI-generated form answer group
"""
enum GeneratedFormAnswerGroupRejectionReasonEnum {
  """
  The proposed note contains factual errors or incorrect details from the encounter
  """
  INACCURATE_INFORMATION


  """
  The proposed note is missing significant details that were discussed during the encounter
  """
  MISSING_DETAILS


  """
  The proposed note did not follow the formatting or content instructions provided
  """
  DIDNT_FOLLOW_INSTRUCTIONS


  """
  The provider already created their own note for this encounter
  """
  DUPLICATE_OR_OWN_NOTE
}
```
