from .udp_client import UdpClient

from lib.network.generated.Protobuf.wrapper_pb2 import WrappedMessage

class VideoClient(UdpClient):
	def send_frame(self, id, frame, address, port):
		wrapped_message = WrappedMessage(name=id, data=frame)
		self.send(address=address, port=port, data=wrapped_message.SerializeToString())
