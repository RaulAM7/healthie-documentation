---
title: deleteTranscript | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletetranscript/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletetranscript/index.md
---

Delete a transcript (realtime capture or processed recording)

## Arguments

[`input` ](#argument-input)· [`DeleteTranscriptInput` ](/reference/2026-01-01/input-objects/deletetranscriptinput)· Parameters for DeleteTranscript

## Returns

[`DeleteTranscriptPayload`](/reference/2026-01-01/objects/deletetranscriptpayload)

## Example

```
mutation deleteTranscript($input: DeleteTranscriptInput) {
  deleteTranscript(input: $input) {
    messages
    success
    transcript_id
  }
}
```
