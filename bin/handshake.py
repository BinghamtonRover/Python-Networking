from lib.network import UdpClient, UdpServer

class TestServer(UdpServer): 
	def on_data(self, data, source):
		print(f"receved <{data}> from {source}")
		print("Sending message *back*")
		client.send(data, address=source[0], port=source[1])

client = UdpClient()
server = TestServer(8001)

server.start()
print("Listening on port 8001")
