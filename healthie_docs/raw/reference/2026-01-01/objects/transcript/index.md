---
title: Transcript | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/transcript/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/transcript/index.md
---

A transcript (in VTT format) of an appointment and associated metadata

## Fields

[`expiring_url` ](#field-expiring-url)· [`String` ](/reference/2026-01-01/scalars/string)· A short-lived URL to download the vtt file

[`id` ](#field-id)· [`String` ](/reference/2026-01-01/scalars/string)· The unique identifier of the transcript

[`status` ](#field-status)· [`TranscriptStatusEnum` ](/reference/2026-01-01/enums/transcriptstatusenum)· The status of the transcript

[`transcript_end` ](#field-transcript-end)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The datetime that the transcript ended

[`transcript_start` ](#field-transcript-start)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The approximate datetime that the transcript started

[`transcript_type` ](#field-transcript-type)· [`TranscriptTypeEnum` ](/reference/2026-01-01/enums/transcripttypeenum)· The type of transcript

## Used By

[`Appointment.transcripts`](/reference/2026-01-01/objects/appointment)

## Definition

```
"""
A transcript (in VTT format) of an appointment and associated metadata
"""
type Transcript {
  """
  A short-lived URL to download the vtt file
  """
  expiring_url: String


  """
  The unique identifier of the transcript
  """
  id: String


  """
  The status of the transcript
  """
  status: TranscriptStatusEnum


  """
  The datetime that the transcript ended
  """
  transcript_end: ISO8601DateTime


  """
  The approximate datetime that the transcript started
  """
  transcript_start: ISO8601DateTime


  """
  The type of transcript
  """
  transcript_type: TranscriptTypeEnum
}
```
