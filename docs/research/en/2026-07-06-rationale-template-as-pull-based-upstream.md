# Pull-Based Upstream: Sovereignty and Self-Determination in Distributed Systems

2026-07-06. Non-normative. Related: ADR 0008, LISS-0001.

> Japanese original (authoritative): [../2026-07-06-rationale-template-as-pull-based-upstream.md](../2026-07-06-rationale-template-as-pull-based-upstream.md), terminology as of commit `d1b86c8`. Agent-read policy and terms: [../README.md](../README.md) (「エージェントと research」「用語」; accepted vs adopted) and [README.md](./README.md) (Glossary). If English lags Japanese, prefer Japanese.

---

Even an excellent template starts aging the moment it is cloned into a project. Obsolescence is not a design bug; time guarantees it. The real failure mode is not "code and rules get old." It is upstream (template maintainers) ignoring downstream local context and forcing rewrites—push-based updating.

I therefore use pull from downstream, not push from upstream. Each adoption adapter (people running an adopting project; see [../README.md](../README.md)) chooses whether and when to sync. Upstream holds no global registry of adopters and no credentials to write into them (ADR 0008).

Distributing and updating a template is far more troublesome than distributing standard software libraries (like NPM or PyPI packages). With a library, updates cross clear interface (API) boundaries and enter as a black box. A template, however, is copied directly into the file system of the adopting repository, where it is edited by human engineers and grows by taking on the "meaning" of the project's specific domain and architecture. Even if the files were exactly identical immediately after adoption, a few weeks later they will be deeply intertwined with the downstream's unique design decisions. Therefore, the true challenge of template updating is not "how to distribute the latest files," but "how to safely merge the universal improvements provided by the upstream with the project-specific sovereignty won by the downstream."

## Protecting Sovereignty by Default: The Philosophy of 3-Way Merge

To address this complex challenge, this template employs a 3-way merge. Portions changed only by the upstream template are straightforwardly updated; portions uniquely changed by the adopting project (downstream) are absolutely preserved; if both changed the same portion differently, it is treated as a conflict requiring human resolution; and if the downstream intentionally deleted a portion, the upstream will not silently resurrect it during an update (ADR 0008 Decision 3). A naive, simple overwrite would instantly destroy the customizations meticulously built by the downstream. This risk of destruction is documented as a heavy cost by the Adjudicator in the ADR.

In particular, the behavior of "respecting deletions" is architecturally critical. From the template provider's perspective, a deleted file might simply look like a "missing file" or an "error." However, from the adopting project's perspective, that deletion is highly likely an explicit and advanced Architectural Decision meaning: "Our project does not need this rule." If the upstream automatically resurrects it, the template becomes a mechanism that unilaterally overwrites the downstream's local design decisions. A 3-way merge is not merely Git's technical merge algorithm; it is a clear philosophical declaration to "respect the sovereignty and self-determination of each project."

[cruft](https://github.com/cruft/cruft) and [Copier](https://copier.readthedocs.io/en/stable/updating/) are great toolsets that have spent years tackling this exact thorny problem of "boilerplate drift" (the divergence between a template and an actual project). While deeply resonating with their philosophy, this template chose to implement an isomorphic structure using pure `git merge-file` to avoid forcing additional tool dependencies (like Python packages) onto the project.

## Synchronization is Also a Normal Change: Docs-as-Code End to End

Updating a template via an update script must never commit directly to the project's trunk (main branch). It must always create a dedicated branch, issue a Pull Request (PR), and pass standard CI (ADR 0008 Decision 4, ADR 0007). There is absolutely no special treatment along the lines of "It's safe unconditionally because it comes from the official upstream template." This is the template version of the robust pattern popularized in the industry by [Renovate](https://docs.renovatebot.com/) and Dependabot: "External updates are automatically proposed as PRs, and are only integrated after passing human review and all CI tests."

It is important to note here that "A clean merge is not the same guarantee as 'nothing needs review'" (ADR 0008 Consequences). Syntactical success (merging mechanically without conflict) and semantic correctness (whether the change is right in the context of the project) are entirely different dimensions.

A PR is not a mere bureaucratic rubber stamp; it is the venue for "Semantic Review." A template update might look like a trivial Markdown phrasing diff, but it could severely impact agent behavior, phase approval gates, privacy budgets, or branching disciplines. CI can mechanically detect leftover Git conflict markers or broken Markdown formatting. But only a human Adjudicator, who understands the local context, can judge whether the change "contradicts our adopter culture or the existing ADRs we have built up."

## Improvements Flow Back from Downstream: Ecosystem Circulation

The gritty, real-world operational feedback from adoption adapters (採用アダプター; see [../README.md](../README.md)) flows back upstream as Issues like LISS-0002 and LISS-0005. [GitLab Flow's upstream first](https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/) preaches the grand principle of integrating bug fixes and shared improvements into the upstream (main) first. This template's operation of "abstracting field feedback into LISS and redistributing it globally from there" is isomorphic to this Upstream-First architecture.

## The Lineage of Delegation and Self-Determination: The Limits of Central Control

This design of "upstream does not coerce; downstream pulls with sovereignty" is not merely a technical argument about Git operations. It is deeply connected to the historical lineage of "decentralization" that has profoundly influenced software engineering. Specifically, the following two historical breakthroughs serve as the ideological foundation (evidence) for this template.

The first foundation is the "shift from Push to Pull" in manufacturing. The centralized, mass "Push" management style, once mainstream like the Ford production system, generated massive waste because it could not adapt to changing conditions on the front lines. In response, Taiichi Ohno established Toyota's "Kanban" system, shifting to a mechanism where the downstream (subsequent process) pulls exactly what it needs, exactly when it needs it, rather than having schedules pushed by the upstream. This ideology of abandoning central control to maximize frontline adaptability later became the foundation of Lean Software Development and heavily influenced the software industry (Poppendieck & Poppendieck, 2003).

The second foundation is the concept of "Empowered Execution" in modern organizations. As detailed in General Stanley McChrystal's book *Team of Teams*, the modern U.S. military found that traditional siloed hierarchies (Command and Control from headquarters) could no longer cope with fast-changing, decentralized network adversaries. The solution was for headquarters to provide "Shared Consciousness" while completely delegating execution decision-making to frontline teams. Rather than waiting for instructions from the center, frontline teams knowing the local context make autonomous decisions. This networked structure is fundamentally isomorphic to the autonomous Scrum teams targeted by modern Agile development.

The fact that this template only publishes "architectural guidelines (Shared Consciousness)" and completely delegates the "Sovereignty" of when and how to adopt them to the adopting projects (frontline teams) is not merely taking the easy way out. It is a deliberate architectural decision aligned with the lessons repeatedly shown by practices in different domains like manufacturing and organizational theory: "In highly volatile environments, empowering the front lines and using Pull-based information retrieval scales far better than central control." Of course, these belong to evidence of memoirs and practice reports, not controlled empirical research. That is why this template adopts this lesson not as an unconditional truth, but as a decision within its own project context via ADR 0008 ([Evidence and Rules](./2026-07-06-rationale-evidence-based-process-design.md)).

## Upstream Does Not Know Downstream: Decentralized Discipline

This Pull-based design achieves both scalability and security (trust) simultaneously. Because the upstream does not manage the downstream, the upstream's operational costs never increase, regardless of whether there are 10 adopting projects or 100,000. Furthermore, because there is no need to centralize the GitHub tokens or credentials of each company upstream, it does not become a massive single point of failure for supply chain attacks.

In exchange for these immense benefits, the upstream accepts the fact that "projects that neglect synchronization (Pull) will be left outdated forever" (ADR 0008 Negative). This is not negligence; it is a consistently intentional choice prioritizing project sovereignty over coercion. It is a graceful surrender of centralized control and quality assurance. The upstream never guarantees that all adopters are always up to date. Adopters proactively pull on their own business timing and integrate them under their own responsibility through reviews. What the template offers the world is not Control, but sustainable Updatability.

The decision to exclude the `research` folder from synchronization ([Normative vs. Reading Documents](./2026-07-06-rationale-normative-vs-reading-documents.md)) is also a consistent manifestation of this sovereignty policy. What should be distributed downstream are only the "norms" that bind the project; the upstream maintainer's philosophy and essays—the "reading materials"—remain local to the upstream. No matter how rich the reading materials become, the operational template (the rules themselves) distributed to the world remains unchanged. If the norms themselves need changing, the ADR must be separately rewritten and placed onto the network of the Pull-based update path.

## References

1. **Repository references**
   - ADR 0007, ADR 0008
   - LISS-0001, LISS-0002
2. **Organizational Theory, Decentralization, and Agile**
   - Ohno, T. *Toyota Production System: Beyond Large-Scale Production*. Diamond, 1978. (Shift from Push to Pull and the supermarket system)
   - Poppendieck, M., & Poppendieck, T. *Lean Software Development: An Agile Toolkit*. Addison-Wesley, 2003. (Application of Kanban to software engineering)
   - McChrystal, S. et al. *Team of Teams: New Rules of Engagement for a Complex World*. Portfolio, 2015. (Shift from silos to networks and Empowered Execution)
3. **Template and Boilerplate Management**
   - cruft. https://github.com/cruft/cruft (Retrieved 2026-07-07)
   - Copier. *Updating a project*. https://copier.readthedocs.io/en/stable/updating/ (Retrieved 2026-07-07)
4. **Dependencies and Flow Updates**
   - Renovate. https://docs.renovatebot.com/ (Retrieved 2026-07-07)
   - GitLab. *GitLab Flow best practices*. https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/ (Retrieved 2026-07-07)
