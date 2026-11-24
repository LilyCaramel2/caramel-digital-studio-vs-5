

## 2026-11-24 — offline checker and automated static workflow

### Scope

Added a dependency-free repository checker, GitHub Actions workflow, and durable agent operations guide. No public website source or payment configuration changed.

### Files added

- `scripts/check_caramel_repo.py` checks tracked text files, retired-provider references, required agent files, branch state, upstream alignment, and uncommitted changes.
- `.github/workflows/caramel-static-checks.yml` runs the checker on pushes and pull requests with read-only repository permission.
- `AGENT_OPERATIONS_AND_TESTING.md` explains where handovers live, how agents start and finish batches, how to recover from stalls, and what the offline checker can and cannot verify.

### Validation

The checker uses only Python’s standard library and local Git commands. It installs no dependencies and does not contact payment providers. GitHub Actions handles detached pull-request checkouts by validating repository content while local release checks remain strict about upstream alignment.

### Next action

Run the checker after commit and push. Review the first GitHub Actions result. Continue with owner-controlled payment and Calendar testing only after the repository checks pass.
