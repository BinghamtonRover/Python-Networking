"""
This code is a demo ONLY. Use the dashboard to display video.
"""

import cv2
import numpy
import socket

from src import ProtoSocket
from src.generated.Protobuf.video_pb2 import *
from src.generated.Protobuf.core_pb2 import *

class VideoServer(ProtoSocket):
	def __init__(self, port): 
		super().__init__(port, device=Device.DASHBOARD, buffer=65_527)

	# Make sure waitKey is called every once in a while
	def on_loop(self): cv2.waitKey(1)

	# Override of ProtoSocket.close()
	def close(self): 
		cv2.destroyAllWindows()
		super().close()

	# Override of ProtoSocket.on_message
	def on_message(self, wrapper): 
		if wrapper.name == VideoFrame.DESCRIPTOR.name:
			data = VideoFrame.FromString(wrapper.data)
			array = numpy.frombuffer(data.frame, dtype="uint8")
			name = CameraName.Name(data.name)
			frame = cv2.imdecode(array, 1)
			cv2.imshow(name, frame)

server = VideoServer(8001)
server.listen()
