---
title: questionBankModules | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/questionbankmodules/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/questionbankmodules/index.md
---

Fetch generic custom modules for use in the form builder

## Arguments

[`category` ](#argument-category)· [`String`](/reference/2026-01-01/scalars/string)

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Terms used for searching question bank modules. Only has effect when category is \`custom\`

## Returns

[`[CustomModule!]`](/reference/2026-01-01/objects/custommodule)

## Example

```
query questionBankModules($category: String, $keywords: String) {
  questionBankModules(category: $category, keywords: $keywords) {
    controls_conditional_modules
    copied_from_form_name
    custom_module_condition
    custom_module_form
    custom_module_form_id
    custom_module_form_section_id
    exclude_from_scribe
    external_id
    external_id_type
    file_attachment
    hipaa_name
    id
    is_custom
    label
    metadata
    mod_type
    options
    options_array
    other_module_ids_to_autoscore_on
    parent_custom_module_id
    position
    position_integer
    required
    sublabel
  }
}
```
