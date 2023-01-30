import time

from lib.network import ProtoClient
from lib.network.generated.Protobuf.drive_pb2 import DriveCommand

client = ProtoClient()

data = DriveCommand(throttle=0.5, left=1.0, right=0.0)

try: 
	while True: 
		client.send_message("DriveCommand", data, "localhost", 8001)
		print("Sent a message")
		time.sleep(1)
except KeyboardInterrupt: pass
finally: 
	client.close()
