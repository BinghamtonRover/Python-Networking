import cv2
import time
from multiprocessing import Process

from src import VideoClient, Device
from src.generated.Protobuf.video_pb2 import *

RESOLUTION = (400, 400)
cv2.setLogLevel(0)  # no logging from OpenCV

CAMERAS = [
	CameraName.ROVER_FRONT, 
	CameraName.ROVER_REAR,
	CameraName.ARM_BASE,
	CameraName.ARM_GRIPPER,
	CameraName.CAMERA_NAME_UNDEFINED
]

class CameraThread(Process):
	def __init__(self, name, id, client):
		print(f"Initializing camera {id}")
		self.camera_name = name
		self.id = id
		self.client = client
		super().__init__()

	def can_read(self): 
		camera = cv2.VideoCapture(self.id)

		if not camera.isOpened(): return False
		success, frame = camera.read()
		if not success: 
			print(f"Camera {self.id} is open but not responding")
		camera.release()
		return success

	def run(self):
		self.camera = cv2.VideoCapture(self.id)
		self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, RESOLUTION[0])
		self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, RESOLUTION[1])
		# self.camera.set(cv2.CAP_PROP_FOCUS, 250)
		self.camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)

		try:
			while True:
				success, frame = self.camera.read()
				if not success: 
					print(f"Could not read frame for camera {self.id}")
					return
				self.client.send_frame(self.camera_name, frame)
				time.sleep(1/24)
		except KeyboardInterrupt: pass

	def close(self): 
		print(f"Closing camera {self.id}")
		self.terminate()
		time.sleep(0.5)
		if hasattr(self, 'camera'):
			self.camera.release()
		super().close()

def get_threads(): 
	threads = []
	cams = 0
	for index in range(10):
		thread = CameraThread(CAMERAS[len(threads)], index, socket)
		if thread.can_read(): threads.append(thread)
	return threads


if __name__ == '__main__':
	print("Initializing...")
	socket = VideoClient(port=8002, destination=("127.0.0.1", 8001), device=Device.VIDEO)
	threads = get_threads()
	if not threads: quit("No workable camera detected")
	print(f"Using cameras {[thread.id for thread in threads]}")
	try: 
		for thread in threads: thread.start()
		for thread in threads: thread.join()
	except KeyboardInterrupt: pass
	finally: 
		for thread in threads: thread.close()
		socket.close()
