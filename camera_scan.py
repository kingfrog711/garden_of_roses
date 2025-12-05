import cv2
import sys

def main():
    source_index = 0
    cap = cv2.VideoCapture(source_index)

    if not cap.isOpened():
        print(f"Error: Could not open video source {source_index}.")
        sys.exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # ngeloading opencv method
    # 'alt2' is generally the most reliable of the default haar cascades
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml'
    )

    print("Camera is open")
    print("press 'q' or 'ESC' to close.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame. Exiting ...")
            break

        # buat mirror
        frame = cv2.flip(frame, 1)

        # 1. Pre-processing: Konversi ke grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 2. FEATURE: Lighting & Reflection Handling (UPDATED)
        # Ganti equalizeHist biasa ke CLAHE (Contrast Limited Adaptive Histogram Equalization).
        # Ini lebih pinter ngurusin refleksi/glare di kacamata daripada equalizeHist biasa.
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        gray = clahe.apply(gray)

        # 3. FEATURE: Noise Reduction (UPDATED)
        # Turunin blur ke (3, 3) dari (5, 5).
        # Blur kebanyakan bikin frame kacamata ilang, jadi kita kurangin dikit.
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        # 4. Detecting
        # scaleFactor: 1.2 (Speed up calculation to fix stutter/lag)
        # minNeighbors: 8 (Strict filter to stop "3 faces in 1" / multiple boxes)
        # minSize: (80, 80) (Adjusted to allow leaning back without detecting noise)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=8,
            minSize=(80, 80)
        )

        #  untuk muka
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #(x,y) top left   (x+w, y+h) bottom right    param 3 hijo  param 4 thickness
            
            # label
            cv2.putText(frame, "monyet", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # untuk display frame
        cv2.imshow('in a garden of roses', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("closed camera")

if __name__ == "__main__":
    main()