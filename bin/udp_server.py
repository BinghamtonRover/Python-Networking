from src import UdpSocket

server = UdpSocket(8001)
try: server.listen()
except KeyboardInterrupt: pass
