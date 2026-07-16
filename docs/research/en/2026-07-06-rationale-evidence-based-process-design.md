# Evidence and Rules: EBSE and the Respect for Context

2026-07-06. Non-normative. Related: LISS-0002, LISS-0005, `process-gap-register.md`.

> Japanese original (authoritative): [../2026-07-06-rationale-evidence-based-process-design.md](../2026-07-06-rationale-evidence-based-process-design.md) at commit `6910bf0` (`6910bf0ecd025b7561b1446568f0459c00283b3d`). Terminology and critical-review fixes (adopter, analogies, less repetition): [../README.md](../README.md) and [README.md](./README.md). If English lags, prefer Japanese.

---

Process "rules" are often set by fashion: industry fads, loud mega-tech case studies, or a few seniors' success stories. The quieter question—"Will this practice work in *our* team size, product phase, and debt?"—is still rare. I investigate before freezing rules, check them against our project context, and leave final responsibility with a human Adjudicator.

When designing collaboration processes with AI, the temptation to jump on fads is particularly strong. New agent features, new prompt engineering techniques, and new "AI-Native best practices" appear almost weekly. While highly topical, no one knows what side effects they might bring in our exact operational context. If we elevate them to normative rules without objective evidence, the template will quickly become a sediment of trends or a Frankenstein of contradictory rules. That is why I strictly separate "research" from "norms." The things we investigated and the processes of discussion remain as `research`, and only those that survive rigorous evaluation and are actually adopted by the project are elevated to "norms (ADRs)."

"Investigate prior research, empirical studies, precedents of existing services, and best practices. Analyze them, and give me a consultation."

These were the words born from a desperate demand on the ground: *do not decide how to handle the `develop` branch based on intuition or mood*. However, this was not a one-off request, but rather an elevation into three robust behavioral patterns as a general rule. First, investigate before setting rules. Second, make failure feedback from agents and adopters the primary input for revision. Third, separate research and norms, keeping records of both.

## The Lineage of EBSE (Evidence-Based Software Engineering)

The monumental paper by Kitchenham, Dybå, and Jørgensen ([ICSE 2004 PDF](https://web-backend.simula.no/sites/default/files/publications/SE.5.Kitchenham.2004.pdf)) proposed porting the methods of "Evidence-Based Medicine," which revolutionized the medical field, into software engineering (EBSE). Subsequent research by Dybå et al. ([IEEE Software 2005 PDF](https://web-backend.simula.no/sites/default/files/publications/Dyba.2005.1.pdf)) warned that adopting technologies based on assumptions without objective evidence leads to fatal misjudgments in projects.

While EBSE takes medicine as its model, it cannot be imported innocently as-is. Medicine has a tradition of double-blind Randomized Controlled Trials (RCTs), but field experiments in software engineering are so heavily context-dependent (relying on human skills and organizational culture) that rigorous reproduction is nearly impossible. That is precisely why EBSE advocates not a mechanistic "decisions are automatically made if objective evidence is found," but a highly intellectual procedure of "critically evaluating evidence and integrating it into our specific context." The flow of "Investigation + Context + Adjudicator Decision" in this template is a direct projection of this EBSE procedure into small-scale daily operations.

The basic steps of EBSE—(1) Formulating the question, (2) Searching for evidence, (3) Critical appraisal, (4) Integration into practical context—are exactly isomorphic to the steps we took in the aforementioned `develop` discussion. We formulated the question (should long-lived branches be completely banned?), searched for evidence (practices by DORA, the GitFlow creator, and mega-tech companies), performed a critical appraisal ("integration latency, not existence itself, is the problem"), and proposed a project-specific rule (permission under an integration contract).

## Correcting Intuition with Data: Lessons from DORA

[DORA](https://dora.dev/capabilities/trunk-based-development/) has statistically measured the correlation between process practices and delivery performance through years of large-scale surveys. The initial, simplistic intuition that "the develop branch is evil and should be completely banned" was revised into a more refined view by decoding DORA's operational definition of data—"integration frequency." This is a prime example of how the demand to place empirical research behind rules actually functioned to eliminate emotional arguments.

*Accelerate* by Forsgren, Humble, and Kim ([IT Revolution](https://itrevolution.com/product/accelerate/)) summarizes DORA's research methodology: measuring the relationship between technical/organizational practices and system performance through statistical analysis based on large-scale surveys. What we must learn is not to blindly agree with their individual claims. We must learn the attitude itself: "evaluate practices based on objective data, not personal intuition or loudness of voice."

However, that attitude must always be paired with a strong caveat: "Correlation depends on context. Elite practices at mega-tech companies elsewhere do not automatically apply to our own budget and constraints."

## Feedback Drives Norms: The Process Gap

"Reports from adopters → gap analysis → norm revision." `process-gap-register.md` (normative) says not to silently ignore ideal–reality gaps: document and register them. LISS-0002 (Session 1) and LISS-0005 (Session 2) are testaments to this. The system repairs itself not only through top-down rules but through bottom-up observations from the field.

## The "Evidence" and "Context" Required by ISSUEs and ADRs

The reason this template consistently and strongly demands that agents provide "supporting references" and "project context" in ISSUEs (plans) and ADRs (Architecture Decision Records) is precisely to enforce this EBSE philosophy as a process.

To the questions "Why choose this design?" or "Why include this library?", mere AI guesses or fluent prose stating "Because it is generally popular" are unacceptable. The reason ADR formats have "Context" and "Consequences" sections, as shown by Michael Nygard's original source, is to record under what local constraints and based on what evidence the decision was made.

In AI collaboration, this constraint carries a dual meaning. Agents can instantaneously pull countless "general best practices" from their training data, but they cannot evaluate whether those practices fit the project's specific context (budget, phase, constraints of the existing system). Therefore, when planning work in an ISSUE or drafting an ADR, the agent is forced to verbalize both "links to official documentation or precedents for the adopted technology (objective evidence)" and "why it is necessary for our current situation (integration into context)", and pass it through the human Adjudicator's verification gate. This is the reality of the Evidence Discipline demanded by the template.

## External resource adoption vs software dependencies

One place EBSE’s “integrate into context” shows up is when something external enters the trust boundary. Do not conflate targets:

- **Software dependencies** (libraries, SDKs, CLIs, …) → `docs/architecture/dependency-policy.md`
- **External resources** (AI-generated artifacts, imported data/content, …) → `docs/architecture/external-resource-adoption-contract.md`

Models may propose “library X is standard,” but cannot judge fit to this team’s security, conflicts, or maintenance structure. For resources, separate check verdicts (`accepted | rejected | needs_recheck`) from trusted use (`accepted -> adopted`); accepted alone is not adopted (see [../README.md](../README.md) / [README.md](./README.md)). In both paths, “seems convenient” is not enough—project-context evidence and explicit Adjudicator approval are required.

## "Investigated" Does Not Mean "Correct": Awareness of Limits

Evidence in software engineering is not as robust as evidence in medicine or physics. RCTs are rare, and context-dependency is overwhelmingly large. That is precisely why decisions are made based on the triad of "Investigation Results + Project Context + Adjudicator Decision." Research is left as non-normative "speculation," and normalization occurs only after Adjudicator approval—this is an extremely valid implementation of EBSE's "integration into practical context" step.

This caution is also directed at the "plausible reasoning (hallucinations)" generated by AI. An agent can write any amount of persuasive reasons. But persuasiveness is never evidence. The documents strictly requiring external source URLs and retrieval dates, and explicitly noting unverified claims, constitute a minimal defense line in the AI era. Claims without sources, no matter how fluent, will not be elevated to norms. Because technical evidence becomes obsolete at terrifying speed, retrieval dates are specified to prepare for future re-verification.

Finally, this reading material itself is not normative. Whether the EBSE stance described here is incorporated into actual operation is a job for ADRs and collaboration documents; philosophical essays in `docs/research/` do not forcefully alter the template's operational rules. Not confusing the gathering of evidence and speculation with the changing of rules and taking action—that in itself is the practice of the EBSE stance this document advocates.

## References

1. **Repository references**
   - LISS-0002, LISS-0005
   - `docs/collaboration/process-gap-register.md`
2. **Evidence-Based Software Engineering (EBSE)**
   - Kitchenham, B., Dybå, T., Jørgensen, M. "Evidence-based Software Engineering." ICSE 2004. https://web-backend.simula.no/sites/default/files/publications/SE.5.Kitchenham.2004.pdf (Retrieved 2026-07-07)
   - Dybå, T., Kitchenham, B., Jørgensen, M. "Evidence-Based Software Engineering for Practitioners." IEEE Software 2005. https://web-backend.simula.no/sites/default/files/publications/Dyba.2005.1.pdf (Retrieved 2026-07-07)
3. **Architecture Decisions and Context**
   - Nygard, M. "Documenting Architecture Decisions." 2011. (The importance of context and evidence in ADRs) https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (Retrieved 2026-07-16)
   - Tyree, J., Akerman, A. "Architecture Decisions: Demystifying Architecture." IEEE Software, 2005. (The demand for documenting context and providing evidence in architecture decisions)
   - Clements, P. et al. *Documenting Software Architectures: Views and Beyond*. 2nd ed. Addison-Wesley, 2010.
4. **DevOps and Evidence**
   - DORA. *Trunk-based development*. https://dora.dev/capabilities/trunk-based-development/ (Retrieved 2026-07-07)
   - Forsgren, N., Humble, J., Kim, G. *Accelerate*. https://itrevolution.com/product/accelerate/ (Retrieved 2026-07-16)
