import time
from src import UdpSocket

client = UdpSocket(port=8002, destination=("127.0.0.1", 8001))

try: 
	while True: 
		client.send(b"Hello")
		print("Sent a message")
		time.sleep(0.2)
except KeyboardInterrupt: client.close()
