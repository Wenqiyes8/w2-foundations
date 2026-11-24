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

Slop: none

Drift: none

Hallucination: none

One fix I would make next time: I would update the skill to require the agent to report the raw command output for every check, so I can verify its findings more easily and avoid relying only on its summary.

### Manual Verification

I manually verified the local development environment by running the following commands in my terminal:

- `python3 --version`: Python 3.15.2
- `psql --version`: psql (PostgreSQL) 18.7 (Homebrew)
- `pg_isready`: /tmp:5432 - accepting connections

All three manual checks passed. Python and PostgreSQL are available, and the PostgreSQL server is accepting connections.

These results provide a baseline for verifying the accuracy of the agent's reported results during the detection pass.