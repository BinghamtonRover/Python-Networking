import socket

class UdpClient:
	def __init__(self, address=None, port=None):
		self.udp_client_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		self.address = address
		self.port = port

	def send(self, data, address=None, port=None):
		if (address is None): address = self.address
		if (port is None): port = self.port
		if (address is None or port is None):
			raise ValueError("No port or address specified")
		# print(f"Sending packet to {address}:{port}")
		self.udp_client_socket.sendto(data, (address, port))

	def close(self):
		self.udp_client_socket.close()
