# Output Contracts and the Boundary of Verifiability

2026-07-05. Non-normative. Related: ADR 0002.

> Japanese original (authoritative): [../2026-07-05-rationale-ai-output-contracts.md](../2026-07-05-rationale-ai-output-contracts.md) at commit `320e59d` (`320e59d79d13ff6ef67589d737f725bd146cdfb3`). Terminology and critical-review fixes (adopter, analogies, less repetition): [../README.md](../README.md) and [README.md](./README.md). If English lags, prefer Japanese.

---

In software engineering, a "contract" is more than an interface signature. Bertrand Meyer's Design by Contract ([Meyer, 1992](https://doi.org/10.1109/2.161279)) makes reliability depend on preconditions, postconditions, and invariants between caller and callee. That idea gains force in the AI era.

Fluent prose is not a guarantee of correctness. That is not mere distrust of LLMs; it is a boundary-design principle. Humans err, search ages, databases omit. Systems always compose imperfect parts. LLM output often arrives as a finished-looking explanation, so guesses look like facts. Credibility must not rest on a "smarter model"; it must rest on verifiable contracts of the kind Meyer described.

## Provider freedom and consumer contracts: interface stability

When Design by Contract is applied to AI-driven edits, Semantic Versioning ([semver.org](https://semver.org/)) offers a **readable analogy**: declare a public API explicitly, and treat backward-incompatible changes as a major version bump. However pretty the provider’s internals, silently breaking a public contract that consumers depend on destroys systemic trust.

Agents rewrite broadly and will happily “clean up” signatures while touching internals. Optimizing internals (e.g. Clean Architecture Adapters) can be fine; **silently changing Interfaces or external calling conventions is not** (aligned with ADR 0002). A contract is more than JSON Schema type checks—it is the trust boundary that contains generative freedom. This does not ask us to transplant a package-versioning regime wholesale. **Analogy aids understanding; it is not a portable law.**

## Separating Prose Fluency from Factuality

The hallucination survey by Ji et al. ([arXiv:2202.03629](https://arxiv.org/abs/2202.03629)) systematically organized how generative fluency and factuality can be independent. Additionally, the summarization research by Maynez et al. ([ACL Anthology](https://aclanthology.org/2020.acl-main.173/)) analyzed how abstractive summarization can generate content not faithful to the input from the perspectives of faithfulness and factuality.

The lessons these studies offer are common. The fundamental problem with AI output is not that "it occasionally lies." It is that looking solely at the surface of the output text makes it inherently impossible to determine what it is based on, how certain it is, or whether it can be adopted as a domain fact for business operations.

What ADR 0002 rejects is prose that cannot be verified, traced to sources, reviewed by a human, or safely written back to a trusted store—"useful-looking prose that cannot be validated, traced to source evidence, reviewed by a human, or safely written back into any trusted store." Output must be received in a form that is rejectable, reviewable, and persistable from the very start.

## Do Not Make Prose the Villain: Information Hiding and Boundary Design

Make no mistake. Prose is not unnecessary. In areas that assist human inspiration and judgment—such as explanations, summaries, explorations, and presenting design alternatives—prose is overwhelmingly suitable. The problem lies in ignoring module boundaries, such as the "Information Hiding" advocated by David Parnas, and passing prose directly inside the trust boundary (the area persisted as system state). The explanatory text displayed on a review screen and the factual record trusted by the domain must be distinct.

This distinction might seem like a mundane point about types and schemas being important. However, when LLMs are integrated, this mundane boundary suddenly becomes easily breached. An SDK return value contains a plausible `message.content`. In a demo, simply displaying it on the screen provides value. Next, you want to save that string to a DB. Finally, the saved string is read by another use case as "verified knowledge." Accidents happen on this slippery slope.

Output contracts create steps on that slippery slope. This is not an emotional plea to "distrust AI," but an architectural requirement to "explicitly declare where trust is placed." Free-text descriptions are treated as descriptions. Trusted knowledge is treated as structured data with sources, confidence levels, review statuses, and scopes of adoption.

## Leaving Reasoning as Evidence: Ensuring Auditability

Reasoning must not be black-boxed as the LLM's hidden thought process. It should be treated as auditable evidence. If it affects user-visible content or persistent state, the grounds, citations, source spans, assumptions, rejected alternatives, confidence levels, and review status must be recorded (ADR 0002). However, what is recorded is not a raw dump of the chain-of-thought. It is structured evidence. The private thought process is not exposed; only a form that can be reviewed as a diff is retained.

This "reasoning as evidence" is also a design choice to reduce human review time. What reviewers want to know is not the internal prose the model navigated. They want to know which input fragments were relied upon, what was assumed, what is uncertain, and what storage destinations or UIs will be affected if this output is adopted. There is no need to short-circuit AI accountability to exposing the chain-of-thought. The accountability required for business operations can be largely fulfilled by appropriate data design for source references and review status.

The Human-AI Interaction guidelines by Amershi et al. (CHI 2019) outline the importance of AI systems appropriately indicating uncertainty and supporting user feedback and corrections. The output contract brings this UI-level principle down to the application's data boundaries. To display uncertainty in the UI, "uncertainty" must first exist as structured data within the system.

## Boiling Down to Rules That Can Be Rejected in Review

This must not end as mere ideals. Use cases that treat free-text AI prose as trusted domain data without any validation are explicitly rejected. AI-derived knowledge persisted without source evidence or review status is also rejected (ADR 0002 Enforcement). Designs that write prose to a DB as business facts are prohibited at the architectural level from the start.

Schema-verifiable output is beginning to be offered as a first-class feature by major providers, such as OpenAI's Structured Outputs and Anthropic's Structured outputs. However, the provider's feature itself is not what's important. Even if a provider can return something akin to a JSON Schema, how that structure connects to the application's trust boundary is the project's responsibility.

From a Clean Architecture perspective, provider SDK convenience features should remain inside the adapter. What the use case receives is not an SDK-specific response, but a DTO and validation result defined by the project. The model returning structured output aids in implementing the contract. But it is not the contract itself. The contract—what is mandatory, what causes rejection if missing, and what state triggers "human review required"—is decided by the project.

## Persistence is a Declaration of Adoption

Temporarily displaying AI output on a screen and saving it to a trusted store carry decisively different weights. Saving easily becomes a declaration that future use cases may reuse that information. Even if the UI displays "Unconfirmed," if the design is such that the review status is lost the moment it is copied to another DB table, the unconfirmed nature effectively vanishes, and contamination spreads throughout the system.

Therefore, the output contract must be considered all the way to its storage destination. Information like `review_status`, `source_refs`, `confidence`, `warnings`, and `scope` are not UI decorations. They are control information that determines how downstream processes may handle that data.

This is the exact same logic behind why `docs/architecture/external-resource-adoption-contract.md` puts an adoption lifecycle on external **resources**. Check outcomes are `accepted | rejected | needs_recheck`; **passing a check (accepted) is not yet trusted use**. Entry into active trusted use is a separate transition, `accepted -> adopted` (see [../README.md](../README.md) / [README.md](./README.md) on accepted vs adopted). Regardless of whether the origin is AI or human, bringing anything of external origin into the project's trust boundary requires strict records of adoption.

## The Etiquette of This Folder Itself

The practice of attaching retrieval dates to sources in `research` and explicitly noting unverified URLs is an application of the same concept of contracts to human-facing documents. Do not supplement literature with guesses. Do not treat hallucinations as a problem solely of code or APIs. Since documentation is a critical element composing the system, it requires the same bulwarks.

However, `docs/research/` is not the place to unilaterally change the rules of the operational template. The writings here are explanations for humans to decipher the philosophy of software development; they are not contracts for AI agents to read mechanically. If an argument is to advance to a project norm, it must be elevated to a different reviewable artifact, such as an ADR, collaboration document, or issue. This separation itself aligns with the philosophy of output contracts. Write rich explanations as explanations. Explicitly adopt the rules to be adopted at a different boundary.

## References

1. **Repository references**
   - `docs/architecture/adr/0002-input-output-reasoning-contracts.md`
   - `docs/architecture/io-reasoning-contracts.md`
   - `docs/architecture/external-resource-adoption-contract.md`
   - `docs/research/README.md`
2. **Software Engineering & Philosophy**
   - Meyer, B. "Applying 'Design by Contract'". IEEE Computer, 1992. https://doi.org/10.1109/2.161279 (Retrieved 2026-07-17)
   - Parnas, D. L. "On the Criteria To Be Used in Decomposing Systems into Modules". CACM, 1972. https://doi.org/10.1145/361598.361623 (Retrieved 2026-07-17)
   - Preston-Werner, T. *Semantic Versioning 2.0.0*. https://semver.org/ (Cited for its rules on declaring a public API and incrementing the major version on incompatible API changes. Retrieved 2026-07-17.)
3. **AI Research & Human-Computer Interaction**
   - Ji, Z. et al. "Survey of Hallucination in Natural Language Generation." *ACM Computing Surveys* / arXiv:2202.03629. https://arxiv.org/abs/2202.03629 (Retrieved 2026-07-16)
   - Maynez, J. et al. "On Faithfulness and Factuality in Abstractive Summarization." ACL 2020. https://aclanthology.org/2020.acl-main.173/ (Retrieved 2026-07-16)
   - Amershi, S. et al. "Guidelines for Human-AI Interaction." CHI 2019. https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ (Retrieved 2026-07-16)
4. **Official Documentation**
   - OpenAI. *Structured Outputs*. https://platform.openai.com/docs/guides/structured-outputs (Retrieved 2026-07-16)
   - Anthropic. *Structured outputs*. https://platform.claude.com/docs/en/build-with-claude/structured-outputs (Retrieved 2026-07-16)
   - Anthropic. *Increase output consistency*. https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency (Retrieved 2026-07-16. Old docs.claude.com URL redirects here.)
