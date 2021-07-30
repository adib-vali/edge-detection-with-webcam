import cv2 

def nothing(x):
    return x
    
cap =cv2.VideoCapture(0,cv2.CAP_DSHOW)
cv2.namedWindow("edgedetection")
cv2.createTrackbar('threshold1','edgedetection',0,255,nothing)
cv2.createTrackbar('threshold2','edgedetection',0,255,nothing)

while(cap.isOpened()):
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    _,frame =cap.read()
    frame =cv2.flip(frame, 1)
    threshold1 =cv2.getTrackbarPos('threshold1','edgedetection')
    threshold2 =cv2.getTrackbarPos('threshold2','edgedetection')
    canny =cv2.Canny(frame,threshold1,threshold2)
    cv2.imshow('edgedetection2',canny)