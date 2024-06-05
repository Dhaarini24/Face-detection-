import time
import datetime
from threading import Thread
import cv2 as cv
from deepface import DeepFace

# Load reference images and names
reference_images = [
    cv.imread("Dhaarini.jpg"),
    cv.imread("srinidhi.jpg"),
    cv.imread("Person3.jpg")
]

reference_names = [
    "Dhaarini K N Hathwar",
    "chiku ",
    "Person 3"
]

# Initialize video capture
capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize face detector
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

frame_count = 0

while capture.isOpened():

    ret, frame = capture.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    small_frame = cv.resize(gray, (0, 0), fx=0.5, fy=0.5)
    faces = face_cascade.detectMultiScale(small_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Adjust face coordinates to original frame size
    faces = [(x * 2, y * 2, w * 2, h * 2) for (x, y, w, h) in faces]

    # Perform face recognition every 10 frames
    if frame_count % 10 == 0:
        # List to store recognition results
        recognition_results = []

        # Verify each detected face
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            for idx, ref_img in enumerate(reference_images):
                try:
                    result = DeepFace.verify(face_img, ref_img, enforce_detection=False)
                    if result['verified']:
                        recognition_results.append((x, y, w, h, reference_names[idx]))
                        break
                except Exception as e:
                    continue

    # Draw results on frame
    for (x, y, w, h, name) in recognition_results:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        frame = cv.putText(frame, name, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display FPS
    fps = capture.get(cv.CAP_PROP_FPS)
    frame = cv.putText(frame, f"FPS: {fps:.2f}", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Display current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    frame = cv.putText(frame, current_time, (10, frame.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Resize and show the frame
    frame = cv.resize(frame, (920, 640))
    cv.imshow("video", frame)

    frame_count += 1

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()