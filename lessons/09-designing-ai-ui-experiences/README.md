---
title: "Lesson 09: User Interface Design in the Age of AI"
description: Design-system context, MCP workflows, verification, and generative UI patterns for AI product interfaces
author: Martyn Gooding
ms.date: 2026-08-09
ms.topic: concept
keywords:
  - AI user interfaces
  - design systems
  - design tokens
  - Model Context Protocol
  - generative UI
---

## Lesson details

> **Course:** ELVTR AI Product Design (AIPD1), APAC cohort
> **Lesson:** 09, User Interface Design in the Age of AI
> **Instructor:** Martyn Gooding
> **Source deck:** [ELVTR AIPD1: 09 Designing AI UI Experiences](https://www.figma.com/design/xjEitGbwo3zSveBEBHdkVH/ELVTR-AIPD1---09-Designing-AI-UI-Experiences?node-id=79-38736&m=dev)

AI can imitate a design system without actually using it. This lesson moves from that distinction
to a workflow in which AI receives current, queryable system context, generated output is verified,
and interfaces adapt within controlled design-system rules.

## Contents

1. How AI is changing UI design: limits, tokens, and structural verification
2. Building with a design system: MCP as the context bridge
3. Making it real: prompt, output, and component checks
4. Generative UI: stable systems and adaptive conditions

## Section 01: How AI is changing UI design

AI changes how interfaces are produced, but it does not remove the need for a design system. The
working question is not whether generated UI looks plausible. It is whether the output remains
connected to the decisions, components, and governance behind the system.

### What AI cannot do reliably

| Limitation | Consequence |
|------------|-------------|
| Build the system | AI cannot reliably create the governance, architecture, and decisions behind a mature design system |
| Use it faithfully | A system-looking screen may still be detached from real tokens and components |
| Ship components | Generated frames need verification before they become production-ready UI |

### Do not trust perfect-looking output

Generated UI can look right while being structurally wrong. Common warning signs include:

* Groups instead of auto layout, making the design hard to resize, adapt, or reuse
* Styled copies instead of components, creating familiar-looking output disconnected from the
  library
* Static values instead of tokens, forcing visual changes to be repaired manually

Treat visual fidelity as evidence to inspect, not proof of system integrity.

### Tokens expose design decisions

Tokens store the visual DNA of a design system as values that tools and models can read. They can
represent:

* Colour and border values
* Corner radii and shadows
* Font family, size, weight, and line height
* Motion values
* Spacing, padding, margins, and grid scales
* Width, height, and minimum or maximum dimensions
* Layering and z-index

Token architecture moves from general values to increasingly specific decisions:

| Layer | Purpose | Example |
|-------|---------|---------|
| Primitive | Stores raw values | `grey-14`, `white`, `16px` |
| Semantic | Describes intended use | `neutral-foreground-1`, `neutral-background-2` |
| Component | Applies a semantic choice to a component property | `button-text-color`, `button-background-color` |

The underlying values are the mathematics beneath the design. Large language models primarily
consume text, so named tokens and documented associations make visual intent available as
structured context.

### From redlines to system references

Traditional handoff documents every dimension and colour as redlines. A system-connected handoff
references existing components, semantic tokens, spacing scales, typography roles, and state
behaviour instead. This creates a single source of truth that can flow from the design library to
the MCP, generated designs, and production code.

### Section 01 recap

1. AI can imitate output, but it does not create the governance behind a mature system.
2. Tokens expose design intent as structured context.
3. A convincing screen can still be detached from the system, so structure needs verification.

> [!IMPORTANT]
> Treat visual fidelity as evidence to inspect, not proof of system integrity.

## Section 02: Building with a design system

Give AI current system context, then verify what it used. Model Context Protocol (MCP) provides the
bridge between an AI workflow and the source design system.

### Why use a design-system MCP

| Without MCP | With a design-system MCP |
|-------------|--------------------------|
| Hallucinated props invent component APIs that do not exist | Current guidance retrieves up-to-date component documentation |
| Stale patterns use an old implementation after the system has moved on | Targeted search finds only the patterns needed for the task |
| Too much context loads whole documentation sets and loses the task | Implementation context returns relevant props, examples, and accessibility guidance |

Connecting Figma through MCP makes the source queryable. The model can inspect components, tokens,
screenshots, and structure instead of guessing from a prompt. Tokens turn a request such as "make
it on-brand" into concrete constraints for colour, stroke, radii, and size.

### Section 02 recap

1. Retrieve current guidance to avoid stale patterns and invented component APIs.
2. Query the source to inspect components, tokens, screenshots, and structure.
3. Constrain the model with system evidence instead of a visual mood.

> [!IMPORTANT]
> The better the context, the less the model has to guess.

## Section 03: From prompt to verified output

The live workflow starts in an AI tool with a direct request, such as:

```text
Create a basic SaaS dashboard using the Fluent UI MCP.
```

The agent searches the system, builds the interface, renders it, checks the result, and refines the
output. A first pass may produce navigation, cards, data display, and hierarchy together, but a
plausible result is not the end of the workflow.

### Verification sequence

1. Prompt from the AI tool and name the design-system MCP as part of the request.
2. Inspect hierarchy, behaviour, and visual fidelity in the generated result.
3. Confirm that tokens are linked rather than reproduced as static values.
4. Confirm that component instances are real rather than styled copies.
5. Use a follow-up prompt when needed to bind generated output to real components.

The critical demo question is: **Did it use the system?** Visual fidelity is only the first check.
Confirm the underlying token and component connections.

> [!IMPORTANT]
> Generation is the start of the workflow. Verification makes it useful.

## Section 04: Generative UI

Generative UI allows an interface to compile different presentations from the same system
conditions. The system and interaction contracts remain stable while the presentation adapts in
real time.

### Design conditions, not screens

Define the rules that determine disclosure, density, ordering, and emphasis:

1. Keep components stable by reusing the same interaction and accessibility contract.
2. Change conditions by allowing user state, task, and environment to influence presentation.
3. Compile the most useful arrangement for the moment.

### Conditions that can shape presentation

| Condition | Adaptation |
|-----------|------------|
| Experience level | A beginner receives clear starting points, progressive disclosure, guidance, and reassurance; an expert receives density, scanning, comparison, and direct control |
| Familiarity | First-time use begins with a concise summary; returning use compresses familiar context and foregrounds open decisions or changes since the previous visit |
| Mood or sensory need | A calm mode softens pacing, contrast, and emphasis while preserving a familiar interaction model |
| Current task | Discovery, review, comparison, or repeated action can produce different arrangements from the same component set |

The goal is not unlimited styling. It is controlled adaptation from system rules.

### The generative UI spectrum

Generative UI is a spectrum rather than a single technique.

| Approach | Model behaviour | Trade-off |
|----------|-----------------|-----------|
| Static | Selects from a fixed library of hand-built components | Highest control, limited flexibility |
| Declarative | Returns a schema describing cards, lists, widgets, and other approved elements | Balanced control and flexibility; composition becomes the risk |
| Open-ended | Generates raw HTML and CSS for the client to render | Maximum flexibility with security, styling, and governance risk |

At the open-ended end of the spectrum, the model is composing rather than choosing from a fixed
vocabulary. It can create novel layouts nobody designed or reviewed. Because the output is
rendered as code, that is also where risk enters.

### Costs of open-ended generation

| Risk | Design and engineering response |
|------|---------------------------------|
| Injection | Render only pre-approved and audited output, or isolate generated markup in a sandbox using least privilege |
| Testing | Test that an intended control exists and works rather than asserting its exact pixel position |
| Latency | Stream UI as it arrives and cache structures for similar requests |
| Accessibility | Encode roles and labels in the schema so the renderer supplies appropriate semantics by component type |

### Machine-readable design guidance

A `design.md` file can place human-authored brand and interaction guidance in front of the model at
generation time. It can describe rules in prose:

```markdown
# Design guidelines

## Layout

One primary action per view.
Never more than three cards at once.

## Type

Titles: 20/26, two lines maximum, then truncate.

## Colour

Tokens only. Never introduce a new hue.

## Never

No modals. No carousels.
Red is reserved for destructive actions.
```

This guidance is accessible to designers because it is prose rather than code. It travels with
tokens and system context, but it steers rather than enforces. Reviews, evaluations, and a named
owner must detect and resolve violations.

### What changes for designers

| Previous focus | Generative UI focus | Example boundary |
|----------------|---------------------|------------------|
| Design the screen | Design the vocabulary | Only approved types such as `workItem`, `email`, `meeting`, and `copilot` can render |
| Draw every state | Bound every state | A title wraps to two lines at 392px and then truncates |
| Approve a mockup | Approve the worst case | Test the longest title, empty body, and longest button label together |

Designers define what the model is allowed to say, the bounds of every state, and the worst-case
combinations the generated interface must survive.

### Section 04 recap

1. Conditions such as task, familiarity, and mood shape presentation.
2. Components preserve behavioural and accessibility continuity across modes.
3. The interface compiles a useful arrangement in real time.

> [!IMPORTANT]
> Generative UI is controlled adaptation from system rules, not unlimited styling.

## Practical workflow

Use this sequence when creating an AI-assisted interface:

1. Establish a maintained design system with tokens, components, documentation, and governance.
2. Make that source queryable through a design-system MCP or equivalent context service.
3. Request only the context needed for the task.
4. Generate an interface using current components and tokens.
5. Inspect the rendered result for hierarchy, behaviour, and visual fidelity.
6. Verify token links, component identity, layout structure, responsiveness, and accessibility.
7. Test worst-case content and failure states, not only the ideal example.
8. Record unresolved mismatches and iterate until the output is structurally connected.

## Lesson summary

1. AI can imitate a design system without using it.
2. MCP gives the model current, queryable system context.
3. Generated output still needs component and token checks.
4. Generative UI changes conditions, not the underlying contract.

**Design systems make adaptation governable.**

## Assignment 03 status

> [!NOTE]
> The source deck intentionally leaves Assignment 03 unconfirmed. Its title, deliverables, points,
> and due date remain open until the course brief is supplied.