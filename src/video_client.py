import cv2

from .proto_client import ProtoClient

from lib.network.generated.Protobuf.video_pb2 import *

class VideoClient(ProtoClient):
	def send_frame(self, name, frame, address=None, port=None):
		encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
		message = VideoFrame(
			name=name,
			frame=buffer.tobytes(),
		)
		self.send_message(message=message, address=address, port=port)
