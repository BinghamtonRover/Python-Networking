from .udp_server import UdpServer
from generated.wrapper_pb2 import WrappedMessage

class ProtoServer(UdpServer):
	def on_data(self, data, source): 
		wrapper = WrappedMessage.FromString(data)
		print(f"Received a {wrapper.name} message from {source}")
