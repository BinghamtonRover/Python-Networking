import time

from .udp_socket import UdpSocket
from .generated.wrapper_pb2 import *
from .generated.core_pb2 import *

heartbeat_interval = 1

class ProtoSocket(UdpSocket): 
	"""A UDP socket that handles incoming data in Protobuf format.

	Since Protobuf messages cannot self-identify, all messages are wrapped in a [WrappedMessage] class
	that contains the name of the underlying message and its binary payload, which can then be parsed
	by a subclass that overrides [on_message].

	This class is capable of understanding structured data, so it is also responsible for monitoring
	the connection to the dashboard. The dashboard will send three types of messages: 
	1) normal commands, to be handled by the specific server (for example, "enable a camera")
	2) handshake messages, which require some sort of confirmation response from the server.
	3) heartbeat messages, periodic handshakes to confirm that the servers are still connected.

	The [Connect] message serves as both the handshake and the heartbeat. A [Connect] message indicates
	who initiated the handshake and who it was intended for. The recipient is then to send another
	[Connect] message in response, but with the updated [sender] and [receiver] fields. The [Connect]
	message is sent periodically, and when the server goes [heartbeat_interval] seconds without one,
	it assumes the dashboard has disconnected and invokes [on_disconnect].

	While the rover's servers are configured with static IP addresses, the user's device (running the
	dashboard), is most likely configured with a dynamic IP address (ie, DHCP). To work around this,
	the [Connect] handshake allows the dashboard to inform the rover about its IP address, which it
	then saves and subsequently uses to send messages to the dashboard.
	"""
	def __init__(self, port, device, destination = None, buffer=1024):
		self.device = device
		self.received_heartbeat = False
		self.last_heartbeat_check = time.time()
		self.settings = None
		self.destination = destination
		super().__init__(port, destination, buffer=buffer)

	def is_connected(self): return self.destination is not None

	def send_message(self, message, destination=None):
		"""Wraps a message and sends it to [destination]."""
		wrapper = WrappedMessage(name=message.DESCRIPTOR.name, data=message.SerializeToString())
		self.send(wrapper.SerializeToString(), destination=destination)

	def on_loop(self):
		"""Check if [heartbeat_interval] seconds have passed since the last heartbeat message.

		If a dashboard had previously connected to this server but failed to send a heartbeat message,
		then this invokes [on_disconnect] to warn the server that the dashboard has disconnected.
		"""
		now = time.time()
		if (now - self.last_heartbeat_check < heartbeat_interval): return
		elif self.received_heartbeat: self.received_heartbeat = False
		elif self.is_connected(): 
			print("Heartbeat not received. Assuming Dashboard has disconnected")
			self.on_disconnect()
		self.last_heartbeat_check = time.time()
		
	def on_disconnect(self): 
		"""Invoked when the dashboard fails to send a heartbeat message

		Use this method to shut down anything that might be dangerous without a human operator. For 
		example, the subsystems server should stop the drive system so the rover doesn't drive away.
		"""
		self.send_message(Disconnect(sender=self.device))
		self.destination = None

	def on_data(self, data, source): 
		"""Handles incoming data in Protobuf format.

		1) If the message is a heartbeat message, respond to it.
		2) If the message is a settings message, handle it.
		3) Allow the implementation to handle other messages
		"""
		wrapper = WrappedMessage.FromString(data)
		if wrapper.name == Connect.DESCRIPTOR.name:  # (1)
			heartbeat = Connect.FromString(wrapper.data)
			self.on_heartbeat(heartbeat, source)
		elif wrapper.name == UpdateSetting.DESCRIPTOR.name:  # (2) 
			settings = UpdateSetting.FromString(wrapper.data)
			self.update_settings(settings)
		else:  # (3)
			self.on_message(wrapper)

	def on_heartbeat(self, heartbeat, source): 
		"""Decides what to do when a heartbeat message has been received

		1) If the heartbeat was meant for another device, log it and ignore it
		2) If it is our dashboard, respond to it
		3) If we are already connected to another dashboard, log it and ignore it
		4) If we are not connected to any dashboard, remember its IP and port, then respond
		"""
		if heartbeat.receiver != self.device:  # (1)
			print(f"Received a misaddressed heartbeat: {heartbeat}")
		elif self.is_connected():
			if self.destination == source: self.send_heartbeat()  # (2)
			else: print(f"This server is still connected to {self.destination}, but got a heartbeat from {source}")  # (3)
		else:  # (4)
			self.destination = source
			self.on_connect(source)
			self.send_heartbeat()

	def send_heartbeat(self): 
		"""Sends a heartbeat response to the dashboard."""
		response = Connect(sender=self.device, receiver=Device.DASHBOARD)
		self.send_message(response)
		self.received_heartbeat = True  # for the next [on_loop] check

	def update_settings(self, settings): 
		"""Handles the [UpdateSettings] handshake.

		To ensure critical settings are in fact updated, the server must respond with its settings after
		making the requested change. That way, the dashboard can perform sanity checks and warn the user.
		""" 
		self.send_message(settings)
		self.settings = settings
		if self.settings.status == RoverStatus.POWER_OFF: 
			print("Shutting down...")
			os.system("sudo shutdown now")

	def on_message(self, wrapper): 
		"""Invoked when a generic command has been received.

		The [wrapper] argument is a [WrappedMessage] message, which contains the name of the contained
		message and its binary payload, which can then be parsed in a server that overrides this method.
		"""
		print(f"Received a {wrapper.name} message: {wrapper.data}")

	def on_connect(self, source): 
		"""Called when a new dashboard has connected to this server."""
		print(f"Connected to a new dashboard at {source}")
