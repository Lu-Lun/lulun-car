import cv2

cap = cv2.VideoCapture(1)    # VideoCapture()中参数是1，表示打开外接usb摄像头
cv2.namedWindow('camera')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('camera', frame)
        cv2.waitKey(1)
