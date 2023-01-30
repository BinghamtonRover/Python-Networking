from .udp_server import UdpServer

from lib.network.generated.Protobuf.wrapper_pb2 import WrappedMessage

class ProtoServer(UdpServer):
	def on_data(self, data, source): 
		wrapper = WrappedMessage.FromString(data)
		self.on_message(wrapper, source)

	# Can override this in a subclass
	def on_message(self, wrapper, source): 
		print(f"Received a {wrapper.name} message from {source}")
