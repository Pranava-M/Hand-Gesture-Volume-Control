#  Hand Gesture Volume Control

Control your **system volume** using **hand gestures** through your **webcam** — no keyboard or mouse required!
This project uses **Python**, **MediaPipe**, **Flask**, and **PyAutoGUI** to recognize gestures in real time and trigger volume control actions.

---

## 🎯 Features

* 🖐️ **Open Hand → Increases volume**
* 👊 **Fist → Decreases volume**
* 👍 **Thumb Up → Mutes/Unmutes**
* 🔁 Live webcam feed directly in browser
* 💻 Works on all laptops and Windows PCs (no driver issues)
* ⚡ Real-time gesture recognition with smooth detection

---

## 🧰 Technologies Used

| Component     | Purpose                                        |
| ------------- | ---------------------------------------------- |
| **Python**    | Main programming language                      |
| **OpenCV**    | Access and process webcam video feed           |
| **MediaPipe** | Detect hand landmarks and gestures             |
| **Flask**     | Create a local web interface for visualization |
| **PyAutoGUI** | Simulate real system volume key presses        |

---

## 📦 Installation & Setup

### 1️⃣ Clone or Download the Repository

```bash
git clone https://github.com/Pranava-M/hand-gesture-volume-control.git
cd hand-gesture-volume-control
```

### 2️⃣ Install Required Packages

Run these commands in your terminal (preferably inside a virtual environment):

```bash
pip install opencv-python mediapipe flask pyautogui
```

### 3️⃣ Folder Structure

```
hand_gesture_volume_control/
├── gesture_app.py
└── templates/
    └── index.html
```

> ⚠️ Make sure the `index.html` file is inside a folder named `templates` (Flask requires this).

---

## ▶️ How to Run

1. Run the Python file:

   ```bash
   python gesture_app.py
   ```

2. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

3. Allow camera access when prompted.

4. Show your hand gestures in front of the camera to control your volume!

---

## 🧠 How It Works

1. **Camera Feed**
   The webcam captures live video frames using OpenCV.

2. **Hand Detection (MediaPipe)**
   MediaPipe detects 21 hand landmarks in each frame — tips, joints, and wrist points.

3. **Gesture Recognition**
   Using landmark positions:

   * The program checks if each finger is raised or folded.
   * The number and pattern of raised fingers determine which gesture is shown.

4. **Action Trigger (PyAutoGUI)**
   Each gesture sends a simulated keyboard command:

   * `volumeup` → Increase volume
   * `volumedown` → Decrease volume
   * `volumemute` → Toggle mute/unmute

5. **Web Display (Flask)**
   Flask hosts a simple webpage that:

   * Shows the live camera feed.
   * Displays the detected gesture text dynamically.

---

## ✋ Best Hand Gestures

| Gesture               | Action                              | Description                       |
| --------------------- | ----------------------------------- | --------------------------------- |
| 🖐️ **Open Hand**     | Volume Up                           | Raise all five fingers clearly    |
| 👊 **Fist**           | Volume Down                         | Fold all fingers into a fist      |
| 👍 **Thumb Up**       | Mute / Unmute                       | Raise only your thumb             |
| ✌️ **Two Fingers**    | Detected as "2 Fingers" (no action) | Used just for testing recognition |
| 🤚 **Other gestures** | Detected count only                 | No volume change triggered        |

> 💡 Ensure your hand is **fully visible** and **well-lit** for accurate detection.

---

## 🧪 Troubleshooting

| Problem               | Possible Fix                                                          |
| --------------------- | --------------------------------------------------------------------- |
| ❌ “No Hand Detected”  | Move your hand closer or adjust lighting                              |
| ❌ Camera not opening  | Close other apps using the webcam                                     |
| ❌ Volume not changing | Run Python as administrator (required for key events on some systems) |
| ❌ Laggy video         | Lower resolution or close background processes                        |

---

## 📸 Example Output

**Web Interface Preview:**

```
✋ Hand Gesture Volume Control
Show your hand to the camera!

Detected Gesture: 🖐️ Open Hand (Volume Up)
```

---

## 🧩 Future Enhancements

* 🎵 Control media playback (play/pause/next)
* 🧠 Add AI-based gesture training for custom actions
* 💡 Show real-time on-screen volume bar
* 📱 Add mobile compatibility for gesture streaming

---

## 🪪 Author

**👨‍💻 Pranav Machireddy**
A simple yet futuristic project exploring computer vision and natural gesture interfaces.

---

## 🧾 License

This project is open-source under the **MIT License** – free to use, modify, and share.

---
