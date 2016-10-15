# Sign-Language-Translator-using-Python-and-OpenCV

Mini-Project (7th Semester) Submission

Sign language Translator, which uses the WebCam to capture hand symbols and gestures, and display the alphabet according to that reading.

Coded in Python and uses OpenCV (Open Source Computer Vision) Library for it's vast array of functions related to image capturing and image processing.

Main Files in the Repository
datacreate.py : Put hand in the Region of Interest (ROI), make a symbol and hit enter to click images (which will be stored in the datasets folder)
match.py :  Put hand in the Region of Interest (ROI), make the same symbol. Compiler will compare the real-time contour readings from that in the datasets and return the Text/Alphabet associated with that symbol.
