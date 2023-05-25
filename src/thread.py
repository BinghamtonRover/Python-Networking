import threading
import time

class ServerThread(threading.Thread):
	def __init__(self, server): 
		super().__init__()
		self.keep_running = True
		self.server = server
		self.daemon = True

	def startThreads(threads): 
		for thread in threads: thread.start()
		try:
			while True: time.sleep(100)
		except (KeyboardInterrupt, SystemExit): pass
		finally: 
			for thread in threads: 
				thread.close()
				thread.join()

	def run(self):
		while True:
			if not self.server.keep_alive: break
			try: self.server.listen()
			except KeyboardInterrupt: break
			except OSError as error: 
				if error.errno in [10054, 101, 10038, 9]: continue
				else: raise error

	def close(self): 
		self.server.keep_alive = False
		self.server.close()
