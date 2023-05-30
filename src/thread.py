import threading
import time

class ServerThread(threading.Thread):
	def startThreads(threads): 
		for thread in threads: thread.start()
		try:
			while True: time.sleep(100)
		except (KeyboardInterrupt, SystemExit): pass
		finally: 
			for thread in threads: 
				thread.close()
				thread.join()
