import socket
import time

class UdpSocket: 
	def __init__(self, port, destination=None, buffer=1024): 
		self.port = port
		self.destination = destination
		self.buffer = buffer
		self.keep_alive = True
		self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
		self.socket.bind( ("0.0.0.0", port) )
		self.socket.settimeout(0.1)

	def send(self, data, destination=None): 
		if destination is None: destination = self.destination
		if destination is None: raise ValueError("No destination specified")
		self.socket.sendto(data, destination)

	def listen(self): 
		print(f"Listening on port {self.port}")
		try: 
			while True:
				if not self.keep_alive: return self.close()
				try: data, source = self.socket.recvfrom(self.buffer)
				except socket.timeout as error: pass
				else: self.on_data(data, source)
				finally: self.on_loop()
		except KeyboardInterrupt as error: 
			self.close()
			raise error from None

	def close(self): 
		self.socket.close()
		print(f"Closed the socket on port {self.port}")

	def on_data(self, data, source): 
		print(f"Received message from {source}: {data}")

	def on_loop(self): pass
