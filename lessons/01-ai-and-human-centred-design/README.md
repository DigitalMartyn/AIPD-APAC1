---
title: "Lesson 01: AI as a Tool for Innovation and Empowering Human-Centred Design"
description: Deciding when AI is the right answer, framing solution-free problem statements, and the three decisions that shape an AI experience
author: Martyn Gooding
ms.date: 2026-08-26
ms.topic: concept
keywords:
  - human-centred design
  - problem framing
  - AI capability
  - AI product lifecycle
  - AI roles
---

## Lesson details

> **Course:** ELVTR AI Product Development (AIPD1), APAC cohort
> **Lesson:** 01, AI and Human-Centred Design
> **Instructor:** Martyn Gooding
> **Working question:** When is AI the right answer?
> **Deck:** [Lesson 01 slides](https://www.figma.com/slides/J048gt9ZAMUSYmuyyGL9IK)
> **Instructor:** [run sheet and timings](RUNSHEET.md)

Design work now starts earlier than the screen. When a model can produce a plausible interface in
seconds, the scarce skill becomes deciding what deserves to exist, and for whom. This lesson gives
you a test for whether AI belongs in a product at all, then the language to frame the problem it
solves.

## Outcomes

By the end of the session you can:

1. Decide whether AI is genuinely the right answer to a problem, and say why.
2. Write a solution-free problem statement with a named user in a named context.
3. Explain what Assignment 01 asks for and how it is graded.

## Contents

1. Design has changed: execution gives way to judgment
2. AI is not the product: design the capability
3. Three decisions that shape the AI experience
4. Framing the problem: the two statements
5. Where this goes: the AI product lifecycle

---

## Section 01: Design has changed

The old pipeline broke. The middle-person job, owning the file and handing it off, has gone. What
replaces it is a different job: deciding what is worth building, then building it.

| Then | The break | Now |
|------|-----------|-----|
| Own Figma. Hand off. Wait for someone else to ship. | AI collapsed the handoff between idea and build. | Figure out the right thing, then build it yourself. |

### The curator's seven moves

The role shifts from specialist to curator, assembling and directing AI-generated work into a
product. Creativity expands rather than shrinks.

| Move | What it means |
|------|---------------|
| Frame the problem | Decide what is actually worth solving |
| Ground it in the user | Keep the real human need in view |
| Direct the AI | Set the intent and steer the output |
| Assemble the pieces | Compose generated parts into a whole |
| Verify the facts | Check that what the model produced is true |
| Set the guardrails | Define the limits it must work within |
| Own the outcome | You remain accountable for the result |

Moves one and two carry the rest of this lesson. The remaining five return in Lesson 02 and
Lesson 07.

---

## Section 02: AI is not the product

Nobody wants AI. They want a job done faster, more easily, or better than before. So get clear on
what the product actually is before designing it.

A feature is something a product already does. A capability is something AI makes possible that was
not possible before.

### The test

> Remove the AI. Does the product still exist?
>
> Yes, it is a feature. No, it is a capability.

| Feature: autocomplete | Capability: Copilot |
|-----------------------|---------------------|
| Corrects what you already wrote | Writes what you had not yet written |
| Same task, fewer typos | A new task becomes possible |
| Remove the AI and you still type | Remove the AI and there is nothing |

> **Why it matters for designers:** the answer sets your design scope. A feature inherits the trust
> the product already has. A capability has to earn it, which means error states, confidence
> signals, and a way for the person to check the work. Decide which you are building before
> designing a single screen.

The test is a threshold, not a wall. The sharper question is one of degree: how much of the user's
job disappears when you remove the model?

| Autocomplete | Copilot | Adobe Express AI mode |
|--------------|---------|-----------------------|
| The model helps you type | The model does a task you could not | The model does the job |

Lesson 03 works through Adobe Express AI Assistant, where the team moved from a chat panel to an
assistant that acts on the canvas. Same idea, fully evidenced.

---

## Section 03: Three decisions that shape the AI experience

Once you know you are designing a capability, you owe three decisions about where the human sits.
Neither pole is correct in isolation. The trade-off is the design decision.

| Decision | One side | Other side | Ask |
|----------|----------|------------|-----|
| Who does the work? | Search: you get a list of links, read them, and work out the answer yourself | Answers: you get one answer written for you, and you check it is right | Does the person still do the work, or does the AI? It changes what they need from you |
| Steps or goal? | Buttons: press the steps in order, quick once learned | Just ask: say what you want in plain words and the AI works out the steps | Does the person know the steps, or just the goal? Let them ask when the steps are hard |
| Prevent or undo? | Undo: the person spots the mistake and fixes it | Prevent: the product stops the mistake first | Will the person notice a wrong answer? If not, stop the mistake before it happens |

> **Why it matters for designers:** these three decisions set what the interface has to show, what
> has to be reversible, and how much the person needs to understand about what just happened.
> Lesson 02 picks up the third as human-in-the-loop control.

### Worked case: Cursor

Before applying changes across a codebase, Cursor states the actual consequence.

> "This will edit 14 files across 3 directories" beats "Are you sure?"

Show the real consequence, not a generic confirmation. Lesson 02 returns to this pattern as
human-in-the-loop control.

---

## Section 04: Framing the problem

Assignment 01 puts 12 of its 20 points on problem framing and user definition, so this section
carries the most weight in the room.

Two statements about the same situation:

| Verdict | Statement |
|:-------:|-----------|
| ✗ | Warehouse supervisors need an AI dashboard |
| ✓ | Warehouse supervisors cannot tell which of 40 open exceptions actually needs them today |

The first forecloses every solution. The second names a decision a person cannot make.

The same move, applied to the examples from Sections 02 and 03:

| ✗ Solution-shaped | ✓ Problem-shaped |
|-------------------|------------------|
| Developers need AI-powered code completion | Developers lose their place re-typing method names they used ten lines above |
| Developers need an AI coding assistant | Developers spend more time recalling syntax and writing boilerplate than solving the problem they were hired to solve |
| The app needs simpler navigation | Daily users hit the same four screens every morning and want them one click away |
| The app needs an AI chat assistant | Occasional users know what they need from the data but not which of forty menu items produces it |
| Users need an undo button | People clearing out old files cannot tell which ones they will want back until after they are gone |
| Plant managers need predictive maintenance | Plant managers cannot tell which machine fails next week, and finding out costs a day of production |

Every statement in the right column names a person and a moment. None of them contains the word AI.

### Exercise: write your pair

Take the idea you walked in with and write both versions of it. The second version must name a
role, a context, and the decision they cannot make. No solution words: if the sentence contains the
answer, it is not a problem statement.

Read-outs are diagnosed against three checks:

1. Is there a solution hiding inside the sentence?
2. Can you picture the person, in a place, on a day?
3. Is there a decision they cannot make right now?

> [!TIP]
> **Go one level deeper.** Once you have the statement, ask why the situation exists at all. Why
> *are* there 40 exceptions? If the system surfaces too many because a confidence threshold sits
> too low, the strongest answer may be to reduce 40 to 10 before anything reaches the supervisor,
> and only then help them prioritise what is left. Root-cause the problem before designing for it,
> or you will spend your effort making a symptom easier to live with.

---

## Section 05: Where this goes

Preview only. Lesson 03 covers the lifecycle in full, with two real case studies.

| Stage | Stage |
|-------|-------|
| 01 Problem and Signal | 05 Private Preview |
| 02 Product Definition | 06 Public Preview |
| 03 Engineering Build | 07 General Availability |
| 04 Release Readiness | 08 Operate and Iterate |

Design leads at stage 02 and again at stage 05. Stage 08 re-enters stage 01, which is why
Assignment 01 is a credible starting point rather than a specification.

## Related assignment

[Assignment 01, Define and Frame Your Capstone Concept](../../assignments/01-define-frame-capstone/README.md)
spans Lessons 01 to 03. From here on, everything builds on one AI product concept.

The deliverable covers a solution-free problem statement, a target user with their context, and the
role AI plays. That role is named from a fixed vocabulary:

| Role | Example |
|------|---------|
| Predict | Churn scoring |
| Generate | Draft copy |
| Classify | Routing a ticket |
| Guide | Next best action |
| Assist | Co-editing |

> **Why it matters for designers:** each role fails differently. A wrong prediction stays invisible
> until later. A wrong classification sends work to the wrong place. A wrong generation sits right
> there on screen. The role tells you what "wrong" looks like and where the person needs to
> intervene.

See the assignment page for format, weight, rubric, and submission details.

> [!NOTE]
> Career positioning content that previously sat in this lesson, covering hands-on expectations,
> merging teams, and AI-native careers, now lives in
> [Lesson 12, Professional Development](../12-professional-development/README.md).
