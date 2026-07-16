# Pull-Based Upstream: Sovereignty and Self-Determination in Distributed Systems

2026-07-06. Non-normative. Related: ADR 0008, LISS-0001.

> Japanese original (authoritative): [../2026-07-06-rationale-template-as-pull-based-upstream.md](../2026-07-06-rationale-template-as-pull-based-upstream.md) at commit `6910bf0` (`6910bf0ecd025b7561b1446568f0459c00283b3d`). Terminology and critical-review fixes (adopter, analogies, less repetition): [../README.md](../README.md) and [README.md](./README.md). If English lags, prefer Japanese.

---

Even an excellent template starts aging the moment it is cloned into a project. Obsolescence is not a design bug; time guarantees it. The real failure mode is not "code and rules get old." It is upstream (template maintainers) ignoring downstream local context and forcing rewrites—push-based updating.

I therefore use pull from downstream, not push from upstream. Each adopter (people running an adopting project; see [../README.md](../README.md)) chooses whether and when to sync. Upstream holds no global registry of adopters and no credentials to write into them (ADR 0008).

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

The gritty, real-world operational feedback from adopters (採用者; see [../README.md](../README.md)) flows back upstream as Issues like LISS-0002 and LISS-0005. [GitLab Flow's upstream first](https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/) preaches the grand principle of integrating bug fixes and shared improvements into the upstream (main) first. This template's operation of "abstracting field feedback into LISS and redistributing it globally from there" is isomorphic to this Upstream-First architecture.

## Delegation and self-determination: technical reasons first, analogies second

The primary reasons for pull are technical and operational: upstream holds no downstream registry or write credentials; adopters can run semantic review in local context; upstream cost does not grow with adopter count—already stated in ADR 0008. **Manufacturing and military stories are not evidence for that decision; they are analogies so readers can picture decentralization.**

If analogies stay in the essay, keep them brief. Toyota’s kanban popularized pull-as-downstream-draws rather than upstream-pushes (Ohno 1978; bridge to lean in Poppendieck & Poppendieck, 2003). McChrystal et al.’s *Team of Teams* is one organizational account of shared consciousness at the center and execution at the edge (memoir / practice report). Neither is a controlled study. They are **aids to reading ADR 0008**, not laws to copy ([Evidence and Rules](./2026-07-06-rationale-evidence-based-process-design.md)).

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
