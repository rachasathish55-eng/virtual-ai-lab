# AGENTS.md — Instructions for OpenHands Coding Agent

You are building **Virtual AI Lab** (Strawberry Studios) — a Distributed AI Operating System.

## THE VISION
A Tauri desktop app (Rust + React) where AI researchers control multiple compute machines
from ONE visual interface. Node Editor canvas for pipelines, Notebook for code, Terminal for
output, and Claw Workers on remote machines executing scripts.

## MANDATORY: Completion Marker
When done, write: /home/ubuntu/workspace/.task-complete/{TASK_ID}.json
```json
{"task_id": "TASK_ID", "status": "done", "files_created": [], "summary": "what you built"}
```

## Git Discipline
```bash
cd /home/ubuntu/workspace && git add -A && git commit -m "feat(TASK_ID): what you built"
```

## Rules
- Workspace: /home/ubuntu/workspace
- Check existing files FIRST (ls, cat) before writing
- Tech stack: Tauri + React + TypeScript + pnpm + Turbo + Python Claw Worker
- Claw Worker: pure asyncio + websockets (NO FastAPI)
- Do NOT overwrite working code
