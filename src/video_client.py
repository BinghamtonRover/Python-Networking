import cv2

from .proto_socket import ProtoSocket

from .generated.Protobuf.video_pb2 import *

class VideoClient(ProtoSocket):
	def send_frame(self, name, frame):
		encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
		message = VideoFrame(name=name, frame=buffer.tobytes())
		self.send_message(message)
