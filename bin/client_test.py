import time
from lib.network.udp_client import UdpClient

client = UdpClient()

try: 
	while True: 
		client.send("localhost", 8001, b"Hello")
		print("Sent a message")
		time.sleep(1)
finally: 
	client.close()