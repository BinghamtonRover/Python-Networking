import socket

class UdpClient:
	def __init__(self, buffer_size=1024):
		self.buffer_size = buffer_size
		self.udp_client_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

	def send(self, address, port, data):
		self.udp_client_socket.sendto(data, (address, port))

	def close(self):
		self.udp_client_socket.close()
