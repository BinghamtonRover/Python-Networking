from lib.can_forwarder import CanForwarder 

server = CanForwarder(port=8001)
server.start()
