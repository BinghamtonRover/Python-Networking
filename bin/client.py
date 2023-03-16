import time
from lib.network import UdpClient

client = UdpClient(address="192.168.1.30", port=8001)

try: 
	while True: 
		client.send(b"Hello")
		print("Sent a message")
		time.sleep(0.2)
except KeyboardInterrupt: pass
finally: 
	client.close()
