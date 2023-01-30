import socket
import asyncio

def start_server(port): 
	loop = asyncio.get_event_loop()
	thread = loop.create_datagram_endpoint(UdpServer, local_addr=("127.0.0.1", port))
	loop.run_until_complete(thread)
	loop.run_forever()

class UdpServer(asyncio.DatagramProtocol):
	def __init__(self):
		super().__init__()

		# self.buffer_size = buffer_size
		# self.udp_server_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
		# self.udp_server_socket.bind(("localhost", port))
		# self.udp_server_socket.settimeout(0.5)

	# def start_receiving(self):
	# 	print(f"Server started on port {self.port}")
	# 	try:
	# 		while(True):
	# 			try:
	# 				bytes_address_pair = self.udp_server_socket.recvfrom(self.buffer_size)
	# 				message = bytes_address_pair[0]
					
	# 				self.handle_message(message)

	# 			except socket.timeout:
	# 				pass
	# 	except KeyboardInterrupt:
	# 		self.close()

	def connection_made(self, transport): 
		print(f"Connection established: {transport}")
		self.transport = transport

	# This is defined by asyncio, do not change the name,
	def datagram_received(self, data, addr): 
		print(f"Received message from {addr}: {data}")
