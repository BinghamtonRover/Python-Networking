import time
import cv2
from lib.network import VideoClient

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
	client = VideoClient(address="localhost", port=8001)
	while True: 
		frame = read_frame(camera)
		client.send_frame("Video demo", frame)
		print("Sent frame")
		time.sleep(1/24)
	camera.release()
