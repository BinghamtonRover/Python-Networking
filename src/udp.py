import asyncio

from lib.network.generated import WrappedMessage, Connect

class UdpSocket:
  async def serve_forever(self):
    try:
      await asyncio.Event().wait()
    finally:
      return self.close()
      return

  async def create(port, device, destination = None):
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
      lambda: UdpSocket(port, device, destination), local_addr=("127.0.0.1", port)
    )
    return protocol

  def __init__(self, port, device, destination = None):
    print("Creating object")
    self.port = port
    self.device = device
    self.destination = destination
    self.handlers = {}

  def connection_made(self, transport):
    print(f"Listening on port {self.port}")
    self.transport = transport

  def connection_lost(self, *args):
    print(f"Socket on port {self.port} has closed")

  def datagram_received(self, data, source):
    wrapper = WrappedMessage()
    wrapper.ParseFromString(data)
    name = wrapper.name
    if name == "Connect":
      if not self.destination:
        self.destination = source
      heartbeat = Connect()
      heartbeat.ParseFromString(wrapper.data)
      response = Connect(sender=heartbeat.receiver, receiver=heartbeat.sender)
      self.send_message(heartbeat)
    elif wrapper.name not in self.handlers:
      print(f"Socket {self.port} received a {wrapper.name} message and doesn't have a handler for it")
      return
    else:
      handler = self.handlers[wrapper.name]
      handler(wrapper.data)

  def close(self):
    print(f"Closing socket on port {self.port}")
    self.transport.close()

  def listen(self, name, constructor, callback):
    def _handler(data):
      message = constructor()
      message.ParseFromString(data)
      callback(message)
    self.handlers[name] = _handler

  def send_bytes(self, data, destination = None):
    dest = destination or self.destination
    if not dest: return
    self.transport.sendto(data, dest)

  def send_wrapper(self, wrapper, destination = None):
    self.send_bytes(wrapper.SerializeToString(), destination=destination)

  def send_message(self, message, destination = None):
    name = message.DESCRIPTOR.name
    wrapper = WrappedMessage(data=message.SerializeToString(), name=name)
    self.send_wrapper(wrapper)
