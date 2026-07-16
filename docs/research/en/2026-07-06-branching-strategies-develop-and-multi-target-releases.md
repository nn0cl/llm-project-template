# Branching Strategies in AI Collaboration: The Economics of Integration Latency and Multi-Target Environments

2026-07-06 Research. Non-normative. Related: The problem of long-lived branches and integration latency.

> Translated from [../2026-07-06-branching-strategies-develop-and-multi-target-releases.md](../2026-07-06-branching-strategies-develop-and-multi-target-releases.md) as of 2026-07-16. The Japanese original is authoritative.

---

The speed at which AI agents generate code far exceeds human typing. However, if that overwhelming generative power is allowed to diverge into unchecked branches, the project will rapidly accumulate a massive technical debt known as "Integration Latency." In large enterprise products with multiple release targets, how should we safely integrate these high-speed artifacts into the mainstream architecture?

This fundamental question arose from a practical failure during a development session (LISS-0005). During the second adapter development session, the agent innocently created a `develop` branch and postponed merging it into the mainstream. As a result, a stack of unintegrated changes continued to pile up on the feature branch. In response, the Adjudicator (the human designer) asked: "Should the template unconditionally ban the existence of `develop`?"

This document is an investigative and philosophical response to that question. I will state the conclusion first. What modern software engineering research fiercely condemns is not the "existence of long-lived branches" per se, but the malignant debt of "integration latency." And the only way to keep a multi-target environment healthy is not through bifurcating the source tree, but through upstream-first propagation and feature divergence at the architectural design level (Feature Toggles or Ports/Adapters).

## Is `develop` Acceptable? The True Meaning of DORA Metrics

Google's DORA (DevOps Research and Assessment), based on surveys of over 30,000 professionals spanning more than seven years, identified Trunk-Based Development as the most powerful technical predictor of elite performance ([DORA Capabilities](https://dora.dev/capabilities/trunk-based-development/)). However, reading its operational definition carefully reveals that it is not simple dogmatism demanding "absolutely zero long-lived branches."

What they require is "keeping the number of active branches to three or fewer, and merging to the trunk (main/master) at least once a day." The harm manifests as integration latency. If there is a `develop` branch that integrates daily and is pushed to main in short cycles, it is functionally close to a trunk. Conversely, a `develop` branch that accumulates divergence from the mainstream for weeks, nurturing a massive merge conflict timebomb, is the exact anti-pattern DORA measured and warned against.

Vincent Driessen, the creator of GitFlow, noted in a 2020 reflection that for modern web applications where Continuous Delivery is a given, he recommends simpler flows like GitHub Flow. He corrected course to say that GitFlow still fits well only for packaged software requiring explicit versioning and in-the-wild support for multiple versions ([nvie.com](https://nvie.com/posts/a-successful-git-branching-model/)). The legitimate survival zone for `develop` is much narrower and more limited than when it became popular in the early 2010s.

This fact changes the premise of the argument. Reflexively banning `develop` just upon seeing the name is not faithful to the evidence. On the other hand, leaving long-lived branches unchecked using the excuse "we use GitFlow" is a betrayal of the evidence. What DORA measures is the degree of "system-wide dysfunction" caused by delayed integration, delayed feedback, and excessively large batch sizes. Therefore, the question to ask is not about the name, but the dynamics of the flow: "How far does this branch drift from main?" "In how many days does it return?" "Which changes propagate in what order?"

If we view `develop` in the context of Forsgren, Humble, and Kim's seminal work *Accelerate* ([IT Revolution](https://itrevolution.com/product/accelerate/)), a branching model is not a religious sect, but the physical design of a feedback loop (Feedback Economics). The only thing that matters is the time it takes for a change to be integrated and verified.

## How Do Multiple Release Targets Flow? The Discipline of Upstream-First

The approach of "We have multiple release targets, so we'll manually assemble features into branches via cherry-pick" is a common industry misconception that invites disastrous results. In studies of elite organizations, main is the Single Source of Truth, and unfinished features are hidden behind feature flags, not split into separate source code branches.

Releases are carved out as immutable snapshots of main at specific points in time. GitLab's release branches, Microsoft Release Flow's sprint branches, Kubernetes' `release-X.Y`, Chromium's release channels—all follow this snapshot model. Cherry-picking is used exclusively for "backporting" critical bug fixes discovered after the cut. Repeatedly cherry-picking between branches that have diverged functionally to maintain differences is a hotbed for conflicts and regressions, and is treated as a clear anti-pattern.

### Upstream-First as a Verifiable Discipline

The discipline that systematically guarantees "all shared changes propagate early" is upstream-first. GitLab Flow puts fixes into main first, then cherry-picks them down to release—they state explicitly that Google and Red Hat use similar methods ([GitLab Flow best practices](https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/)). The Microsoft Azure DevOps team makes changes on mainline and ports them to release ([Microsoft branching guidance](https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops)). Kubernetes strictly requires contributors to have cherry-picks present in main first, then sequentially apply them from the newest release to the oldest across all applicable active branches ([cherry-pick policy](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-release/cherry-picks.md)).

### Divergence is Solved by Design, Not by VCS

Differences between targets (release destinations) should not be created in a maze of Version Control System (VCS) branches. They should be created at the software architecture level via feature flags, configuration, build setups, or module boundaries (Ports/Adapters) ([Hodgson: Feature Toggles](https://martinfowler.com/articles/feature-toggles.html)). Permanent per-target branches (dedicated branches for each release destination) are the worst kind of technical debt, suffering doubly from DORA's warnings against long-lived branches.

These elite organizations impose strict disciplines such as "1 PR = 1 self-contained logical change; protect unfinished features with flags" precisely to make backporting and reverting safe and mechanical. Fine-grained discipline is a prerequisite for making upstream-first work; it is not a means to assemble releases.

However, feature flags are not magic. As Pete Hodgson details in his essay on martinfowler.com, toggles have distinct types, differing in lifespan and responsibility. A temporary release toggle carries a different design weight than a long-lived permissioning or experiment toggle. When using flags to support multiple targets, you must manage flag ownership, removal conditions, test matrix explosions, and default configuration values. Moving divergence from VCS to configuration files without addressing the underlying design merely shifts complexity to a place where it is harder to see.

## GitFlow's `develop` vs Downstream Release Lines

GitFlow places `develop` upstream of `main`. In contrast, Release Flow and GitLab Flow place `main` as the sole integration trunk, with release and environment branches positioned downstream. To propagate shared changes quickly to all release destinations, a downstream model is structurally easier to guarantee. If a project must retain the name `develop`, there is room to redefine its substance as a downstream staging/environment verification branch off main.

When names diverge from reality, AI agents learn incorrectly from the names. If `develop` is the "true integration destination" and `main` is "a place for occasional releases," then the trunk is effectively develop. If `main` is the sole integration trunk and `develop` is a downstream snapshot for environment verification, then it is no longer the `develop` of GitFlow. What the template strongly demands is not unified naming, but that its reality and operational contract be documented in an ADR.

## Proposal for Operational Contracts in Multi-Target Environments

The default etiquette of this template is Trunk-oriented (main and short-lived branches), and long-lived branches like `develop` are generally not recommended. However, relaxing this "generally not recommended" stance into a pragmatic approach of "tolerating long-lived branches under a clear integration contract (ADR)" is amply supported by the evidence above. Long-lived integration, release, or environment branches can be justified for the specialized requirements of multi-version or multi-target systems, but the adopting project's ADR must explicitly define that operational contract.

When formalizing this into a normative rule, this document proposes the following five points to be addressed in that ADR (adoption and exact wording are up to the Adjudicator and the adopting project):
- The upstream source of truth (declaring that shared changes are upstream-first).
- Quantified integration frequencies (e.g., daily to integration lines, within 1-2 weeks to main. Exceeding this is visualized as a violation).
- Propagation rules (apply to all active targets in new-to-old order, tracked by a single issue).
- Hierarchical design for divergence (flags -> configuration -> port/adapter -> permanent per-target branch as a last resort requiring a separate ADR).
- EOL (End of Life) and locking policies for each release branch.

This proposal does not alter the operational rules of `llm-project-template` solely via this research document. If they are to be made normative, sorting out which points should be elevated to an ADR or collaboration document—that is where the job of this document ends.

## References

1. **Project Internal Regulations**
   - LISS-0005, `docs/collaboration/branch-commit-pr-discipline.md`
2. **DevOps and Elite Performance Research**
   - DORA. *Trunk-based development*. https://dora.dev/capabilities/trunk-based-development/ (Retrieved 2026-07-07)
   - Forsgren, N., Humble, J., Kim, G. *Accelerate*. https://itrevolution.com/product/accelerate/ (Retrieved 2026-07-16)
3. **Origins and Evolution of Branching Strategies**
   - Driessen, V. *A successful Git branching model* (reflection 2020). https://nvie.com/posts/a-successful-git-branching-model/ (Retrieved 2026-07-07)
   - GitLab. *GitLab Flow best practices*. https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/ (Retrieved 2026-07-07)
   - Microsoft. *Git branching guidance*. https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops (Retrieved 2026-07-07)
4. **Practices in Multi-Target and Feature Divergence**
   - Kubernetes SIG Release. *Cherry-pick policy*. https://github.com/kubernetes/community/blob/main/contributors/devel/sig-release/cherry-picks.md (Retrieved 2026-07-07)
   - Hodgson, P. "Feature Toggles (aka Feature Flags)." martinfowler.com. https://martinfowler.com/articles/feature-toggles.html (Retrieved 2026-07-07)
   - Runway. "Cherry-picks vs backmerges." https://www.runway.team/blog/cherry-picks-vs-backmerges-whats-the-right-way-to-get-fixes-into-your-release-branch (Retrieved 2026-07-07)
   - Squires, J. "Comparing release branch strategies." 2022. https://www.jessesquires.com/blog/2022/03/27/comparing-release-branch-strategies/ (Retrieved 2026-07-07)
   - Chromium. "How to merge a change to a release branch." https://www.chromium.org/developers/how-tos/drover/ (Retrieved 2026-07-16. Page indicates migration to current procedures (deprecated). Cited as circumstantial evidence of an operational model for merging to release branches.)
