
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def get():
    return HTMLResponse("<h1>WebSocket Server</h1>")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data == "ping":
            await websocket.send_text("pong")
        else:
            await websocket.send_text("status: server is running")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7331)
