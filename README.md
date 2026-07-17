# 🛡️ VisionGuard AI

> An AI-powered smart surveillance system that detects and recognizes faces in real time, manages unknown-person sessions, captures evidence, sends instant Telegram alerts, and interacts with external hardware using ESP8266.

---

## 📖 Overview

VisionGuard AI is a modular computer vision and security system built with Python and OpenCV. It combines real-time face recognition, event-driven architecture, and hardware integration to create an intelligent surveillance solution.

Unlike traditional face recognition projects, VisionGuard AI introduces the concept of **session-based monitoring**. Instead of generating repeated alerts for every video frame, the system groups continuous detections of the same unknown person into a single session, preventing notification spam while maintaining accurate event tracking.

When an unknown person is detected, VisionGuard AI automatically:

- Starts a new security session
- Captures an evidence image
- Logs the event
- Sends a Telegram alert with the captured image
- Activates an external ESP8266 device (LED)

When the unknown person leaves the camera view for the configured timeout period, the session ends automatically.

## ✨ Features

### 🤖 AI Recognition

- Real-time face detection
- Face recognition using InsightFace embeddings
- Register and manage known faces
- High-accuracy embedding matching

### 🚨 Security System

- Session-based unknown person tracking
- Automatic session start and end detection
- Configurable session timeout
- Prevents duplicate alerts for the same person

### 📷 Evidence Collection

- Captures evidence images of unknown visitors
- Stores images with timestamps
- Event logging with session information

### 📱 Smart Notifications

- Telegram text notifications
- Telegram image alerts
- One notification per unknown session
- Fault-tolerant notification handling

### 💡 Hardware Integration

- ESP8266 (NodeMCU) integration
- USB Serial communication
- LED activation during an active unknown session

### 🏗️ Software Architecture

- Modular project structure
- Event-driven design
- Configurable settings
- Easy to extend with new notification channels and hardware

## 🚀 Current Status

### ✅ Completed

- Face Detection
- Face Recognition
- Face Registration
- Face Database
- Session Management
- Event Management
- Telegram Alerts
- ESP8266 LED Integration
- Event Logging
- Image Capture

### 🔄 In Progress

- Documentation
- Project diagrams

### 📌 Planned

- Video Recording
- Web Dashboard
- Multiple Camera Support
- Email & WhatsApp Notifications
- Database Integration

## 🏗️ System Architecture

VisionGuard AI follows a modular, event-driven architecture where each component has a single responsibility.

```text
                         VisionGuard AI

                              Webcam
                                 │
                                 ▼
                    Face Detection & Recognition
                                 │
                                 ▼
                         Session Manager
                                 │
                                 ▼
                          Event Manager
                                 │
          ┌──────────────┬──────────────┬──────────────┐
          ▼              ▼              ▼
     Image Saver    Event Logger   Notification Layer
                                             │
                               ┌─────────────┴─────────────┐
                               ▼                           ▼
                        Telegram Alert          ESP8266 Controller
                               │                           │
                               ▼                           ▼
                     📱 Telegram Message        💡 LED Indicator(for now)
```

### Workflow

1. Capture video frames from the webcam.
2. Detect and recognize faces.
3. Determine whether the detected person is **Known** or **Unknown**.
4. If an unknown person is detected:
   - Start a new session (if one is not already active).
   - Save an evidence image.
   - Log the event.
   - Send a Telegram alert.
   - Turn ON the ESP8266 LED.
5. While the unknown person remains visible:
   - Keep the session active.
   - Do not send duplicate alerts.
6. If the unknown person disappears for the configured timeout:
   - End the session.
   - Log the session summary.
   - Turn OFF the ESP8266 LED.


## 📁 Project Structure

```text
VisionGuard-AI/
│
├── alerts/              # Notification services
│   └── telegram_alert.py
│
├── camera/              # Webcam handling
│
├── database/            # Face embeddings database
│
├── detection/           # Face detection
│
├── events/              # Session and event management
│
├── hardware/            # ESP8266 communication
│
├── known_faces/         # Registered face images
│
├── logs/                # Event logs
│
├── models/              # AI models
│
├── recognition/         # Recognition pipeline
│
├── registration/        # Face registration
│
├── tools/               # Testing utilities
│
├── unknown_faces/       # Captured unknown-person images
│
├── utils/               # Helper utilities
│
├── config.py            # Project configuration
├── requirements.txt     # Python dependencies
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/VisionGuard-AI.git
cd VisionGuard-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Download the InsightFace model

The first time you run the application, InsightFace automatically downloads the required **buffalo_l** model.

### 6. Configure Telegram

Create a `.env` file in the project root.

```env
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
TELEGRAM_CHAT_ID=YOUR_CHAT_ID
```

### 7. Connect ESP8266

- Connect the NodeMCU ESP8266 to your computer via USB.
- Update the COM port in:

```text
hardware/esp8266_controller.py
```

Example:

```python
ESP8266Controller(port="COM3")
```

### 8. Run the application

```bash
python -m tools.test_recognition
```


## ⚙️ Configuration

Most project settings can be configured from `config.py`.

```python
FACE_MATCH_THRESHOLD = 0.60

RECOGNITION_INTERVAL = 5

SESSION_TIMEOUT_SECONDS = 10

CAMERA_INDEX = 0

ENABLE_TELEGRAM_ALERTS = True
```

These settings allow you to adjust:

- Face recognition sensitivity
- Recognition frequency
- Session timeout duration
- Camera selection
- Telegram notifications



## 🚀 Usage

### Register a Known Person

Place the person's images inside the `known_faces/` directory.

Example:

```text
known_faces/
├── subh/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── image3.jpg
```

Then build the face database by running:

```bash
python -m tools.build_database
```

> This generates face embeddings for all registered people and stores them in the local database.

---

### Start VisionGuard AI

Run the recognition system:

```bash
python -m tools.test_recognition
```

The application will:

- Open the webcam.
- Detect and recognize faces in real time.
- Display recognition results on the screen.
- Monitor unknown-person sessions.

---

### Unknown Person Detection

When an unknown person is detected, VisionGuard AI automatically:

- Starts a new session.
- Captures an evidence image.
- Logs the event.
- Sends a Telegram alert with the captured image.
- Turns ON the ESP8266 LED.

The system sends **only one alert per session**, preventing duplicate notifications.

---

### Session End

If the unknown person leaves the camera view for the configured timeout period:

- The session ends automatically.
- The session summary is logged.
- The ESP8266 LED turns OFF.

If the same person returns later, a **new session** is created automatically.



## 🛠️ Tech Stack

### Programming Language

- Python 3.13

### Computer Vision

- OpenCV
- InsightFace
- ONNX Runtime

### Hardware

- NodeMCU ESP8266
- External LED
- USB Serial Communication

### Notifications

- Telegram Bot API

### Development Tools

- VS Code
- Git & GitHub
- Arduino IDE



## 🗺️ Roadmap

### Completed ✅

- Real-time Face Detection
- Face Recognition
- Face Registration
- Face Embedding Database
- Session-based Event Management
- Evidence Image Capture
- Telegram Alerts
- ESP8266 LED Integration
- Event Logging

### Planned 🚀

- Video Recording
- Web Dashboard
- Multiple Camera Support
- Email Notifications
- WhatsApp Notifications
- Database Integration
- Cloud Deployment


## 👨‍💻 Author

**Subham Mohanty**

- GitHub: https://github.com/subhamohanty07
- LinkedIn: www.linkedin.com/in/subhamohantyy


## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.