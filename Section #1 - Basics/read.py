#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/cat_large.jpg')
cv.imshow('Cats', img)

cv.waitKey(0) #* this is used 

# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4') #! (0/1/2) 0 for webcam, 1 for attach cam1

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()

## I learn a lot of things