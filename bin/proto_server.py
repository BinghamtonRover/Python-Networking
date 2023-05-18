from src import ProtoSocket
# Examples in this repository cannot use generated.py
from src.generated.core_pb2 import Device

server = ProtoSocket(port=8001, device=Device.DASHBOARD)
try: server.listen()
except KeyboardInterrupt: pass
