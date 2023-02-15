"""
This code is a demo ONLY. Use the dashboard to display video.
"""

import cv2
import numpy
import socket

from lib.network import ProtoServer
from lib.network.generated.Protobuf.video_pb2 import *

class VideoServer(ProtoServer):
	# Overriding to add cv2.waitKey
	def start(self):
		print(f"Server started on port {self.port}")
		try:
			while(True):
				try: message, source = self.socket.recvfrom(50000)
				except socket.timeout: continue
				else: self.on_data(message, source)
				cv2.waitKey(1)
		except KeyboardInterrupt: self.close()

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

server = VideoServer(8001)
try: server.start()
finally: server.close()
