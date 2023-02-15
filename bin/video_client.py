import time
import cv2
from lib.network import VideoClient
import threading
import subprocess
from lib.network.generated.Protobuf.video_pb2 import *


class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cam = cv2.VideoCapture(camID)
    #Set to lower resolution for shared USB bus
    cam.set(3,640)
    cam.set(4,280)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        rval, frame = cam.read()
        client.send_frame(camID, frame)
        print(f"Sent frame {camID}")
    cam.release()
    
    
#def init_camera(id):
#	camera = cv2.VideoCapture(id)
#	if not camera.isOpened(): 
#		print("[Error] Cannot open camera")
#		quit()
#	return camera

def read_frame(camera): 
	ret, frame = camera.read()
	if not ret: 
		print("[Error] Cannot receive frame")
		quit()
	return frame

if __name__ == '__main__':
	print("Initializing...")
	#camera = init_camera(0)
	#cam2 = init_camera(1)
	#cam3 = init_camera(2)
	thread1 = camThread("Camera 1", 0)
	thread2 = camThread("Camera 2", 2)
	client = VideoClient(address="localhost", port=8001)
	thread1.start()
	thread2.start()
	#while True: 
	#	frame1 = read_frame(camera)
	#	client.send_frame(CameraName.CAMERA_NAME_ROVER_FRONT, frame1)
		#frame2 = read_frame(cam2)
		#client.send_frame(CameraName.CAMERA_NAME_ROVER_REAR, frame2)
		#frame3 = read_frame(cam3)
		#client.send_frame(CameraName.CAMERA_NAME_ARM_BASE, frame3)
		#print("Sent frame")
	#	time.sleep(1/12)
	#camera.release()
