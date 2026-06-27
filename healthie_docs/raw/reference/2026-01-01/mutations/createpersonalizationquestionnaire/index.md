---
title: createPersonalizationQuestionnaire | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpersonalizationquestionnaire/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpersonalizationquestionnaire/index.md
---

create Personalization Questionnaire

## Arguments

[`input` ](#argument-input)· [`createPersonalizationQuestionnaireInput` ](/reference/2026-01-01/input-objects/createpersonalizationquestionnaireinput)· Parameters for createPersonalizationQuestionnaire

## Returns

[`createPersonalizationQuestionnairePayload`](/reference/2026-01-01/objects/createpersonalizationquestionnairepayload)

## Example

```
mutation createPersonalizationQuestionnaire(
  $input: createPersonalizationQuestionnaireInput
) {
  createPersonalizationQuestionnaire(input: $input) {
    messages
    was_saved
  }
}
```
