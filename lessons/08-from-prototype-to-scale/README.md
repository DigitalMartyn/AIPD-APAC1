# Lesson 08 · From Prototype to Scale

> **Course:** ELVTR — AI Product Development (AIPD1), APAC cohort
> **Lesson:** 08 · From Prototype to Scale (deck: *From Prototype to Scale*)
> **Instructor:** Martyn Gooding · AI for Designers
> **Framing:** *You came in with a tested concept. You leave knowing how to make it
> scale — Prototype → Production → Scale.*
> **Source deck:** [ELVTR AIPD1 — 08 From Prototype to Scale (Figma)](https://www.figma.com/design/7e4neraAaNJrg4BrfPHOv2/ELVTR-AIPD1---08-From-Prototype-to-Scale?node-id=177-187)

This knowledge source captures the finished deck (the file's **TO DESIGN** section). The lesson is
the bridge where your tested concept becomes something you can actually ship and scale. It looks at
scale from three angles — how **big products** scale, how **start-ups** scale, and how to
**productionise** your own prototype with an AI workflow — and sets the new bar for designers who
ship.

## Where you start

**You're not starting from zero.** By now you've done the hard part:

- **You've got a product** *(from Assignment 02)* — a working, end-to-end, full-featured and tested
  experience, even if it isn't edge-case-complete yet.
- **That's your starting line** — feature-complete and tested. This is not incubation from scratch;
  you enter with something real in your hands.
- **Next is Assignment 03** — scaling and productionising the UI. The next lessons take this from
  *working* to *shippable and scalable*.

*(The UX and the research are already behind you. From here, it gets real.)*

## Contents

1. **How big products scale** — the Microsoft model: gated stages, ringed rollout, enterprise
   discipline.
2. **How start-ups scale** — speed, virality, the new cost of AI, and raising the money to climb.
3. **Productionising with HVE-Core** — direct an AI workflow to take your concept from prototype to
   production-ready.

---

## Section 01 · How big products scale

### Five stages: internal to scale

You don't arrive at scale from scratch. A feature-complete, tested product moves through **five
gated stages**, from internal use to full scale. Each stage has a **gate** you must pass to advance.

| # | Stage | What it is | Gate to advance |
|---|-------|-----------|-----------------|
| 01 | **Internal incubation** | "Customer Zero" dogfooding — the product team uses the AI itself to validate value and flush out bugs. | Team uses it daily; value proven, blocker bugs cleared. |
| 02 | **Private preview** | A few lighthouse customers co-innovate with engineers and a partner, creating reference wins. | ≥1 reference win with a measurable outcome. |
| 03 | **General availability** | The public launch. Anyone can adopt it, with full support, SLAs and documentation. | Docs, support and SLAs ready; it can stand on its own. |
| 04 | **Scale** | Grow usage and load. Infrastructure, cost and reliability tuned for real volume. | Handles peak load reliably, at a cost you can defend. |
| 05 | **Operate & improve** | Keep it healthy. Telemetry, updates and support drive continuous improvement. | A telemetry-driven improvement loop is running. |

### Case in point · Microsoft 365 Copilot

Copilot followed the five-stage trajectory exactly — from a tiny NDA pilot to millions of users in
roughly a year.

1. **Tested with 20 pilot customers** *(2022)* — iterative improvement before any public signal.
2. **Broad announcement** *(Mar 2023)* — early access for enterprises, then paid availability.
3. **General availability** *(Nov 2023)* — anyone could buy it, with enterprise support and SLAs.
4. **Rolled out in rings** *(2024)* — gradual expansion with telemetry, catching issues before full
   scale.
5. **Millions of users within a year** *(2024–25)* — from 20 pilot customers to organisations
   worldwide.

### Safe deployment · Ringed rollout with telemetry

Microsoft Product Groups release features gradually through expanding **"rings"**, each gated by
telemetry and feedback before the next (dogfood → internal rings → external rings → all users).

| # | Ring / step | What happens |
|---|-------------|-------------|
| 1 | **1–2 internal rings** | Employees only, dogfood daily. *Exit gate:* no P0/P1 bugs in real use. |
| 2 | **1–3 external rings** | Insider "Fast" then "Slow" preview rings of growing size. *Exit gate:* crash & latency within target. |
| 3 | **Telemetry at every stage** | Crash rates, latency, usage frequency + qualitative feedback. |
| 4 | **A/B online experiments** | Measure real impact; halt or roll back on anomalies. *Exit gate:* neutral-to-positive result. |
| 5 | **General availability** | Reach hundreds of millions with high confidence in quality. |

### Engineering discipline · Built for enterprise scale

Beyond ringed rollouts, Product Groups combine global infrastructure with rigorous quality,
security and continuous improvement:

- **Global infrastructure** — services are multi-tenant, geo-distributed and highly available, with
  SRE teams and one of the world's largest update-distribution networks. *(99.9%+ availability SLAs;
  updates reach billions of devices.)*
- **Security & compliance** — extensive integration testing, responsible-AI guidelines, data
  security and regulatory compliance before a service is production-ready. *(Safety gates block
  release until RAI + security checks pass.)*
- **Continuous improvement** — instrumented features feed data-driven updates. *(Adoption nudged
  from 5% to 60% daily active via training and champions.)*

> The PG model trades some speed for enterprise-grade robustness — a necessity when an outage could
> affect millions. Once stable, partners take it to scale.

### Recap · Section 01

1. **Stages, not a leap** *(internal → GA)* — feature-complete, private preview, public preview,
   general availability. Earn each step.
2. **Ship in rings** *(safe deployment)* — roll out gradually with telemetry, so problems surface
   small before they surface everywhere.
3. **Built for the enterprise** *(discipline at scale)* — security, reliability and support are the
   price of admission at scale.

> Big tech scales slowly and safely. Next, the opposite approach.

---

## Section 02 · How start-ups scale

### Speed, virality, cloud-native

Small consumer start-ups scale very differently, emphasising rapid iteration, early user growth and
elastic cloud infrastructure over formal process:

- **Rapid iteration to PMF** — ship a rough MVP, then reshape it around real usage until you hit
  product-market fit: the point where people genuinely want it.
- **Cloud-native elasticity** — build on AWS, Azure or GCP so going from ten users to ten million is
  a config change, not a rebuild.
- **Focus and hard trade-offs** — small teams win by doing one thing brilliantly and deliberately
  saying no to everything else.

### The old playbook · Scaling used to be almost free

The last generation of consumer start-ups reached millions on cheap cloud infrastructure. Serving
one more user cost almost nothing, so **"launch free, monetise later"** worked.

- **Instagram** *(≈ £0 per new user)* — tens of millions of users on a handful of engineers; hosting
  and open-source software cost almost nothing per person.
- **Dropbox** *(storage on demand)* — cloud storage scaled seamlessly and cheaply as user files
  ballooned; you paid pennies as you grew.
- **Uber · Airbnb · Zoom** *(software margins)* — once the product was built, each extra ride,
  booking or call added negligible marginal cost.

> **The old maths:** ≈ £0 to serve one more user. AI does not play by these rules.

### The AI reality · AI doesn't scale for free

Every response your product generates is a model call, and every call is money out the door. Costs
scale with usage from day one, long before revenue does.

- **Per-call inference** *(billed per token)* — each message, image or answer is metered per request.
  Growth means a bigger bill before it means a bigger margin.
- **Costs before revenue** *(free users still cost)* — a trial, a demo, a viral spike: they all burn
  model spend, whether or not a single user ever pays you.
- **Premium models** *(quality costs)* — the best models carry the biggest price tags. "Just use the
  best model" is a budget decision in disguise.

> **The new maths:** £ / call — every response has a price tag. There is no free-to-start in AI. You
> either pass the cost on from day one, or fund the burn until revenue catches up. **£0 revenue ≠ £0
> cost:** costs start on day one; revenue doesn't.

### Funding the climb · Why VC, and who's out there

AI is capital-intensive: model costs, compute and talent all come before revenue. Venture capital
exists for exactly this — trading equity for the runway to reach scale.

**Types of backer:**

- **Angels** — individuals writing early cheques from their own money.
- **VC firms** — pooled funds investing from seed to growth in return for equity.
- **Corporate VC** — strategic investment arms of larger companies, such as cloud providers.
- **Family offices** — private wealth backing founders directly.
- **Accelerators** — cash plus mentorship and network (Y Combinator, Techstars and others).

**Funding stages** *(each answers a different question and attracts a different backer):*

| Stage | The question |
|-------|-------------|
| **Pre-seed** | Prove the idea works. |
| **Seed** | Find product-market fit. |
| **Series A** | Scale what already works. |

### Finding the right investors

Don't spray and pray. Target investors who back your stage, sector and geography, then do your
homework before you reach out:

1. **Define your needs** — how much, what for, and at what stage.
2. **Leverage your network** — warm introductions beat cold emails every time.
3. **Use curated lists** — start from vetted investor databases, not guesswork.
4. **Research each investor** — check their thesis and past deals. Do they actually back AI?
5. **Strong first impression** — a sharp deck and a clear story open doors.

### Where the money actually is

The funding world is more mapped than it looks. A few directories show you who invests in what:

- **Crunchbase · PitchBook** — who funded whom, and for how much.
- **AngelList** — angels and early-stage rounds.
- **Accelerators** — Y Combinator, Techstars, and their cohorts.
- **AI-focused funds** — the investors actually writing AI cheques.

> **Coming up · Lesson 12 — then you sell it.** Raising money and shipping are only half the story.
> Getting people to care about your work is its own craft; Lesson 12 goes deep on storytelling, the
> pitch, and selling your work. *(Your pitch deck lives there.)*

---

## Section 03 · Productionising with HVE-Core

### The gap · A prototype isn't a product

A prototype proves the idea. **Production** means it holds up for real users, every day, at a cost
you can defend.

- **Reliability** *(works every time)* — a demo can fail gracefully in front of one person.
  Production has to hold for thousands, on a bad day.
- **Guardrails & evals** *(trust, measured)* — you need safety checks, fallbacks and evals, not a
  feeling that it "seemed fine" in the room.
- **Cost & observability** *(you can see it)* — every call costs money and can break. You need
  logging, monitoring and a bill you understand.

> Shipping is a different job from proving. Plan for it from day one.

### Meet HVE-Core

An open, **MIT-licensed** workflow system for GitHub Copilot. It turns AI-assisted work into
something repeatable and standards-aligned, built from four pieces:

| # | Piece | What it is |
|---|-------|-----------|
| 01 | **Agents** | Specialised tasks — research, plan, implement, review — each a focused role you call on. |
| 02 | **Prompts** | Repeatable entry points — start the same workflow the same way, every time. |
| 03 | **Instructions** | Standards, applied automatically — coding and writing conventions the AI follows by default. |
| 04 | **Skills** | Reusable tool capabilities — packaged know-how the agents can pick up and use. |

### The through-line · Your concept becomes a scalable product

This is the lesson where your tested concept becomes something you can actually ship and scale.
Lessons 5 and 7 got you here:

- **Lesson 5** — you built a prototype.
- **Lesson 7** — you tested it with users.
- **Lesson 8** — you productionise it, and scale it.

*(Tested concept on one side, a shippable product on the other. This lesson is the bridge.)*

### Your role · Designers who ship

You're not becoming an engineer. But the bar has moved — here's what's expected of a designer now,
from the floor up:

- **At least — understand the process.** Know how a product gets from prototype to shipped. Being
  aware of it is the new baseline.
- **Better — fix what's yours.** Shipping bugs in UX patterns and design components are yours to fix.
  And you make the call: is this idea actually shippable?
- **The bar — designers who ship.** The industry now expects designers who can take an idea all the
  way, not just hand over a mock.

*(Solo or a small team? This lesson teaches you ways to self-ship stable products.)*

### Live demo · HVE-Core, end to end

**Set up the demo.** Point HVE-Core at a real vibe-coded prototype and let it show exactly what it
takes to make it production-ready:

1. **What you bring** *(your vibe-coded prototype)* — the repo you built, warts and all. Point
   HVE-Core straight at it.
2. **What happens** *(HVE-Core assesses it)* — it reads the whole codebase and grades every issue it
   finds, most urgent first.
3. **The output** *(a prioritised fix list)* — critical to low, each with the file and the fix. For
   example: a key hardcoded in the client, or a crash on empty input.

The live demo walks the graded output in four buckets — **Critical fixes**, **High-priority fixes**,
**Medium fixes**, and **Low fixes & done well** — populated from the real assessment during the
session.

### Production-ready checklist

If you can tick these, you're not demoing any more — you're shipping. *Before you call it done:*

- ✓ Context & data documented
- ✓ Build plan written down
- ✓ Costs & rate limits understood
- ✓ Evals defined
- ✓ Safety checks & fallbacks
- ✓ Logging & monitoring
- ✓ Error states designed
- ✓ Commit & PR standards
- ✓ Tests passing
- ✓ A rollback plan
- ✓ Owner & handoff clear
- ✓ Next iteration named

> Ticking these is the difference between "it worked in the demo" and "it works in production".

### Get HVE-Core

Open, MIT-licensed and free to install. Three ways in:

1. **GitHub** — [`github.com/microsoft/hve-core`](https://github.com/microsoft/hve-core) — the repo,
   docs and examples.
2. **VS Code Marketplace** — `ise-hve-essentials.hve-core` — install the extension in one click.
3. **Copilot CLI** — `copilot plugin marketplace add microsoft/hve-core` — if you prefer the
   terminal.

### Recap · Section 03

1. **A prototype isn't a product** *(the gap is real)* — looking done and being done are not the same
   thing. The gap is where shipping lives.
2. **AI closes the gap with you** *(HVE-Core + your judgement)* — you direct it, it does the
   engineering, the guardrails keep it honest.
3. **You leave with a fix list** *(critical → low)* — every issue graded, located and paired with a
   fix. That's a scalable product taking shape.

> You stayed the designer. The product got production-ready.

---

## In summary · What we covered

Three ways of thinking about scale, and a way to actually get there:

1. **How big products scale** *(the Microsoft model)* — stages from internal to GA, ringed rollout,
   enterprise discipline.
2. **How start-ups scale** *(fast, scrappy, funded)* — speed and virality, the new cost of AI, and
   raising the money to climb.
3. **Productionising with HVE-Core** *(designers who ship)* — direct an AI workflow to take your
   concept from prototype to production-ready.

> You came in with a tested concept. You leave knowing how to make it scale.

---

## Related assignment

This lesson leads into **Assignment 03 · Scaling & Productionising the UI** — take the working,
tested product from Assignment 02 and make it shippable and scalable. Use the production-ready
checklist as your bar, and HVE-Core to close the gap between "worked in the demo" and "works in
production".
