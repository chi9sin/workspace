import cv2

# raspberry pi sony cam video cap "1"
# hp and orangepi sony cam video cap "0"
cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
