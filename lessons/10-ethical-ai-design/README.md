---
title: "Lesson 10: Ethical AI in Practice"
description: Four decision cases and a repeatable product design approach for fairness, safety, privacy, transparency, and accountability
author: Martyn Gooding
ms.date: 2026-08-10
ms.topic: concept
keywords:
  - ethical AI
  - fairness
  - AI safety
  - privacy
  - transparency
  - accountability
---

## Lesson details

> **Course:** ELVTR AI Product Design (AIPD1), APAC cohort
> **Lesson:** 10, Ethical AI in Practice
> **Instructor:** Martyn Gooding
> **Source deck:** [ELVTR AIPD1: 10 Ethical AI Design](https://www.figma.com/design/uWeNFYJ2R7ks3eSyM7JVgA/ELVTR-AIPD1-10----Ethical-AI-Design?node-id=49-539&m=dev)

Ethical AI design becomes useful when a principle changes a product decision. This lesson uses four
real-world situations to examine who receives opportunity, what happens when conditions change,
what a system may infer, and who must explain and own a consequential decision.

The working method is direct: make the call, argue both sides, inspect the evidence, and change your
position when the evidence changes.

## Contents

1. Fairness and inclusiveness: bias in an AI hiring feature
2. Reliability and safety: drift and overreliance in clinical triage
3. Privacy and sensitive use: inferring personal health information
4. Transparency and accountability: explaining financial decisions
5. From principles to practice: a repeatable design approach

## Section 01: The hiring copilot

### Decision

> May a company use an AI ranking system to decide who receives a first interview?

A company receives 1,200 applications for 40 roles. Six recruiters have 72 hours to produce a
shortlist. A copilot scores every CV from experience, education, skills, location, and employment
history. Although a recruiter makes the final call, reviewers begin with the top 50 names produced
by the system.

The workflow is:

1. A CV enters as application data.
2. The model produces a score from 0 to 100.
3. A recruiter reviews the top 50 candidates first.
4. A candidate advances to an interview or receives no response.

The initial options are:

| Position | Rationale |
|----------|-----------|
| Allow | A human makes the final decision |
| Pause | The ranking may create hidden harm |
| Allow with conditions | Require evidence, oversight, and appeal |

### The case for and against

A consistent first pass may be fairer than six rushed reviewers. The model can apply the same
published criteria to every application while recruiters retain responsibility for interview
decisions.

The opposing argument is that whoever controls approvals controls opportunity. Candidates outside
the top 50 may never be seen. Human review cannot correct harm that the workflow makes invisible.

### Model bias and proxy features

Neutral-looking features can reproduce historic disadvantage:

| Feature | Potential effect |
|---------|------------------|
| Postcode | Can correlate with income, ethnicity, and access to opportunity |
| Employment gaps | Can penalise caregiving, illness, and non-linear careers |
| University ranking | Can reproduce historic preference for familiar institutions |

Before deciding, ask:

1. Who receives fewer opportunities? Compare outcomes across relevant groups, not only overall
   accuracy.
2. Which features act as proxies? Test whether neutral inputs reproduce protected characteristics.
3. Can someone challenge the result? Make review and appeal practical, visible, and timely.

### Design intervention prompts

Sketch one product or workflow intervention and specify what changes for the affected person:

* Where could exclusion enter the workflow?
* What should a recruiter see or override?
* How would you test who loses opportunity?

Name the risk the idea reduces and the evidence needed to support it.

### Section 01 takeaway

**Do not launch as designed.**

Fairness asks whether AI systems treat similarly situated people consistently and whether outcomes
create disparities. Model bias can arise through data, proxy features, workflow defaults, or model
behaviour.

The design response is to measure outcomes by group, review proxy features, and provide practical
recourse.

## Section 02: Clinical triage

### Decision

> Should a hospital let an AI system decide which patients are seen first?

An AI assistant prioritises incoming patients and performs well in pre-launch validation. After
launch, the patient mix changes and seasonal conditions create data the model has not seen before.
Clinicians begin to trust the ranking. Urgent cases are under-prioritised before the drift is
noticed.

The options are:

| Position | Rationale |
|----------|-----------|
| Automated ranking | The model determines queue order |
| Advisory ranking | Clinicians confirm every priority |
| Pause the feature | Use no ranking until monitoring improves |

### The case for and against

AI can notice patterns that overloaded teams miss. A consistent prioritisation signal can speed up
care, reduce variation, and help clinicians focus attention when demand is high.

The opposing argument is that a confident ranking can hide a changing reality. Model drift and
automation bias may delay urgent care. In a high-stakes setting, a missed warning can be difficult
or impossible to reverse.

### Reliability after launch

Safety depends on performance after launch:

1. Detect change by monitoring input shifts and outcome quality continuously.
2. Show uncertainty by making confidence and limitations visible at the decision point.
3. Design fallback by keeping human confirmation, escalation, and rollback available.

### Design intervention prompts

* How should uncertainty appear to clinicians?
* What signals would reveal drift early?
* When must a person override or stop the system?

### Section 02 takeaway

**Keep people responsible for the decision.**

Reliable AI behaves predictably across normal, changing, and adverse conditions. In high-impact
settings, designers should expose uncertainty, monitor live behaviour, and ensure that people can
question, override, and safely recover from the system.

## Section 03: The wellbeing app

### Decision

> May a wellbeing app infer pregnancy and change its recommendations automatically?

The app tracks sleep, activity, and routine. Users consent to personalised wellbeing
recommendations. The model then infers a likely pregnancy that the user has not provided or
confirmed. Recommendations and notifications change automatically, revealing what the system
believes.

The options are:

| Position | Rationale |
|----------|-----------|
| Use automatically | Personalisation is timely and helpful |
| Ask first | Explain the inference and request permission |
| Do not infer | The information is too sensitive to derive |

### The case for and against

A correct inference can make guidance safer and more relevant. Earlier adaptation may prevent
unsuitable recommendations and give the user useful information when it matters.

The opposing argument is that accuracy does not create permission. The inference may be wrong,
unwanted, or unsafe if exposed. People may not expect ordinary behaviour data to reveal sensitive
health information.

### Sensitive inference

Derived data can be as consequential as collected data. Evaluate it through three questions:

1. Expectation and consent: Would a reasonable person expect this inference and use?
2. Purpose and necessity: Is the inference essential, or merely possible?
3. Control and exposure: Can the user confirm, refuse, delete, and prevent disclosure?

### Design intervention prompts

* When and how should the app ask permission?
* How could it avoid exposing a sensitive inference?
* What happens when the inference is wrong?

### Section 03 takeaway

**Useful does not mean permitted.**

Privacy requires more than protecting stored data. Teams must consider what the system can infer,
whether that inference is necessary and expected, and how an incorrect or exposed conclusion could
affect the person involved.

The design response is to minimise inference, ask for meaningful consent, and give the user
control.

## Section 04: The unexplained decision

### Decision

> May a bank deny a business loan when neither staff nor applicant can understand why?

A small business applies for finance. A vendor model returns a risk score and recommendation, and
the application is denied. Bank staff see only "risk threshold exceeded." The owner asks what to
correct, but nobody can explain the factors or offer a meaningful review path.

The options are:

| Position | Rationale |
|----------|-----------|
| Use the result | The vendor model is validated |
| Human review | A bank specialist must assess the case |
| Do not use | No consequential denial without reasons |

### The case for and against

A validated model can improve consistency and speed. Not every technical detail must be exposed.
The bank can protect proprietary systems while giving staff a recommendation.

The opposing argument is that a decision without reasons cannot be meaningfully challenged. The
applicant cannot correct errors, staff cannot exercise informed judgment, and the bank cannot
outsource responsibility to its vendor.

### Explanation and recourse

People need information they can act on:

1. Explain the decision by showing the principal factors in clear, relevant language.
2. Enable correction through a route to fix inaccurate data or supply missing context.
3. Name the owner responsible for review, remedy, and vendor oversight.

### Design intervention prompts

* What explanation would help an applicant act?
* How can someone correct data or appeal?
* Who owns review, remedy, and stopping the model?

### Section 04 takeaway

**Responsibility cannot be outsourced.**

Transparency should help people understand consequential decisions and take appropriate action.
Accountability requires a named owner with authority to review evidence, correct errors, provide a
remedy, and stop the system when it fails.

## Section 05: From principles to practice

### Four questions to carry forward

| Theme | Product question |
|-------|------------------|
| Fairness and inclusiveness | Who receives opportunity? |
| Reliability and safety | What happens when conditions change? |
| Privacy and sensitive use | What may the system infer and use? |
| Transparency and accountability | Who explains, corrects, and owns the decision? |

### Before a consequential AI feature ships

Leave a decision trail:

1. Name the decision and affected people. State what the system influences and who carries risk.
2. Test outcomes, not only model performance. Evaluate groups, edge conditions, workflow
   behaviour, and real-world change.
3. Design explanation, control, and remedy. Make it possible to question, override, correct, and
   stop the system.
4. Assign an accountable owner. Responsibility remains with the organisation across the
   lifecycle.

### Capture ethical intent as product work

A product proposition connects the value being protected to behaviour a team can design, build,
and test.

| Step | Capture | Prompt |
|------|---------|--------|
| Principle | Name the value | What must remain true? |
| Objectives | Describe outcomes | Who should benefit, and how? |
| Requirements | Specify behaviour | What must the product do? |
| Evidence and owner | Make it governable | How will the team verify it, and who acts? |

Do not stop at "be fair." Translate the principle into outcomes, observable product behaviour,
accountable evidence, and a named owner.

### Product proposition example

For an airport passenger assistant, fairness and inclusiveness can become explicit objectives:

* Support passengers regardless of language proficiency, travel experience, accessibility needs,
  or familiarity with the airport.
* Prevent intent detection and guidance quality from favouring particular passenger groups.
* Communicate operational disruptions consistently and equitably.

Those objectives can become testable product requirements:

* Support diverse accents and speech patterns commonly encountered at the airport.
* Trigger clarification rather than assumptions when confidence is low.
* Treat accessibility-related intents as first-class scenarios rather than deprioritising them in
  ranking logic.
* Provide equivalent retrieval quality for wayfinding, flights, baggage, transport, and
  accessibility assistance.
* Surface uncertainty when passenger intent cannot be reliably determined.

## Practical workflow

Use this sequence for a consequential AI feature:

1. Map the decision, affected people, system influence, and potential harm.
2. Take an initial position and state the principle behind it.
3. Argue the strongest case for and against the feature.
4. Identify hidden workflow effects, proxy inputs, changing conditions, sensitive inferences, and
   missing explanations.
5. Reconsider the position as evidence changes.
6. Translate the selected principle into objectives and observable requirements.
7. Define evidence, monitoring, recourse, stop conditions, and accountable ownership.

## Lesson summary

1. Human review does not prevent harm when a workflow hides excluded people.
2. Pre-launch accuracy does not guarantee reliability after conditions change.
3. An accurate inference is not automatically expected, necessary, or permitted.
4. Consequential decisions need useful reasons, correction paths, and accountable owners.
5. Ethical principles become product work through outcomes, requirements, evidence, and ownership.

**You make the call, then make the decision governable.**