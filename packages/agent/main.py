
from fastapi import FastAPI, WebSocket\nimport json\nimport asyncio\nimport subprocess\nimport io\nimport contextlib\n\napp = FastAPI()\n\n@app.get(\"/health\")\ndef health():\n    return {\"status\": \"healthy\"}\n\n@app.websocket(\"/ws\")\nasync def websocket_endpoint(websocket: WebSocket):\n    await websocket.accept()\n    while True:\n        data = await websocket.receive_text()\n        message = json.loads(data)\n        if message.get(\"type\") == \"execute\":\n            code = message.get(\"code\")\n            request_id = message.get(\"request_id\")\n            stdout = io.StringIO()\n            stderr = io.StringIO()\n            status = \"success\"\n            try:\n                with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):\n                    exec(code)\n            except Exception as e:\n                status = \"error\"\n                stderr.write(str(e))\n            response = {\n                \"type\": \"result\",\n                \"request_id\": request_id,\n                \"stdout\": stdout.getvalue(),\n                \"stderr\": stderr.getvalue(),\n                \"status\": status\n            }\n            await websocket.send_text(json.dumps(response))\n        else:\n            await websocket.send_text(\"Invalid message format\")\n

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")
