import time
from src import UdpSocket

socket = UdpSocket(port=8000, destination=("127.0.0.1", 8001))

try: 
	while True: 
		socket.send(b"Hello")
		print("Sent a message")
		time.sleep(0.2)
except KeyboardInterrupt: 
	socket.close()
