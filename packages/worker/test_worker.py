import pytest\n\n@pytest.mark.asyncio\nasync def test_execute_node(websocket):\n    node_id = "node-123"\n    code = "print(\'Hello, World!\')"\n    payload = json.dumps({\'id\': node_id, \'code\': code, \'language\': \'python\'})\n    # Simulate sending the execute_node message\n    await websocket.send_text(payload)\n    # Assert the result\n    result = await websocket.receive_text()\n    assert result[\'type\'] == \'result\'\n    assert result[\'id\'] == node_id\n    assert result[\'status\'] == \'success\'\n    assert result[\'stdout\'] == \'Hello, World!\\n\'\n
def test_execute_node():\n    node_id = "node-123"\n    code = "print(\'Hello, World!\')"\n    payload = json.dumps({\'id\': node_id, \'code\': code, \'language\': \'python\'})\n    # Simulate sending the execute_node message\n    result = await websocket.send_text(payload)\n    # Assert the result\n    assert result[\'type\'] == \'result\'\n    assert result[\'id\'] == node_id\n    assert result[\'status\'] == \'success\'\n    assert result[\'stdout\'] == \'Hello, World!\\n\'\n

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

async def test_execute_node():\n    async with websockets.connect("ws://localhost:7331/ws") as websocket:\n        code = "print(\'Hello from execute_node!\')"  \n        message = {"type": "execute_node", "id": "node-123", "code": code}\n        await websocket.send(json.dumps(message))\n\n        response = await websocket.recv()\n        result = json.loads(response)\n\n        assert result["type"] == "result"\n        assert result["id"] == "node-123"\n        assert result["status"] == "success"\n        assert "Hello from execute_node!" in result["stdout"]\n\n# To run the test, use an asyncio event loop\nif __name__ == "__main__":\n    asyncio.run(test_execute_node())\n
# To run the test, use an asyncio event loop
if __name__ == "__main__":
    asyncio.run(test_execute_code())
