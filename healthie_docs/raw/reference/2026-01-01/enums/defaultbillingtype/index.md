---
title: DefaultBillingType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/defaultbillingtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/defaultbillingtype/index.md
---

The default billing type for a patient

## Used By

[`User.default_billing_type`](/reference/2026-01-01/objects/user)

[`createClientInput.default_billing_type`](/reference/2026-01-01/input-objects/createclientinput)

[`updateClientInput.default_billing_type`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateUserInput.default_billing_type`](/reference/2026-01-01/input-objects/updateuserinput)

## Definition

```
"""
The default billing type for a patient
"""
enum DefaultBillingType {
  """
  Patient pays out of pocket
  """
  SELF_PAY


  """
  Patient pays via insurance
  """
  INSURANCE_PAY
}
```
