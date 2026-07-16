# Target End State: The Necessity of "Structure" in AI Collaboration

2026-07-05. Non-normative. Gateway to detailed topics.

> Japanese original (authoritative): [../2026-07-05-rationale-target-end-state.md](../2026-07-05-rationale-target-end-state.md), terminology as of commit `d1b86c8`. Agent-read policy and terms: [../README.md](../README.md) (「エージェントと research」「用語」; accepted vs adopted) and [README.md](./README.md) (Glossary). If English lags Japanese, prefer Japanese.

---

Having AI write code is no longer a surprise or technical magic. What is surprising in modern development is how often "nothing remains" of a project after that generation burst: scattered chat fragments and a sudden multi-hundred-line diff. Who approved what and when, why that design won over alternatives, and where the next developer should start reading—the most valuable contexts in software engineering—vanish into the mist. I do not call such non-reproducible generative work "software engineering."

Coding agents move with surprising freedom inside their sandboxes. Freedom of the parts and integration into one project are different problems. For AI and humans to collaborate long-term, the **team** needs structure: Operating Paths, operational contracts, the Adjudicator's approval loop, and persisted artifacts. That premise is expanded in [The Agent is a Sandbox](./2026-07-07-rationale-saas-agent-as-sandbox.md).

This template does not aim to be a magic box where AI finishes everything for humans. It provides "Scaffolding" so AI and humans can **collaborate** sustainably—moving ad-hoc chat into a process that is reproducible and reviewable. That is not "slow down now and bolt governance on later." It places the trio—Adjudicator, Agent, and Deterministic Tool—plus contracts, artifacts, and approval points up front as system premises. Governance is not a tax on speed; it is how rapid generation becomes a sustainable product.

## The Center of the Target End State: Three Questions

The "target end state" this template aims for is not a situation where the AI autonomously decides everything and the project is finished while humans sleep. Quite the opposite. While AI freely explores the design space, generates massive amounts of code, and assists with mechanical verification, the target end state is exactly the state where humans can reliably stop the process and make decisions at singularities where the "meaning" or "responsibility" of the project changes. Rather than tossing all responsibility to AI, it safely connects AI's overwhelming reasoning and generative capabilities to human architectural judgments.

At the center of this are three fundamental questions that must be asked of every change (Pull Request or Diff):

1. **What business or domain requirements does this change satisfy?** (What & Why)
2. **Where in the project was that decision recorded?** (Where is the Truth)
3. **Where can the next human (or agent) who touches this code resume the context?** (Resumability)

A diff that cannot clearly answer these three questions is, from a software engineering perspective, "incomplete," even if all unit tests are Green. Completion includes not just the code running on a computer, but a state where a human can read its lineage and trace the locus of responsibility.

## Working Under a Contract

Human designers (Adjudicators) and AI agents should collaborate only under an explicitly written operational contract. Approvals and arbitration are handled by humans; generation and mechanical verification are handled by agents. This division of responsibility does not change based on the engineer's mood that day or fluctuations in chat prompts; it is robustly fixed as code within the repository in `AGENTS.md` and `CLAUDE.md`. The README calls this "a shared, written operating contract," which is essentially a strong declaration: "We will not settle our relationship with AI through verbal promises or personal tacit knowledge."

In the history of software development, it is not uncommon for a team's processes and etiquette to break down before the source code itself does. Skipping reviews. Not updating Issue statuses. Creating tests after implementation just to make ends meet. Secretly rewriting CI scripts locally. AI executes and amplifies this "process deviation" at a speed incomparable to human manual work. That is why the operational contract is not merely a set of commands to the agent, but also a mirror for humans to maintain the discipline of their own collaboration.

## Decisions Must Not Disappear: Docs-as-Code

Specifications, architectural decisions, plans, work records, and handoffs—every context in software development must be a version-controlled artifact within the repository. Acceptance specifications in EARS/Gherkin formats, ADRs (Architecture Decision Records), local issues and work plans, traces, and handoff documents. SaaS chat logs are unsearchable, highly volatile noise, not artifacts. The ability for future maintainers to logically trace the lineage of changes is not a mere "bonus" of the system; it is an indispensable part constituting the product's quality.

As an extension of the Docs-as-Code philosophy ([Write the Docs](https://www.writethedocs.org/guide/docs-as-code/))—managing processes in the repository just like code—this template subjects even the "contract files that define agent behavior" to version control and CI. If applying review and CI to documentation is the common sense of modern development, it is a natural consequence to apply the same discipline to documents (prompts) that dictate the agent's output behavior.

Michael Nygard's ADR proposal ([Cognitect](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)) presented an extremely practical paradigm of leaving important decisions as short texts under version control. This template extends this philosophy beyond just system architecture decisions to the realm of operational decisions on "how we collaborated with AI."

## The Template Does Not Dictate the Domain: The Humility of Boundaries

The technology stack, data store selection, external providers, and the core domain logic—this template does not involve itself in these project-specific areas. What it provides is strictly "Scaffolding" for processes and collaboration. Undecided architecture is not a blank for the agent to guess and fill in appropriately; it is explicitly marked as "undecided for now" under `Current Non-Decisions`. We never tell the agent "just figure it out." We command it: "If there are undecided items, request the human Adjudicator to create an ADR."

This is a manifestation of "humility" as a template. An operational template must not pretend to know the adopting project's business domain or technical constraints. It can provide a process for collaboration. However, which datastore is optimal, which provider to trust, or which business concept to call an entity belongs entirely to the adopting project's context and the Adjudicator's design judgment. The moment it crosses this boundary, the template becomes an invasion of the project, not development support.

## The Target End State is Not Static: Pull-Based Sync and Self-Evolution

The template begins to become obsolete the moment it is cloned into a project. That is why upstream updates are synced not by forced push, but by proactive pull from the project side, protecting the sovereignty of the downstream (the project side) via 3-way merge (ADR 0008). Project-specific improvements flow back from the downstream and return to the upstream repository as LISS if necessary. This is not a completed, static discipline, but a vessel to continue self-evolving as an ecosystem.

"Completion" here does not mean a final, fixed version where all rules are set, but the completion of the structure of "how to update the rules safely." Software process documents are not "write once and done." AI tool specifications change. The surface agents can intervene in increases. Gaps between the process and reality are found in actual operation. The template approaching completion does not mean changes become impossible, but that the way to make changes becomes clearer and safer.

## The Courage Not to Hide Imperfection

`process-gap-register.md` frankly self-reports that highly parallel agent operations and complex disaster recovery procedures are still immature. If the true target end state includes "safe parallel operation," this template has not reached it yet. The worktree separation by ADR 0007 is merely a technical stepping stone toward that distant goal. Making the level of process attainment a subject of objective self-evaluation is also an important part of architectural design.

Openly and explicitly stating imperfection is proof of trust in developers. Discourse on AI collaboration often falls into an irresponsible omnipotence: "If you leave it to AI, it can do anything." However, what is needed for a practical operational template is not omnipotence, but the ability to accurately state "how far we can safely automate with current mechanisms, where human judgment is indispensable, and which process gaps are unresolved." The Gap Register is not a confession of inadequate capability, but a starting point for continuous improvement.

## Human Approval Points: Implementation of Human-AI Interaction

Establish checkpoints, delegate generation, and stop for review—this structure points in the same direction as the agent workflow best practices described in Anthropic's agent design explanation ([Anthropic Research](https://www.anthropic.com/research/building-effective-agents)). However, the uniqueness of this template lies in physically fixing those approval points (Human-in-the-loop) not as vague recommendations, but as robust documents and irreversible phase gates. No matter how powerful models become in the future, this gate remains. Because it is a design to ensure human responsibility and auditability in the system, not to compensate for the AI's lack of capability.

As Bainbridge's irony of automation ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0005109883900468)) sharply pointed out, automation does not make humans unnecessary; it often makes the work left to humans extremely difficult. That is why the human's role must not be "the person who looks at all the code at the end and guarantees safety." The Adjudicator is strategically placed in advance at the position where the most difficult and valuable design judgments are required.

## Do Not Mix Reading Materials and Norms

The contents of the `docs/research/` folder, including this text, are explanations for humans to decipher the philosophy of software development. Agents need not read this folder as daily task input (not a physical ban; excluded from the normal allowlist — see [../README.md](../README.md)). Furthermore, the discourses and references here do not alter the actual rules of the practical project operational template provided by `llm-project-template`.

This separation of "norms" and "explanations" is architecturally critical. The absolute operational rules agents must follow are strictly defined in documents like `AGENTS.md`, ADRs, `architecture/`, and `collaboration/`. `research/` is the place to write in-depth the Rationale behind why those rules are necessary. It is fertile ground for humans to deeply understand the ideology, maintain the rules without letting them become dead letters, and, if necessary, elevate them to another artifact through discussion. It is not, in itself, a direct document of commands to the agent.

## To Detailed Topics

The following discourses expand the fundamental philosophy stated in this manuscript into specific themes.

- [The Agent is a Sandbox](./2026-07-07-rationale-saas-agent-as-sandbox.md)
- [The Adjudicator and Phases](./2026-07-05-rationale-adjudicator-centered-collaboration.md)
- [Design First and Context](./2026-07-05-rationale-design-first-minimal-context.md)
- [Output Contracts](./2026-07-05-rationale-ai-output-contracts.md)
- [Reviewable Code](./2026-07-05-rationale-code-for-human-review.md)
- [Repository-Native Planning](./2026-07-05-rationale-repository-native-planning-and-change-control.md)
- [Pull-Based Upstream](./2026-07-06-rationale-template-as-pull-based-upstream.md)
- [Branching Strategies in AI Collaboration](./2026-07-06-branching-strategies-develop-and-multi-target-releases.md)
- [Normative vs. Reading Documents](./2026-07-06-rationale-normative-vs-reading-documents.md)
- [Evidence and Rules](./2026-07-06-rationale-evidence-based-process-design.md)

## References

1. **Repository references**
   - `README.md`
   - `docs/collaboration/template-benefits.md`
   - `docs/collaboration/process-gap-register.md`
2. **Documentation and Architecture Management**
   - Write the Docs. *Docs as Code*. https://www.writethedocs.org/guide/docs-as-code/ (Retrieved 2026-07-16)
   - Nygard, M. "Documenting Architecture Decisions." 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (Retrieved 2026-07-16)
3. **AI Collaboration and Philosophy of Automation**
   - Anthropic. *Building effective agents*. https://www.anthropic.com/research/building-effective-agents (Retrieved 2026-07-16)
   - Bainbridge, L. "Ironies of Automation." *Automatica*, 1983. https://www.sciencedirect.com/science/article/abs/pii/0005109883900468 (Retrieved 2026-07-16)
