import cv2
import numpy as np
import face_recognition
import os
import EntryReg
import mailgen
import Voice

list = ["xxx@gmail.com", "yyy@gmail.com"] # reciever's mail.

path = 'Valid'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def invalmail(list):
    try:
        msg = "Burglary Attempt!"
        for i in range(len(list)):
            mailgen.SendEmail(list[i], msg)
        print("The e-mail has been sent successfully!")
    except Exception as e:
        print(e)
        print("Sorry, unable to send the e-mail.")


print("Encoding....")
encodeListKnown = findEncodings(images)
print('Encoding Complete')
Voice.speak("Please look into the camera")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
        #     # print(name)
        #     y1, x2, y2, x1 = faceLoc
        #     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        #     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        #     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        #     cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            EntryReg.EntryLog(name)

    if True in matches:
        Voice.greeting()
        Voice.speak(name)
        Voice.speak("Give today's password: ")
        pas = Voice.accept().lower()
        if pas == Voice.set_pas():
            Voice.speak("Valid!, access granted!")
            break
        else:
            invalmail(list)
            break


    elif True not in matches:
        invalmail(list)
        break