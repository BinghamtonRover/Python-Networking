import time

from src import ProtoSocket
from src.generated.Protobuf.drive_pb2 import DriveCommand
from src.generated.Protobuf.core_pb2 import *

client = ProtoSocket(port=8002, device=Device.DASHBOARD, destination=("127.0.0.1", 8001))

data1 = DriveCommand(throttle=0.5)
data2 = DriveCommand(left=1.0)
data3 = DriveCommand(right=0.5)

try: 
	while True: 
		client.send_message(data1)
		client.send_message(data2)
		client.send_message(data3)
		print("Sent a message")
		time.sleep(1)
except KeyboardInterrupt: pass
finally: 
	client.close()
