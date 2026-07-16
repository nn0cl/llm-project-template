# Normative vs. Reading Documents: Documentation Architecture

2026-07-06. Non-normative. Related: `docs/research/README.md`, `agent-quickstart.md`.

> Japanese original (authoritative): [../2026-07-06-rationale-normative-vs-reading-documents.md](../2026-07-06-rationale-normative-vs-reading-documents.md), terminology as of commit `d1b86c8`. Agent-read policy and terms: [../README.md](../README.md) (「エージェントと research」「用語」; accepted vs adopted) and [README.md](./README.md) (Glossary). If English lags Japanese, prefer Japanese.

---

As a project matures, documentation volume grows. The line between rules the system must obey and background reading blurs. Humans skip what they do not need right now. Agents cannot: anything in the context window—chatty notes or deep philosophy—shapes reasoning and code generation. So agent inputs are a strict allowlist, and reading material and philosophy sit outside that list by structure.

However, "agents need not read reading materials as daily task input" is not a physical access ban, but an architectural expectation (see [../README.md](../README.md)). It means there is no need to load `research` as normal task input. The rich text (philosophy) written for humans to deeply understand the development ideology, and the operational contracts (constitution) that agents mechanically follow, have entirely different purposes and readers. If this distinction is blurred, we are forced to choose: either we write rich reading materials that bloat agent instructions and dull their reasoning, or we write strict agent instructions that make human-facing explanations thin and dry. Structural separation of documentation is an architecture designed to achieve both at the highest quality.

"I want to manage investigation results as reports with Sources, separate from design documents and operational constraint documents—as reading material that agents need not read as daily task input. The research folder is not copied when the template is rolled out to other repositories."

In this template, documents have three distinct tiers: Design Documents (Architecture), Operational Constraints (Collaboration), and Reading Materials (Research). The agent's context is always composed solely of the top two "Norms." However, investigation results and philosophy are not discarded. They are accumulated with their Sources for future human engineers. Only the conclusions that are debated, agreed upon, and codified into rules are extracted and "elevated" into ADRs, collaboration docs, or issues.

Editing `docs/research/` does not change the project's operational template (the operational rules themselves) provided by `llm-project-template`. No matter how many references you add, or how thickly and philosophically you rewrite an essay, that alone does not constitute any change to the norms. If a change in norms is required, it must be submitted separately as a diff to an ADR or collaboration document and pass the Adjudicator's review. It is precisely because of this sharp dividing line that humans can safely write deeply and richly about philosophy and background without fear of breaking the system's behavior.

## Correspondence with Diátaxis: Information Architecture

[Diátaxis](https://diataxis.fr/) categorizes software documentation into four quadrants by purpose (tutorials / how-to / reference / explanation) and boldly states that "mixing these together fatally degrades documentation quality." The design documents and operational constraints in this template correspond strongly to `reference` and `how-to` in Diátaxis. Conversely, `research` corresponds to pure `explanation`. Agents need not read `explanation` as daily task input—this is exactly the implementation of the strict Diátaxis rule "do not mix explanation into reference," adapted for the AI agent era.

The most important lesson of Diátaxis is that there is no hierarchy of superiority among documents, but rather a "difference in purpose." A reference prioritizes accuracy and searchability above all else. A how-to prioritizes the mechanical completion of steps. An explanation aids the reader's deep understanding and reflection. We can write rich research as explanation precisely because the references and how-tos that the agent must follow are isolated in different folders. Conversely, if we mix direct instructions (rules) into research, the explanation devolves into a preachy rulebook, and the reference becomes overloaded and ambiguous.

## The RFC Tradition: Normative and Informative

Since [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119), which built the foundation of the Internet, the strict distinction between "normative" (prescriptive/obligatory) text and "informative" (reference/non-normative) text has been an absolute fundamental in the world of technical standardization. The "reading material" referred to in this document is informative text—it does not directly affect system compliance, i.e., the agent's correct code generation or tool behavior.

In the RFC world, normative text and informative examples sometimes coexist within the exact same document. But in this template, we separate them even more strongly, physically, using "folders" and script-based "reference paths." The reason, as stated repeatedly, is agent context management. Human engineers can visually distinguish that "this section is a background column," but when a long document is handed to an agent, its entire text is often interpreted flatly as "grounds for action (prompt)." That is why they must never be mixed; reading materials are placed in their own isolated location as reading materials.

## An Allowlist is Stronger than a Denylist: Security and Budget

`privacy-context-budget-policy.md` standardizes the minimization of context payloads. To satisfy this constraint, the most robust implementation to guarantee that reading materials are excluded from what agents read is not an exclusion list (Denylist), but an "Allowlist." Documents that are not referenced are guaranteed to be effectively non-existent to the system.

A Denylist is fragile against a file system where entropy constantly increases. When new reading materials or temporary files are added, simply forgetting to explicitly add them to the exclusion list instantly allows them to bleed into the agent payload as noise. An Allowlist is the exact opposite. The Operating Path explicitly lists the documents to be read on a whitelist, and new documents will never become input context unless they are explicitly added through architectural consensus. This robust property strongly serves both privacy (protection of sensitive information) and reasoning budgets (maintenance of reasoning precision).

## Elevation is One-Way

"Elevation" from `research` to ADR / collaboration / issue (via the Adjudicator's judgment) is encouraged. However, the reverse path is absolutely never created. If a normative document references the contents of `research` normatively (as a rule to follow), the carefully constructed structural separation collapses. The technical guarantee that research is out of scope for synchronization is physically enforced by the fact that `docs/research` is entirely excluded from the enumerated list in `collaboration-template-paths.sh`.

The fact that the elevation path is one-way does not mean that research is taken lightly. Rather, it is to make the intellectual activity of research truly free. Here, bold hypotheses, historical backgrounds, rejected counterarguments, and comparative readings of literature from other companies can be written richly without worrying about word counts. There is no need to forcefully squeeze soft ideas, which are not yet established rules, into the form of short, rigid imperative sentences (prompts). We deliberately separate this space from the cold environment the agents obey to secure a place for humans to think deeply and mature their philosophy.

## References

1. **Repository references**
   - `docs/research/README.md`
   - `docs/collaboration/privacy-context-budget-policy.md`
   - `docs/architecture/agent-quickstart.md`
   - `scripts/lib/collaboration-template-paths.sh`
2. **Documentation Architecture**
   - Diátaxis. https://diataxis.fr/ (Retrieved 2026-07-07)
   - Canonical. "Diátaxis, a new foundation for Canonical documentation." https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation (Retrieved 2026-07-07)
3. **Principles of Technical Standardization**
   - RFC 2119. *Key words for use in RFCs to Indicate Requirement Levels*. https://www.rfc-editor.org/rfc/rfc2119
   - RFC 8174. *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*. https://www.rfc-editor.org/rfc/rfc8174 (Retrieved 2026-07-16)
