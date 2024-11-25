# import socket
# import time
# import threading

# class UdpSocket(threading.Thread):
# 	def __init__(self, port, destination=None, buffer=1024):
# 		super().__init__()
# 		self.port = port
# 		self.destination = destination
# 		self.buffer = buffer
# 		self.keep_alive = True
# 		self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 		self.socket.bind( ("0.0.0.0", port) )
# 		self.socket.settimeout(0.1)

# 	def send(self, data, destination=None):
# 		if destination is None: destination = self.destination
# 		if destination is None: raise ValueError("No destination specified")
# 		self.socket.sendto(data, destination)

# 	def run(self):
# 		print(f"Listening on port {self.port}")
# 		while self.keep_alive:
# 			try:
# 				data, source = self.socket.recvfrom(self.buffer)
# 				self.on_data(data, source)
# 				# Remove this line once heartbeats are threaded
# 				self.on_loop()
# 			except socket.timeout as error: pass
# 			except OSError as error:
# 				if error.errno in [10054, 101, 10038, 9]: continue
# 				else: raise error

# 	def close(self):
# 		self.keep_alive = False

# 	def close_socket(self):
# 		self.socket.close()
# 		print(f"Closed the socket on port {self.port}")

# 	def on_data(self, data, source):
# 		print(f"Received message from {source}: {data}")

# 	def on_loop(self): pass
