import time

from .udp_server import UdpServer

from lib.network.generated.Protobuf.wrapper_pb2 import WrappedMessage
from lib.network.generated.Protobuf.core_pb2 import *
from lib.network.generated.Protobuf.autonomy_pb2 import *


heartbeat_interval = 1

class ProtoServer(UdpServer):
        def __init__(self, port, device, client = None):
            self.client = client
            self.device = device
            self.received_handshake = False
            self.last_handshake_check = time.time()
            self.status = RoverSatatus.MANUAL
            super().__init__(port)

        def is_connected(self): return self.client.address is not None

        #Overriden from super class UdpServer -- do not rename
        def on_loop(self):
		now = time.time()
		if (now - self.last_handshake_check < heartbeat_interval): return
		# detect dropped connections
		if not self.received_handshake: 
			if self.is_connected(): self.on_disconnect()
		else: self.received_handshake = False
		self.last_handshake_check = time.time()        
    
        def on_disconnect(self): 
		print("Handshake not received. Assuming Dashboard has disconnected")
		self.client.address = None
		#PATCH NOTE! - removed line 'self.can.stop_driving()'
		'''In the can specific version of heartbeat enabled ProtoServer the above line was included.
                This suggests that each device should have their own sequence of shutdown steps
                '''
		self.device_shutdown()

	def device_shutdown(self):
            pass

        #Overriden from super class UdpServer -- do not rename
	def on_data(self, data, source): 
		wrapper = WrappedMessage.FromString(data)
		self.on_message(wrapper, source)
		
        #respond to heartbeats
	def send_heartbeat(self): 
		response = Connect(sender=self.device, receiver=Device.DASHBOARD)
		self.client.send_message(response)
		self.received_handshake = True

        
	def on_handshake(self, handshake, source): 
		"""Decides what to do when a heartbeat message has been received
		- If the heartbeat was meant for another device, log it and ignore it
		- If we are not connected to any dashboard, connect to it and respond
		- If we are already connected to another dashboard, ignore it
		- If it is our dashboard, respond to it
		"""
		if handshake.receiver != self.device:  # not meant for us
			print(f"Received a misaddressed handshake intended for {handshake.receiever}, sent by {handshake.sender}")
		elif not self.is_connected():  # new dashboard, let's connect
			self.client.address = source[0]
			self.client.port = source[1]
			self.send_heartbeat()
		elif self.client.address != source[0]:
			# We're already connected to a dashboard, and a new one tried connecting -- ignore
			return
		else:  # heartbeat from the already-connected dashboard -- respond with a heartbeat back
			self.send_heartbeat()

        #detect regular messages and handle then however we want
	# This function comes from ProtoServer -- do not rename!
        def on_message(self, wrapper, source): 
		if wrapper.name == Connect.DESCRIPTOR.name: 
			handshake = Connect.FromString(wrapper.data)
			self.on_handshake(handshake, source)
		elif wrapper.name == UpdateSetting.DESCRIPTOR.name: 
			settings = UpdateSetting.FromString(wrapper.data)
			print(f"Received a request to update status={settings.status}")
			self.client.send_message(settings)  # must send in return
			self.status = settings.status
			if settings.status == RoverStatus.AUTONOMOUS:
				self.client.send_message(AutonomyCommand(enable=True), address="192.168.1.30", port=8006)
			elif settings.status == RoverStatus.MANUAL:
				self.client.send_message(AutonomyCommand(enable=False), address="192.168.1.30", port=8006)

		else: 
			# print(f"Received UDP message {wrapper.name}")
			#PATCH NOTE! removed line - 'self.can.send(id, wrapper.data)'
			'''In the can specific version of heartbeat enabled ProtoServer the above line was included.
                        This suggests that each device should have their own message handling method.
                        '''
			self.handle_message(wrapper.data)

        def handle_message(self):
                pass
