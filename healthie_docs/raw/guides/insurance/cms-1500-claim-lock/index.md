---
title: CMS 1500 Claim Lock | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/insurance/cms-1500-claim-lock/index
  md: https://docs.gethealthie.com/guides/insurance/cms-1500-claim-lock/index.md
---

Claim Lock freezes a CMS 1500 claim’s data once it has been submitted, so later edits to the patient, insurance, or provider don’t change what was sent to the payer. To correct a submitted claim, create a correction claim: a new CMS 1500 that inherits the original’s data, stays linked to it, and starts in `Not Sent` so it can be edited freely.

For general product context, see the Help Center article on [viewing or exporting a completed claim form](https://help.gethealthie.com/article/877-view-or-export-a-completed-claim-form).

Feature flag

Claim Lock is gated by an organization-scoped feature flag. When the flag is off, the `claim` query, the `updateClaim` and `createClaimCorrection` mutations, and the `is_locked` and `original_cms1500_id` fields on `Cms1500Type` are not visible in the schema. Contact your Healthie account team to enable Claim Lock for your organization.

## Locked statuses

A CMS 1500 is locked when its `status` matches one of the values below. Any other status, including `Not Sent` and `null`, leaves the claim editable.

| Status                        | State   |
| ----------------------------- | ------- |
| `Not Sent`                    | Mutable |
| `Sent`                        | Locked  |
| `Batched`                     | Locked  |
| `Rejected by Clearinghouse`   | Locked  |
| `Denied by Insurance`         | Locked  |
| `Client's Deductible Applies` | Locked  |
| `Partially Paid`              | Locked  |
| `Fully Paid`                  | Locked  |
| `Closed`                      | Locked  |

Read a claim’s lock state from the `is_locked` field, available on both `Cms1500Type` and `ClaimType`:

```
query checkLock($id: ID) {
  cms1500(id: $id) {
    id
    status
    is_locked
  }
}
```

`is_locked` returns `false` for all claims when Claim Lock is not enabled for the organization, regardless of the claim’s status.

### Default status for new claims

New claims are created in `Not Sent` and stay editable until they move into a locked status. This applies to claims created through the `createCms1500` mutation, the “Export as CMS 1500” action in the Healthie web app, and the organization’s `auto_create_cms1500` setting.

## Retrieving a claim with its snapshot

```
query claim($id: ID!) {
  claim(id: $id) {
    id
    status
    is_locked
    has_been_submitted
    has_claim_submission_claim_data
    submitted_at
    submission_method


    patient {
      full_name
      dob
      gender
      location { line1 city state zip }
    }


    rendering_provider {
      full_legal_name
      npi
      qualifications
    }


    billing_provider {
      name
      npi
      tax_id
      tax_id_type
      phone_number
    }


    service_lines {
      units
      fee
      service_date
      mod1
      pointers
      cpt_code { code display_name }
    }


    diagnoses {
      code
      display_name
      active
    }
  }
}
```

The `claim` query returns a `ClaimType`. For a submitted claim (one with a `ClaimSubmission`), `ClaimType` returns the frozen snapshot captured at submission time. For a draft claim, it returns the same fields from the live `Cms1500` record, so the same query works for both.

| Input | Info                                        |
| ----- | ------------------------------------------- |
| `id`  | **Required**. The ID of the claim to fetch. |

Returns a `ClaimType` object.

### Choosing between `claim` and `cms1500`

Both queries resolve to the same claim.

* Use `cms1500(id)` to see the claim’s current state. It always returns live data from the `Cms1500` record and its associations; later edits to the patient profile, insurance policies, or provider info show up here immediately.
* Use `claim(id)` to see what was sent to the payer. For submitted claims it returns the frozen snapshot; for drafts it falls back to live data.

### Correction chain fields

`ClaimType` exposes the link between an original claim and any corrections created from it.

| Field                             | Description                                                          |
| --------------------------------- | -------------------------------------------------------------------- |
| `original_claim_id`               | ID of the parent claim, or `null` if this claim is not a correction. |
| `original_claim`                  | The parent `ClaimType`, or `null` if this claim is not a correction. |
| `correction_claims`               | A connection of child corrections of this claim.                     |
| `is_correction`                   | `true` when the claim was created by `createClaimCorrection`.        |
| `has_claim_submission_claim_data` | `true` when a frozen snapshot exists for this claim.                 |

## Retrieving the frozen snapshot

Each submission creates a `ClaimSubmission` record that stores the full claim data as JSON on `claim_data`. Submissions are created when a claim is sent to ChangeHealth, Office Ally, Claim.MD, or Candid, and when a claim’s status is moved to `Sent` through `updateClaim`. Batching a claim does not create a submission (it’s a download action, not a payer submission), but the claim still becomes locked.

Retrieve the raw snapshot through the `claim_submissions` connection on `ClaimType`:

```
query claimSnapshots($id: ID!) {
  claim(id: $id) {
    id
    status
    claim_submissions(first: 5) {
      nodes {
        id
        created_at
        integration
        claim_data
      }
    }
  }
}
```

`claim_data` is a JSON scalar, access nested fields directly on the returned object (`patient`, `rendering_provider`, `billing_provider`, `service_lines`, `diagnoses`, `primary_policy`, `referral_info`, and the scalar claim fields).

Access to `claim_data` is restricted to organization administrators and the provider on the claim. Other authenticated users see `null`.

## Updating a claim

```
mutation updateClaim(
  $id: ID
  $patient: PatientInput
  $cms1500_policies: [Cms1500PolicyInput!]
  $icd_codes_cms1500s: [IcdCodesCms1500Input!]
  $cpt_codes_cms1500s: [CptCodesCms1500Input!]
  $amount_paid: String
  $patient_account_num: String
  $status: Cms1500Status
) {
  updateClaim(
    input: {
      id: $id
      patient: $patient
      cms1500_policies: $cms1500_policies
      icd_codes_cms1500s: $icd_codes_cms1500s
      cpt_codes_cms1500s: $cpt_codes_cms1500s
      amount_paid: $amount_paid
      patient_account_num: $patient_account_num
      status: $status
    }
  ) {
    cms1500 {
      id
      status
      is_locked
    }
    messages {
      field
      message
    }
  }
}
```

`updateClaim` accepts the same input fields as [`updateCms1500`](/guides/insurance/#updating-a-cms1500) and additionally checks the claim’s lock state before applying any change. If the claim is locked, the mutation leaves the claim as-is and returns an error in `messages` with `cms1500: null` in the payload.

| Input            | Info                                            |
| ---------------- | ----------------------------------------------- |
| `id`             | **Required**. The ID of the CMS 1500 to update. |
| All other fields | Optional. Same shape as `updateCms1500`.        |

Returns an `UpdateClaimPayload` object.

### Moving a claim to `Sent`

When `updateClaim` moves a claim from `Not Sent` to `Sent`, the mutation also:

* Creates a `ClaimSubmissionBatch` with `integration: manual` and `submission_method: manual`.
* Creates a `ClaimSubmission` capturing the claim’s current data as the frozen snapshot.
* Locks the claim, so subsequent calls to `updateClaim` return the locked-claim error.

This is the path for claims printed and mailed to a small clearinghouse, or otherwise sent outside Healthie’s integrations. Automated submissions through the built-in clearinghouse integrations continue to create their own `ClaimSubmission` records as they always have. Moving a claim directly to `Batched`, `Rejected by Clearinghouse`, `Denied by Insurance`, or another locked status also locks the claim, but only `Sent` triggers the manual snapshot.

### Locked claim error response

When a caller attempts to edit a locked claim, `updateClaim` returns HTTP 200 with a single entry in `messages`:

```
{
  "data": {
    "updateClaim": {
      "cms1500": null,
      "messages": [
        {
          "field": "base",
          "message": "This claim has a locked status and cannot be modified."
        }
      ]
    }
  }
}
```

The error message is stable and safe to pattern-match on. It appears only in `messages`, not in the GraphQL top-level `errors` array. Query `is_locked` on the claim first if you want to avoid hitting this error.

Once a claim is locked, its status cannot be changed through `updateClaim` either. Downstream status changes on locked claims — for example, moving a `Sent` claim to `Partially Paid` when an ERA arrives — are applied by Healthie’s ERA processing and do not require an API call.

To fix data on a locked claim, create a correction.

## Creating a correction claim

```
mutation createClaimCorrection($id: ID!) {
  createClaimCorrection(input: { id: $id }) {
    cms1500 {
      id
      status
      original_cms1500_id
    }
    messages {
      field
      message
    }
  }
}
```

`createClaimCorrection` creates a new CMS 1500 prefilled with the original claim’s data, linked to the original through `original_cms1500_id`, and set to `Not Sent` so it is immediately editable. The original claim is not modified.

| Input | Info                                                                       |
| ----- | -------------------------------------------------------------------------- |
| `id`  | **Required**. ID of the original locked claim to create a correction from. |

Returns a `CreateClaimCorrectionPayload` object.

### What the correction inherits

The correction copies the following from the original:

* CPT codes and their modifiers, units, fees, pointers, service dates, EPSDT and family planning flags.
* ICD codes and their active, end-date, and first-symptom metadata.
* Referral info, including the referring physician.
* The patient’s currently active insurance policies.
* Scalar claim fields such as `amount_paid`, `accept_assignment`, `use_indiv_npi`, `include_referrer_information`, and `claim_codes`.

The correction does not inherit the original’s `ClaimSubmission` history. It starts in `Not Sent` and is editable through `updateClaim` or `updateCms1500`. Once its status moves into a locked value, it becomes immutable like any other claim.

You can create multiple corrections from the same original. You cannot create a correction from another correction — corrections always come from an original claim.

### Validation errors

`createClaimCorrection` rejects the request in the following cases. Each error is returned in both the GraphQL top-level `errors` array and the payload’s `messages` field.

| Condition                                                                                          | Error message                                                                                              |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| The requesting user lacks permission to view the claim, or the CMS 1500 permission is not granted. | `You don't have permission to perform this operation. Please reach out to support if the problem persists` |
| The feature flag is off for the organization.                                                      | `This feature is not enabled`                                                                              |
| The target claim is not locked (for example, still `Not Sent`).                                    | `Cannot create correction for unlocked claim. Only submitted claims can have corrections.`                 |
| The target claim is itself a correction.                                                           | `Cannot create correction from a correction claim. Please create corrections from the original claim.`     |

## Related

* [Insurance](/guides/insurance/) — general CMS 1500 CRUD operations and Superbills.
* [Webhooks](/guides/webhooks/) — `cms1500.created`, `cms1500.updated`, and `cms1500.deleted` events.
* [Help Center: View or export a completed claim form](https://help.gethealthie.com/article/877-view-or-export-a-completed-claim-form).
