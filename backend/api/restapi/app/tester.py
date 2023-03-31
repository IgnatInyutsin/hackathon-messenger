import websocket
ws = websocket.WebSocket()
ws.connect("ws://localhost:98/ws/chat/7/?token=161ef9b129a1ac755bb7d55ff28e730c58808c32")
ws.send('{"text": "хуйrr"}')
print(ws.recv())