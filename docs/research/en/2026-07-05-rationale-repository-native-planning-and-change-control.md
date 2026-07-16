# Keeping Plans in the Repository: Docs-as-Code Taken Seriously

2026-07-05. Non-normative. Related: ADR 0005, ADR 0006.

> Japanese original (authoritative): [../2026-07-05-rationale-repository-native-planning-and-change-control.md](../2026-07-05-rationale-repository-native-planning-and-change-control.md), terminology as of commit `d1b86c8`. Agent-read policy and terms: [../README.md](../README.md) (「エージェントと research」「用語」; accepted vs adopted) and [README.md](./README.md) (Glossary). If English lags Japanese, prefer Japanese.

---

A chat window is not a project artifact. Decisions, plans, and payload context left only in chat history bury themselves in logs and fall off the context window. An agent may move freely inside a sandbox; the wiring that integrates its work—plans, history, approval flows—must live outside the sandbox: repository, CI, and human process ([The Agent is a Sandbox](./2026-07-07-rationale-saas-agent-as-sandbox.md)).

Plans, instructions, and work histories belong in plain text in the repository, under the same review, CI, and version control as source. Anything that changes system behavior changes with a reason, a review trace, and a diff.

This idea of "keeping decisions alongside code" was not newly invented for the AI era. Software development has long suffered from the problem of "implicit decisions evaporating and disappearing." Crucial architectural decisions are made in verbal meetings or buried deep in issue tracker comments, and months later only the "conclusion" remains while the "reason why" is lost. AI agents dramatically accelerate this information evaporation problem. Sessions are short, generation is fast, and the diffs that ripple outward from the conversation are massive. Therefore, placing plans in the repository is not a special workaround for AI; it is a stricter, unavoidable answer to the recording problem software engineering has always faced.

## Plans are Files: The Local-First Principle

In this project, local issues (LISS) and work plans are placed in `docs/issues/` and `docs/work-plans/` in Markdown format. Planning is self-contained within the local environment, entirely independent of external network access like GitHub (ADR 0005). This is not simply to enable offline work. It is absolutely necessary to have repository-local artifacts that the agent can read autonomously during design intake. We assume the "agent" as a first-class citizen and primary reader of these plans.

A plan is not merely a ToDo list. It is a dependency graph expressed through metadata like `depends_on`, `blocks`, and `parent`. Work must not begin on an issue with unresolved `depends_on` dependencies. By explicitly writing these dependencies in files, not only humans but also agents can accurately reconstruct "what to do next." This is the technical foundation for session resumption after a break.

For lightweight tasks such as editing reading materials, the Adjudicator may explicitly omit creating an issue (granting a waiver). Even then, this waiver should not be handled casually by verbal agreement but explicitly recorded in the work trace. Not creating an issue is an architectural decision to streamline a process; it is not a decision to erase the history of the work.

## ADRs are not Records, they are "Laws"

The idea of placing architecture decisions in repository history traces back to Michael Nygard's proposal for ADRs (Architecture Decision Records) ([Cognitect](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). For teams composed only of humans, ADRs might have functioned simply as "memos summarizing decisions and their context." However, in an environment where AI agents operate autonomously, **ADRs must be redefined not as mere records, but as "Legislation" in the system space.**

In *Code and Other Laws of Cyberspace*, Lawrence Lessig argued that code—as an architecture—regulates human behavior much like law (the famous "Code is Law"). AI collaboration introduces a reversal of this relationship: **the rules (Law) written in the repository dictate the generated code (Code).** For an AI, which loses context with every new session and uses provided documents as initial conditions for inference, the rules in the repository serve as the supreme governing law. However, this is not physical enforcement ([The Agent is a Sandbox](./2026-07-07-rationale-saas-agent-as-sandbox.md)). If ADRs are treated merely as "past memos," AI will gravitate toward its learned general best practices and casually violate them. Therefore, the normative documents must clearly declare that "ADRs are laws, and generating code contrary to them is strictly forbidden," and the execution of this law must be backed by the Adjudicator's review and CI.

This template extends the philosophy of ADRs into a comprehensive legal system governing the entire project:
- **ADRs** are the basic laws that must be obeyed.
- **Instructions (Contract files / AGENTS.md)** are the "enforcement regulations" for executing the laws on the ground.
- **Plans (Issues) and Histories (Traces)** are the "administrative procedures and records" for operating and revising the laws.

In AI collaboration, the very acts of "which files the agent is instructed to read" and "at which phase work is stopped" have a decisive impact on the implementation. To change the AI's behavior, one must alter the enforcement regulations (contract files), which requires going through the proper procedures (Issues/Traces). Running this strict legal system—which classical ADRs alone cannot cover—is the reality of sustainable project management in the AI era.

## Prompts are Code, Not Configuration

Files such as `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md` define the operational contracts of the agents. If left unmanaged, they will silently drift in their own directions (ADR 0006). Modifying these files requires a clear reason, review by the Adjudicator, consistency checks across files, and a recorded trace. CI will mechanically reject any unbacked changes.

This is the ultimate extension of the Docs-as-Code philosophy ([Write the Docs](https://www.writethedocs.org/guide/docs-as-code/)). However, the object of management is not just a manual for humans. It is the program that directly controls the agent's behavior. Prompts and agent instructions are akin to the system's runtime environment variables, or the source code of the rules themselves. Changing a single word alters the quality of hundreds of lines of output. If it is that powerful, it must be reviewable at the exact same standard as source code.

Saying "prompts are code" here does not mean making prompts as complex as programming languages. Rather the opposite. If we treat prompts like code, we must harbor the same disdain for DRY-violating duplication, dead code (unused instructions), implicit dependencies, and untestable vague changes as we do in code reviews. A change to a contract file must declare which agent surface (UI/CLI) it targets, which trace backs it up, and which ADR justifies it.

## Local-First Planning and the Role of External Tools

The concept of Local-First Software advocated by Ink & Switch ([Ink & Switch](https://www.inkandswitch.com/essay/local-first/)) emphasizes the importance of placing data ownership and system availability in the local environment. While GitHub and Jira are extremely useful tools, the primary ledger (Source of Truth) for project planning is plain text within the repository—this two-tiered structure can be read as a Local-First architecture for agile planning.

Of course, Local-First does not deny remote collaboration (like GitHub Issues). GitHub Issues and Pull Requests excel at asynchronous notification, team review, and public visibility. Meanwhile, the ability for an agent to begin design intake directly from the local filesystem without network dependencies, the fact that project history remains intact even after forks or template adoption, and the capability to completely restore the relationship between branches and issues simply by running `git checkout` carry absolute value that no SaaS can replace. Local issues are not a degraded copy of GitHub Issues. They are repository-native planning artifacts optimized for collaboration with AI.

## Observation Updates Norms: The Feedback Loop

The risks listed as Negatives in ADR 0005 (drift between local files and GitHub metadata, over-reliance on human discipline for status updates) became a reality during adoption-adapter-side reviews in the second stage of development, manifesting as "parent issue staleness." This practical observation flowed back into a new issue, LISS-0005, triggering process improvements.

The operational rule derived from this lesson—**"Always update the status when an ISSUE is completed (mark it done or change state to Done)"**—is not merely the addition of trivial administrative paperwork. It is a "lifeline" rule designed to prevent the file-based dependency graph (`blocks` / `depends_on`) from collapsing, keeping the inference foundation sound for when the agent next resumes the session. Norms must not end as desk theories. The feedback loop discussed in [Evidence and Rules](./2026-07-06-rationale-evidence-based-process-design.md) is functioning exactly here.

What is decisively important here is not to directly mix field observations and ad-hoc judgments into "normative files." Failures are recorded as "history" in research or traces. If rules need changing, they are "declared" via ADRs or collaboration docs. If plans are to be updated, local issues are "revised." It is precisely because roles are strictly segregated by file type that future human readers can instantly distinguish: "Is this a background fact, an enacted rule, or just a future work plan?"

## Does Recording Slow Things Down?

The objection that "writing things down in text files slows development" is intuitively fair. Recording has a cognitive cost. Not recording costs more later: reconstructing context on resume, agents repeating mistakes, reviewing large diffs with unclear intent, drift in agent instructions and issue status. The faster AI generates code, the more this "debt of not recording" corrodes the project—quietly, but surely.

Therefore, our goal is not "record everything conceivable," but "reliably record the minimum required for human review and session resumption." A compact design note is sufficient for the Fast Path. Large tasks require detailed issues and traces. Changing project norms demands an ADR. The meticulous division of document types exists not to increase the total volume of recording, but as an economically rational choice to place necessary records only when and where they are needed.

## References

1. **Repository references**
   - ADR 0005, ADR 0006
   - `docs/collaboration/local-issue-planning.md`
   - `docs/collaboration/prompt-instruction-change-control.md`
   - `docs/collaboration/ai-work-trace-log.md`
2. **Architecture Documentation and Cyberlaw**
   - Nygard, M. "Documenting Architecture Decisions." 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (Retrieved 2026-07-16)
   - MADR. *Markdown Architectural Decision Records*. https://adr.github.io/madr/ (Retrieved 2026-07-16)
   - Lessig, L. *Code and Other Laws of Cyberspace*. Basic Books, 1999.
   - Write the Docs. *Docs as Code*. https://www.writethedocs.org/guide/docs-as-code/ (Retrieved 2026-07-16)
3. **Local-First Philosophy**
   - Kleppmann, M. et al. "Local-first software." Ink & Switch, 2019. https://www.inkandswitch.com/essay/local-first/ (Retrieved 2026-07-16. Old `/local-first/` URL is broken.)
