# LLM application readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Evaluation boundary
- Define intended tasks, unacceptable outcomes, user roles, model/prompt/tool/index versions, and rollout audience. Build representative held-out cases with documented expected behavior and failure criteria.
- Evaluate success, abstention, citation fidelity, structured output, latency, and cost with enough repeated runs to expose variability. Separate offline scores, human judgment, and observed live outcomes.
- Include realistic adversarial, ambiguous, multilingual, long-context, missing-evidence, and provider-outage cases as relevant. Do not select only passing examples or treat model self-grading as independent proof.

## Retrieval and trust
- Verify document/row permissions at retrieval and after identity changes; test cross-tenant queries, stale ACLs, deleted documents, index refresh, and cache isolation.
- Treat user input, retrieved pages, documents, tool output, and conversation memory as untrusted data. Test instruction injection that attempts credential disclosure, permission escalation, or tool redirection.
- Require authorization and validation at actual tool execution boundaries. Test forged tool arguments, replayed actions, excessive paths/URLs, and user cancellation. A prompt instruction cannot enforce server permissions.
- Verify citations against retrieved source passages and distinguish missing/contradictory evidence from supported answers. Define refusal, fallback, or human escalation for consequential uncertainty.

## Tool use and runtime limits
- Bound tokens, context, tool calls, recursion, elapsed time, concurrency, retries, and per-user spend. Test runaway loops, provider 429/5xx, streaming disconnects, and budget exhaustion.
- Validate structured output and tool results before side effects. Apply idempotency and durable state to retries; test a crash between a tool action and its recorded completion.
- If code execution is offered, test isolation, filesystem/network permissions, resource quotas, cleanup, and access to secrets. Use deliberately safe fixtures.
- Verify session/memory isolation, retention/deletion, provider data handling settings, and redacted traces. Do not log full prompts or retrieved private documents by default.

## Release and monitoring
- Version prompts, models, embedding settings, retrieval transforms, and tool contracts with the candidate. Retest relevant evaluations after any of them change.
- Verify fallback models against the same critical criteria and tool authority; a fallback must not silently weaken controls or exceed cost/latency bounds.
- Roll out with defined stop criteria, monitor task failures and cost safely, retain a compatible prior configuration, and document escalation/incident ownership. State evaluation limits rather than promising hallucination-free output.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/)
- [NIST AI risk management](https://www.nist.gov/itl/ai-risk-management-framework)
