import time
from ultralytics import YOLO
import cv2
from util import read_license_plate


license_plate_detector = YOLO('./models/license_plate.pt')

cap = cv2.VideoCapture('./sample.mp4')

frame_nmr = -1
ret = True

width  = cap.get(3)
height = cap.get(4)

ret, frame = cap.read()
cv2.imshow('frame', frame)

while ret:

    frame_nmr += 5
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr-1)
    ret, frame = cap.read()

    padding_left = round(width/4) #
    padding_top = 1*round(height/5) # Change the siz of the scanning area here
    padding_right = round(width/4) #
    padding_bottom = 1*round(height/5) #

    if ret:

        focus_crop = frame[int(padding_top):int(height-padding_bottom), int(padding_left):int(width-padding_right), :]

        if focus_crop.shape[0] > 0 and focus_crop.shape[1] > 0:

            detections = license_plate_detector(focus_crop)[0]

            for detection in detections.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = detection

                cv2.rectangle(frame, (int(x1 + padding_left - 10), int(y1 + padding_top)), (int(x2 + padding_left + 10), int(y2 + padding_top)), (0, 255, 0), 3)

                license_plate_crop = frame[int(y1 + padding_top - 10):int(y2 + padding_top + 10), int(x1 + padding_left - 10):int(x2 + padding_left + 10), :]

                license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
                _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

                license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

                if license_plate_text is not None:

                    plate = {'license_plate': {'bbox': [x1, y1, x2, y2],
                                                'text': license_plate_text,
                                                'bbox_score': score,
                                                'text_score': license_plate_text_score}}

                    plate_loc = plate['license_plate']['bbox']
                    x1, y1, x2, y2 = plate_loc

                    x1 += padding_left
                    y1 += padding_top
                    x2 += padding_left
                    y2 += padding_top

                    cv2.rectangle(frame, (int(x1), int(y1 - 60)), (int(x2), int(y1 - 10)), (255, 255, 255), -1)
                    cv2.putText(img=frame, text=license_plate_text, org=(int(x1), int(y1) - 30),
                                fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 0), thickness=3)
                    
    cv2.rectangle(frame, (int(padding_left), int(padding_top)), (int(width-padding_right), int(height-padding_bottom)), (255, 0, 0), 3)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
