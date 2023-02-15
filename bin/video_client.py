import cv2
import time
from multiprocessing import Process

from lib.network import VideoClient
from lib.network.generated.Protobuf.video_pb2 import *

RESOLUTION = (450, 450)
cv2.setLogLevel(0)  # no logging from OpenCV

class CameraThread(Process):
	def __init__(self, name, id, client):
		print(f"Initializing camera {id}")
		self.name = name
		self.id = id
		self.camera = cv2.VideoCapture(id)
		self.client = client
		super().__init__()
		self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, RESOLUTION[0])
		self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, RESOLUTION[1])

	def can_read(self): 
		return self.camera.isOpened()

	def run(self):
		try:
			while True:
				success, frame = self.camera.read()
				if not success: 
					print(f"Could not read frame for camera {self.id}")
					return
				self.client.send_frame(self.id, frame)
		except KeyboardInterrupt: pass

	def close(self): 
		print(f"Closing camera {self.id}")
		self.terminate()
		time.sleep(0.5)
		self.camera.release()
		super().close()

def get_threads(): 
	threads = []
	client = VideoClient(address="192.168.1.10", port=8009)
	for index in [0, 2, 4, 6]:
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
	except KeyboardInterrupt: pass
	finally: 
		for thread in threads: thread.close()
