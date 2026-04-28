import cv2

img = cv2.imread('car.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    ratio = w / h

    if 2 < ratio < 6 and w > 100:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        break

cv2.imshow("Detected Plate", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
