import socket

class UdpServer:
	def __init__(self, port, buffer=1024):
		self.port = port
		self.buffer = buffer
		self.socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		self.socket.bind(("0.0.0.0", port))
		self.socket.settimeout(0.1)

	def start(self):
		print(f"Server started on port {self.port}")
		try:
			while(True):
				try: message, source = self.socket.recvfrom(self.buffer)
				except socket.timeout: continue
				else: self.on_data(message, source)
				finally: self.on_loop()
		except KeyboardInterrupt: self.close()

	# Override this to insert your own logic in between waiting
	def on_loop(self): pass

	def on_data(self, data, source): 
		print(f"Received message from {source}: {data}")

	def close(self): 
		print("Closing the socket...")
		self.socket.close()
