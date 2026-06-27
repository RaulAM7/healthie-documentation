---
title: Environments | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/environments/index
  md: https://docs.gethealthie.com/guides/api-concepts/environments/index.md
---

Healthie offers two API environments - Sandbox and Production. Sandbox and Production are fully seperate environments, and it is not possible for Healthie to copy data between them. Please note, before hard-coding IDs into your integration, that they will be different on Sandbox and Production.

The examples in this documentation use the Sandbox environment’s API URL. The URLs are as follows:

| Name       | URL                                           |
| ---------- | --------------------------------------------- |
| Sandbox    | <https://staging-api.gethealthie.com/graphql> |
| Production | <https://api.gethealthie.com/graphql>         |

## Sandbox Limitations

The sandbox environment is intended for testing and development purposes only. It is not intended for production use. Due to the nature of the environment, some of the features of the API are not available in the sandbox environment. The table below shows which features are available in the sandbox environment.

| Feature / integration    | Available in sandbox |
| ------------------------ | -------------------- |
| Change Healthcare E-Labs | No                   |
| Faxing                   | No                   |
| FitBit                   | **Yes**              |
| Stripe                   | **Yes**              |
| Withings                 | No                   |
| Zoom                     | No                   |
| ICD + CPT codes          | Limited              |

### Stripe

You can test Stripe payments in the Healthie sandbox environment. You’ll be prompted to add a bank account in the Healthie portal - follow the instructions and use [Stripe test data](https://stripe.com/docs/testing#test-account-numbers) for the bank info. You can use any U.S. address.

If you receive the following error when using the `createBillingItem` or `completeCheckout` mutations, you likely need to complete your setup of the test bank info: “Your destination account needs to have at least one of the following capabilities enabled: transfers, crypto\_transfers, legacy\_payments”

### Change Healthcare: E-Labs

Change Labs is not currently available in the sandbox environment. We recommend working instead with `LabOrder` objects, but not with the actual Change connection. Unfortunately, this restriction comes from Change — their developer environment does not have the ability to automatically trigger tests end-to-end, nor to provision new accounts.

You can generate `LabOrder` objects, which the Change integration also generates, in the staging environment via the API to help simulate an end-to-end testing experience.

### ICD + CPT codes

Healthie provides a limited subset of ICD and CPT codes in the sandbox environment. We recommend building any workflows that rely on these codes in sandbox using stand-in codes as needed.
