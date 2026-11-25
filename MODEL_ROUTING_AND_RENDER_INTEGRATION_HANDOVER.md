# Model routing and Render integration handover

**Status:** future architecture reference
**Current site:** static HTML, CSS, Tailwind CDN, and JavaScript
**Rule:** keep this layer separate from the current static source

## Recommended model roles

### Gemma and Google Workspace

Use Gemma for local or owner-controlled Google-adjacent work: document classification, source summarisation, Workspace file preparation, Apps Script drafting, translation support, and structured handover preparation. Google’s Gemma documentation describes local execution through tools such as Ollama, LM Studio, llama.cpp, MLX, and LiteRT-LM.

Use Gemini in Google Workspace for approved Gmail, Docs, Drive, Sheets, Calendar, Meet, and Apps Script workflows where the account plan and privacy settings support the task. Treat Workspace permissions and file ownership as the control boundary.

Gemma or Gemini may prepare a Google Pay workflow, explain a payment request, classify a payment receipt, or draft a confirmation message. Payment authorisation, account access, receipt verification, and client confirmation remain owner-controlled operations through the approved payment provider.

### Qwen

Use Qwen and Qwen Code for local coding, repository analysis, skills, tests, refactoring, and agent handovers. The official Qwen Code repository documents local-model support through Ollama and vLLM, runtime switching, skills, subagents, MCP, worktrees, and approval modes.

Qwen is a strong default for token-conscious development work where the repository and tools remain local.

### GLM

Use GLM models for local or approved hosted coding, reasoning, structured tool use, and agent experiments. Select a checkpoint by available hardware, licence, context requirement, and tested tool behaviour. GLM documentation describes tool invocation, reasoning modes, structured output, and agent-oriented coding use cases. Record the selected checkpoint and runtime before deployment.

### OpenManus

Use OpenManus as a local orchestration and browser/tool experiment. Its repository documents local Python execution, MCP support, browser automation, configurable model providers, and experimental multi-agent flows. Keep it in a separate sandbox or repository until its permissions, model routing, tool boundaries, and cost are tested.

## Routing principle

1. Keep private source, client records, credentials, and intellectual property local or in the approved Google-backed file silo.
2. Route ordinary coding and document work to the smallest capable local model.
3. Route Google Workspace actions through the approved Google account and permission boundary.
4. Route payment actions through the official payment workflow, with owner receipt review.
5. Route long-running hosted jobs to Render only when a local process cannot complete the task.
6. Record model, runtime, data class, tool permissions, cost tier, and approval state for each connected workflow.

## Render call paths

A Render web service receives inbound HTTPS through its public `onrender.com` or custom-domain URL. The service must listen on `0.0.0.0` and the `PORT` environment variable. Use this path for an approved API endpoint, webhook receiver, or small orchestration service.

A Render private service is suitable for internal service-to-service traffic. A background worker is suitable for queues and long-running jobs. Use a web service for public inbound HTTP; use a worker for processing after a request is accepted by a web service.

Render workspace webhooks send HTTPS POST notifications to a public endpoint and require a Pro or higher workspace. Each receiver must return a 2xx response within 15 seconds, validate the webhook signature, use the event ID for idempotency, and handle retries. A free-tier design should use a normal secured web-service endpoint where that is sufficient, then queue work for a worker.

## Future implementation shape

`Google Workspace and approved file silo → web service endpoint → validation and idempotency → queue or worker → local model or selected hosted model → result file → controlled reference in Linear, Render, Supabase, GitHub Issues, or Calendar`

Keep the static site separate until the owner approves the connected-systems phase. Add authentication, rate limits, secret storage, audit logs, retry rules, deletion rules, and owner approval before exposing any endpoint.

## Official references

- [Gemma local execution](https://ai.google.dev/gemma/docs/run)
- [Google Workspace with Gemini](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/google-workspace-with-gemini)
- [Qwen Code](https://github.com/QwenLM/qwen-code)
- [GLM-4.5](https://docs.z.ai/guides/llm/glm-4.5)
- [OpenManus](https://github.com/FoundationAgents/OpenManus)
- [Render web services](https://render.com/docs/web-services)
- [Render webhooks](https://render.com/docs/webhooks)
