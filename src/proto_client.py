from .udp_client import UdpClient

from lib.network.generated.Protobuf.wrapper_pb2 import WrappedMessage

class ProtoClient(UdpClient):
	def send_message(self, message, address=None, port=None):
		wrapped_message = WrappedMessage(name=message.DESCRIPTOR.name, data=message.SerializeToString())
		self.send(data=wrapped_message.SerializeToString(), address=address, port=port)
