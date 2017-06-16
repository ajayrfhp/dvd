import cv2
import numpy as np
def MoG2(vid, min_thresh = 800, max_thresh = 10000):
    cap = cv2.VideoCapture(vid)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    fgbg = cv2.createBackgroundSubtractorMOG2()
    connectivity = 4
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        output = cv2.connectedComponentsWithStats(fgmask, connectivity, cv2.CV_32S)
        for i in range(output[0]):
            if output[2][i][4] >= min_thresh and output[2][i][4] <= max_thresh:
                cv2.rectangle(frame, (output[2][i][0],output[2][i][1]),(output[2][i][0] + output[2][i][2],output[2][i][1] + output[2][i][3]), (0, 255, 0), 2)
        cv2.imshow('detection',frame)
    cap.release()
    cv2.destroyAllWindows()
