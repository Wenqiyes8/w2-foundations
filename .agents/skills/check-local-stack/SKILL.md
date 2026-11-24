---
name: check-local-stack
description: Check whether the local engineering environment is ready for development by verifying required tools and workspace configuration.
---

# Check Local Stack

## Instructions

1. Run `pwd` to confirm the current workspace directory.
2. Run `git --version` and `git status` to verify Git is installed and the workspace is a Git repository.
3. Run `python3 --version` to verify Python is installed.
4. Run `node --version` and `npm --version` to check the Node.js environment.
5. Check whether the `.agents` and `scripts` directories exist.
6. Report the results, including any missing tools or configuration issues.

## Rules

- Only perform read-only checks.
- Do not install software automatically.
- Do not delete or modify existing files.
- Ask the user before making any changes.
