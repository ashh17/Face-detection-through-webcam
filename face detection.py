import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    faces = face.detectMultiScale(frame, 1.1, 9)

    for x, y, w, h in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.putText(frame, 'Person', (x, y), cv2.FONT_ITALIC, 2, (0, 0, 0))
        cv2.imshow('Face Detected', frame)
    if cv2.waitKey(1) == 13:  # ASCII for enter
        break

cap.release()  # destructor
cv2.destroyAllWindows()
