# W2 Foundations - Challenge Notes

**Project path:** `/Users/katew/CodePlatoon/w2-foundations`

**Why a harness matters:** A harness keeps agent instructions and safety configurations organized in a consistent workspace so they can be shared, reused, and reviewed through Git.

## 1. Skill Test

**Skill name:** check-local-stack

### Prompt Used

Use the check-local-stack skill to check my local development environment.

### Agent Summary

Pending verification in Antigravity.

### Tool Call Approvals

Pending verification.

### Failed Commands

Pending verification.

### Why a File-Backed Skill Is Useful

A file-backed skill saves reusable instructions so developers do not have to repeat the same prompt every time. It also allows team members to share and improve instructions through Git.

### Real-World Use

A development team can use a skill to verify that new developers have the required tools installed before starting a project.

## 2. Hook Test

**Hook name:** deny-rm

**Event:** PreToolUse

**Matcher:** run_command

**Script:** scripts/deny_rm.py

### Denied Command

Command: `rm hook-test.txt`

Actual result: Pending verification in Antigravity.

### Allowed Command

Command: `ls NOTES.md`

Actual result: Pending verification in Antigravity.

### Dry Run

**Deny test:**

Input:

`{"toolCall":{"name":"run_command","args":{"CommandLine":"rm NOTES.md"}}}`

Output:

`{"decision": "deny", "reason": "Course hook blocks rm. Use a safer cleanup path or run rm yourself in your own terminal."}`

Result: Passed.

**Allow test:**

Input:

`{"toolCall":{"name":"run_command","args":{"CommandLine":"ls NOTES.md"}}}`

Output:

`{"decision": "allow"}`

Result: Passed.

Both local dry-run tests passed. The script correctly denied the blocked command and allowed the safe command.

### How the Hook Works

Antigravity sends tool-call information to the Python script as JSON through stdin. The script checks the command and returns a JSON decision through stdout. This makes the hook easy to understand and test independently.

### Real-World Use

A development team can use a PreToolUse hook to prevent agents from executing destructive commands or accessing sensitive information.

### Limitations

The current hook only checks basic rm patterns. It does not replace permissions or sandbox restrictions.

## 3. Permissions

### Deny Rules

Pending configuration verification.

### Ask Rules

Pending configuration verification.

### Allow Rules

Pending configuration verification.

### Permission Evaluation

When permission rules conflict, Deny takes priority over Ask and Allow. If no Deny rule matches, Ask takes priority over Allow. A broad Allow rule cannot override an explicit Deny rule.

### Why Permissions Matter

Permissions help protect sensitive files and prevent the agent from performing risky operations without human approval.

## Detection pass

## Detection pass

**Slop:** The agent performed additional checks that were not required by the original lesson skill, including Git, Node.js, npm, and workspace directory checks.

**Drift:** The agent expanded the local stack verification beyond Python and PostgreSQL. It checked Python successfully but omitted the PostgreSQL client version and server readiness checks required by the original lesson.

**Hallucination:** No confirmed hallucination was identified. The reported Python version matched my manual terminal output. However, the reported hook working directory issue still requires verification through an actual hook test.

**One fix I would make next time:** I would make the skill more explicit about its scope by requiring the agent to execute every listed command, report the raw output, and avoid unrelated checks unless explicitly requested.

### Agent Summary

The agent checked the workspace directory, Git version, repository status, Python version, Node.js version, npm version, and project directory structure.

It reported that Python 3.15.2 was available and identified a potential relative path issue in the PreToolUse hook configuration.

However, the agent did not check the PostgreSQL client version or PostgreSQL server readiness as required by the original lesson skill.

No files were modified during the verification.

### Manual Verification

I independently ran the following commands in my terminal:

- `python3 --version`: Python 3.15.2
- `psql --version`: PostgreSQL 18.7 (Homebrew)
- `pg_isready`: /tmp:5432 - accepting connections

All three manual checks passed.