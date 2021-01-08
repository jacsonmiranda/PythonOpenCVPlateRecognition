import cv2
out = "/home/jacson/Desktop/PythonOpenCVPlateRecognition/output/"

img = cv2.imread(out+"carro3.jpg")
cv2.imshow('img', img)


cv2.waitkey(0)
cv2.destroyAllWindows()