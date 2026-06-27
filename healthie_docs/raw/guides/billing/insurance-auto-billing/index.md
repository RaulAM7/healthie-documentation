---
title: Insurance Auto-Billing | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/billing/insurance-auto-billing/index
  md: https://docs.gethealthie.com/guides/billing/insurance-auto-billing/index.md
---

# Insurance Auto-Billing

Healthie’s Insurance Auto-Billing feature enables healthcare providers to automatically charge patients their insurance responsibility amounts (copays, coinsurance, or unmet deductibles) when appointments are marked as “Occurred”. This feature integrates seamlessly with Healthie’s existing auto-charge infrastructure and billing workflows, streamlining the patient billing process while ensuring accurate insurance-based pricing.

## Overview

Insurance Auto-Billing automates the calculation and collection of patient responsibility amounts based on their insurance policy configuration. When an appointment with an insurance-enabled appointment type is completed, the system:

1. **Validates Insurance Setup**: Checks if the patient has proper insurance billing configuration
2. **Calculates Patient Responsibility**: Determines the amount owed based on copay, coinsurance, or unmet deductible
3. **Integrates with Auto-Charge**: Leverages existing auto-charge/auto-invoice infrastructure
4. **Creates Billing Items**: Automatically generates billing items with calculated amounts
5. **Processes Payments**: Charges patients or sends invoices based on payment method preferences

This feature reduces administrative overhead while providing transparency and consistency in patient billing for insurance-covered services.

## Prerequisites and Requirements

### Provider Requirements

Before implementing insurance auto-billing, ensure your organization meets these requirements:

* **Healthie Plan**: Plus plan or above
* **Insurance Billing Automation**: Access to insurance billing automation features
* **Auto-Charge/Auto-Invoice**: Either auto-charge or auto-invoice enabled in appointment settings

### System Configuration Requirements

1. **Contracted Rates**: CPT code rates configured by payer
2. **CPT Code Mapping**: Appointment types linked to appropriate CPT codes
3. **Insurance Plans**: Accepted insurance plans configured in system
4. **Payment Processing**: Stripe integration for payment processing

## Configuration Requirements

### Provider Plan Validation

Only providers with appropriate plans can access insurance auto-billing:

```
query validateProviderAccess {
  currentUser {
    organization {
      subscription_plan
      insurance_billing_automation_enabled
    }
  }
}
```

## Patient Insurance Setup

### Policy Billing Methods

Patient policies support three automatic billing methods:

| Method              | Description                   | Use Case                                | Required Fields         |
| ------------------- | ----------------------------- | --------------------------------------- | ----------------------- |
| `copay`             | Fixed dollar amount per visit | Standard copay arrangements             | `copay_value` > 0       |
| `coinsurance`       | Percentage of contracted rate | Patient pays percentage after insurance | `coinsurance_value` > 0 |
| `unmet_deductible`  | Full contracted rate          | Patient hasn’t met deductible           | No additional fields    |
| `no_billing_method` | No automatic billing          | Default/disabled state                  | None                    |

### Configuring Patient Insurance Billing

Use the `updateClient` mutation to configure patient insurance billing:

```
mutation configurePatientInsuranceBilling(
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
      first_name
      last_name
      policies {
        id
        insurance_billing_method
        copay_value
        coinsurance_value
        payer_name
        payer_id
      }
    }
    messages {
      field
      message
    }
  }
}
```

### Example Configurations

**Setting up a $25 copay:**

```
{
  "variables": {
    "id": "patient_123",
    "policies_attributes": [
      {
        "id": "policy_456",
        "insurance_billing_method": "copay",
        "copay_value": 2500,
        "coinsurance_value": 0
      }
    ]
  }
}
```

**Setting up 20% coinsurance:**

```
{
  "variables": {
    "id": "patient_123",
    "policies_attributes": [
      {
        "id": "policy_456",
        "insurance_billing_method": "coinsurance",
        "copay_value": 0,
        "coinsurance_value": 20
      }
    ]
  }
}
```

**Setting up unmet deductible billing:**

```
{
  "variables": {
    "id": "patient_123",
    "policies_attributes": [
      {
        "id": "policy_456",
        "insurance_billing_method": "unmet_deductible",
        "copay_value": 0,
        "coinsurance_value": 0
      }
    ]
  }
}
```

### Validation Rules

The system enforces strict validation for insurance billing methods:

* **Copay Method**: `copay_value` must be greater than 0 when billing method is `"copay"`
* **Coinsurance Method**: `coinsurance_value` must be greater than 0 when billing method is `"coinsurance"`
* **Permission Requirements**: Users must have appropriate permissions to modify patient insurance billing settings

## Appointment Type Configuration

### Enabling Insurance Billing on Appointment Types

Appointment types must have insurance billing explicitly enabled:

```
mutation createInsuranceEnabledAppointmentType(
  $name: String!
  $length: Int!
  $insurance_billing_enabled: Boolean!
) {
  createAppointmentType(
    input: {
      name: $name
      length: $length
      insurance_billing_enabled: $insurance_billing_enabled
      clients_can_book: true
    }
  ) {
    appointmentType {
      id
      name
      length
      insurance_billing_enabled
    }
    messages {
      field
      message
    }
  }
}
```

### CPT Code Linkage

For coinsurance calculations, appointment types must be linked to CPT codes with contracted rates:

```
# Example appointment type with CPT code linkage
{
  "appointmentType": {
    "id": "123",
    "name": "Physical Therapy Session",
    "insurance_billing_enabled": true,
    "cpt_codes": ["97110", "97112"],
    "contracted_rates": {
      "Aetna_A1B2C3": {
        "97110": 85.00,
        "97112": 75.00
      },
      "BlueCross_D4E5F6": {
        "97110": 90.00,
        "97112": 80.00
      }
    }
  }
}
```

## Automatic Billing Workflow

### Complete Workflow Example

Here’s a complete example of the insurance auto-billing workflow:

#### Step 1: Create Insurance-Enabled Appointment

```
mutation createAppointmentWithInsurance(
  $user_id: String!
  $appointment_type_id: String!
  $datetime: String!
  $contact_type: String!
) {
  createAppointment(
    input: {
      user_id: $user_id
      appointment_type_id: $appointment_type_id
      datetime: $datetime
      contact_type: $contact_type
    }
  ) {
    appointment {
      id
      date
      appointment_type {
        id
        name
        insurance_billing_enabled
      }
      user {
        id
        first_name
        last_name
        primary_policy {
          insurance_billing_method
          copay_value
          coinsurance_value
        }
      }
    }
    messages {
      field
      message
    }
  }
}
```

#### Step 2: Complete Appointment and Trigger Auto-Billing

```
mutation completeAppointmentAndTriggerBilling(
  $id: ID!
) {
  updateAppointment(
    input: {
      id: $id
      pm_status: "Occurred"
    }
  ) {
    appointment {
      id
      pm_status
      # Auto-billing triggers automatically
    }
    messages {
      field
      message
    }
  }
}
```

#### Step 3: Verify Billing Item Creation

After marking the appointment as “Occurred”, verify the billing item was created:

```
query verifyInsuranceBilling(
  $patient_id: ID
  $sort_by: String
) {
  billingItems(
    provider_id: $patient_id
    sort_by: "newest"
    offset: 0
  ) {
    id
    amount_paid
    created_at
    note
    sender {
      id
      full_name
    }
    recipient {
      id
      full_name
    }
  }
}
```

### Pricing Calculation Logic

The system calculates patient responsibility amounts based on the configured billing method:

#### Copay Calculation

```
// Simple copay calculation
const patientAmount = policy.copay_value / 100.0;
// Example: copay_value = 2500 → patient pays $25.00
```

#### Coinsurance Calculation

```
// Coinsurance calculation requires contracted rate
const contractedRate = getContractedRate(appointmentType.cptCodes, policy.payer_id);
const patientAmount = (contractedRate * policy.coinsurance_value) / 100.0;
// Example: contracted rate = $100, coinsurance = 20% → patient pays $20.00
```

#### Unmet Deductible Calculation

```
// Unmet deductible uses full contracted rate
const contractedRate = getContractedRate(appointmentType.cptCodes, policy.payer_id);
const patientAmount = contractedRate;
// Example: contracted rate = $100 → patient pays $100.00
```

## API Integration Examples

### Complete Implementation Example

This example demonstrates a complete implementation for each billing method:

```
# Query to check patient insurance configuration
query checkPatientInsuranceSetup($patient_id: ID!) {
  user(id: $patient_id) {
    id
    first_name
    last_name
    primary_policy {
      id
      insurance_billing_method
      copay_value
      coinsurance_value
      payer_name
      payer_id
    }
  }
}


# Mutation to create appointment with insurance validation
mutation createValidatedInsuranceAppointment(
  $user_id: String!
  $appointment_type_id: String!
  $datetime: String!
  $contact_type: String!
) {
  createAppointment(
    input: {
      user_id: $user_id
      appointment_type_id: $appointment_type_id
      datetime: $datetime
      contact_type: $contact_type
    }
  ) {
    appointment {
      id
      date
      appointment_type {
        insurance_billing_enabled
      }
      user {
        primary_policy {
          insurance_billing_method
        }
      }
    }
    messages {
      field
      message
    }
  }
}


# Mutation to complete appointment and enable auto-billing
mutation completeWithInsuranceBilling($id: ID!) {
  updateAppointment(
    input: {
      id: $id
      pm_status: "Occurred"
    }
  ) {
    appointment {
      id
      pm_status
    }
    messages {
      field
      message
    }
  }
}
```

### Error Handling Implementation

Comprehensive error handling for insurance billing scenarios:

```
# Example error responses and handling
{
  "data": {
    "updateAppointment": {
      "appointment": null,
      "messages": [
        {
          "field": "insurance_billing",
          "message": "Patient does not have primary insurance policy configured"
        }
      ]
    }
  }
}


{
  "data": {
    "updateAppointment": {
      "appointment": null,
      "messages": [
        {
          "field": "appointment_type",
          "message": "Appointment type must have insurance billing enabled"
        }
      ]
    }
  }
}


{
  "data": {
    "updateClient": {
      "user": null,
      "messages": [
        {
          "field": "copay_value",
          "message": "Copay value must be greater than 0 for copay billing method"
        }
      ]
    }
  }
}
```

## Best Practices

### Configuration Best Practices

1. **Test Environment Validation**

   * Always test insurance billing configuration in sandbox environment
   * Verify all patient policies before enabling auto-billing
   * Test each billing method (copay, coinsurance, unmet deductible) individually

2. **Appointment Type Setup**

   * Enable insurance billing only for appointment types that should trigger automatic billing
   * Ensure CPT codes are properly linked for coinsurance calculations
   * Configure contracted rates for all accepted insurance payers

3. **Patient Policy Configuration**

   * Validate patient insurance information before setting billing methods
   * Ensure copay and coinsurance values are accurate and current
   * Document billing method choices and reasoning

### Workflow Integration Best Practices

1. **Pre-Appointment Validation**

   * Check patient insurance configuration during appointment booking
   * Verify appointment type has insurance billing enabled
   * Confirm CPT codes and contracted rates are configured

2. **Post-Appointment Monitoring**

   * Monitor billing item creation after appointments are marked as “Occurred”
   * Review failed charges and resolve configuration issues promptly
   * Track auto-billing success rates and patient payment collection

3. **Error Resolution**

   * Implement graceful error handling for missing insurance configuration
   * Provide clear error messages to staff for configuration issues
   * Maintain fallback billing processes for complex scenarios

### Performance and Reliability

1. **System Configuration Management**

   * Monitor system configuration status regularly
   * Plan rollout strategy for enabling insurance auto-billing
   * Maintain ability to disable feature quickly if issues arise

2. **Permission Management**

   * Ensure appropriate staff have insurance billing method permissions
   * Review and audit permission changes regularly
   * Document permission requirements for new staff

3. **Integration Monitoring**

   * Monitor integration with existing auto-charge/auto-invoice workflows
   * Track billing item creation success rates
   * Monitor payment processing success and failure rates

## Troubleshooting

### Common Configuration Issues

**Issue: Auto-billing not triggering**

```
# Check system configuration
query checkSystemConfiguration {
  currentUser {
    organization {
      insurance_billing_automation_enabled
    }
  }
}


# Verify appointment type configuration
query checkAppointmentType($id: ID!) {
  appointmentType(id: $id) {
    id
    name
    insurance_billing_enabled
  }
}


# Check patient insurance setup
query checkPatientInsurance($id: ID!) {
  user(id: $id) {
    primary_policy {
      insurance_billing_method
      copay_value
      coinsurance_value
    }
  }
}
```

**Issue: Incorrect billing amounts**

* Verify copay values are in cents (2500 = $25.00)
* Check coinsurance percentages are whole numbers (20 = 20%)
* Confirm contracted rates are configured for CPT codes
* Validate CPT code linkage to appointment types

**Issue: Permission errors**

* Verify user has appropriate permissions to modify patient insurance billing settings
* Check organization subscription plan and feature access
* Confirm system configuration is properly enabled for the organization

### Validation Checklist

Before enabling insurance auto-billing, verify:

* [ ] Provider has Plus plan or above
* [ ] Insurance billing automation is enabled for the organization
* [ ] Auto-charge or auto-invoice is enabled in appointment settings
* [ ] Appointment types have `insurance_billing_enabled: true`
* [ ] CPT codes are linked to appointment types
* [ ] Contracted rates are configured for accepted payers
* [ ] Patients have primary insurance policies configured
* [ ] Billing methods are properly set with appropriate values
* [ ] Staff have necessary permissions for insurance billing management

For related functionality, see:

* **[Insurance](/guides/insurance/)**: General insurance functionality and policy management
* **[Billing Items](/guides/billing/billing-items/)**: Manual billing item creation and management
* **[Payment Processing](/guides/billing/payment-processing/)**: Payment processing and auto-charge setup
* **[Appointments](/guides/scheduling/appointments/)**: Appointment creation and management

For end-user setup instructions, refer to the [Healthie Help Center article on Auto-Billing for Copays, Deductibles, and Coinsurance](https://help.gethealthie.com/article/1313-auto-billing-for-copays-deductibles-and-coinsurance).
