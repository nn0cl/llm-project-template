# The Agent is a Sandbox: An Architecture of Freedom and Control

2026-07-07. Non-normative.
Related: [Target End State](./2026-07-05-rationale-target-end-state.md), [The Adjudicator and Phases](./2026-07-05-rationale-adjudicator-centered-collaboration.md), [Repository-Native Planning](./2026-07-05-rationale-repository-native-planning-and-change-control.md), [Design First and Context](./2026-07-05-rationale-design-first-minimal-context.md).

> Japanese original (authoritative): [../2026-07-07-rationale-saas-agent-as-sandbox.md](../2026-07-07-rationale-saas-agent-as-sandbox.md) at commit `6910bf0` (`6910bf0ecd025b7561b1446568f0459c00283b3d`). Terminology and critical-review fixes (adopter, analogies, less repetition): [../README.md](../README.md) and [README.md](./README.md). If English lags, prefer Japanese.

---

I am trying to build a way for AI and humans to advance software development by truly **collaborating**. This is not a dystopia where engineers lose creative work and AI automates everything. Humans own advanced design decisions and accountable approvals (governance); agents explore a large design space and generate large amounts of code (execution). Documentation, persisted artifacts, and phase reviews connect that boundary—the shape of engineering collaboration in this era.

Modern coding agents already move with surprising freedom: they read project files widely, run shell commands, refactor across many files, and retry when tests fail. Each SaaS product grants that freedom inside an OS-level "isolated" and "ephemeral" execution space—a sandbox (GitHub Copilot: [cloud and local sandboxes](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes), Cursor: [agent sandboxing](https://cursor.com/blog/agent-sandboxing)). Physical freedom and safety—blocking malicious execution and host destruction—come from that vendor boundary.

Freedom of local operation is not yet an enterprise "project." Integrating generated snippets into a coherent system is not a product vendors ship as a package; **it is an architecture the team writes into their own repository.** This template is a concrete blueprint for that integration and collaboration layer.

A vendor sandbox covers part of OS-level physical safety; it does not cover "semantic safety" as software. Isolating the filesystem does not isolate a diff with a serious bug born from a misunderstood spec. Restricting the network does not stop Clean Architecture violations where domain rules leak into UI components or DB Adapters (Clean Architecture; not adopters). Execution safety and the project's acceptable semantic boundary are different things. Confusing them is a dangerous shortcut: "It ran in a sandbox, so the output is safe."

## The Trio of Collaboration: Explicit Division of Responsibility

`docs/collaboration/ai-human-scheme.md` splits roles three ways: **Adjudicator** (owns decision points), **Agent** (generation and visibility inside a phase), **Deterministic Tool** (formatters, linters, tests—verify without relying on model probability, as deterministically as practical). Success is not single-model IQ.

The point is not to blur blame but to ask, when main breaks, which role’s gate was poorly designed—not “the model hallucinated, so nothing to do.”

### The Trio Expands into a Team: Hierarchy and Escalation

The "Trio of Collaboration" is not a fixed scheme assuming a single agent. As multi-agent research—such as AutoGen (Wu et al., [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)), which coordinates multiple LLM agents through conversation—shows, the "Agent" seat can be occupied by multiple LLMs. Furthermore, delegating a capability hierarchy—an executive role overseeing the entire implementation, a lightweight role rapidly handling scoped mechanical tasks, and a strong reasoning role called only at highly uncertain decision points—is not a speculative idea, but a pattern with measured prior research. LLM Cascade research (Yue et al., [arXiv:2310.03094](https://arxiv.org/abs/2310.03094)) demonstrated that a configuration where a weak model answers first, and then delegates to a strong model using answer consistency as an uncertainty signal, can drastically reduce inference costs while maintaining accuracy. Learning-based routing (RouteLLM: Ong et al., [arXiv:2406.18665](https://arxiv.org/abs/2406.18665)) formulated the very act of assigning strong or weak models based on query difficulty as a learnable problem. Additionally, Anthropic reported that operating an orchestrator-worker configuration with a strong model as the lead agent and lighter models as parallel sub-agents significantly outperformed a single strong model in internal evaluations ([How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system). However, this is a vendor's self-report based on internal evaluation, not externally verified numbers). These confirm that the "capability ladder" described in [Design First and Context](./2026-07-05-rationale-design-first-minimal-context.md) can be applied even within the agent itself.

However, one must not conclude from this stratification that "the boundary between human and AI disappears." An agent team is free to self-organize within the sandbox, but at the point where their output changes the meaning of the project, they must pass through the exact same approval gates regardless of the team's composition. Why escalation to a strong model and an approval request to an Adjudicator—though they look similar—are semantically distinct is detailed in [The Adjudicator and Phases](./2026-07-05-rationale-adjudicator-centered-collaboration.md). What the division of the three roles protects is this asymmetry of responsibility.

## The Controls Placed by This Repository—Not Forced Execution, but Norms of Collaboration

Let's clear up a common misunderstanding here. The `CLAUDE.md` and `AGENTS.md` provided by this template are not mechanisms that programmatically force-block (intercept) an agent from running `rm -rf`. Nor do they rewrite the OS permissions model of the vendor-provided sandbox. They are the **Constitution** shared by the agent and humans. They are an oath to the system that declares throughout the session what may be done, when to stop, and what must not be guessed.

Controls are connected in the following layered manner:

### The First Gate—The Operating Path Allowlist

`docs/architecture/agent-quickstart.md` forces the selection of one of three paths—Fast / Feature / Architecture—depending on the nature of the request. Each path **strictly enumerates (allowlist) the documents the agent should read as daily task input**. Documents not listed there are treated as outside normal task input for that work. This is an implementation designed to exclude philosophical reading materials like `research` from normal task input (agents need not read them daily; see [../README.md](../README.md)), thereby securing the Context Budget and privacy ([Normative vs. Reading Documents](./2026-07-06-rationale-normative-vs-reading-documents.md)).

`scripts/init-llm-context.sh` bakes this "order and scope to read" into the initial system prompt at the start of a session. It instructs: "If neither acceptance specifications nor phase definitions exist yet, do not immediately jump into code implementation; present a design intake and halt." Collaboration never starts with "suddenly generating a massive amount of code."

This allowlist controls the "cognitive file system" of the agent entering the sandbox. Just as an OS sandbox restricts the physical paths an agent can read, the Operating Path restricts the semantic paths an agent should consider. Of course, this is not a perfect physical constraint. However, by radically narrowing the initial conditions of the agent's reasoning, it makes it easier for humans later to trace during review: "On exactly which context of which specification document did the AI base this code?"

### The Constitution—Synchronized Operational Contracts

`AGENTS.md` (the tool-agnostic core constitution), `CLAUDE.md` (instructions for Claude), and `.github/copilot-instructions.md` (instructions for Copilot) are **operational contracts** that synchronize the same phase disciplines and dependency boundaries across different AI agents. CLI tools like Claude Code are designed to pull in `CLAUDE.md` from the repository root as the global context for a session ([Use Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)). This is precisely why the constitution is proudly placed at the center of the repository, not hidden in a user's local PC folder. The vendor's sandbox is merely a subordinate execution environment that clones and reads it upon startup.

And the alteration of this constitution (contract) itself is subject to strict control. `prompt-instruction-change-control.md` requires deep review and Trace (verification records of changes) by the Adjudicator for any prompt changes, and the CI mechanically rejects "Pull Requests for contract changes without Trace records." The act of changing the rules of collaboration is itself subordinated to the rules of collaboration.

### Guidance—Design Intake and the Prime Directive

There are three Prime Directives enshrined at the top of `AGENTS.md`:
1. No implementation without a human-reviewed acceptance specification.
2. No phase skipping (Phase 1~3).
3. No hidden business logic in Adapters (external connection layers).

Every request must begin with a Design Intake. In the Feature / Architecture Paths, the agent uses a `[THOUGHT]` block to lock down the target behavior, context include/omit, Ports/Adapters boundaries, "Must not guess" unresolved items, and the routing of models and tools *before* writing code. This is not a mere rite-of-passage briefing before work; it is **powerful Guidance that continues to bind the agent's reasoning throughout the entire work process**.

### Live Control—The Adjudicator's Approval Loop

Static normative documents alone do not complete dynamic collaboration. A human intervenes in the loop during execution. The Adjudicator not only "owns" the decision points but actively exercises control by physically **stopping and gating** the agent at the junctures of each phase. Phase 2 (production implementation) is permitted to start only after Phase 1 (test code) has been human-reviewed. Phase transitions require an explicit request trigger from the Adjudicator, not the agent's self-judgment.

This is the core of the integration architecture provided by this template. The unconstrained generative capacity inside the sandbox is transformed into valuable project progress only when it passes through the deliberate approval points of the Adjudicator.

### The Exit—PRs, Human Review, and Thin CI

The changes output from the sandbox eventually land in a Pull Request (PR) and undergo human review. Here, CI is strictly an "auxiliary checkpoint." The CI in this template merely verifies the "skeleton of metadata"—whether contract files correctly exist, whether ADR numbers are assigned, or whether Trace logs exist during contract changes. It is not a magical layer that fully judges on every commit whether phases were truly obeyed or whether the code aligns with the design intent. The ultimate responsibility for integration lies firmly with the Adjudicator and human reviewers. The instruction to the agent to "Report Red, Green, Refactor, or Fast Path status honestly" is the final bastion where the system demands honest status reporting from the agent.

## Do Not Confuse the Two Worlds

To organize the argument, let us clearly separate the following two:

1. **The Vendor's Sandbox**—The freedom of execution granted to the agent and the OS-level safety boundary (protection from file destruction, shell runaways, and network leaks). This is encapsulated and provided by the SaaS products of each vendor.
2. **The Team's Collaborative Norms**—`CLAUDE.md` / `AGENTS.md`, Operating Paths, the approval loop by the Adjudicator, persistent artifacts, and the PR flow. These are defined and provided by the team themselves as the repository's architecture.

When I say, "The inside (the sandbox) should be extremely free, while the outside (integration into the system) should be extremely explicit and strict," the protagonists governing the outside are not mechanical CI tools, but **written normative documents, human approval loops, and persisted design artifacts**. Precisely because vendors provide powerful sandboxes, we can comfortably entrust internal code generation to AI. Simultaneously, precisely because we define robust collaborative norms in the repository, we can maintain the semantic consistency of the project on the outside. If either is missing, enterprise development using AI collapses.

## What This Template Is and Is Not

This repository is not a web application or SaaS product that runs out of the box. It is "Scaffolding" for processes and collaboration in the AI era. The `CLAUDE.md` and `AGENTS.md` found here exist not only for this template repository; they are blueprints designed to **be copied to the adopting project (your project) and function as a living constitution there for the first time**.

What this template aims to do is extremely clear: **Safely connect agents that move freely at overwhelming speeds into an engineering workflow where humans can hold responsibility.** We neither omit human control mechanisms out of overconfidence in the agent's intelligence, nor do we crush all its generative freedom out of fear of it going rogue. We create a sustainable, integrated development environment through the collaborative loop of the three roles (Adjudicator / Agent / Tool), the explicit norms written in the repository, and the precise approval gates of the Adjudicator.

The various topics in the `docs/research/` folder—the Adjudicator, design-first, output contracts, reviewable code, and repository planning—are all merely philosophical details resting atop this single, massive skeletal design.

## References

1. **Repository references**
   - `AGENTS.md`, `CLAUDE.md`
   - `docs/architecture/agent-quickstart.md`
   - `docs/collaboration/ai-human-scheme.md`
   - `docs/collaboration/prompt-instruction-change-control.md`
   - `scripts/init-llm-context.sh`
   - ADR 0007
2. **AI Agents and Sandbox Architectures**
   - GitHub Docs. *About cloud and local sandboxes for GitHub Copilot*. https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes (Retrieved 2026-07-07)
   - Cursor. *Implementing a secure sandbox for local agents*. https://cursor.com/blog/agent-sandboxing (Retrieved 2026-07-07)
   - Anthropic. *Use Claude Code on the web*. https://code.claude.com/docs/en/claude-code-on-the-web (Retrieved 2026-07-07)
3. **AI Collaboration and Reasoning Limits (and Hierarchical Agents)**
   - Anthropic. *Building effective agents*. https://www.anthropic.com/research/building-effective-agents (Retrieved 2026-07-07)
   - Anthropic. *How we built our multi-agent research system*. https://www.anthropic.com/engineering/built-multi-agent-research-system (Retrieved 2026-07-16. Vendor internal self-report.)
   - Shi, F. et al. "Large Language Models Can Be Easily Distracted by Irrelevant Context." arXiv:2302.00093. https://arxiv.org/abs/2302.00093 (Retrieved 2026-07-07)
   - Wu, Q. et al. "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." arXiv:2308.08155. https://arxiv.org/abs/2308.08155 (Retrieved 2026-07-16)
   - Yue, M. et al. "Large Language Model Cascades with Mixture of Thoughts Representations for Cost-efficient Reasoning." ICLR 2024 / arXiv:2310.03094. https://arxiv.org/abs/2310.03094 (Retrieved 2026-07-16)
   - Ong, I. et al. "RouteLLM: Learning to Route LLMs with Preference Data." arXiv:2406.18665. https://arxiv.org/abs/2406.18665 (Retrieved 2026-07-16)
