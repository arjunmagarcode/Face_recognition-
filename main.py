import cv2
import numpy as np
import face_recognition 
# this is the step 1 
imgAllu = face_recognition.load_image_file('images/Alluu.jpeg')
imgAllu = cv2.cvtColor(imgAllu, cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('images/test.jpeg')
imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)

# step 2 finding the images in the picture and then finding their importants as well.
# for the image
faceLocs = face_recognition.face_locations(imgAllu)

if faceLocs:
    faceLoc = faceLocs[0]  # Get the first face location
    encodeAlluu = face_recognition.face_encodings(imgAllu)[0]  # Safe only if one face
    top, right, bottom, left = faceLoc

    cv2.rectangle(imgAllu, (left, top), (right, bottom), (255, 0, 255), 2)
else:
    print("No face found in the image.")

# for the test 
faceLocsTest = face_recognition.face_locations(imgtest)

if faceLocsTest:
    faceLoc1 = faceLocsTest[0]  # Get the first face location
    encodeTest = face_recognition.face_encodings(imgtest)[0]  
    top, right, bottom, left = faceLoc1

    cv2.rectangle(imgtest, (left, top), (right, bottom), (255, 0, 255), 2)
else:
    print("No face found in the image.")
    
    
    
#  third step is comparing faces and finding the distance betweeen them.

results= face_recognition.compare_faces([encodeAlluu],encodeTest )



#  face distance is for how much similar they are
facedis = face_recognition.face_distance ([encodeAlluu], encodeTest)
print(results,facedis)


cv2.putText(imgtest, f'{results} {round(facedis[0],2)}', (50, 50 ), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 2)
cv2.imshow('Allu Arjun', imgAllu)
cv2.imshow('Allu Test', imgtest)
cv2.waitKey(0)
