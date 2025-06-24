import cv2
from pyzbar.pyzbar import decode
import re

def is_url(text):
    return re.match(r'^https?://', text)

def main():
    cap = cv2.VideoCapture(0)
    found_links = set()

    print("'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        codes = decode(frame)
        for code in codes:
            data = code.data.decode('utf-8')
            if is_url(data) and data not in found_links:
                print(f"Found link: {data}")
                found_links.add(data)
                with open("qr_links.txt", "a") as f:
                    f.write(data + "\n")

        # Show camera feed
        cv2.imshow("QR Code Scanner", frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
