# Virtual AI Lab (Strawberry Studios)

**A Distributed AI Operating System — Your Virtual AI Lab**

Control local machines, AWS EC2, and Google Colab from one visual desktop interface.
Build AI pipelines with a node editor, write code in Jupyter-like notebooks, and
execute on any hardware via lightweight Claw Worker daemons.

## Architecture
```
Tauri Desktop App (Rust + React)
├── Node Editor    (ReactFlow — visual pipeline builder)
├── Notebook       (CodeMirror — Jupyter-like code cells)
├── Terminal       (streaming stdout/stderr from workers)
├── Worker Panel   (connected hardware dashboard)
└── RPC Server     (WebSocket/gRPC bridge)

Claw Worker (Python daemon — any machine)
├── WebSocket server (port 7331)
├── Script executor (streams stdout back)
├── Hardware telemetry (CPU/RAM/GPU every 5s)
└── Auto-reconnect systemd service
```

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Desktop | Tauri (Rust) |
| Frontend | React + TypeScript + Vite |
| Node Editor | ReactFlow |
| Notebook | CodeMirror 6 |
| State | Zustand (USM) |
| Worker | Python asyncio + websockets |
| Build | pnpm + Turbo |

## Built Autonomously By
- **OpenClaw (Gemini)** — Research brain, plans what to build
- **OpenHands (Claude/GPT)** — Coding executor, writes the code
