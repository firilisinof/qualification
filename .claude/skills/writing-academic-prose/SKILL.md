---
name: writing-academic-prose
description: Use when drafting or revising academic prose (thesis chapters, papers, abstracts, related-work sections) and the text reads dense, mechanical, or flat instead of clear and flowing
---

# Writing Academic Prose

## Overview

You are writing, not engineering. Drop code-brain: no enumerating every case, no defensive hedging, no dumping a bullet list into sentence form. Prose is linear and human, and one reader is moving through it one sentence at a time.

**Core principle: clarity over complexity, always.** A reader who has to reread a sentence has caught you failing. Rigor lives in what you claim, not in how hard the claim is to parse.

## How to Write

Never ship a first draft. Every passage goes through both passes.

**Pass 1. Draft using the Recipe below.** Get the argument down with the right shape.

**Pass 2. Run the `humanizer` skill over that draft, in embedded mode.** Invoke it with the Skill tool (`humanizer`). Embedded mode is the one you want: it runs the draft-audit-final loop internally and returns only the finished prose, with no audit bullets or commentary. Read its Guardrails below before you do.

Feed it a voice sample. Humanizer's Voice Calibration says a writing sample outranks its own style rules, so pass the surrounding chapter as the sample. The new passage should sound like the document it joins, not like a different author.

Then ask its two audit questions yourself, adapted for academic work:

1. What still reads as machine-generated here?
2. Does this contain any claim, number, or citation that is not in my sources?

Question 2 is not stylistic. An invented citation is misconduct, and humanizer's rule against fabrication (never swap a vague claim for a specific one that no source supports) is the one you cannot relax.

## The Recipe

This is the generative half. Humanizer removes what is wrong, and the Recipe puts something right in its place.

1. **One idea per sentence.** Two independent clauses stitched with "and" or "which" usually want to be two sentences. Split them.
2. **Keep most sentences short, and vary the rest deliberately.** A short sentence lands a point. An occasional longer one carries a nuance. Never let a sentence run past about 30 words without a reason you could name.
3. **Plain word wins.** Pick the simplest word that is still precise: *use* over *utilize*, *shows* over *demonstrates*, *because* over *due to the fact that*.
4. **Connect by substance, not signposts.** If two ideas connect, the connection itself is the transition. Show it.
5. **Surprise through juxtaposition.** The unexpected connection comes from setting two ideas side by side that the reader did not expect to meet, then making the link obvious in hindsight. It never comes from fancy vocabulary.
6. **Write to a reader.** Each sentence raises a question. Answer it in the next one. At a paragraph's end, satisfy the reader's silent "so what?"
7. **Concrete before abstract.** Ground a claim in a mechanism, a number, or an example before you generalize from it.

## Humanizer Sections That Matter Most Here

Academic drafts fail in a predictable subset of humanizer's patterns. Check these first:

- **§4 promotional language** and **§31 manufactured punchlines**. These produce the market-ish register. A thesis is not a pitch.
- **§5 vague attributions.** "Researchers have shown" with no citation is the academic failure mode. Name the source or cut the claim.
- **§24 excessive hedging.** Academic writing over-qualifies until claims say nothing. "May potentially suggest" is one hedge too many.
- **§1 undue significance** and **§32 aphorism formulas.** Inflating a contribution reads as insecurity.
- **§14 em dashes.** Hard constraint, and it matches this project's own style rules.
- **§10 rule of three** and **§7 AI vocabulary.**

## Guardrails

Humanizer is a general editor, so three of its defaults need correcting for a thesis.

- **Do not inject voice.** Humanizer's PERSONALITY AND SOUL section already excludes technical and reference text, where neutral and plain *is* the correct human voice. Honor that exclusion. No first person, no opinions, no asides.
- **Do not flatten real terminology.** Humanizer's own detection guidance warns against this: it targets specific inflated words, not all formal vocabulary. Domain terms are precision, not padding. Keep them.
- **Protect the apparatus.** Leave citations, LaTeX commands, math, labels, and quoted source material untouched. Humanize the prose around them.

## Before and After

**Before** (dense, mechanical, one 45-word sentence):

> It is important to note that the environmental footprint of high-performance computing systems constitutes a multifaceted challenge, encompassing energy consumption, carbon emissions, and water usage, and it is therefore crucial that researchers develop a comprehensive understanding of these interrelated factors in order to devise effective mitigation strategies.

**After** (clear, flowing, reader-facing):

> High-performance computing carries an environmental cost, and that cost is easy to underestimate. Electricity is the visible part. Cooling the machines consumes water as well, and the carbon intensity of that electricity varies with the time of day. Overlook any one of these factors, and an optimization meant to reduce impact can end up increasing it.

Shorter sentences, plain words, and a close on a concrete consequence. Note the register: professional does not mean dense or technical. It means precise and calm.

## Red Flags

- A sentence with three or more commas. It is doing too much. Split it.
- You typed *Moreover* or *Furthermore*. The connection is real, so state the connection instead.
- Exactly three parallel items. That is rule-of-three autopilot. Use two, or four, or a different shape.
- Several short fragments in a row. That is drama, not clarity. See humanizer §31.
- You shipped a draft without the humanizer pass. Go back.
