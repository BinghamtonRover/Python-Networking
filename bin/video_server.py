import cv2

from lib.network import ProtoServer

class VideoServer(ProtoServer):
	def on_message(self, wrapper, source): 
		cv2.imshow(wrapper.name, wrapper.data)

server = VideoServer()
try: server.start(8001)
finally: cv2.destroyAllWindows()

# _, frame = camera.read()
# data = frame.tobytes()
# buf = numpy.frombuffer(data, dtype="uint8")
# buf = buf.reshape(data.shape())
# while True: cv2.waitKey(1)
# cv2.imshow("frame", buf)
# cv2.destroyAllWindows()
