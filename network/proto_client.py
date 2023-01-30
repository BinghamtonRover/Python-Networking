from .udp_client import UdpClient

from generated.wrapper_pb2 import WrappedMessage

class ProtoClient(UdpClient):
	def send_message(self, name, message, address, port):
		wrapped_message = WrappedMessage(name=name, data=message.SerializeToString())
		self.send(address=address, port=port, data=wrapped_message.SerializeToString())
