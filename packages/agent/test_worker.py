
import asyncio
import websockets
import json

async def test_execute_code():
    async with websockets.connect("ws://localhost:7331/ws") as websocket:
        # Send a message to execute code
        code = "print('hello')"
        message = {"type": "execute", "code": code, "request_id": 1}
        await websocket.send(json.dumps(message))

        # Receive the response
        response = await websocket.recv()
        result = json.loads(response)

        assert result["type"] == "result"
        assert result["status"] == "success"
        assert "hello" in result["stdout"]

# Run the test
if __name__ == "__main__":
    asyncio.run(test_execute_code())


import json
import asyncio
import websockets

async def test_execute_code():
    async with websockets.connect("ws://localhost:7331/ws") as websocket:
        # Send a message to execute code
        code = "print('Hello, World!')"
        request_id = "test_request"
        message = json.dumps({"type": "execute", "code": code, "request_id": request_id})
        await websocket.send(message)

        # Receive the response
        response = await websocket.recv()
        result = json.loads(response)

        assert result["type"] == "result"
        assert result["status"] == "success"

# To run the test, use an asyncio event loop
if __name__ == "__main__":
    asyncio.run(test_execute_code())
