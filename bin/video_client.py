import cv2
import threading
import time

from lib.network import VideoClient
from lib.network.generated.Protobuf.video_pb2 import *

RESOLUTION = (640, 280)
DELAY = 1/24
cv2.setLogLevel(0)  # no logging from OpenCV

class CameraThread(threading.Thread):
	def __init__(self, name, id, client):
		super().__init__()
		self.name = name
		self.id = id
		self.camera = cv2.VideoCapture(id)
		self.client = client
		# self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, RESOLUTION[0])
		# self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, RESOLUTION[1])

	def can_read(self): 
		return self.camera.isOpened()

	def run(self):
		print("Starting loop")
		while True:
			success, frame = self.camera.read()
			if not success: 
				print(f"Could not read frame for camera {self.id}")
				return
			self.client.send_frame(self.id, frame)
			print(f"Sent frame for camera {self.id}")
			time.sleep(DELAY)

	def close(self): 
		print(f"Closing camera {self.id}")
		self.camera.release()


def get_threads(): 
	threads = []
	client = VideoClient(address="192.168.1.10", port=8009)
	for index in range(8):  # 8 is a reasonable amount of cameras
		thread = CameraThread(f"Camera {index}", index, client)
		if thread.can_read(): threads.append(thread)
	return threads

if __name__ == '__main__':
	print("Initializing...")
	threads = get_threads()
	if not threads: quit("No workable camera detected")
	print(f"Using cameras {[thread.id for thread in threads]}")
	try: 
		for thread in threads: thread.start()
		for thread in threads: thread.join()
	finally: 
		for thread in threads: thread.close()
