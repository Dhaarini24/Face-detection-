# Face-detection-Running the Facial Recognition Software on a New Computer

This document explains how to set up and run the provided Python code for facial recognition on a new computer.

Prerequisites:

Python 3.x (https://www.python.org/downloads/)
OpenCV library (https://opencv.org/)
DeepFace library (https://github.com/serengil/deepface)
A webcam
Installation:

Install Python: If you don't have Python installed already, download and install the latest version of Python 3.x from https://www.python.org/downloads/.

Install OpenCV: Open a terminal or command prompt and run the following command to install OpenCV using pip (the Python package manager):


pip install opencv-python
Use code with caution.
content_copy
Install DeepFace: Install the DeepFace library using pip:


pip install deepface
Use code with caution.
content_copy
Preparing the Code:

Reference Images and Names: The code uses a list of reference images (reference_images) and corresponding names (reference_names) to identify faces. You'll need to replace these with your own images and names.
Images: Save images of the people you want to recognize in the same folder as the Python script. Rename the files to person1.jpg, person2.jpg, etc. (you can adjust the filenames as needed).
Names: Update the reference_names list in the code with the corresponding names for each image.
Running the Code:

Save the Script: Save the provided Python code as a file with a .py extension (e.g., facial_recognition.py).

Open Terminal: Open a terminal or command prompt and navigate to the directory where you saved the script.

Run the Script: In the terminal, run the following command to execute the script:


python facial_recognition.py
Use code with caution.
content_copy
Explanation of Changes:

The code now assumes your reference images are stored in the same folder as the script.
You'll need to modify the filenames in reference_images and names in reference_names to match your images.
Additional Notes:

This code performs facial recognition every 10 frames to improve performance. You can adjust this value in the if frame_count % 10 == 0 line.
The code displays the frame rate (FPS) and current time on the video window.
Press the 'q' key on your keyboard to quit the program.
Troubleshooting:

If you encounter errors during installation or execution, refer to the documentation for OpenCV and DeepFace for troubleshooting tips.
Ensure the file paths for your reference images are correct in the code.
By following these steps, you should be able to run the facial recognition code on a new computer with your own reference images and names.
