import socket

class UdpClient:
	def __init__(self, address=None, port=None, buffer_size=1024):
		self.buffer_size = buffer_size
		self.udp_client_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		self.address = None
		self.port = None

	def send(self, data, address=None, port=None):
		if (address is None): address = self.address
		if (port is None): port = self.port
		self.udp_client_socket.sendto(data, (address, port))

	def close(self):
		self.udp_client_socket.close()
