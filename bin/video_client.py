import cv2
from lib.network import VideoClient, ProtoServer

class VideoServer(ProtoServer):
	def on_message(self, wrapper, source): 
		cv2.imshow(wrapper.data)

def init_camera():
	camera = cv2.VideoCapture(1)
	if not camera.isOpened(): 
		print("[Error] Cannot open camera")
		quit()
	return camera

def read_frame(camera): 
	ret, frame = camera.read()
	if not ret: 
		print("[Error] Cannot receive frame")
		quit()
	return frame

if __name__ == '__main__':
	camera = init_camera()
	while True: 
		frame = read_frame(camera)
		cv2.imshow(camera)
