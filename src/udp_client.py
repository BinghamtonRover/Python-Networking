import socket

class UdpClient:
	def __init__(self, address=None, port=None, buffer_size=1024):
		self.buffer_size = buffer_size
		self.udp_client_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		self.address = address
		self.port = port

	def send(self, data, address=None, port=None):
		if (address is None): address = self.address
		if (port is None): port = self.port
		if (address is None or port is None):
			raise ValueError("No port or address specified")
		self.udp_client_socket.sendto(data, (address, port))

	def close(self):
		self.udp_client_socket.close()
