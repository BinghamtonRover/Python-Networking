"""
This code is a demo ONLY. Use the dashboard to display video.
"""

import cv2
import numpy
import socket

from lib.network import ProtoServer
from lib.network.generated.Protobuf.video_pb2 import *

class VideoServer(ProtoServer):
	# Make sure waitKey is called every once in a while
	def on_loop(self): cv2.waitKey(1)

	def close(self): 
		cv2.destroyAllWindows()
		super().close()

	def on_message(self, wrapper, source): 
		if wrapper.name == VideoFrame.DESCRIPTOR.name:
			data = VideoFrame.FromString(wrapper.data)
			array = numpy.frombuffer(data.frame, dtype="uint8")
			name = CameraName.Name(data.name)
			frame = cv2.imdecode(array, 1)
			cv2.imshow(name, frame)

server = VideoServer(8009)
try: server.start()
finally: server.close()
