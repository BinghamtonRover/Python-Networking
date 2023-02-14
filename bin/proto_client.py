import time

from lib.network import ProtoClient
from lib.network.generated.Protobuf.drive_pb2 import DriveCommand

client = ProtoClient(address="localhost", port=8001)

data1 = DriveCommand(throttle=0.5)
data2 = DriveCommand(left=1.0)
data3 = DriveCommand(right=0.5)

try: 
	while True: 
		client.send_message("DriveCommand", data1)
		client.send_message("DriveCommand", data2)
		client.send_message("DriveCommand", data3)
		print("Sent a message")
		time.sleep(1)
except KeyboardInterrupt: pass
finally: 
	client.close()
