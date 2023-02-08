import socket
import cv2
import imutils
import time
import base64
import numpy as np

cv2.destroyAllWindows()

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 9004)
bufferSize          = 65536

camId = 1;


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


cap = cv2.VideoCapture(camId)


while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    #frameToSend = cv2.resize(frame, (10, 10), fx=0, fy=0, interpolation = cv2.INTER_CUBIC)
    #print(type(frameToSend))
    frame = cv2.resize(frame, (150, 150));
    encoded, buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])

    #buffer[200] = camId + 100
    message = base64.b64encode(buffer)
    print(type(buffer))
    print(buffer)
    #t = (camId).to_bytes(2, byteorder='big') + buffer
    #print((camId).to_bytes(2, byteorder='big').join(message))
    print("t: ")
    #print(t)
    print("done")
    print("single frame \n \n")
    # Display the resulting frame
    #cv2.imshow('Frame',message)
    #print("buffer data type:")
    #print(type(encoded))

    UDPClientSocket.sendto(buffer, serverAddressPort)
    messageDecode = base64.b64decode(message) #break loop
    #msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    #msg = "Message from Server {}".format(msgFromServer[0])
    #print(msg)
    # Press Q on keyboard to  exit
    key = cv2.waitKey(25) & 0xFF
    if key == ord('q'):
      UDPClientSocket.close()
      cv2.destroyAllWindows()
      break

  # Break the loop
  else:
    break
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
UDPClientSocket.close()


# Send to server using created UDP socket

