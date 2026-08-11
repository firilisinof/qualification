---
name: writing-academic-prose
description: Use when drafting or revising academic prose (thesis chapters, papers, abstracts, related-work sections) and the text reads dense, mechanical, or flat instead of clear and flowing
---

# Writing Academic Prose

## Overview

You are writing, not engineering. Drop code-brain: no enumerating every case, no defensive hedging, no dumping a bullet list into sentence form. Prose is linear and human, and one reader is moving through it one sentence at a time.

**Core principle: clarity over complexity, always.** A reader who has to reread a sentence has caught you failing. Rigor lives in what you claim, not in how hard the claim is to parse.

## The Recipe

Apply to every paragraph you write or revise.

1. **One idea per sentence.** Two independent clauses stitched with "and", "which", or a semicolon usually want to be two sentences. Split them.
2. **Keep most sentences short; vary the rest deliberately.** A short sentence lands a point. An occasional longer one carries a nuance. Never let a sentence run past ~30 words without a reason you could name.
3. **Plain word wins.** Pick the simplest word that is still precise: *use* over *utilize*, *shows* over *demonstrates*, *because* over *due to the fact that*, *to* over *in order to*.
4. **Connect by substance, not signposts.** Cut *Moreover*, *Furthermore*, *Additionally*, *It is important to note that*. If two ideas connect, the connection itself is the transition. Show it.
5. **Surprise through juxtaposition.** The "unpredictable connection" comes from setting two ideas side by side that the reader did not expect to meet, then making the link obvious in hindsight. It never comes from fancy vocabulary.
6. **Write to a reader.** Each sentence raises a question. Answer it in the next one. At a paragraph's end, satisfy the reader's silent "so what?"
7. **Concrete before abstract.** Ground a claim in a mechanism, a number, or an example before you generalize from it.

## Cut List

Filler that kills flow. Delete on sight:

- "It is worth noting / important to note that"
- "plays a crucial / vital / key role"
- "a wide range of", "a myriad of"
- "In order to" → "To"
- rule-of-three padding (three adjectives or examples on autopilot)

## Before / After

**Before** (dense, mechanical, one 45-word sentence):

> It is important to note that the environmental footprint of high-performance computing systems constitutes a multifaceted challenge, encompassing energy consumption, carbon emissions, and water usage, and it is therefore crucial that researchers develop a comprehensive understanding of these interrelated factors in order to devise effective mitigation strategies.

**After** (clear, flowing, reader-facing, unexpected link):

> High-performance computing carries an environmental cost, and that cost is easy to underestimate. Electricity is the visible part. Cooling the machines consumes water as well, and the carbon intensity of that electricity varies with the time of day. Overlook any one of these factors, and an optimization meant to reduce impact can end up increasing it.

The second version says the same thing in shorter sentences and plain words, and it closes on a concrete consequence. Note the register: professional does not mean dense or technical. It means precise and calm.

## Red Flags — You Are Drifting Back

- A sentence with three or more commas → it is doing too much. Split it.
- You typed *Moreover* / *Furthermore* → the connection is real, so state the connection instead.
- Exactly three parallel items → rule-of-three autopilot. Use two, or four, or a different shape.
- Every sentence the same length → monotone. Break the rhythm on purpose.
- You reached for the longer word → is the shorter one still precise? Then use it.

## Related

For a *revision* pass that strips AI-writing tells (em-dash overuse, inflated symbolism, negative parallelisms, vague attribution) from text that already exists, use the `humanizer` skill. This skill generates good prose; `humanizer` cleans up prose that already went wrong. Match the document's language (write the fix in the language of the surrounding text).
