import time
from lib.network import UdpClient

client = UdpClient()

try: 
	while True: 
		client.send("localhost", 8001, b"Hello")
		print("Sent a message")
		time.sleep(1)
except KeyboardInterrupt: pass
finally: 
	client.close()