import cv2,time
cam=cv2.VideoCapture(0)

try:
	cont = 0
	while True:
		cont = cont + 1
		ret,frame=cam.read()
		img_name="%s.png" %(cont) 
		cv2.imwrite(img_name,frame)
		print "FOTO CAPTURADA"
		time.sleep(10)

except KeyboardInterrupt:
	cam.release()
	print "DETENIDO"
