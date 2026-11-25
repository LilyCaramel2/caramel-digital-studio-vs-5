# Caramel operating system and model routing summary

**Date:** 2026-11-25
**Repository:** `LilyCaramel2/caramel-digital-studio-vs-5`
**Current layer:** static HTML, CSS, Tailwind CDN, and JavaScript
**Status:** documentation and future-architecture handover

## Owner and operating model

Caramel Digital Studio is a solo developer studio supported by agents. Melissa owns purpose, judgement, authorship, quality, security, approvals, client communication, and publication. Agents provide research, memory, drafting, analysis, coding, testing, and handover support.

The repository uses Markdown as the primary coordination format. Use Markdown, YAML, JSON, source files, checklists, and handovers for agent work. Use presentation slides only for an explicitly requested client pitch or presentation.

## Resource and privacy policy

Use local open-source models and deterministic local tools first. Use free services where they meet the task. Paid APIs, paid upgrades, and hosted processing require owner approval and a written reason.

Conserve tokens and compute by reading existing files first, reusing approved research, selecting the smallest capable model, working in bounded batches, transferring context through files, and leaving concise handovers.

Keep private source, prompts, client records, payment details, credentials, research, and intellectual property in owner-controlled files and approved repositories. Use the owner-approved C-drive silo or Google-backed storage as the durable file layer. Linear, Render, Supabase, GitHub Issues, and similar systems can reference approved files through controlled links while the file store remains the source.

Record ownership, access scope, privacy, retention, link status, model, runtime, data class, tool permissions, cost tier, and approval state for each connected workflow.

## Google-first coordination layer

Use Google Workspace as the default low-cost coordination and file layer when a client has Gmail or free Workspace access. Use Gemini in approved Gmail, Drive, Docs, Sheets, Calendar, Meet, and Apps Script workflows when account permissions and privacy settings support the task.

Use Gemma for local or owner-controlled Google-adjacent work such as document classification, file preparation, source summarisation, Apps Script drafting, translation support, and handover preparation. Gemma can run locally through tools such as Ollama, LM Studio, llama.cpp, MLX, and LiteRT-LM.

Gemma or Gemini can prepare a Google Pay explanation, classify a receipt, or draft a confirmation. Payment authorisation, account access, receipt verification, and client confirmation remain owner-controlled through the approved payment workflow.

## Model routing

### Gemma and Gemini

Route Google Workspace preparation, approved file organisation, document support, receipt classification, and translation assistance to Gemma or Gemini according to the privacy boundary and available runtime.

### Qwen and Qwen Code

Route local repository analysis, coding, refactoring, skills, test scripts, structured handovers, and token-conscious development to Qwen or Qwen Code. Qwen Code supports local models through Ollama and vLLM, plus skills, subagents, MCP, worktrees, and approval modes.

### GLM

Route tested coding, reasoning, structured output, and tool-use experiments to a selected GLM checkpoint when its hardware, licence, context, and tested behaviour fit the task. Record the checkpoint and runtime before deployment.

### OpenManus

Use OpenManus as an isolated local orchestration and browser/tool experiment. Keep it in a separate sandbox or repository until permissions, model routing, tool access, cost, and audit behaviour have been tested.

### Hosted models and research tools

Perplexity, Google Flow, Nano Banana Pro, Veo, and other hosted tools remain optional future tools. Verify current availability, account plan, regional access, cost, data handling, and owner approval at the time of use. Keep the core workflow functional through local or free alternatives where possible.

## Content production process

For blogs and articles:

1. Research from approved sources and record citations.
2. Create a source-grounded brief.
3. Draft original copy through the Caramel writing audit.
4. Run the grammar, spelling, terminology, freshness, restricted-language, and em-dash checks.
5. Complete owner review and approval.
6. Store the approved Markdown and source record in the approved file silo.

For images and videos:

1. Create a brief from the approved article or campaign source.
2. Assign image, video, motion, and accessibility requirements.
3. Use a local or approved generation tool according to the data and budget boundary.
4. Record prompts, source assets, licences, model/tool, output location, and review state.
5. Check factual accuracy, brand fit, accessibility, captions, alt text, rights, and file size.
6. Publish only after owner approval.

## Render and endpoint architecture

A Render web service receives inbound HTTPS through its public URL when it listens on `0.0.0.0` and the `PORT` environment variable. Use a web service for public inbound HTTP. Use a private service for internal service-to-service traffic. Use a background worker for queues and long-running jobs after a request has been accepted.

Render workspace webhooks require a Pro-or-higher workspace. A receiver must return a 2xx response within 15 seconds, validate the signature, use event IDs for idempotency, and handle retries.

Preferred future flow:

`Google Workspace and approved file silo → secured web-service endpoint → authentication and validation → idempotency check → queue or worker → selected local or hosted model → result file → controlled reference in Linear, Render, Supabase, GitHub Issues, or Calendar`

Add authentication, rate limits, secret storage, audit logs, retry rules, deletion rules, and owner approval before exposing an endpoint.

## Current verification result

The repository currently contains no actual local-model runtime configuration, model download, Ollama or vLLM service, Render service definition, `render.yaml`, Dockerfile, webhook receiver, endpoint URL, or environment configuration for this architecture.

Therefore:

- the local model route is documented but remains unconfigured;
- the secured Render endpoint is documented but remains unconfigured;
- end-to-end privacy and token-conservation behaviour remain future implementation tests;
- the current static site remains clean and separate from connected-system work.

The next implementation batch must create a small local-model test, record hardware and model requirements, create a minimal secured endpoint in a separate approved project, and test file flow without adding credentials to this repository.

## Next-agent build batches

1. **Baseline:** read this handover, `AGENT_LANGUAGE_PROTOCOL.md`, `CARAMEL_WRITING_AUDIT_AGENTIC.md`, `MODEL_ROUTING_AND_RENDER_INTEGRATION_HANDOVER.md`, `AGENT_OPERATIONS_AND_TESTING.md`, and Issue #1.
2. **Local model test:** shortlist one small Gemma model and one small Qwen model, verify licence, hardware, runtime, memory, latency, output quality, and local data handling.
3. **GLM and OpenManus review:** record candidate checkpoints and run isolated experiments only after the local baseline passes.
4. **File-layer test:** use a non-sensitive sample PDF or media file in the approved silo and test controlled references from a task record.
5. **Render endpoint design:** specify authentication, request schema, response schema, idempotency, rate limits, secrets, logs, retries, deletion, and cost controls before deployment.
6. **Content pipeline:** test one research-to-blog-to-image/video workflow with citations, writing audit, accessibility review, and owner approval.
7. **Connected-system gate:** keep the static site unchanged until the owner approves the separate application phase.
8. **Close the batch:** run all skill validators, `git diff --check`, the offline checker, and the Issue #1 update. Commit only intended files.

## Official references

- [Gemma local execution](https://ai.google.dev/gemma/docs/run)
- [Google Workspace with Gemini](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/google-workspace-with-gemini)
- [Qwen Code](https://github.com/QwenLM/qwen-code)
- [GLM-4.5](https://docs.z.ai/guides/llm/glm-4.5)
- [OpenManus](https://github.com/FoundationAgents/OpenManus)
- [Render web services](https://render.com/docs/web-services)
- [Render webhooks](https://render.com/docs/webhooks)
