# Lesson 03 · End-to-End Process for Designing AI Products

> **Course:** ELVTR — AI Product Development (AIPD1), APAC cohort
> **Lesson:** 03 · End-to-End Process for Designing AI Products
> **Theme:** *How AI products move from a request or an idea, through build, to scale —
> grounded in two real case studies.*
> **Source board:** [ELVTR 03 · End-to-End Process for Designing AI Products (FigJam)](https://www.figma.com/board/qUe7gjHa3InrBp735gh5o8/ELVTR-03-%C2%B7-End-to-End-Process-for-Designing-AI-Products)

This knowledge source captures the lesson's two models for building AI products, a side-by-side
comparison, and two worked case studies (Spotify Wrapped Archive 2025 and Adobe Express AI
Assistant).

## Agenda

1. Two ways to build AI products.
2. The end-to-end process.
3. Case study · Spotify Wrapped Archive.
4. Case study · Adobe Express AI Assistant.
5. Lessons for your practice.

---

## 1. Two ways to build AI products

The lesson contrasts two delivery models. The core difference is **not quality — it is starting
condition**. Forward Deployed Engineering starts with one customer and proves value; Product
Groups start with scale and prove reliability. **Both are necessary.**

| Dimension | Forward Deployed Engineering | Product Group |
|-----------|------------------------------|---------------|
| **How work starts** | A request comes in through a single, structured intake form; a central team reviews it before any engineering begins. | Product Managers own the roadmap. Work comes from strategy, customer feedback, or partner signals — not a shared intake queue. |
| **Role of design** | Designers are embedded from the start — running discovery, shaping the problem, co-building alongside engineers in the same engagement. | Design involvement varies widely by team and feature. There is no formal design gate in the standard release lifecycle. |
| **What proof looks like** | A successful outcome for one specific customer, in production, under real conditions. The customer result is the proof. | Telemetry at scale. Does the feature work reliably for millions over time? Usage data and support signal are the proof. |
| **What MVP means** | A production-intent build: real infrastructure, real data, deployed to a live customer — not a prototype or PoC. | A Private Preview: feature-complete enough to test with a small group, but not yet under full service-level commitments. |
| **Team ownership** | Time-boxed crews. A team works intensively on one engagement, then moves on. Ownership is project-scoped. | Long-lived product teams. The same team builds, ships, operates, and iterates on the same product continuously. |
| **Speed of feedback** | Real-time. Customer reaction and usage shape the build while it is still happening. | Structured cycles. Telemetry, support cases, and user research inform the next planning and sprint cadence. |
| **Core tension** | Moving fast enough to prove value — without eroding trust with the customer you are building for. | Shipping quickly enough to stay competitive — while meeting the reliability, scale, and support standards required for GA. |

---

## 2. The end-to-end process

### Process A · Forward Deployed Engineering — from request to scale

How enterprise AI products move from an initial request through discovery, build, and into
production — and how the work gets reused at scale. Each step is annotated with the **design
role**: `CORE DESIGN WORK`, `DESIGN INVOLVED`, or `LIGHT / NOT A GATE`.

| # | Step | What happens | Design role |
|---|------|--------------|-------------|
| 01 | **Request Submission** | Requests from account/sales, executive escalation, partner/ISV, or internal business units — all through a single intake form. | *Light.* Translate the stated problem into a clear brief; separate what was asked for from what is needed. |
| 02 | **Request Review** | A central team checks completeness and fills gaps. Enough to qualify? If not, go back for clarity. | *Involved.* Challenge scope — right problem? Symptoms or causes? |
| 03 | **Qualification & Routing** | Weekly cross-functional call (engineering, sales, industry, product): right problem for this team? Priority? Who owns it? | *Involved.* Map the customer journey to locate where the AI intervention sits. |
| 04 | **Technical Assessment** | Customer-facing discovery. Define what will be built, validate feasibility, surface production constraints. Output: a signed-off scope. | *Involved.* Review constraints for UX feasibility — latency, data, fallback states. Flag risks before build. |
| 05 | **Commercial & Legal** | Funding confirmed, offer type locked, legal signed. Nothing enters delivery without clearing this gate. | *Light.* Confirm the agreed scope is design-compatible. |
| 06 | **Co-Build & Delivery** | Engineers work hands-on alongside the customer's team — building together, not consulting from the sidelines. | **Core.** Fully embedded: usability tests, iterating interface/interaction design, QA against brief. Most design happens here. |
| 07 | **Production & Knowledge Capture** | A production solution or production-ready MVP ships; document what was built and learned; capture reusable patterns. | *Involved.* Document patterns, edge cases, handover notes. |
| 08 | **Scale & Reuse** | Patterns become reusable building blocks; feedback loops into the roadmap; solutions replicate across industries. | *Light.* Review assets for reuse; formalise patterns into components/templates. |

> **MVP here means production-intent, not throwaway.**

### Process B · Product Group — from idea to General Availability

How a product or feature moves from initial idea through build, testing, release, and into ongoing
operation.

| # | Step | What happens | Design role |
|---|------|--------------|-------------|
| 01 | **Problem & Signal** | Work starts from customer feedback, strategic bets, security mandates, or field signals. Every item gets a tracked work item and a named PM owner. | *Light / typically absent.* A gap worth closing — design input would improve signal quality. |
| 02 | **Product Definition** | The PM defines the problem, target customer, success metrics, and milestone plan (early access → full release). | **Core — design's primary entry point.** Lead problem framing, personas from research, current-state journeys, design principles. |
| 03 | **Engineering Build** | Development in tracked sprints, built with tests, telemetry hooks, and rollback plans. Must be able to release, pause, or roll back safely. | **Core.** Interaction specs, component patterns, prototypes for handoff; sprint-cadence reviews. |
| 04 | **Release Readiness** | Support, docs, and comms must be ready before any customer sees the feature (~90 days before broad release). Non-negotiable for GA. | *Involved.* Review onboarding flows, docs, in-product guidance for clarity and consistency. |
| 05 | **Private Preview** | A small cohort tests under real conditions: validate feasibility, understand support burden, confirm workflows. | **Core.** Run/support moderated usability research; findings feed the backlog before Public Preview. |
| 06 | **Public Preview** | Broader exposure. Monitor scalability, reliability, operational performance under real load. | *Involved.* Synthesise usage signals into iteration briefs; prepare final changes before GA freeze. |
| 07 | **General Availability** | Full support with formal SLAs; comms live; incident and post-incident processes apply. | *Light.* Confirm nothing broke in the final build; ops ownership transfers to product team. |
| 08 | **Operate & Iterate** | Real usage data, support cases, and feedback shape the next iteration; each improvement re-enters planning, closing the loop. | *Involved.* Analyse journey-level telemetry; translate into the next design problem statement. |

---

## 3. Case study · Spotify Wrapped Archive 2025

For 2025 Wrapped, Spotify went deeper: identifying up to **five remarkable listening days per
user**, then generating personalized LLM-powered narratives grounded entirely in real data.

- **Scale:** ~350 million eligible users · ~1.4 billion reports generated · global single-moment launch.
- **Source:** engineering.atspotify.com — *"Inside the Archive: The Tech Behind Your 2025 Wrapped Highlights"* (Mar 2026).

### End-to-end process (Discover → Build → Ship)

| Phase | # | Step | Summary |
|-------|---|------|---------|
| **Discover** | 01 | Define Concept | Move beyond annual stats to personal storytelling — up to five remarkable days per user. |
| | 02 | Design Heuristics | Priority-ordered algorithms ranked by narrative potential and statistical strength. |
| **Build** | 03 | Engineer Prompts | Two-layer system + user prompt, iterated daily for three months with LLM-as-judge + human review. |
| | 04 | Distil Model | Frontier model → gold dataset → fine-tuned smaller model; DPO reached preference parity. |
| | 05 | Build Infrastructure | Column-oriented key-value DB with per-day column qualifiers — no locks, no coordination. |
| **Ship** | 06 | Generate at Scale | ~1.4B reports across 350M users; thousands of req/sec for four days; sequential per user. |
| | 07 | Evaluate & Fix | LLM-as-judge on ~165K samples (accuracy, safety, tone, formatting); structured remediation. |
| | 08 | Launch Globally | Pre-scaled compute + DB nodes; synthetic load warmed caches; single-moment launch, nothing cold. |

### Detail

- **Problem — from summary to storytelling.** Go beyond stats to narrate the year's standout
  moments (a discovery that changed everything, a six-hour "yearning" spell, a hard left turn in
  taste) — identified algorithmically across hundreds of millions of users, then narrated with
  warmth and accuracy at planetary scale.
- **Algorithm — spotting remarkable days.** A distributed pipeline computed candidate days per
  user using heuristics ranked by narrative potential and statistical strength: biggest music/
  podcast day; biggest discovery day; biggest top artist/genre day; most nostalgic day; most
  unusual day; contextual anchors (birthday, New Year). Hundreds of millions of events narrowed to
  **≤ 5 standout days per user**.
- **Prompt engineering — two-layer prompt system.** A **system prompt** set the creative contract
  (data-driven storytelling; witty, sincere tone; trust & safety by default). A **user prompt**
  removed ambiguity with detailed daily listening logs, a pre-computed stats block, overall Wrapped
  data + day category, previously generated reports, and the user's country for localisation.
  *Key insight:* prompting was a loop — prototype → LLM-as-judge → human review → iterate — over
  three months of daily practice.
- **Distillation — shrinking the model.** Frontier models were great for prototyping but
  uneconomical at 1B+ reports: (1) frontier model produces reference outputs; (2) curate a "gold"
  dataset; (3) fine-tune a smaller production model; (4) DPO via A/B-tested human evaluations.
  *Result:* preference parity with the frontier baseline at a fraction of the cost.
- **Infrastructure — 1.4 billion reports.** Sustained thousands of requests/sec for days; reports
  generated sequentially per user to avoid repetition. A column-oriented key-value DB gives each
  day its own column qualifier, so concurrent writes touch different cells — no locks, no
  coordination. *Launch:* pre-scaled compute + DB nodes; synthetic load warmed pools and caches, so
  "when real traffic arrived, nothing was cold."
- **Quality assurance — pressure-testing at scale.** At 1B+ reports, even 0.1% failure = millions
  of broken stories. LLM-as-judge graded ~165K samples on accuracy, safety, tone, and formatting,
  alongside rule-based queries. *Remediation:* evaluators + human review find failures → SQL +
  regex surface similar issues → batch deletion + guardrail updates.
- **Lessons learned.** Less is more (more instructions = less creativity); prompting doesn't scale
  without evaluation; concurrency problems are data-modeling problems; fault isolation starts at
  the architecture level; engineering expertise drives while AI assistants amplify; **the LLM call
  is the easy part**. Built with care, tested with rigour, engineered responsibly end to end.

---

## 4. Case study · Adobe Express AI Assistant

What would Adobe Express look like if it were powered by and designed around an AI core? A design
challenge from Senior Design Director Ben Matthews sparked a reimagination that reached Adobe's
CEO. Principal Designer Claude Piché led a design-led transformation — from vision prototypes to a
beta launch at **Adobe MAX 2025**.

- **Five design principles:** Simple · Empowering · Tailored · Unified · Reliable — guiding every
  decision from concept to launch.
- **Source:** adobe.design — *"Behind the Design: Adobe Express AI Assistant"* (Dec 2025).

### Detail

- **Insight — "we're not a chatbot."** The first instinct was a conversational panel on the
  existing editor (the "safe" start). User testing showed people didn't want lengthy back-and-forth
  chats with a creation tool — they wanted an assistant that *completes the work* on clear commands.
  *Key quote:* *"We're not a chatbot, we're a do-bot."* — George Goodman, Lead PM.
- **Process — from tooling-first to AI-first.** Express had grown crowded. The team mapped the
  content-creation journey, aligned cross-functionally on core capabilities, pivoted from a
  conversational panel to a dedicated **AI mode**, and designed a simple toggle between AI and the
  classic editor. That toggle became the release's mascot ("Flip the switch").
- **Design challenge — limitless possibilities.** A prompt bar means no single design path. The
  team wanted the best of both worlds — speed of prompting *and* full manual control: canvas +
  prompt bar + manual controls; layered document editing (not flat output); prompt suggestions to
  reduce blank-canvas anxiety; one-click imaging presets; context-aware suggestions. *The hard
  part:* the final 10% of polish — motion, timing, animation — was hardest, but elevates the whole.
- **Motion design — motion as communication.** Motion isn't decoration; it is core to how the
  experience communicates: prompt-bar loading animation, a gradient bouncy switch toggle, a
  delightful intro, close partnership with front-end engineers, co-designed in the browser (not
  just mockups). Early motion involvement shaped the whole system and made the Assistant feel
  approachable.
- **Process — complexity behind simplicity.** *"It takes a lot of complexity to achieve
  simplicity."* Unlike pre-AI projects with linear workflows, this had no predictable steps — some
  days magical, others where nothing worked. A date-driven MAX deadline gave clarity and focus:
  fewer things, done well, obsessing over pixel-perfect UI.
- **Lessons learned.**
  - A prompt bar is a bold promise the experience must rise to meet.
  - Adding panels to a crowded editor adds complexity — the opposite of the goal.
  - Users want assistants that *do*, not assistants that *show how*.
  - Design principles must guide decisions when the design space is infinite.
  - Co-designing with engineers in the browser beats handing off mockups.
  - Small details (motion, timing) elevate the entire product.
  - Hard deadlines create focus, not compromise.
  - *Next:* mobile (voice prompts — "Take out the photobomber") and building directly in the
    browser rather than prototyping in design tools.

---

## 5. Lessons for your practice

- Choose the model that fits your **starting condition**: prove value with one customer (Forward
  Deployed) or prove reliability at scale (Product Group).
- Know **where design has leverage** in each process — and where it is currently absent (e.g.
  intake/signal), which is a gap worth closing.
- For LLM products, **the model call is the easy part**: the hard engineering is heuristics,
  prompt-and-evaluation loops, distillation for cost, data-model design for concurrency, and QA at
  scale.
- Design *around* an AI core rather than bolting a chat panel onto an existing tool — build a
  "do-bot," not a chatbot.
- Let **principles guide** decisions when the design space is effectively infinite, and treat
  motion/polish as communication, not decoration.
