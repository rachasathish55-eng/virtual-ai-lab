
import asyncio
import websockets
import json

async def run_code():
    async with websockets.connect("ws://localhost:7331/run_code") as websocket:
        code_data = {
            "id": "test_node",
            "code": "print('Hello, World!')",
            "language": "python"
        }
        await websocket.send(json.dumps(code_data))
        response = await websocket.recv()
        print("Response:", response)

asyncio.run(run_code())


import asyncio
import websockets
import json

async def run_code(code):
    async with websockets.connect("ws://localhost:7331/run_code") as websocket:
        await websocket.send(json.dumps({"code": code}))
        response = await websocket.recv()
        print("Response:", response)

if __name__ == "__main__":
    code_to_run = "print('Hello, World!')"
    asyncio.run(run_code(code_to_run))
