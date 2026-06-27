---
title: ClaimMdRejectionMessagesInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/claimmdrejectionmessagesinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/claimmdrejectionmessagesinfo/index.md
---

The reason why a ClaimMd rejection messages field is empty

## Used By

[`Cms1500.claim_md_rejection_messages_info`](/reference/2026-01-01/objects/cms1500)

## Definition

```
"""
The reason why a ClaimMd rejection messages field is empty
"""
enum ClaimMdRejectionMessagesInfo {
  CLAIM_MD_REJECTION_MESSAGES_NOT_AVAILABLE
    @deprecated(
      reason: "This value is no longer returned. The cms1500s-rejection-reason feature flag has been permanently enabled."
    )
  NO_RECENT_CLAIM_SUBMISSION
  NOT_A_CLAIM_MD_CLAIM
  NO_REJECTION_MESSAGES
}
```
