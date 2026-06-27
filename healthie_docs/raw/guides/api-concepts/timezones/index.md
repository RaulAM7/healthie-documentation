---
title: Timezones | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/timezones/index
  md: https://docs.gethealthie.com/guides/api-concepts/timezones/index.md
---

Healthie uses dates and times heavily throughout our APIs (in both inputs and outputs). Healthie stores all datetimes in UTC, but processes and returns them in specified timezones. By default, these datetimes are always displayed in the timezone of the authenticated user account.

If the authenticated user is a patient, and does not have a timezone set, the API falls back to the timezone of the patient’s provider.

If the provider does not have a timezone set (which is exceedingly rare), we default to America/New\_York. Healthie’s list of valid timezones comes from the [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

In some cases, especially when the API takes in a date and/or time argument, or when creating something recurring (e.g weekly availability), we support sending in a timezone argument. This argument is used when the date and time gets parsed, and does not impact the timezone used for the return fields.
