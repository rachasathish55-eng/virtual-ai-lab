# Virtual AI Lab - Agent Instructions

## CRITICAL RULES (read before ANY action)
1. Monorepo layout: packages/app, packages/agent, packages/shared -- NOT apps/ or workers/
2. Claw Worker: SINGLE FILE packages/agent/claw_worker.py -- use pure asyncio + websockets ONLY. NO FastAPI. NO Flask. NO uvicorn.
3. Task completion: ALWAYS write /home/ubuntu/workspace/.task-complete/{task_id}.json when done
4. Tech stack LOCKED: Tauri + React + TypeScript + Vite + pnpm + Turbo + Python asyncio websockets + Zustand
5. Model: openai/gpt-4o-mini (DO NOT use gpt-5-mini)

## Build Order
Phase 1: monorepo-scaffold -- pnpm + turbo, packages/app + agent + shared  
Phase 2: claw-worker-core -- packages/agent/claw_worker.py (pure asyncio websockets)  
Phase 3: shared-types -- TypeScript types in packages/shared  
Phase 4: tauri-shell -- Tauri desktop app in packages/app  
Phase 5: node-editor -- ReactFlow canvas  
Phase 6: usm-store -- Zustand store  
Phase 7: extension-registry -- Plugin system  

## Task Completion Protocol
At the end of EVERY task, write this EXACTLY:

import json, os, time
task_id = "YOUR_TASK_ID_HERE"
os.makedirs("/home/ubuntu/workspace/.task-complete", exist_ok=True)
with open(f"/home/ubuntu/workspace/.task-complete/{task_id}.json", "w") as f:
    json.dump({"task_id": task_id, "status": "complete", "ts": time.time()}, f)
print("TASK COMPLETE: " + task_id)
