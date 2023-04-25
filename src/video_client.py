import cv2

from .proto_socket import ProtoSocket

from .generated.video_pb2 import *

class VideoClient(ProtoSocket):
	def __init__(self, compression, *args, **kwargs): 
		self.compression = compression
		super().__init__(*args, **kwargs)

	def send_frame(self, name, frame):
		encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, self.compression])
		message = VideoFrame(name=name, frame=buffer.tobytes())
		self.send_message(message)
