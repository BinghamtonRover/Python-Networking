import time
from lib.network import UdpClient

client = UdpClient(address="localhost", port=8001)

try: 
	while True: 
		client.send(b"Hello")
		print("Sent a message")
		time.sleep(1)
except KeyboardInterrupt: pass
finally: 
	client.close()
