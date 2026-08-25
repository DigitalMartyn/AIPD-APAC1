# Lesson 05 · Rapid Prototyping

> **Course:** ELVTR — AI Product Development (AIPD1), APAC cohort
> **Lesson:** 05 · Rapid Prototyping
> **Instructor:** Martyn Gooding
> **Framing:** *Prototypes drive clarity — now they run on top of AI. Clarity is the deliverable;
> the prototype is just how we get there.*
> **Source deck:** [ELVTR AIPD1 · 05 · Rapid Prototyping (Figma)](https://www.figma.com/design/AShKsdrKjJ6ixqZpnsj21K/ELVTR-AIPD1-%C2%B7-05-%C2%B7-Rapid-Prototyping)

## Agenda

1. Why we prototype.
2. The types — shown, not told.
3. Vibe coding: the landscape (live: sketch → Figma Make).
4. Vibe debt · what are you prototyping.
5. Prototyping AI behaviour.
6. HAX · open repos · your assignment.

## Carry forward from the workshop

You don't start from scratch — you leave the workshop with artefacts about your idea, and carry them
forward here, starting with the **product proposition**:

> *For [the user] who [need], [your product] is a [category] that [key value] — unlike [the
> alternative].*

Plus the **target user & job** (the job they're hiring it to do), your honest **desirability ·
feasibility · viability** read, and the **prioritised slice** you chose on impact vs effort. Today
you turn that proposition into something you can test.

---

## Section 01 · Why we prototype

Most of this job is **driving clarity**:

- Big multidisciplinary teams — alignment doesn't happen by itself.
- Design artefacts keep everyone building the right thing — no feature creep.
- The prototype is the sharpest artefact in the toolbox.

> **Prototypes are arguments, not artefacts.** A prototype is an argument the customer can *touch* —
> and people give better feedback to things they can play with.

### The types of prototype

Every type trades **speed against truth**:

| Type | Upside | Downside |
|------|--------|----------|
| **Pen & paper** | Fastest to make, easiest to correct | Slowest to share |
| **Wireframes** | Structure without seduction | Static — no behaviour |
| **Clickable** | Flows you can feel | Still no real logic |
| **Vibe-coded** | Working software in hours | Feature-complete by default |
| **UX engineering** | Real AI behaviour, shaped | A diminishing role |

**Clickable wireframes** are a useful jump-off: flows you can feel, behaviour without build cost.

### Recap · Section 01

1. **Prototypes are arguments.** You're persuading a stakeholder, not decorating a screen.
2. **Show, don't tell.** People give better feedback to things they can see and touch.
3. **Match type to question.** Pen, wireframe, clickable, vibe-coded — each trades speed for truth.

> **The takeaway:** pick the cheapest prototype that answers the real question.

---

## Section 02 · Vibe coding

> **Working software is the new wireframe.**

### Vibe coding: an overview

Natural language in, running software out — more change in a year than the previous ten. Pick the
tool for the question, not the fashion:

| Tool | Upside | Downside |
|------|--------|----------|
| **VS Code + Copilot** | Full control, real code | Developer discipline required |
| **Cursor** | AI-native IDE, fast iteration | Easy to lose the thread |
| **Figma Make** | Design-native — sketch straight in | Young and opinionated |
| **Lovable / v0** | Fastest zero-to-app | Feature-complete by default |

> IDEs for depth. Design tools for speed.

**Live demo · sketch → running app (Claude Code).** Hand it a photo of a rough sketch; it scaffolds
components and wires logic; you run, react, and iterate in one loop. *The sketch is the spec — the AI
does the typing.*

### Vibe debt

Fast code hides assumptions:

- You set out to prove one thing — it builds the entire application.
- Feature-complete by default is never your beat.
- Discipline is the new craft: define the features, place them deliberately.

### What are you prototyping?

**A prototype is not a user experience.** Be clear about what you're communicating — don't build the
whole thing:

| Scope | The question |
|-------|-------------|
| **POC** | Can it work at all? |
| **MVP** | Will anyone use it? |
| **Vertical slice** | One journey, end to end. |
| **Feature** | One question, isolated. |

> Start from the proposition you brought from the workshop — prototype its **riskiest assumption**,
> not the whole product.

### Recap · Section 02

1. **Working software is the new wireframe.** You can prototype in hours, not weeks.
2. **It feels real, so it persuades.** A running slice beats a static mock.
3. **Mind the vibe debt.** Fast code hides assumptions — don't ship the scaffolding.

> **The takeaway:** vibe-code to learn, then decide what's worth keeping.

---

## Section 03 · Prototyping AI

> **AI doesn't have an interface — its behaviour is the interface.**

The visible UI is minimal; screens teach you little. So prototype *how the AI turns up, and how it
behaves*.

- **Coaching the AI** — put a terminal on the AI's thinking: a conversational front plus a backend
  view of what the model is doing. You coach it by watching it work, then tune how it turns up.
- **Use the HAX Toolkit** — pull patterns, don't invent them. Microsoft's interaction guidelines for
  human-AI products are ready to lift; use them to choose the right features for your prototype, then
  build only those.
- **Use accelerators & open repos** — don't start from zero. Accelerators get you to
  working-and-secure; open-source repos are the same idea, public (e.g. the VERA voice prototype).

**Live demos:**

- **Zero UI observability** (Langfuse / Arize Phoenix) — there's no screen, so prototype the
  *traces*: watch prompts, tool calls and cost stream through live, and design the moment a human
  needs to step in. *With Zero UI, the observability is the interface.*
- **Figma Make + HAX** — pick one HAX guideline as the design constraint, prompt Figma Make to build
  the feature around it, and pressure-test the AI's behaviour, not just the pixels. *Scope to a
  single feature — let the guideline lead.*
- **Accelerator starter** (Vercel AI SDK `ai-chatbot`) — clone an open AI starter (chat, streaming,
  tools already wired), swap in your model/prompt/data, and get a working AI feature in minutes. Good
  open starters: Vercel AI SDK · create-llama (RAG) · assistant-ui · Chainlit.

### Wireframing at low fidelity

**Low fidelity is a feature, not a shortcut.** Vibe-coded output looks final, so people review the
pixels, not the question — the same trap as when Figma + Fluent made wireframes look finished. Keep
it deliberately rough so feedback lands on the idea.

### Recap · Section 03

1. **AI doesn't have an interface.** The behaviour is the product, not the screen.
2. **Coach the model.** Prompts, examples and guardrails are your design surface.
3. **Borrow before you build.** HAX patterns, accelerators and open repos cut the distance.

> **The takeaway:** prototype the AI's behaviour, and keep the fidelity low.

---

## Section 04 · Ship it

> **Prototype the priority, not the product.**

**Your assignment — what will you prototype, and why?**

- Based on the project you're building: which question needs an answer first?
- Pick the slice deliberately: POC, MVP, vertical slice, or one feature.
- Be honest about time — prototype the priority, not the product.

Bring your answer to the next session; we'll pressure-test the slice, not the pixels.

### Recap · Section 04

1. **Prototype the priority.** Answer the riskiest question first, not the whole product.
2. **Pick the slice deliberately.** POC, MVP, vertical slice or one feature — choose on purpose.
3. **Clarity is the deliverable.** Ship the smallest thing that makes the argument.

> **The takeaway:** bring a sharp slice to the next session, not a polished product.

---

## In summary · Four things to hold onto

1. **Prototypes are arguments** — you're persuading a stakeholder, not decorating a screen.
2. **Vibe coding is real** — working software is the new wireframe, but mind the vibe debt.
3. **AI has no interface** — prototype the behaviour and coach the model, not just the UI.
4. **Clarity is the deliverable** — ship the smallest thing that proves the point.

> Clarity is the deliverable. The prototype is just how we get there.

---

## Related work

- Rapid prototyping feeds your **capstone** (Assignment 01 defines the AI product you'll prototype,
  refine and present).
- The prototype you build here is the input to **Assignment 02 · Prototype & Test** (Lessons 5 + 7).

## Referenced tools & links

- **Microsoft HAX Toolkit** — interaction guidelines for human-AI products.
- **Vibe-coding tools** — VS Code + Copilot · Cursor · Figma Make · Lovable / v0.
- **Observability** — Langfuse · Arize Phoenix.
- **Open starters** — [`github.com/vercel/ai-chatbot`](https://github.com/vercel/ai-chatbot) ·
  create-llama (RAG) · assistant-ui · Chainlit.
- **VERA** voice prototype — open-source reference repo.
