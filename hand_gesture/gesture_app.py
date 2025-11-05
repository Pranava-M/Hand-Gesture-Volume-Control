# gesture_app.py
from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import pyautogui

app = Flask(__name__)

# ---- Mediapipe setup ----
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
cap = cv2.VideoCapture(0)

gesture = "No Hand Detected"
muted = False


def detect_gesture(frame):
    global gesture, muted

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            tip_ids = [4, 8, 12, 16, 20]
            h, w, _ = frame.shape
            lm = [(int(l.x * w), int(l.y * h)) for l in hand_landmarks.landmark]

            fingers = []

            # Thumb detection (x comparison)
            if lm[tip_ids[0]][0] > lm[tip_ids[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers detection (y comparison)
            for id in range(1, 5):
                if lm[tip_ids[id]][1] < lm[tip_ids[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = fingers.count(1)

            # ---- Gesture Logic ----
            if total_fingers == 0:
                gesture = "👊 Fist (Volume Down)"
                pyautogui.press("volumedown")

            elif total_fingers == 5:
                gesture = "🖐️ Open Hand (Volume Up)"
                pyautogui.press("volumeup")

            elif fingers == [1, 0, 0, 0, 0]:  # Thumb up
                muted = not muted
                pyautogui.press("volumemute")
                gesture = "👍 Thumb Up (Mute/Unmute)"

            else:
                gesture = f"{total_fingers} Fingers"
    else:
        gesture = "No Hand Detected"

    return frame


def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        frame = detect_gesture(frame)
        ret, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/gesture')
def get_gesture():
    return jsonify({'gesture': gesture})


if __name__ == "__main__":
    app.run(debug=True)
