# Lesson 07 · Researching & Testing AI Products

> **Course:** ELVTR — AI Product Development (AIPD1), APAC cohort
> **Lesson:** 07 · Researching & Testing AI Products (deck: *User Testing AI Products*)
> **Framing:** *Testing methods, real user sessions, and iteration with real usage —
> Observe → Test → Iterate.*
> **Source deck:** [ELVTR AIPD1 — 07 Researching & Testing AI Products (Figma)](https://www.figma.com/design/cLUAEY4oqmXvnJbJdEu9oV/ELVTR-AIPD1---07-Researching---Testing-AI-Products)

This knowledge source captures the finished deck (the file's **TO DESIGN** section). The lesson
argues that testing AI products is fundamentally different from traditional UX testing, and gives
methods for studying **behaviour, failure, and mental models** rather than opinions.

## The shift

**AI is probabilistic, not deterministic.** Most UX testing assumes the system behaves the same
way twice — AI doesn't. When AI enters the loop, three new questions matter:

- **Behaviour** — how does the user act when working with AI?
- **Failure** — what happens when the AI is wrong?
- **Mental model** — what do they believe is happening inside?

*(Framing: traditional UX → human-AI collaboration.)*

## Contents

1. **Designing for the real world** — what it means to test an AI product where it actually lands.
2. **Testing methods for AI products** — four layers of testing, each going one layer deeper
   (behaviour / overreliance / appropriate trust).

---

## Section 01 · Designing for the real world

### What is the real world?

The world your product lands in is messy and human — not a tidy profile. It includes things like:
fear of losing your job, Netflix, TikTok, ADHD, the school run, hybrid work, software updates,
pandemics, supply chains, division, inequality.

> **Stop designing for personas. Start designing for the real world.**

### Adoptability

**Adoptability** = whether real people, in the real world, will actually pick it up.

**Adoption is earned.** The single most recurring problem seen across customers: AI solutions that
**nobody uses**, and the design failures that cause it.

### Case study · The airline strike

- **Problem:** reach hundreds of staff, fast, and ask them to come back to work.
- **Solution:** a personalised AI voice caller going out to everyone in parallel — built in a
  hackathon, working inside an hour (hundreds of personalised calls).
- **The insight nearly missed:** a robot asking you to break a strike is easy to hang up on. A
  person you've flown with carries **social stakes**.
- **The wrong metric:** "reach 1,000 people an hour" → the real question is **how many change
  their mind?**
- **Complete product proposition:** **AI value + human value** together (not AI alone).

### Case study · The smart ward & Dragon Copilot

- **The smart ward:** too much health data and too many ward metrics to monitor — vitals,
  telemetry, dashboards, alerts streaming in faster than any one person can track.
- **What we heard on the floor:** *"A nurse doesn't come to work to run mission control. They come
  to be with people."* Design to let humans see things an AI cannot.
- **Dragon Copilot:** doctors spend huge parts of the day writing documentation and notes after
  consultations. The AI runs **behind the human** — same patient, same notes — so the clinician
  stays the face of the room, extending (not replacing) human capability.
- **Impact:** ~**1 hr** per doctor per day given back to seeing patients; **100k** clinicians and
  counting, live worldwide.

### Recap · Section 01

1. **Design for the world, not the persona.** Your product lands in real human tension, not a tidy
   profile.
2. **Adoption is earned, not assumed.** Name the tension before you name the AI.
3. **AI extends people, it doesn't replace them.** Dragon Copilot, the smart ward — the AI works
   behind the human.

> **The takeaway:** start from the human tension; the AI is the answer, not the point.

---

## Section 02 · Research methods for AI products

### Four layers of AI UX testing

Stack the methods — each layer answers a deeper question than the last, moving from interface
evaluation into the study of human-AI collaboration.

| # | Layer | Question |
|---|-------|----------|
| 01 | **Usability** | Can the user complete the task? |
| 02 | **Behaviour** | How do they act while working with AI? |
| 03 | **Trust** | Do they trust the AI appropriately? |
| 04 | **Mental models** | Do they understand what the AI is doing? |

**The progression:** Traditional UX › AI UX › Human-AI Collaboration › Responsible AI Research.

Mapped to methods:

| # | Method | What it answers |
|---|--------|-----------------|
| 01 | Traditional UX | Can people use it? |
| 02 | Task-based & think-aloud | How do they behave with the AI? |
| 03 | Overreliance studies | What happens when it's wrong? |
| 04 | Cognitive walkthroughs | Do they trust it appropriately? |

### Method 01 · Observe behaviour, not surveys

**Behaviour is more reliable than opinion.** Give people a realistic task and watch them do it.
With AI the question shifts from "can they use it?" to "how do they behave when the AI joins the
decision?"

*Example — server recovery script:* during an outage the AI generates a recovery script; the task
*looks* done, but watch what they actually do — do they read it? test it before running? check its
assumptions? or just hit run?

**Capture four things:** **Intent** (what are they trying to achieve?), **Reasoning** (why do they
trust this answer?), **Verification** (do they check sources & alternatives?), **Decision quality**
(did the AI lead to a better call?).

> Don't ask "would you verify the AI?" — observe "**did** you verify the AI?" That distinction is
> everything.

### Method 02 · Measure trust, not satisfaction

**Success can hide a problem.** A user can finish fast, feel confident, and report high
satisfaction — while making poor decisions because they trusted the AI too much. That is
**overreliance**.

*Why surveys miss it:* a survey says "the AI helped," but can't tell you whether the answer was
correct, whether they checked it, whether they noticed the errors, or how they'd behave in a
higher-risk situation.

**The mindset shift:**

- **From:** can people use the system? → **To:** what happens when it's wrong?
- **Design around** failures, not successes.
- **Assume** AI errors are inevitable.

> One of the first UX methods built around **uncertainty** rather than usability.

**Build the failure map first.** Before running anything, map how the AI is likely to be wrong and
how much each error matters:

- **Failure types:** Information (wrong facts, fabricated sources, stale data) · Timing (stale data,
  delayed updates) · Context (misreads the situation or intent) · Recommendation (suggests
  inappropriate or incomplete actions).
- **Risk matrix:** align effort to risk (e.g. *typo → low*, *wrong recommendation → medium*,
  *fabricated fact → high*, *unsafe action → critical*).

> **Assume it will be wrong.** The question isn't *whether* the AI will make mistakes — it's what
> happens when it does.

### Method 03 · Mental models & appropriate trust

**What does the user think the AI is doing?** Walk the experience as the user; at each step ask
what they believe the AI knows, what it's doing, and how much they'll trust it.

*The mental-model gap:* a user asks Copilot about "my files" and believes it reads everything
(SharePoint, email, all files) — but it answered from one open document. The gap quietly creates
**misplaced trust**. *"It said it checked my files." It had read one open document.*

Ask at every step: **Knows** (what do they think it knows?), **Doing** (what do they think it's
doing now?), **Trust** (how much will they trust this output?), **Signals** (what in the UI shaped
that belief?).

**Design for appropriate trust, not maximum trust.** The goal isn't more trust — it's the *right
amount*, and knowing when to verify or override:

| Under-trust | Appropriate trust *(the target)* | Overreliance |
|-------------|----------------------------------|--------------|
| Ignores genuinely useful help | Uses the AI — and verifies it | Accepts answers blindly |

Calibration happens when the user can tell confident output from uncertain output, know when to
verify vs override, and recognise the limits of what the AI actually knows.

**Instrument the behaviours in real usage** (lab studies start it; real usage proves it). Six
signals turn "the AI feels helpful" into evidence of whether trust is calibrated:

- **Error detection** — do users catch wrong answers?
- **Verification** — do they check sources & alternatives?
- **Challenge** — do they push back on the AI?
- **Blind acceptance** — do they accept without checking?
- **Recovery** — do they recover after a bad answer?
- **Decision quality** — better outcomes, not just faster?

### Workshop labs

The deck includes run-of-show workshop templates for practising these methods:

- **Think-Aloud Evaluation Lab** — behaviour grid: Intent · Reasoning · Verification · Decision.
  Needs a realistic, high-stakes task, the actual UI/prototype, and a behaviour-logging grid.
- **Failure-Injection Study Design** — measures Detection · Verification · Challenge · Recovery.
  Needs your AI failure map and paired correct/incorrect responses.
- **Cognitive Walkthrough Lab** — walk an AI flow step-by-step across Before · During · After ·
  Signals, flagging where the UI mis-calibrates trust.

---

## Close · Six things to hold onto

1. **Test in the real world** — not just clicking around a screen.
2. **AI is probabilistic** — test how it behaves, not just whether it works.
3. **Watch behaviour, not opinions** — what people do beats what they say.
4. **Success can hide overreliance** — did they catch it when the AI was wrong?
5. **Design for appropriate trust** — not blind trust, and not none.
6. **Test with intent** — a method to answer a question, not arbitrary clicking.

---

## Related assignment

This lesson feeds **Assignment 02 · Prototype & Test** (Lessons 5 + 7): turn your concept into a
working prototype, then test it with users *with intent*. Submit the prototype (built from your
workshop artefacts), the question you're testing, the method (task-based · think-aloud · failure ·
walkthrough), who & where you tested, findings with evidence, and the next iteration your testing
points to. *(Format: PDF, Figma, or Slides. Weight/due: TBC — after Lesson 7.)*
