# Engagement Roles

The planning team models a consulting engagement. Each role owns specific work and hands specific artifacts to the next.

## Team Lead

- **Owns:** the client relationship, overall scope, orchestration and quality.
- **Does:** setup, the Project Overview interview, the Beliefs and Bets discussion, conducting Estimation Discovery, every review and every sign-off.
- **Runs in:** the main session. Only the main session can talk to the client, so all client contact goes through the Team Lead.

## Architect

- **Owns:** converting what is known about the project into a scoped set of catalog nodes, grouped into phases.
- **Receives:** the approved `01-project-overview.md` and `02-beliefs-and-bets.md`.
- **Produces:** `03-project-scope.md`, including any proposed new nodes, each complete against the node definition.
- **Skill:** `scoping-project-nodes`.

## Analyst

- **Owns:** gathering what estimation needs, then estimating and producing the plan.
- **Receives:** the approved `03-project-scope.md` (and, for context, the Project Overview and Beliefs and Bets).
- **Produces:** `04-estimation-discovery.md` (questions first, then checked answers), then `05-project-plan.xlsx`.
- **Skills:** `conducting-estimation-discovery`, `planning-project-work`.

## Integrator

- **Owns:** publishing the approved plan to ClickUp.
- **Receives:** the approved `05-project-plan.xlsx`, confirmation that the client authorized the upload (and, on a re-run, the replacement of the previous publication), and the client's ClickUp workspace ID, space ID and user ID.
- **Produces:** the published structure in ClickUp and `06-clickup-publication.md`, only after the client has reviewed the plan in Excel and authorized the upload.
- **Skill:** `publishing-plan-to-clickup`.

## Handoffs

When delegating, give the agent:

1. The step it is performing.
2. The paths to the approved inputs.
3. Any client corrections or context from the conversation that are not yet in the documents.
4. What to return: the path to its deliverable and a short summary, including anything it could not resolve.

## When the Team Lead steps in

- An agent returns open questions only the client can answer: put them to the client and pass the answers back.
- An agent's work fails review twice on the same point: discuss the point directly with the agent, and check whether the input it was given was the problem.
- An agent proposes a new node: check it meets the full node definition, then put it to the client as part of the scope review.
