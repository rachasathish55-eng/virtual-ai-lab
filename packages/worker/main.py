#!/usr/bin/env python3
"""
Claw Worker — Strawberry Studios WebSocket Daemon
Listens on ws://0.0.0.0:7331
Handles StrawberryNode execution requests via WebSocket RPC.
"""
from __future__ import annotations

import asyncio
import contextlib
import io
import json
from datetime import datetime

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="Claw Worker", version="1.0.0")


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "claw-worker",
        "ts": datetime.utcnow().isoformat()
    }


@app.websocket("/ws")
async def ws_ping(websocket: WebSocket):
    """Simple ping/pong for connectivity testing."""
    await websocket.accept()
    try:
        while True:
            msg = await websocket.receive_text()
            await websocket.send_text(json.dumps({"type": "pong", "echo": msg}))
    except WebSocketDisconnect:
        pass


@app.websocket("/run_code")
async def run_code(websocket: WebSocket):
    """
    Execute a StrawberryNode's code payload.

    Expected JSON input:
      { "id": "node-123", "code": "print('hello')", "language": "python" }

    Response JSON:
      { "type": "result", "id": "node-123", "stdout": "...", "stderr": "...", "status": "success|error" }
    """
    await websocket.accept()
    try:
        while True:
            raw = await websocket.receive_text()

            # Parse payload
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError as e:
                await websocket.send_text(json.dumps({
                    "type": "error",
                    "error": f"Invalid JSON: {e}"
                }))
                continue

            node_id  = payload.get("id", "unknown")
            code     = payload.get("code", "")
            language = payload.get("language", "python").lower()

            # Only Python supported for now
            if language != "python":
                await websocket.send_text(json.dumps({
                    "type": "result",
                    "id": node_id,
                    "stdout": "",
                    "stderr": f"Language '{language}' not yet supported.",
                    "status": "error"
                }))
                continue

            # Execute the code safely\nfrom packages.worker.executor import run_node_code\n\n            if language == "python":\n                result = run_node_code(code)\n                await websocket.send_text(json.dumps({\n                    "type": "result",\n                    "id": node_id,\n                    "stdout": result['output'],\n                    "stderr": "",\n                    "status": result['status']\n                }))\n                continue\n            \n            # Existing code for handling unsupported languages\n
            stdout_buf = io.StringIO()
            stderr_buf = io.StringIO()
            status = "success"
            try:
                with contextlib.redirect_stdout(stdout_buf), \
                     contextlib.redirect_stderr(stderr_buf):
                    
            except Exception as exc:
                status = "error"
                stderr_buf.write(f"{type(exc).__name__}: {exc}")

            await websocket.send_text(json.dumps({
                "type":   "result",
                "id":     node_id,
                "stdout": stdout_buf.getvalue(),
                "stderr": stderr_buf.getvalue(),
                "status": status,
            }))

    except WebSocketDisconnect:
        pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7331, reload=False, log_level="info")
