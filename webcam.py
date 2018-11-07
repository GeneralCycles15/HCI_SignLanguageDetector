# References
# ----------
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html
# https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv/34588758

import cv2

# Create namedWindow objects
cv2.namedWindow("Current_Stream", cv2.WINDOW_NORMAL)
cv2.namedWindow("Last_Capture", cv2.WINDOW_NORMAL)

# Frame settings
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

# Initialize counter for captured images
img_counter = 0

while True:
    # Read and display initial frame from webcam
    ret, frame = cam.read()
    cv2.imshow("Current_Stream", frame)

    # Display placeholder image on load
    if img_counter == 0:
        placeholder = cv2.imread("images/placeholder.jpg", 0)
        cv2.imshow("Last_Capture", placeholder)

    # Wait for keystroke
    k = cv2.waitKey(1)

    if not ret:
        break

    # Actions for when SPACE is pressed
    if k%256 == 32:
        # Concatenate image path/filename
        img_name = "images/opencv_frame_{}.png".format(img_counter)
        # Save captured frame
        cv2.imwrite(img_name, frame)
        print("The file {} was created!".format(img_name))
        # Increment counter to keep track of captured frames
        img_counter += 1
        # Display last frame capture
        cv2.imshow("Last_Capture", frame)

    # Actions for when ESC is pressed
    elif k%256 == 27:
        print("ESC key entered, now closing application!")
        break

cam.release()
cv2.destroyAllWindows()