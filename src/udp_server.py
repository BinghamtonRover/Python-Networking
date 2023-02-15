import socket

BUFFER_SIZE = 1024

class UdpServer:
	def __init__(self, port):
		self.port = port
		self.socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		self.socket.bind(("0.0.0.0", port))
		self.socket.settimeout(0.1)

	def start(self):
		print(f"Server started on port {self.port}")
		try:
			while(True):
				try: message, source = self.socket.recvfrom(BUFFER_SIZE)
				except socket.timeout: continue
				else: self.on_data(message, source)
		except KeyboardInterrupt: self.close()

	def on_data(self, data, source): 
		print(f"Received message from {source}: {data}")

	def close(self): 
		print("Closing the socket...")
		self.socket.close()
