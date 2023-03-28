from src import ProtoSocket
from src.generated.Protobuf.core_pb2 import *

server = ProtoSocket(port=8001, device=Device.DASHBOARD)
server.listen()
