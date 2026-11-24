
---
name: check-local-stack
description: Checks whether the local engineering environment is ready for development by verifying Python, PostgreSQL, Git, Node.js, and workspace configuration. Use when preparing for local application development or troubleshooting the development environment.
---

# Check Local Stack

## Instructions

1. State the commands you will run before executing them.
2. Run `pwd` to confirm the current workspace directory.
3. Run `git --version` and `git status` to verify Git and repository status.
4. Run `python3 --version` to verify Python is installed.
5. Run `psql --version` to verify PostgreSQL client access.
6. If `pg_isready` exists, run it to check PostgreSQL server readiness.
7. Run `node --version` and `npm --version` to check the Node.js environment.
8. Check whether the `.agents` and `scripts` directories exist.
9. Report the raw command outputs and summarize what is ready and what is missing.

## Rules

- Only perform the read-only checks listed above.
- Do not install software automatically.
- Do not delete or modify existing files.
- Ask the user before making any changes.
- Do not report a failed command as successful.
- Do not claim that a tool is available without verification.
