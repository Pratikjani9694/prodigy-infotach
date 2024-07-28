import cv2
from pyzbar.pyzbar import decode
import time
import webbrowser

# Initialize the camera
cam = cv2.VideoCapture(0)

# Set the camera resolution
cam.set(3, 640)
cam.set(4, 480)

# Flag to control the loop
camera = True

while camera == True:
    # Read a frame from the camera
    success, frame = cam.read()

    # Decode the QR code in the frame
    for i in decode(frame):
        # Extract the QR code data
        qr_data = i.data.decode('utf-8')

        # Print the QR code type and data
        print(f"QR Code Type: {i.type}")
        print(f"QR Code Data: {qr_data}")

        # Check if the QR code data is a URL
        if qr_data.startswith("http"):
            # Open the URL in the default browser
            webbrowser.open(qr_data)
            print("Opening URL...")
        else:
            # Display the QR code data on the screen
            cv2.putText(frame, qr_data, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Display the frame with the QR code data
        cv2.imshow("QR Code Scanner", frame)

        # Wait for a key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera = False

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
