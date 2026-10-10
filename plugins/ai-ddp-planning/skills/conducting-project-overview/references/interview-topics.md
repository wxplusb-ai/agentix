# Interview Topics

Thirteen topics for the Project Overview interview. The first eight frame the project. The last five settle which catalog categories and nodes apply; without them, whole categories stay undecided and scoping would rest on guesses.

Each topic lists what to learn, some opening questions, and the catalog nodes its answers decide. The questions are starting points. Ask what you need to settle the "Decides" column, in the client's language.

Not every project needs every topic. Once you know the project's nature, rule out what clearly does not apply rather than asking about it. A personal project on the client's own machine skips most of topics 9, 12 and 13: no sign-in, no hosting cluster, no billing, no analytics. Tell the client what you ruled out so they can correct you.

## Contents

- Framing topics: 1 Goals, 2 Product and market, 3 Technology, 4 Current state, 5 Timelines, 6 Budget and capacity, 7 Assumptions and risks, 8 Perceived next steps
- Scoping topics: 9 Users, roles and access, 10 Workflow and autonomy, 11 Data and knowledge, 12 Integrations and operating environment, 13 Quality bar, safety, compliance and commercial model
- When you have enough

## Framing topics

### 1. Goals

- **Learn:** the problem, for whom, what success looks like at maturity, and how it will be measured.
- **Ask:** What problem does this solve, and for whom? If it works, what changes for them? How will you know it has worked?
- **Decides:** 1.1 Product Requirements Document; whether success metrics exist or must be defined.

### 2. Product and market

- **Learn:** target users and buyers, what they use today, competitors, and how much evidence exists that the problem is real and worth paying for.
- **Ask:** Who has this problem today, and how do they handle it now? Who else is solving it? Have you talked to people who have the problem?
- **Decides:** 1.4 Customer Problem Validation, 1.5 Alternatives Landscape Analysis, 1.6 Solution Concept Validation, 1.7 Business Viability Assessment. Little evidence makes these early, high-priority nodes.

### 3. Technology

- **Learn:** preferred models and providers, existing stack and platforms, constraints on technology choice, and whether the task has been tried with a model yet.
- **Ask:** Have you tried this task with a model? With which, and how did it do? What stack and platforms must this fit? Any providers you must use or avoid?
- **Decides:** 1.2 Non-Agentic Baseline Specification, 1.3 AI Feasibility Spike, 8.3 Model Selection Decision Matrix, 8.1 Unified LLM Gateway Proxy (if several providers).

### 4. Current state

- **Learn:** what exists: research, designs, prototypes, code, data, evaluations. For an in-flight project: what is complete, in progress and planned, and what the completed work proved.
- **Ask:** What has been done so far? What exists that we can build on? What did you learn from it?
- **Decides:** which nodes are already complete and must not be planned again, and which inputs already exist.

### 5. Timelines

- **Learn:** hard dates, milestones the client is committed to, and why.
- **Ask:** Are there dates you must hit? What drives them?
- **Decides:** phase ordering and how far the first phases must reach; not node selection directly.

### 6. Budget and capacity

- **Learn:** the funding envelope, who will do the work, and how many hours per week they have.
- **Ask:** Who will build this, and how much of their time is available? Is there a budget ceiling?
- **Decides:** how ambitious the first phases can be; capacity is needed later for dates. Treat budget as a constraint, not a target.

### 7. Assumptions and risks

- **Learn:** what the client believes must be true, what worries them, and what would make them stop.
- **Ask:** What has to be true for this to work? What keeps you up at night about it? What would make you abandon it?
- **Decides:** the raw material for Step 2. Record these in the client's words.

### 8. Perceived next steps

- **Learn:** what the client thinks should happen next and why.
- **Ask:** If you started tomorrow, what would you do first?
- **Decides:** a check on your own view; differences are worth exploring.

## Scoping topics

### 9. Users, roles and access

- **Learn:** who uses the application, through what interface, whether they sign in, whether different users can see or do different things, and whether the agent acts on a user's behalf.
- **Ask:** Who uses it, and how: web, mobile, chat, API, inside another product? Do users sign in? Do different users have different permissions? Does the agent act using a user's own access?
- **Decides:** Category 2 User Experience Design (2.1, 2.2), Category 3 Frontend Engineering (3.1 to 3.4; 3.2 if output streams, 3.3 if the model generates interface elements), Category 4 Identity and Access Management (4.1 to 4.3; 4.4 if the agent acts with user permissions).

### 10. Workflow and autonomy

- **Learn:** the task the application performs, step by step; how much it decides on its own; which actions are irreversible; where a person must review or approve; whether the task splits naturally into specialist roles; whether it runs long or in the background.
- **Ask:** Walk me through the task from start to finish. Which steps should the application do on its own, and which need a person? What actions can't be undone? Does it run while the user waits, or in the background? Is it one job or several specialist jobs?
- **Decides:** Category 9 Cognitive Agent Architecture (9.1 to 9.3), Category 11 Multi-Agent Orchestration (11.1 to 11.4, only if several cooperating agents are needed), 2.3 Human-in-the-Loop Interaction Patterns and Category 14 Human Operations (14.1, 14.2) if people review decisions, 12.3 Asynchronous Task Worker Queue Engine if tasks run long, 13.4 Watchdog Supervisor Engine if the agent runs autonomously.

### 11. Data and knowledge

- **Learn:** what the application must know (documents, records, domain knowledge), where it lives, how much, how often it changes, how sensitive it is; whether the application keeps its own records; whether it must remember users across sessions; whether models will be adapted with project data.
- **Ask:** What information does it need to do the job, and where does that live today? How much is there, and how often does it change? Does it contain personal or confidential data? Should it remember users between sessions? Do you expect to fine-tune a model?
- **Decides:** Category 5 Operational Data Engineering (5.1 to 5.4; 5.4 if external data must be synchronized), Category 6 Knowledge Retrieval Engineering (6.1, 6.2, 6.4; 6.3 if relationships between entities matter), Category 7 Context and Memory Engineering (7.1, 7.2; 7.3 if it remembers users), Category 20 Model Adaptation and Continuous Improvement (20.1 to 20.4, only if models will be adapted or improved from production feedback), 13.2 PII Redaction Engine if personal data is involved.

### 12. Integrations and operating environment

- **Learn:** the systems the application reads from or acts on, whether it must run generated code, where it will be hosted, expected usage and scale, and the operating expectations once live.
- **Ask:** Which systems does it need to read from or take action in? Will it ever need to run code it writes? Where must it be hosted? How many users or tasks do you expect? Who runs it once it is live, and how will they know it is healthy?
- **Decides:** Category 10 Tool Surface Integration (10.1, 10.3; 10.2 if tools are exposed via MCP; 10.4 if generated code runs), Category 12 Backend Application Engineering (12.1, 12.2), Category 8 Model Gateway Operations (8.1, 8.2 if volume and cost justify caching), Category 16 Deployment and Cloud Infrastructure (16.1 to 16.3; 16.4 if new versions must be proven on live traffic first), Category 17 Telemetry and Observability (17.1, 17.2).

### 13. Quality bar, safety, compliance and commercial model

- **Learn:** how good the output must be and how that will be judged; the cost of a wrong answer or wrong action; regulatory and audit obligations; exposure to hostile users; how the application makes money; what product usage the client wants to measure.
- **Ask:** How good does it need to be before people rely on it, and who judges that? What happens if it gets something wrong? Are there regulations or audit requirements? Could users try to misuse it? How will it make money: subscription, usage, internal savings? What do you want to learn from how people use it?
- **Decides:** Category 15 Quality Engineering and Evaluation (15.1, 15.2, 15.4; 15.3 if exposed to adversarial users), Category 13 Runtime Safety and Moderation (13.1, 13.3 if audit is required, 13.5 for any application exposed to untrusted input or acting on systems), Category 18 Usage Metering and Monetization (18.1 if usage is limited or billed, 18.2 if payments are taken), Category 19 Product Analytics (19.1, 19.2), 1.7 Business Viability Assessment.

## When you have enough

You have enough for scoping when:

- Every one of the 20 categories is marked in play, out of play or unknown, with a reason.
- For in-play categories, you know which of its nodes the client's answers point to, or what you would need to ask to tell.
- The client's beliefs and risks are recorded in their words.
- For an in-flight project, completed work is identified well enough to exclude it.

You do not need counts, volumes or sizes for estimating. Those come in Estimation Discovery.
