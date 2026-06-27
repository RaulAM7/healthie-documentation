---
title: Insurance | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/insurance/index
  md: https://docs.gethealthie.com/guides/insurance/index.md
---

# Insurance

Please refer to [Healthie’s Help Portal](https://help.gethealthie.com/category/260-cms-1500-forms) for a general information about the Insurance feature.

## Policies

### The Policy object

```
{
  "id": "1",
  "name_and_id": "ExampleHealth - A1B2C3",
  "is_accepted": true, // whether this Policy is accepted within the organization
  "payer_id": "A1B2C3",
  "payer_name": "ExampleHealth"
}
```

Within the API, Insurance Policies are `InsurancePlan` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/insuranceplan).

### Listing Policies

```
query insurancePlans($ids: String, $keywords: String, $is_accepted: Boolean, $sort_by: String) {
  insurancePlans(ids: $ids, keywords: $keywords, is_accepted: $is_accepted, sort_by: $sort_by) {
    id
    name_and_id
    payer_id
    payer_name
  }
}
```

Listing Policies is done via the `insurancePlans` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/insuranceplans#arguments).

| Input         | Info                                                        |
| ------------- | ----------------------------------------------------------- |
| `ids`         | Optional. Array of plan IDs to fetch.                       |
| `keywords`    | Optional. Can be searched by Payer name or ID.              |
| `is_accepted` | Optional. Set to `true` to fetch only Accepted Policies.    |
| `sort_by`     | Optional. Valid options are:- `accepted`
- `payer_name_asc` |

Returns a list of [InsurancePlan](/reference/2024-06-01/objects/insuranceplan) objects.

### Accepting a Policy

```
mutation createAcceptedInsurancePlan($insurance_plan_ids: [ID]) {
  createAcceptedInsurancePlan(input: { insurance_plan_ids: $insurance_plan_ids }) {
    accepted_insurance_plans {
      id


      insurance_plan {
        id
      }
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createacceptedinsuranceplaninput).

| Input                | Info                                                   |
| -------------------- | ------------------------------------------------------ |
| `insurance_plan_ids` | **Required**. IDs of the Insurance Policies to accept. |

Returns a [`createAcceptedInsurancePlanPayload`](/reference/2024-06-01/objects/createacceptedinsuranceplanpayload) object.

### Removing a Policy from the list of accepted Policies

```
mutation deleteAcceptedInsurancePlan($id: ID) {
  deleteAcceptedInsurancePlan(input: { id: $id }) {
    accepted_insurance_plan {
      id


      insurance_plan {
        id
      }
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleteacceptedinsuranceplaninput).

| Input | Info                                                                             |
| ----- | -------------------------------------------------------------------------------- |
| `id`  | **Required**. The ID of the Policy to remove from the list of accepted Policies. |

Returns an [`deleteAcceptedInsurancePlanPayload`](/reference/2024-06-01/objects/deleteacceptedinsuranceplanpayload) object.

## Superbills

### The Superbill object

```
{
  "id": "1",
  "amount_paid": "1000.00",
  "balance_due": "500.00",
  "provider": {
    "id": "1"
  },
  "patient": {
    "id": "2"
  }
}
```

Superbills are `SuperBill` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/superbill).

### Listing Superbills

```
query superBills($keywords: String, $sort_by: String, $provider_id: ID, $client_id: ID, $status: String) {
  superBills(
    keywords: $keywords
    sort_by: $sort_by
    provider_id: $provider_id
    client_id: $client_id
    status: $status
  ) {
    id
    amount_paid
    balance_due
    total_fee
    status
  }
}
```

Listing Superbills is done via the `superBills` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/superbills#arguments).

| Input         | Info                                                                                                                                                                                                                                                                          |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort_by`     | Optional. Valid options are:- `name_asc`
- `name_desc`
- `billed_date_asc`
- `billed_date_desc`
- `created_date_asc` or `oldest` (default)
- `created_date_desc` or `newest`
- `amount_billed_asc`
- `amount_billed_desc`
- `amount_paid_asc`
- `amount_paid_desc`
- `status` |
| `keywords`    | Optional. Can be searched by Superbill status, Patient first and last name, or Provider first and last name.                                                                                                                                                                  |
| `client_id`   | Optional. ID of the Patient that is associated with the Superbill.                                                                                                                                                                                                            |
| `provider_id` | Optional. ID of the Provider that is associated with the Superbill.                                                                                                                                                                                                           |
| `status`      | Optional. Return only Superbills that have one of the following statuses:- `Sent`
- `Not Sent`
- `Fully Paid`
- `Rejected`                                                                                                                                                    |

Returns a list of [Superbill](/reference/2024-06-01/objects/superbill) objects.

### Retrieving a Superbill

```
query superBill($id: ID) {
  superBill(id: $id) {
    id
    name
    patient {
      id
    }
  }
}
```

Retrieving a specific Superbill is done via the `superBill` query.

| Input | Info                          |
| ----- | ----------------------------- |
| `id`  | ID of the Superbill to query. |

Returns a [Superbill](/reference/2024-06-01/objects/superbill) object.

### Creating a Superbill

```
mutation createSuperBill(
  $patient_id: ID,
  $patient_dob: String,
  $dietetitian_id: ID,
  $provider_name: String,
  $service_date: String,
  $amount_paid: String,
  $status: String,
  icd_codes_super_bills: [IcdCodesSuperBillInput]
  cpt_codes_super_bills: [CptCodesSuperBillInput],
  $receipt_line_items: [ReceiptLineItemInput]
) {
  createSuperBill(input: {
    patient_id: $patient_id,
    patient_dob: $patient_dob,
    dietetitian_id: $dietetitian_id,
    provider_name: $provider_name,
    service_date: $service_date,
    amount_paid: $amount_paid,
    status: $status,
    icd_codes_super_bills: $icd_codes_super_bills,
    cpt_codes_super_bills: $cpt_codes_super_bills,
    receipt_line_items: $receipt_line_items
  }) {
    superBill {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createsuperbillinput).

| Input                   | Info                                                                                                                        |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `patient_id`            | **Required**. ID of the Patient to create the Superbill for.                                                                |
| `patient_dob`           | **Required**. Date of birth of the Patient. Format: `YYYY-MM-DD`.                                                           |
| `dietetitian_id`        | **Required**. ID of the Provider.                                                                                           |
| `provider_name`         | **Required**. Name of the Provider.                                                                                         |
| `service_date`          | **Required**. Service date. Format: `YYYY-MM-DD`.                                                                           |
| `icd_codes_super_bills` | Optional. An array of [`IcdCodesSuperBillInput`](/reference/2024-06-01/input-objects/icdcodessuperbillinput) input objects. |
| `cpt_codes_super_bills` | Optional. An array of [`CptCodesSuperBillInput`](/reference/2024-06-01/input-objects/cptcodessuperbillinput) input objects. |
| `receipt_line_items`    | Optional. An array of [`ReceiptLineItemInput`](/reference/2024-06-01/input-objects/receiptlineiteminput) input objects.     |

Returns a [`createSuperBillPayload`](/reference/2024-06-01/objects/createsuperbillpayload) object.

### Updating a Superbill

```
mutation updateSuperBill(
  $id: ID,
  $patient_id: ID,
  $patient_dob: String,
  $dietetitian_id: ID,
  $provider_name: String,
  $service_date: String,
  $amount_paid: String,
  $status: String,
  icd_codes_super_bills: [IcdCodesSuperBillInput]
  cpt_codes_super_bills: [CptCodesSuperBillInput],
  $receipt_line_items: [ReceiptLineItemInput],
  $should_email_to_client: Boolean
) {
  updateSuperBill(input: {
    id: $id,
    patient_id: $patient_id,
    patient_dob: $patient_dob,
    dietetitian_id: $dietetitian_id,
    provider_name: $provider_name,
    service_date: $service_date,
    amount_paid: $amount_paid,
    status: $status,
    icd_codes_super_bills: $icd_codes_super_bills,
    cpt_codes_super_bills: $cpt_codes_super_bills,
    receipt_line_items: $receipt_line_items,
    should_email_to_client: $should_email_to_client
  }) {
    superBill {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateSuperBill` mutation shares many common inputs with [`createSuperBill`](#creating-a-superbill) and those inputs (e.g `service_date` or `receipt_line_items` work the same in both places).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatesuperbillinput).

| Input                    | Info                                                                            |
| ------------------------ | ------------------------------------------------------------------------------- |
| `id`                     | **Required**. The ID of the Superbill to update.                                |
| `should_email_to_client` | Optional. Set to `true` in order to resend the email to the associated Patient. |

Returns an [`updateSuperBillPayload`](/reference/2024-06-01/objects/updatesuperbillpayload) object.

### Deleting a Superbill

Superbills can be deleted by authorized providers and staff members via the `deleteSuperBill` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletesuperbillinput).

```
mutation deleteSuperBill($id: ID) {
  deleteSuperBill(input: { id: $id }) {
    superBill {
      id
    }


    messages {
      field
      message
    }
  }
}
```

| Input | Info                                         |
| ----- | -------------------------------------------- |
| `id`  | **Required**. ID of the Superbill to delete. |

Returns a [`deleteSuperBillPayload`](/reference/2024-06-01/objects/deletesuperbillpayload) object.

## CMS1500s

Please refer to [Healthie’s Help Portal](https://help.gethealthie.com/article/109-create-and-submit-a-cms-1500-form-using-healthie) for a general information about CMS 1500 claims.

### The CMS1500 object

```
{
  "id": "1",
  "amount_paid": "1500.00",
  "amount_reimbursed": "1000.00",
  "status": "Partially Paid",
  "patient": {
    "id": "2"
  }
}
```

CMS 1500 Claims are `Cms1500` objects.

You can view the full list of available fields [here](/schema/cms1500.doc.html).

### Listing CMS1500s

```
query cms1500s($keywords: String, $sort_by: String, $status: String, $client_id: ID, $provider_id: ID) {
  cms1500s(keywords: $keywords, sort_by: $sort_by, status: $status, client_id: $client_id, provider_id: $provider_id) {
    id
    name
    patient {
      id
    }
  }
}
```

Listing CMS1500s is done via the `cms1500s` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/cms1500s#arguments).

| Input         | Info                                                                                                                                                                                                                                                       |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort_by`     | Optional. Valid options are:- `created_date_asc`
- `created_date_desc` (default)
- `status_asc`
- `status_desc`
- `primary_plan_name_asc`
- `primary_plan_name_desc`
- `patient_name_asc`
- `patient_name_desc`
- `service_date_asc`
- `service_date_desc` |
| `client_id`   | Optional. ID of the Patient that is associated with the CMS1500.                                                                                                                                                                                           |
| `provider_id` | Optional. ID of the Provider.                                                                                                                                                                                                                              |
| `keywords`    | Optional. Can be searched by status, Patient first and last name, Provider first and last name, Payer name or Payer ID.                                                                                                                                    |
| `status`      | Optional. Valid options are:- `Not Sent`
- `Sent`
- `Batched`
- `Rejected by Clearinghouse`
- `Denied by Insurance`
- `Client's Deductible Applies`
- `Partially Paid`
- `Fully Paid`
- `Closed`
                                                          |

Returns a list of [Cms1500](/schema/cms1500.doc.html) objects.

### Retrieving a CMS1500

```
query cms1500($id: ID) {
  cms1500(id: $id) {
    id
    name
    patient {
      id
    }
  }
}
```

Retrieving a specific CMS1500 is done via the `cms1500` query.

| Input | Info                        |
| ----- | --------------------------- |
| `id`  | ID of the CMS1500 to query. |

Returns a [Cms1500](/schema/cms1500.doc.html) object.

### Creating a CMS1500

```
mutation createCms1500(
  $patient: PatientInput
  $dietitian: DietitianInput
  $service_location_id: String
  $amount_paid: String
  $cms1500_policies: [Cms1500PolicyInput!]
  $icd_codes_cms1500s: [IcdCodesCms1500Input!]
  $cpt_codes_cms1500s: [CptCodesCms1500Input!]
  $client_sig_on_file: Boolean
) {
  createCms1500(
    input: {
      patient: $patient
      dietitian: $dietitian
      service_location_id: $service_location_id
      amount_paid: $amount_paid
      cms1500_policies: $cms1500_policies
      icd_codes_cms1500s: $icd_codes_cms1500s
      cpt_codes_cms1500s: $cpt_codes_cms1500s
      client_sig_on_file: $client_sig_on_file
    }
  ) {
    cms1500 {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/schema/createcms1500input.doc.html).

| Input                 | Info                                                                                                                                                                                                                                     |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `patient`             | **Required**. A [`PatientInput`](/reference/2024-06-01/input-objects/patientinput) object to specify a Patient. Note that the `PatientInput` MUST include a [`LocationInput`](/reference/2024-06-01/input-objects/locationinput) object. |
| `dietitian`           | **Required**. A [`DietitianInput`](/reference/2024-06-01/input-objects/dietitianinput) object to specify the provider.                                                                                                                   |
| `service_location_id` | **Required** The `ID` of the location where the patient received service.                                                                                                                                                                |
| `cms1500_policies`    | **Required** An `Array` of [`Cms1500PolicyInput`](/schema/cms1500policyinput.doc.html) objects. Can be an empty array.                                                                                                                   |
| `amount_paid`         | Optional. Amount paid.                                                                                                                                                                                                                   |

Returns a [`createCms1500Payload`](/schema/createcms1500payload.doc.html) object.

### Updating a CMS1500

```
mutation updateCms1500(
  $id: ID
  $patient: PatientInput
  $dietitian: DietitianInput
  $service_location_id: String
  $amount_paid: String
  $cms1500_policies: [Cms1500PolicyInput!]
  $icd_codes_cms1500s: [IcdCodesCms1500Input!]
  $cpt_codes_cms1500s: [CptCodesCms1500Input!]
  $client_sig_on_file: Boolean
) {
  updateCms1500(
    input: {
      id: $id
      patient: $patient
      dietitian: $dietitian
      service_location_id: $service_location_id
      amount_paid: $amount_paid
      cms1500_policies: $cms1500_policies
      icd_codes_cms1500s: $icd_codes_cms1500s
      cpt_codes_cms1500s: $cpt_codes_cms1500s
      client_sig_on_file: $client_sig_on_file
    }
  ) {
    cms1500 {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateCms1500` mutation shares many common inputs with [`createCms1500`](#creating-a-cms1500) and those inputs (e.g `service_date` or `receipt_line_items` work the same in both places).

You can view a full list of potential inputs [here](/schema/updatecms1500input.doc.html).

| Input | Info                                           |
| ----- | ---------------------------------------------- |
| `id`  | **Required**. The ID of the CMS1500 to update. |

Returns an [`updateCms1500Payload`](/schema/updatecms1500payload.doc.html) object.

### Deleting a CMS1500

CMS1500s can be deleted by authorized providers and staff members via the `deleteCms1500` mutation.

You can view a full list of potential inputs [here](/schema/deletecms1500input.doc.html).

```
mutation deleteCms1500($id: ID) {
  deleteCms1500(input: { id: $id }) {
    cms1500 {
      id
    }


    messages {
      field
      message
    }
  }
}
```

| Input | Info                                       |
| ----- | ------------------------------------------ |
| `id`  | **Required**. ID of the CMS1500 to delete. |

Returns a [`deleteCms1500Payload`](/schema/deletecms1500payload.doc.html) object.

## Patient Insurance Billing Configuration

Healthcare providers can configure automatic billing for patient insurance responsibility amounts (copays, coinsurance, and deductibles) through patient policy settings. This feature automatically bills patients their portion after appointments are marked as “Occurred”.

### Policy Billing Methods

| Billing Method      | Description                               |
| ------------------- | ----------------------------------------- |
| `copay`             | Fixed dollar amount per visit             |
| `coinsurance`       | Percentage of contracted rate             |
| `unmet_deductible`  | Full contracted rate until deductible met |
| `no_billing_method` | No automatic billing (default)            |

### Configuring Billing Methods

Use the `updateClient` mutation to configure patient insurance billing:

```
mutation updatePatientInsuranceBilling(
  $id: ID!
  $policies_attributes: [ClientPolicyInput]
) {
  updateClient(
    input: {
      id: $id
      policies_attributes: $policies_attributes
    }
  ) {
    user {
      id
      policies {
        id
        insurance_billing_method
        copay_value
        coinsurance_value
      }
    }
  }
}
```

**Example: Setting up a $25 copay**

```
{
  "id": "123",
  "policies_attributes": [
    {
      "id": "456",
      "insurance_billing_method": "copay",
      "copay_value": 2500
    }
  ]
}
```

### Key Policy Fields

* `insurance_billing_method`: Billing method (`"copay"`, `"coinsurance"`, `"unmet_deductible"`, or `"no_billing_method"`)
* `copay_value`: Copay amount in cents (e.g., `2500` = $25.00)
* `coinsurance_value`: Coinsurance percentage (e.g., `20` = 20%)

View all Policy fields in the [API reference](/reference/2024-06-01/objects/policy).

For comprehensive setup instructions, complete workflow examples, error handling, and troubleshooting guidance, see the **[Insurance Auto-Billing](/guides/billing/insurance-auto-billing/)** guide.
