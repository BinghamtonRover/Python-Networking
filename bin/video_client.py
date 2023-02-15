import time
import cv2
from lib.network import VideoClient
from lib.network.generated.Protobuf.video_pb2 import *

def init_camera(id):
	camera = cv2.VideoCapture(id)
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
	print("Initializing...")
	camera = init_camera(0)
	cam2 = init_camera(1)
	cam3 = init_camera(2)
	client = VideoClient(address="localhost", port=8001)
	while True: 
		frame1 = read_frame(camera)
		client.send_frame(CameraName.CAMERA_NAME_ROVER_FRONT, frame1)
		frame2 = read_frame(cam2)
		client.send_frame(CameraName.CAMERA_NAME_ROVER_REAR, frame2)
		frame3 = read_frame(cam3)
		client.send_frame(CameraName.CAMERA_NAME_ARM_BASE, frame3)
		print("Sent frame")
		time.sleep(1/24)
	camera.release()
