# Design First and Controlling Context Boundaries

2026-07-05. Non-normative. Related: ADR 0001.

> Japanese original (authoritative): [../2026-07-05-rationale-design-first-minimal-context.md](../2026-07-05-rationale-design-first-minimal-context.md) at commit `6910bf0` (`6910bf0ecd025b7561b1446568f0459c00283b3d`). Terminology and critical-review fixes (adopter, analogies, less repetition): [../README.md](../README.md) and [README.md](./README.md). If English lags, prefer Japanese.

---

When running LLMs, competing over "clever prompts" misses the engineering point. The hard work is boundary control, as in module design: what to pass, what to omit, which tool owns which operation. The most reliable control on an autonomous coding agent is the design of its payload. Include/omit choices are the integration layer that tells the sandbox what to see and what not to guess ([The Agent is a Sandbox](./2026-07-07-rationale-saas-agent-as-sandbox.md)).

I treat context selection as a reviewable design artifact, not personal prompt craft. Every request starts with design; tests and implementation follow.

In the Design Intake, the target behavior, VO/DTO candidates, Ports and Adapters boundaries, contexts to include and omit, model/tool routing, and "boundaries where guessing is prohibited" are decided upfront (ADR 0001). Design is not a mere ritual. It is a record of decision-making. An excellent design intake provides the agent not only with instructions on "what to do," but also guardrails on "what it must not proceed without knowing."

## The Illusion That More Context is Always Better

If a goal can be achieved with a smaller payload, do not indiscriminately send the entire repository. The reason is not just token cost or processing time. Irrelevant context physically degrades the model's reasoning performance.

The study by Shi et al. ([arXiv:2302.00093](https://arxiv.org/abs/2302.00093)) demonstrated that simply adding irrelevant information to a problem statement significantly lowers an LLM's reasoning accuracy. The payload must be strictly selected and sent. This is less a best practice and more an empirically backed constraint.

Furthermore, Liu et al.'s "Lost in the Middle" ([arXiv:2307.03172](https://arxiv.org/abs/2307.03172)) showed that even for models capable of handling extremely long contexts, information utilization performance changes in a U-shape depending on where the relevant information is located in the document (easy to recall at the beginning and end, but easy to forget in the middle). A large context window is not a panacea memory space. Rather, the longer the window, the heavier the design responsibility of "what to put in" weighs on the human side. Handing over a massive amount of documents with the instruction "read this well" is an abandonment of design.

Context should be treated as a scarce resource. Anthropic's explanation on context engineering ([Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)) recommends keeping the information passed to an agent "informative, yet tight." Making the ledger of include/omit a mandatory item in the design is a concrete implementation form to realize this tight context.

## Omit is Not Passive Skipping: The Boundary of Guessing

In software design, many documents describe "what the system does (what it includes)." However, in collaborating with AI, "what the system does not do (what it does not include)" is equally important. Omit is not mere saving. It is a proactive design act that draws a boundary of guessing for the model.

For example, if you include a discussion process containing an unresolved data store selection in the payload, the agent might see that vocabulary, treat it as a fait accompli, and mix it into the implementation. If you pass irrelevant past implementation examples, it might mimic outdated patterns that differ from current new design policies. Passing private data broadly exposes data unnecessarily and creates security risks. Omit confines these dangers not as vague natural language requests to "be careful," but as a physical block of input data.

This is why `docs/collaboration/privacy-context-budget-policy.md` establishes a payload budget. Privacy protection and reasoning performance improvement are not contradictory; they are two sides of the same coin. Not passing unnecessary things reduces the surface area for information leaks, reduces reasoning noise, and narrows the scope of evidence humans must review.

## The Capability Ladder: Demarcation of Responsibility and Cost Optimization

Mechanical formatting tasks go to deterministic tools. Simple completions go to small models. Boundary judgments, interpretations of ambiguous domain logic, and advanced decisions involving privacy go to strong reasoning models. The bottom-level principle is extremely simple: "Do not use a probabilistic LLM for something a deterministic tool can handle."

The economics of model routing are backed by the FrugalGPT study by Chen, Zaharia, and Zou ([arXiv:2305.05176](https://arxiv.org/abs/2305.05176)), and the subsequent RouteLLM ([arXiv:2406.18665](https://arxiv.org/abs/2406.18665)) formulated the very act of assigning strong or weak models based on query difficulty as a learnable problem. Not calling a powerful model for tasks where a cheap model suffices is not merely about saving cloud costs. Abusing strong models creates an architectural risk where the locus of decision-making becomes ambiguous.

If you ask an AI to decide what a code formatter or Linter should decide, the output reproducibility drops, and CI becomes unstable. If you settle violation checks of dependency boundaries with human-persuasive prose, they will not remain in the codebase as mechanical constraints. The "capability ladder" is a design of the demarcation point of responsibility before it is a means of cost optimization.

The "strong reasoning" referred to here is also not an omnipotent authority. Calling a strong reasoning agent in the Architecture Path is not to let it unilaterally adopt an ADR (Architecture Decision Record). It is to have it prepare the options and rationale for a human architect (Adjudicator) to judge. The higher the capabilities of the tools, the more explicitly we must design the boundary between what the tool may decide autonomously and what humans ultimately decide.

## Undecided is Not Blank: Managing the Unknown

In requirements definition, undecided matters are not "empty blanks." They are explicit states of "not yet decided." Items listed under `Current Non-Decisions` are not areas the agent may freely fill in with guesses. They are topics for future ADRs. "Must not guess" is a mandatory field in the design note. As a method to control input ambiguity, structured approaches in requirements engineering like EARS ([IEEE Xplore](https://ieeexplore.ieee.org/document/5328509)) are also instructive.

If ambiguous requirements are passed as-is along with a large payload, the model will attempt to fill the blanks with "plausible hallucinations." This is not so much a defect of the model as it is an essential characteristic of generative models that continuously predict the next token. This is exactly why a syntax is needed to make the system recognize a blank as a "blank" and prevent it from proceeding further. Items like `Ambiguities`, `Open decisions`, and `Stop conditions` in the design note are not just for stopping work, but are bulwarks for explicitly preserving areas that must not be filled by guessing.

## Design First is Not Waterfall

Saying "start from design" might evoke the heavy, exhaustive Big Design Up Front of classic Waterfall development. However, the Design Intake in this project is not for deciding everything in advance. Rather, it is an extremely agile, lightweight gate to separate "what needs to be decided now" from "what must not be decided yet."

The compact design note in the Fast Path is proof of this. Fixing a typo or performing mechanical refactoring does not require an exaggerated design document. Yet, scope, omitted context, and deterministic checks are briefly stated in a few lines. The value of Design First lies not in the volume of the document, but in being conscious of the "boundary of the change" prior to the work.

In the Feature Path, acceptance specifications and phase gates become the center of the design. In the Architecture Path, we distinguish whether we are changing rules, writing reading materials, or issuing an ADR. This distinction is especially important in work involving writing reading materials like `docs/research/`. Reading materials may be written with deep philosophical thickness. But the foundational rules of the operational template must not be arbitrarily changed. Precisely because this boundary is set first, free and creative work is possible within specific domains.

## Confining Uncertainty: The Discipline of Design

The principle of prioritizing deterministic tools is a design that intentionally confines the inherent uncertainty of LLMs to a narrow space. Minimizing the situations where uncertainty is handled within the system is itself part of the discipline of software engineering in the AI era. This is an idea that pairs with [Evidence and Rules](./2026-07-06-rationale-evidence-based-process-design.md).

The Design First approach is not a wasteful ritual to slow down the AI's work speed. It is a structure to transform the overwhelming generation speed of AI into a form the project can safely absorb (digestible changes). The ability to generate quickly does not directly mean the ability to integrate quickly. To generate continuously integrable code, we must decide "based on what evidence," "at which boundary," and "up to which phase to proceed" *before* hands start moving.

## References

1. **Repository references**
   - `docs/architecture/adr/0001-design-first-ai-request-routing.md`
   - `CLAUDE.md`
   - `docs/collaboration/privacy-context-budget-policy.md`
   - `docs/collaboration/llm-cost-reduction.md`
2. **AI Model Reasoning Performance and Context Research**
   - Shi, F. et al. "Large Language Models Can Be Easily Distracted by Irrelevant Context." arXiv:2302.00093. https://arxiv.org/abs/2302.00093 (Retrieved 2026-07-16)
   - Liu, N. F. et al. "Lost in the Middle: How Language Models Use Long Contexts." arXiv:2307.03172. https://arxiv.org/abs/2307.03172 (Retrieved 2026-07-16)
   - Anthropic. *Effective context engineering for AI agents*. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (Retrieved 2026-07-16)
3. **Cost Optimization and Requirements Engineering**
   - Chen, L., Zaharia, M., Zou, J. "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance." arXiv:2305.05176. https://arxiv.org/abs/2305.05176 (Retrieved 2026-07-16)
   - Ong, I. et al. "RouteLLM: Learning to Route LLMs with Preference Data." arXiv:2406.18665. https://arxiv.org/abs/2406.18665 (Retrieved 2026-07-16)
   - Mavin, A. et al. "Easy Approach to Requirements Syntax (EARS)." IEEE RE'09. https://ieeexplore.ieee.org/document/5328509 (Retrieved 2026-07-16)
