from websocket import create_connection
ws = create_connection("ws://localhost:98/ws/chat/4/?token=161ef9b129a1ac755bb7d55ff28e730c58808c32")
ws.send("")
result =  ws.recv()
print(result)