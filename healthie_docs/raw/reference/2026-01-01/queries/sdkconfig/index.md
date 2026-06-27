---
title: sdkConfig | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sdkconfig/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sdkconfig/index.md
---

SDK configuration

## Arguments

[`version` ](#argument-version)· [`String` ](/reference/2026-01-01/scalars/string)· SDK version to obtain the configuration for

## Returns

[`SDKConfig!`](/reference/2026-01-01/objects/sdkconfig)

## Example

```
query sdkConfig($version: String) {
  sdkConfig(version: $version)
}
```
