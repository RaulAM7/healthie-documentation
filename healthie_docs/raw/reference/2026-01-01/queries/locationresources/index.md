---
title: locationResources | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/locationresources/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/locationresources/index.md
---

Get location resources

## Arguments

[`location_ids` ](#argument-location-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

## Returns

[`[LocationResourceType!]`](/reference/2026-01-01/objects/locationresourcetype)

## Example

```
query locationResources($location_ids: [ID]) {
  locationResources(location_ids: $location_ids) {
    resourceId
    resourceTitle
  }
}
```
