---
title: Integrations | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/integrations/index
  md: https://docs.gethealthie.com/guides/integrations/index.md
---

# Integrations

Healthie offers a number of [integrations](https://help.gethealthie.com/article/637-integrations-and-healthie) with other apps and software platforms. Here we describe some of the ways in which you use those integrations via the Healthie API, and limitations on using certain integrations via the API.

## Change Healthcare: E-Labs

The [Change Healthcare](https://help.gethealthie.com/article/1055-change-healthcare-and-healthie) + Healthie integration for E-labs enables providers to order, track & receive lab results from over 500 unique lab companies directly within Healthie. Lab vendors within the Change Healthcare network include Quest Diagnostics and LabCorp.

When using the integration, data from Change Healthcare feeds into Healthie `LabOrder` objects. You cannot order labs via Change Healthcare directly via the API when using the integration — it functions in an iframe in the Healthie portal. You can, however, retrieve the ingested results via API.

## Fullscript

[Fullscript integrates with Healthie](https://help.gethealthie.com/article/420-fullscript-and-healthie) to make it easy for you to provide product & supplement recommendations within Healthie, and directly connect your Fullscript account with your Healthie account.

When using the integration via the API, start by looking at the following queries in our [API Explorer](https://docs.gethealthie.com/docs/explorer.html):

* `dynamicLink`
* `fullscriptPractitioners`
* `fullscriptPractitionerTypes`
* `treatmentPlans`
