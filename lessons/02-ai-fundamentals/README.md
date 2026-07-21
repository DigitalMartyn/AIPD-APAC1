# Lesson 02 · AI Fundamentals — Understanding Machine Learning & Principles

> **Course:** ELVTR — AI Product Development (AIPD1), APAC cohort
> **Lesson:** 02 · AI Fundamentals: Understanding Machine Learning and Principles
> **Framing:** *An LLM product guide — the concepts every AI product designer should know, and why
> each one changes how you design.*
> **Source board:** [ELVTR AIPD1 — 02 AI Fundamentals (FigJam)](https://www.figma.com/board/iw7qf7LzT0SrfQHxVPIMQf/ELVTR-AIPD1---02-AI-Fundamentals--Understanding-Machine-Learning-and-Principles)

This knowledge source captures the deck's concept, diagram, and example cards, organized under the
deck's three sections. A recurring lens on every concept card is **"why it matters for
designers."**

> **Scope note:** the source deck also contains ~27 narrative "Slide" frames within these three
> sections whose text lives in Figma components not exposed by the board API. This document
> captures the fully-readable concept/diagram/example cards plus the section structure; the
> narrative walkthrough slides are summarized rather than transcribed verbatim.

## Sections

1. **How LLMs Work** — what AI is, the layers of the stack, and the core vocabulary.
2. **Known Capabilities** — how models become products, and the trade-offs that shape them.
3. **Risks & Opportunities** — designing safe control points around AI actions.

---

## 1 · How LLMs Work

### What is AI?

Artificial Intelligence is the broad field of building systems that can perform tasks that
typically require human intelligence — perceiving, reasoning, deciding, generating.

AI isn't one thing. The term covers a wide range of techniques, tools, and systems, each with
different behaviours, failure modes, and design implications.

> **Why it matters for designers:** knowing which type of AI is in your product changes what users
> can expect, where it fails, and how you design around it.

### AI vs ML vs Generative AI

These terms are often used interchangeably but they're **nested, not synonymous**:

- **AI** — the umbrella. Any system mimicking human cognition.
- **Machine Learning** — AI that learns patterns from data rather than explicit rules.
- **Deep Learning** — ML using layered neural networks; powerful for images and language.
- **Generative AI** — models that produce new content: text, images, code, audio.

Think of it as nested circles: **Generative AI ⊂ Deep Learning ⊂ ML ⊂ AI**.

> **Why it matters for designers:** when someone says "AI feature," ask which layer they mean. The
> design implications of a recommendation algorithm are completely different from a generative text
> feature.

### The AI Stack

*Real product — Spotify Discover Weekly.* From data to a finished feature, the stack runs:

**Data** (your listening history) → **Training** (patterns across millions of users) → **Model**
(recommendation engine) → **API** (Spotify internal) → **Product** (your Monday playlist).

> The model never "knows" you — it *infers*. **Design for inference, not memory.**

### Types of AI in products

*Real products — Figma AI vs Midjourney vs Perplexity.* Three AI types, three design implications:

- **Figma AI** = LLM for text + ML for design suggestions.
- **Midjourney** = image-generation model.
- **Perplexity** = LLM + live web retrieval (RAG).

Each has different failure modes, latency profiles, and trust expectations. **Know which you're
designing for.**

### Foundation vs Fine-tuned vs RAG

- **Foundation model** — trained on vast general data. Knows a lot, specialises in nothing.
- **Fine-tuned model** — a foundation model further trained on specific domain data. Narrower but
  sharper.
- **RAG (Retrieval-Augmented Generation)** — the model retrieves relevant documents at query time
  before generating. Stays current, no retraining needed.

> **Why it matters for designers:** RAG introduces *retrieval failure* as a new error state.
> Fine-tuning introduces *scope limits*. Know which your product uses — it changes what "good"
> looks like and how you design for errors.

### Tokens & context windows

- **Token** — the basic unit a model reads and writes. Roughly ¾ of a word ("designer" = 2
  tokens).
- **Context window** — the total text (input + output) a model can hold in memory at once. Beyond
  this, it forgets.

Models have no memory outside the context window. When a conversation exceeds it, earlier content
is silently dropped.

> **Why it matters for designers:** long documents, multi-step tasks, and extended conversations
> hit context limits. Design must account for what happens at the edges — when the model forgets
> something the user assumed it remembered.

---

## 2 · Known Capabilities

### The AI Product Stack

How foundation models become the products you use every day (top built on the layer beneath):

1. **Products** — ChatGPT · Siri · Microsoft Copilot · Gemini · Claude.ai · Perplexity. Consumer-
   facing applications; users interact with products, never directly with the model underneath.
2. **API / integration layer** — OpenAI API · Azure OpenAI · Gemini API · Anthropic API · system
   prompts · RAG pipelines. Companies access models via API and wrap them in system prompts and
   product logic.
3. **Foundation models** — GPT-4o (OpenAI) · Gemini (Google) · Claude (Anthropic) · Llama (Meta) ·
   Grok (xAI) · Mistral. Pre-trained on internet-scale data at a cost of $10M–$100M+. Most
   companies never build one — they rent access. (Apple pays ~$1B/year for Gemini access; OpenAI
   is embedded in Siri for complex queries.)

> Only a handful of companies can afford to train foundation models. **The product layer is where
> design decisions live.**

### The Quality / Speed / Cost trade-off

| Quality | Speed | Cost |
|---------|-------|------|
| More capable models, more accurate outputs. Usually slower and more expensive. | Faster responses, lower latency. Often requires smaller or cached models. | Compute cost per response, which affects pricing and product margins. |

> Optimising for two usually compromises the third. Know where your product sits **before**
> designing latency expectations and error handling.

### Example · Foundation vs Fine-tuned vs RAG

*ChatGPT vs Harvey vs Perplexity:*

- **ChatGPT** = general foundation model.
- **Harvey** = fine-tuned on legal case law.
- **Perplexity** = foundation model + live web retrieval (RAG).

Fine-tuned feels more precise but has a narrower scope. RAG feels current but introduces retrieval
failure as a new error state to design for.

### Example · Foundation model vs product

Every major AI product runs on **someone else's model**:

- GPT-4o → ChatGPT, Copilot, Siri (complex queries)
- Gemini → Siri (future, ~$1B/yr), Google Search AI
- Claude → Claude.ai, Slack AI
- Llama → Meta AI, WhatsApp AI

Most companies — even Apple — don't build models. They rent access to someone else's.

### Example · How Siri's architecture works

One product, multiple models — three tiers:

- **Tier 1 (on-device):** Apple Intelligence. Private tasks, never leaves the device.
- **Tier 2 (private cloud):** Apple's own cloud model. Apple-controlled privacy.
- **Tier 3 (third-party):** OpenAI ChatGPT now + Google Gemini finalising (~$1B/yr).

> **Design note:** latency, privacy, and capability differ per tier — design for which tier
> handles each task. When you ask Siri a complex question, you're sometimes talking to OpenAI.

---

## 3 · Risks & Opportunities

### Pattern · Human-in-the-Loop

Designing moments where humans **review, approve, or override** AI actions — especially critical as
autonomy increases. Core controls: **preview before action → approval gates → async review →
override controls**.

> **Why it matters for designers:** the more irreversible the action, the more explicit the
> confirmation should be. Show the actual consequence, not a generic "Are you sure?"

### Example · Approval gates for irreversible actions

*Real product — Cursor Workspace.* Before applying changes across an entire codebase, Cursor shows
a summary of what will change, which files, and why — the user confirms before execution.

> "This will edit 14 files across 3 directories" is better UX than "Are you sure?" — **show the
> actual consequence in plain language.**

---

## Principles at a glance

- AI is a family of techniques, not one thing — name the layer (ML, deep learning, generative).
- Design for **inference, not memory**: models infer from patterns and forget outside the context
  window.
- Every product sits on a **stack** (foundation model → API → product); design lives at the product
  layer.
- Choose the model approach — **foundation, fine-tuned, or RAG** — knowing each brings its own error
  state.
- Balance **quality, speed, and cost**; optimising two compromises the third.
- As autonomy rises, design **human-in-the-loop** control points and show real consequences before
  irreversible actions.
