


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        stdout = io.StringIO()\nstderr = io.StringIO()\nstatus = "success"\ntry:\n    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):\n        exec(code)\nexcept Exception as e:\n    status = "error"\n    stderr.write(str(e))\nresponse = {\n    "type": "result",\n    "stdout": stdout.getvalue(),\n    "stderr": stderr.getvalue(),\n    "status": status\n}\nawait websocket.send_text(json.dumps(response))
