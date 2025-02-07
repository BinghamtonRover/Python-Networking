import threading
import time
from typing import List

def runThreads(threads: List[threading.Thread]):
  for thread in threads:
    thread.start()
  try:
    while True:
      time.sleep(100)
  except (KeyboardInterrupt, SystemExit):
    pass
  finally:
    for thread in threads:
      thread.close()
      thread.join()
