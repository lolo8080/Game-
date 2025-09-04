import cv2
import numpy as np

def preprocess_frame(frame):
    """Convert the frame to HSV and apply a blue color mask."""
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define HSV range for blue
    lower_blue = np.array([100, 150, 50], dtype=np.uint8)
    upper_blue = np.array([140, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    return mask

def count_fingers(frame, contour):
    """Count the number of fingers raised."""
    hull = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull)

    if defects is None:
        return 0

    # Count defects based on angle
    finger_count = 0
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])

        # Measure angles to determine if it's a finger
        a = np.linalg.norm(np.array(start) - np.array(far))
        b = np.linalg.norm(np.array(end) - np.array(far))
        c = np.linalg.norm(np.array(start) - np.array(end))
        angle = np.degrees(np.arccos((a**2 + b**2 - c**2) / (2 * a * b)))

        if angle < 90:  # Finger detected
            finger_count += 1
            cv2.circle(frame, far, 5, (0, 0, 255), -1)

    return finger_count

# Main program
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    mask = preprocess_frame(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour, assuming it's the hand
        largest_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)

        # Count fingers
        fingers = count_fingers(frame, largest_contour)
        cv2.putText(frame, f"Fingers: {fingers}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Hand Tracking", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
