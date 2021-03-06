import numpy as np
import cv2

# Get video capture object for camera 0
cap = cv2.VideoCapture(0)

# Create named window for diaply
cv2.namedWindow('preview')

# Loop until 'q' pressed
while(True):
    # Read most recent frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Computer Vision Code
    # --------------------
    thresh = 128
    ret, binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    # --------------------

    # Display the resulting frame
    cv2.imshow('preview', binary)

    # Wait for a keypress, and quit if 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the caputre
cap.release()

# Destroy display window
cv2.destroyAllWindows()