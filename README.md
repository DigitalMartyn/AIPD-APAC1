---
title: AIPD-APAC1
description: Knowledge base for the ELVTR AI Product Development APAC cohort 1
ms.date: 2026-07-29
ms.topic: overview
---

Knowledge base for the **ELVTR — AI Product Development (AIPD)** course, APAC cohort 1.

Content is captured as self-contained knowledge sources — structured, searchable Markdown that can
be referenced, revised, and reused independently of the original slide decks and briefs.
[`lessons/`](lessons/) holds course lesson content; [`assignments/`](assignments/) holds capstone
and course assignments.

## Lessons

| # | Lesson | Knowledge source |
|---|--------|------------------|
| 01 | AI as a Tool for Innovation & Empowering Human-Centred Design | [lessons/01-ai-and-human-centred-design](lessons/01-ai-and-human-centred-design/README.md) |
| 02 | AI Fundamentals: Understanding Machine Learning & Principles | [lessons/02-ai-fundamentals](lessons/02-ai-fundamentals/README.md) |
| 03 | End-to-End Process for Designing AI Products | [lessons/03-end-to-end-process](lessons/03-end-to-end-process/README.md) |
| 04 | Running a Workshop | [lessons/04-running-a-workshop](lessons/04-running-a-workshop/README.md) |
| 05 | Rapid Prototyping | [lessons/05-rapid-prototyping](lessons/05-rapid-prototyping/README.md) |
| 06 | TBC | [lessons/06-tbc](lessons/06-tbc/README.md) |
| 07 | Researching & Testing AI Products | [lessons/07-researching-testing-ai-products](lessons/07-researching-testing-ai-products/README.md) |
| 08 | From Prototype to Scale | [lessons/08-from-prototype-to-scale](lessons/08-from-prototype-to-scale/README.md) |
| 09 | User Interface Design in the Age of AI | [lessons/09-designing-ai-ui-experiences](lessons/09-designing-ai-ui-experiences/README.md) |
| 10 | Ethical AI in Practice | [lessons/10-ethical-ai-design](lessons/10-ethical-ai-design/README.md) |

## Assignments

| # | Assignment | Knowledge source |
|---|------------|------------------|
| 00 | Overall AI Product Design Capstone Brief | [assignments/00-overall-capstone-brief](assignments/00-overall-capstone-brief/README.md) |
| 01 | Define & Frame Your Capstone Concept | [assignments/01-define-frame-capstone](assignments/01-define-frame-capstone/README.md) |
| 02 | Prototype & Test Your Concept | [assignments/02-prototype-test-concept](assignments/02-prototype-test-concept/README.md) |

## Project files

Standalone, cloneable example prototypes referenced by the lessons — each one runs with no build
step so students can clone and try it immediately.

| Project | Description | Path |
|---------|--------------|------|
| Voice Chat Starter | Talk-to-AI prototype demoing the speech-to-text → LLM → text-to-speech pipeline, using the OpenAI API | [project-files/voice-chat-starter](project-files/voice-chat-starter/README.md) |

## Structure

```text
lessons/
  <nn>-<slug>/
    README.md   # the lesson knowledge source
assignments/
  <nn>-<slug>/
    README.md   # the assignment knowledge source
project-files/
  <slug>/
    README.md   # setup + how it works for a standalone example prototype
```

## Conventions

- One folder per lesson or assignment, prefixed with its number (`04-`, `01-`, ...).
- Each folder has a `README.md` as its primary knowledge source.
- Source of truth is the ELVTR Figma deck or assignment brief; this repo is the extracted knowledge.
- Project files are standalone, zero-build, minimal-dependency prototypes with their own README
  covering setup and how they work.
