# Contra Project — Meeting Audio to Notes, Actions & Bilingual SRT

## Project title

Meeting Audio → Notes, Actions & Bilingual SRT

## Short description

A transcript-first workflow that transcribes a meeting, applies human correction, extracts decisions and action items with owners and due dates, and packages English, Chinese, and bilingual subtitles.

## Project type

Audio automation · Transcription · Meeting notes · Subtitles · Python

## The problem

A meeting recording contains decisions, risks, and next steps, but raw ASR is not ready to send. Names, numbers, and similar-sounding words get misrecognized. Turning the recording into an action list and subtitles is still manual work.

## What I built

- Synthetic meeting audio and ground-truth transcripts
- Vosk ASR with word timestamps
- Word error rate measurement against ground truth
- Human-corrected transcript used for final notes
- Rule-based extraction of key points, decisions, risks, and action items
- Owner, task, due date, due phrase, and source sentence for each action
- English, Chinese, and bilingual SRT generation
- Excel workbook with dashboard, meetings, actions, decisions, risks, key points, and transcript segments
- Self-contained proof page and captioned walkthrough

## Demo results

| Metric | Result |
|---|---:|
| Meetings | 3 |
| Audio duration | 4:21 |
| Raw ASR WER* | 19.5% |
| Action items | 13 |
| Decisions | 3 |
| Risks | 3 |
| Captions | 25 |
| Automated tests | 6 / 6 passed |

\* Measured on synthetic ground-truth transcripts. The final notes use the human-corrected transcript.

## What was validated

- ASR output and word timings
- WER against ground truth
- Date parsing for “by Wednesday”, “next Tuesday”, and explicit dates
- Action item extraction with owner and task
- Decision and risk separation
- English / Chinese / bilingual SRT generation
- Excel workbook generation

## Deliverables

- Meeting notes (Markdown)
- Action-item CSV
- Decisions and risks CSV
- Excel workbook
- English SRT
- Chinese SRT
- Bilingual SRT
- Sample MP3 audio
- Repeatable source script
- README with assumptions and limits

## Stack

Python 3.15, Vosk, openpyxl, Pillow, imageio-ffmpeg, Windows Speech Synthesis for the synthetic audio.

## Status

**Independent demo — synthetic audio.** No client names, logos, testimonials, or revenue claims are used.

## CTA

Send one sample recording and the output format you need. I will confirm fit, scope, and a fixed price before work starts. A small paid pilot is available for one meeting.

## Proposal template

Hi [name] — I saw you need [specific meeting output].

I built a similar demo: [case page / sample output link]. For your recording, I would:

1. Check the audio quality and run ASR with timestamps
2. Apply a human correction pass for names, numbers, and terms
3. Extract decisions, risks, and action items
4. Package notes and the subtitle format you need

The main risk is [overlapping speakers / noisy audio / missing names], so I would review a short sample before scaling. We can start with a paid pilot on one meeting and expand only if the output meets your spec.

## Service listing

### Meeting Notes + Action Items — from $95

- Up to 45 minutes of audio
- Summary, key points, decisions, risks, action items
- CSV/Excel action list
- English transcript
- 2-day delivery
- 2 revisions

### Bilingual Meeting Subtitles — from $120

- English + Chinese SRT
- Bilingual SRT
- Timestamped transcript
- Glossary/name pass
- 2-day delivery

### Recurring Meeting Pack — from $280

- Weekly or monthly meeting batch
- Notes, action items, decisions, risks
- English/Chinese/bilingual subtitles
- Excel workbook and exception/review queue
- Optional monitoring quote
