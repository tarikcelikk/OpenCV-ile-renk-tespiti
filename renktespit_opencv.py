import cv2
import numpy as np
import time

camera = cv2.VideoCapture(0)
while True:
	belirli = 0
	ret, image = camera.read()
	ters = cv2.flip(image, 0)
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	lower = np.array([160, 125, 170])
	upper = np.array([195, 160, 255])
	mask = cv2.inRange(hsv, lower, upper)
	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	areas = [cv2.contourArea(c) for c in contours]
	print(len(contours))
	if len(contours) == 0:
		pass
	else:
		max_index = np.argmax(areas)
		cnt = contours[max_index]
		c = contours[0]
		area = cv2.contourArea(c)
		x, y, w, h = cv2.boundingRect(cnt)
		(x, y), radius = cv2.minEnclosingCircle(cnt)
		center = (int(x), int(y))
		radius = int(radius)
		solust = (int(x + (h) - w / 2), int(y + w / 2))
		sagalt = (int(x - (h) + w / 2), int(y - w / 2))
		cv2.circle(image, center, radius, (0, 255, 0), 2)
		cv2.rectangle(image, solust, sagalt, (0, 255, 0), 2)
		center2 = (325, 225)
		cv2.rectangle(image, (300, 200), (345, 245), (0, 255, 0), 2)
		cv2.line(image, center, center2, (0, 0, 255), 2)
		cv2.putText(image, "kirmizi cember", (int(x - 30), int(y - 40)),
		            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
		cv2.putText(
			image, "merkez", (center2[0] + 10, center2[1] + 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
		print(center)
		if int(x) > 0:
			print("kirmizi renk goruldu")
		if 300 <= int(x) | int(x) <= 345:
			if 200 <= int(y) | int(y) <= 245:
				cv2.putText(image, "Belirlendi", cv2.FONT_HERSHEY_PLAIN,
				            ((20, 90)), 2, (255, 0, 0), 2)
				belirli = 1
				print("merkezde")
			else:
				if int(y) >= 245:
					print("Down")
				if int(y) <= 200:
					print("Up")
		else:
			if int(x) >= 345:
				print("Right")
			if int(x) <= 300:
				print("Left")
	
	cv2.imshow("deneme", image)
	if cv2.waitKey(25) & 0xFF == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()
