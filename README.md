
# Face Recognition Project

## What this project does

This project uses Python and the `face_recognition` library combined with OpenCV (`cv2`) to perform simple facial recognition. It compares a known reference image with a test image, identifies faces, draws rectangles around detected faces, and measures how similar the faces are.

---

## How the code works — Step by step

1. **Loading and Preparing Images**

   * The project loads two images: one reference image (`Alluu.jpeg`) and one test image (`test.jpeg`) using `face_recognition.load_image_file()`.
   * Each image is then converted from BGR to RGB color format using OpenCV’s `cv2.cvtColor()`. This is necessary because OpenCV loads images in BGR format but `face_recognition` expects RGB.

2. **Detecting Faces**

   * It detects face locations (coordinates of faces) in both the reference and test images using `face_recognition.face_locations()`.
   * If a face is found, the coordinates (top, right, bottom, left) are extracted.
   * Rectangles are drawn around the detected faces on both images using OpenCV’s `cv2.rectangle()` function, with a purple outline (color code `(255, 0, 255)`).

3. **Encoding Faces**

   * Facial features from the detected faces are extracted and encoded into a numeric representation (face embeddings) using `face_recognition.face_encodings()`.
   * These encodings represent unique facial features for comparison.

4. **Comparing Faces**

   * The reference image’s face encoding is compared against the test image’s face encoding using `face_recognition.compare_faces()`. This returns a boolean result indicating whether the faces match.
   * Additionally, a face distance score is calculated using `face_recognition.face_distance()`. This score measures similarity: smaller values mean the faces are more alike.

5. **Displaying Results**

   * The boolean result and face distance score are printed.
   * The test image displays the comparison result and similarity score as text on the image using `cv2.putText()`.
   * Both images with rectangles are displayed in windows using `cv2.imshow()`.
   * The program waits for a key press to close the display windows.

---

## What I learned building this project

* **Face detection and encoding concepts:** I learned how facial recognition works by detecting faces and encoding their features into vectors that computers can compare.
* **Image processing with OpenCV:** I gained practical experience loading images, converting color formats, drawing on images, and displaying them.
* **Handling face recognition with Python:** I used the `face_recognition` library to simplify complex tasks like face detection, encoding, and comparison.
* **Debugging and validating:** I handled cases where no face was detected to avoid errors, making the program more robust.
* **Working with coordinate systems:** Learned how face locations are represented and used to draw bounding boxes correctly.
* **Similarity metrics:** Understood how the face distance metric reflects similarity and how to interpret it.
* **Combining multiple libraries:** Coordinated OpenCV and `face_recognition` smoothly for a practical application.

---

This project gave me a hands-on understanding of the basics of facial recognition and image processing, which can be expanded into real-time webcam applications or more complex AI-based facial analysis.

---

Would you like me to also help draft a professional **README.md** file format for your GitHub?
