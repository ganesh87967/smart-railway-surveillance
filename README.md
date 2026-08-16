
<div align="center">

# 🚆 Smart Surveillance in Indian Railways

### Deep Learning-Based Person Re-Identification for Public Safety

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=2400&pause=700&color=6366F1&center=true&vCenter=true&width=900&lines=Intelligent+Railway+Surveillance;Deep+Learning+%2B+Computer+Vision;Automated+Person+Re-Identification;Video+Monitoring+%26+Alert+Management"/>

<br><br>

<img src="https://img.shields.io/badge/Python-3.7.2-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/CNN-Deep%20Learning-FF6F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Random%20Forest-Machine%20Learning-6366F1?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SVM-Classification-7C3AED?style=for-the-badge"/>
<img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>

<br><br>

<a href="https://github.com/ganesh87967">
<img src="https://img.shields.io/badge/GitHub-Ganesh%20Vindekoti-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://www.linkedin.com/in/ganesh-vindekoti-630191278/">
<img src="https://img.shields.io/badge/LinkedIn-Ganesh%20Vindekoti-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

</div>

---

## 📌 Overview

**Smart Surveillance in Indian Railways** is a deep learning and machine learning-based **Person Re-Identification (Re-ID)** system designed to support intelligent surveillance and public safety in railway environments.

The system extracts high-level **facial and pose features using Convolutional Neural Networks (CNNs)** and uses **Random Forest** and **Support Vector Machine (SVM)** classifiers to identify suspicious individuals from surveillance footage.

The platform provides separate workflows for **Railway Administrators** and **Employees**. Administrators can manage suspicious-person datasets, extract features, train classification models, manage employees, and review alerts. Employees can upload surveillance videos for automated person re-identification and detection.

When a suspicious individual is identified, the system records an alert that can be reviewed by an administrator.

---

## 🎯 Problem Statement

Traditional person identification systems often rely on manually crafted visual features, which can become challenging under real-world surveillance conditions.

The system considers variations such as:

- Different lighting conditions
- Changes in pose
- Camera-angle variations
- Changes in appearance
- Clothing variations
- Complex surveillance environments

Manual monitoring of multiple CCTV feeds is also time-consuming and can be prone to human error.

This project addresses these challenges by combining **CNN-based feature extraction** with **machine learning classification** to automate person re-identification from surveillance footage.

---

## 💡 Proposed Solution

The system follows an end-to-end surveillance workflow:

```text
                 ┌──────────────────────────┐
                 │  Suspicious Person Data   │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │      Dataset Upload      │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │   CNN Feature Extraction │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │   Face + Pose Features   │
                 └────────────┬─────────────┘
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
              ┌─────────────┐   ┌─────────────┐
              │Random Forest│   │     SVM     │
              └──────┬──────┘   └──────┬──────┘
                     │                 │
                     └────────┬────────┘
                              ▼
                 ┌──────────────────────────┐
                 │    Model Evaluation      │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │    Railway Surveillance  │
                 │          Video           │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Person Re-Identification │
                 └────────────┬─────────────┘
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
             Suspicious Match       No Match
                     │                 │
                     ▼                 ▼
              Generate Alert        Continue
                     │
                     ▼
               Store Detection
                     │
                     ▼
                 Admin Review
````

---

# 🧠 How It Works

## 1. Suspicious-Person Dataset

The administrator uploads images of known suspicious individuals into the system.

The dataset acts as the reference database used during person re-identification.

---

## 2. CNN Feature Extraction

The uploaded images are processed using **Convolutional Neural Networks (CNNs)**.

The CNN extracts high-level visual information including:

* Facial features
* Pose information
* Visual representations useful for identification

These extracted features are then provided to the machine learning classifiers.

---

## 3. Model Training

The extracted CNN features are used to train two classification approaches:

* 🌲 Random Forest
* 📐 Support Vector Machine (SVM)

The models are evaluated and compared based on their performance.

---

## 4. Video Monitoring

Railway employees can upload surveillance footage through the employee interface.

The system processes the video and attempts to determine whether a person in the footage matches an individual from the suspicious-person database.

---

## 5. Person Re-Identification

The system processes surveillance footage and compares extracted features against the trained identification model.

```text
CCTV / Test Video
        │
        ▼
 Frame Processing
        │
        ▼
Feature Extraction
        │
        ▼
 Feature Matching
        │
        ▼
  Classification
        │
        ▼
Person Identified?
```

---

## 6. Alert Generation

If a suspicious person is identified, the system generates and stores an alert.

Administrators can then review the generated detections.

---

# 🏗️ System Architecture

```text
                       ┌───────────────────────┐
                       │ Suspicious Person     │
                       │       Dataset         │
                       └───────────┬───────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │   CNN Feature         │
                       │     Extraction        │
                       └───────────┬───────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │ Extracted Features    │
                       └───────────┬───────────┘
                                   │
                     ┌─────────────┴─────────────┐
                     │                           │
                     ▼                           ▼
              ┌──────────────┐            ┌──────────────┐
              │Random Forest │            │     SVM      │
              └──────┬───────┘            └──────┬───────┘
                     │                           │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │   Model Evaluation    │
                       └───────────┬───────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │   Railway Video       │
                       │      Monitoring       │
                       └───────────┬───────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │ Person                │
                       │ Re-Identification     │
                       └───────────┬───────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │   Alert Generation    │
                       └───────────┬───────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │   Admin Alert Review  │
                       └───────────────────────┘
```

---

# 👨‍💼 Admin Module

The Admin interface provides centralized control over the surveillance system.

### Features

* 🔐 Admin Login
* 📁 Suspicious-person Dataset Upload
* 🧠 CNN Feature Extraction
* 🤖 Machine Learning Model Training
* 📊 Model Performance Comparison
* 👥 Employee Management
* 🚨 Alert Management
* 📋 Surveillance Detection Review

### Admin Workflow

```text
Admin Login
     │
     ▼
Upload Suspicious Dataset
     │
     ▼
CNN Feature Extraction
     │
     ▼
Train Models
     │
     ▼
Compare Models
     │
     ▼
Manage Employees
     │
     ▼
Review Alerts
```

---

# 👮 Employee Module

The Employee interface allows authorized railway staff to monitor surveillance footage.

### Features

* 🔐 Employee Login
* 🎥 Railway Surveillance Video Upload
* 🔍 Automated Person Re-Identification
* 🚨 Suspicious-Person Detection
* 📋 Detection Processing
* 🔔 Alert Generation

### Employee Workflow

```text
Employee Login
      │
      ▼
Railway Video Monitoring
      │
      ▼
Upload Video
      │
      ▼
Process Video
      │
      ▼
Person Re-Identification
      │
      ▼
Detection Result
      │
      ▼
Alert if Match Found
```

---

# 🚨 Alert Management

When the system identifies a suspicious individual, the detection is recorded as an alert.

```text
             Video Analysis
                   │
                   ▼
             Person Detected
                   │
                   ▼
              Feature Match
                   │
          ┌────────┴────────┐
          │                 │
         YES                NO
          │                 │
          ▼                 ▼
     Create Alert        No Alert
          │
          ▼
    Store Detection
          │
          ▼
     Admin Review
```

The alert-management workflow allows administrators to review detections generated from monitored videos.

---

# 📊 Model Evaluation

The system evaluates two machine learning approaches:

| Model            | Purpose               |
| ---------------- | --------------------- |
| 🧠 CNN           | Feature Extraction    |
| 🌲 Random Forest | Person Classification |
| 📐 SVM           | Person Classification |

The project compares Random Forest and SVM after training on CNN-extracted features.

**Random Forest achieved higher accuracy in the tested environment and was selected as the better-performing classifier for the implemented system.**

---

# 📈 Results

The implemented system demonstrates:

* ✅ CNN-based feature extraction
* ✅ Face and pose feature processing
* ✅ Random Forest classification
* ✅ SVM classification
* ✅ Automated person re-identification
* ✅ Surveillance video processing
* ✅ Suspicious-person detection
* ✅ Automated alert logging
* ✅ Admin alert management
* ✅ Separate Admin and Employee workflows

The system successfully demonstrates detection of known suspicious individuals from test surveillance videos.

---

# 🖥️ Screenshots

Add the actual project screenshots here.

### Admin Dashboard

![Admin Dashboard](screenshots/admin-dashboard.png)

### Dataset Management

![Dataset Management](screenshots/dataset-upload.png)

### CNN Feature Extraction

![CNN Feature Extraction](screenshots/cnn-feature-extraction.png)

### Model Training

![Model Training](screenshots/model-training.png)

### Model Comparison

![Model Comparison](screenshots/model-comparison.png)

### Employee Dashboard

![Employee Dashboard](screenshots/employee-dashboard.png)

### Railway Video Monitoring

![Video Monitoring](screenshots/video-monitoring.png)

### Suspicious Person Detection

![Suspicious Detection](screenshots/suspicious-detection.png)

### Alert Management

![Alert Management](screenshots/alerts.png)

---

# 📂 Project Structure

```text
smart-railway-surveillance/
│
├── README.md
├── requirements.txt
├── Database.txt
├── run.bat
│
├── testVideos/
│   ├── video1.mp4
│   ├── video2.mp4
│   └── ...
│
├── dataset/
│   └── suspicious-person-images/
│
├── model/
│   └── trained-model-files/
│
├── templates/
│   ├── admin/
│   └── employee/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── application/
    ├── models/
    ├── views/
    └── utilities/
```

---

# 🛠️ Technology Stack

### Programming

![Python](https://img.shields.io/badge/Python-3.7.2-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

### Deep Learning

![CNN](https://img.shields.io/badge/CNN-Deep%20Learning-FF6F00?style=for-the-badge)

### Machine Learning

![Random Forest](https://img.shields.io/badge/Random%20Forest-Classification-16A34A?style=for-the-badge)

![SVM](https://img.shields.io/badge/SVM-Classification-6366F1?style=for-the-badge)

### Database

![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)

### Application

![Web Application](https://img.shields.io/badge/Web--Based%20Application-7C3AED?style=for-the-badge)

### Domain

![Railway](https://img.shields.io/badge/Indian%20Railways-Surveillance-DC2626?style=for-the-badge)

---

# ⚙️ System Requirements

### Operating System

* Windows

### Programming Language

* Python 3.7.2

### Database

* MySQL

### Hardware

The project is designed as a prototype and may require additional computing resources depending on the dataset size and surveillance-video processing workload.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ganesh87967/smart-railway-surveillance.git
```

```bash
cd smart-railway-surveillance
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ MySQL Database Setup

The application uses **MySQL** for storing application and detection-related data.

The project includes a `Database.txt` file containing the required database setup information.

### Setup Workflow

```text
Install MySQL
     │
     ▼
Create Required Database
     │
     ▼
Execute Database Configuration
     │
     ▼
Configure Database Credentials
     │
     ▼
Start Application
```

### Important

Do not upload real passwords, database credentials, API keys, or other secrets to GitHub.

---

# ▶️ Running the Application

The project provides a `run.bat` script for starting the application locally.

On Windows:

```bash
run.bat
```

Follow the local server URL displayed by the application.

---

# 🧪 Testing the System

### Admin

1. Login as administrator.
2. Upload suspicious-person images.
3. Extract CNN features.
4. Train Random Forest and SVM.
5. Compare model performance.
6. Add employee accounts.
7. Review generated alerts.

### Employee

1. Login as an employee.
2. Open railway video monitoring.
3. Upload a test surveillance video.
4. Allow the system to process the video.
5. Observe the identification result.
6. Check whether an alert is generated.

---

# 🔄 End-to-End Workflow

```text
                         START
                           │
                           ▼
                      Admin Login
                           │
                           ▼
                    Upload Dataset
                           │
                           ▼
                 CNN Feature Extraction
                           │
                           ▼
                    Train RF + SVM
                           │
                           ▼
                  Compare Performance
                           │
                           ▼
                   Prepare Monitoring
                           │
                           ▼
                    Employee Login
                           │
                           ▼
                   Upload CCTV Video
                           │
                           ▼
                     Analyze Video
                           │
                           ▼
                   Extract Features
                           │
                           ▼
                Person Re-Identification
                           │
                     ┌─────┴─────┐
                     ▼           ▼
                   Match      No Match
                     │           │
                     ▼           ▼
               Generate Alert  Continue
                     │
                     ▼
                  Store Alert
                     │
                     ▼
                 Admin Review
                     │
                     ▼
                    END
```

---

# 💡 Key Features

| Feature                   | Description                             |
| ------------------------- | --------------------------------------- |
| 🧠 CNN Feature Extraction | Extracts high-level visual features     |
| 👤 Person Re-ID           | Identifies known suspicious individuals |
| 🌲 Random Forest          | Classification model                    |
| 📐 SVM                    | Alternative classification model        |
| 🎥 Video Monitoring       | Processes surveillance footage          |
| 👨‍💼 Admin Panel         | Dataset, employee and alert management  |
| 👮 Employee Panel         | Surveillance video monitoring           |
| 🚨 Alert System           | Records suspicious detections           |
| 🗄️ MySQL                 | Persistent application data storage     |

---

# 🔐 Security & Privacy

This project is an educational/research prototype involving person re-identification and surveillance.

A production deployment would require additional controls such as:

* Secure authentication
* Authorization and role management
* HTTPS
* Encrypted data storage
* Secure biometric-data handling
* Audit logging
* Access control
* Data retention policies
* Privacy protection
* Legal and regulatory compliance
* Human review of automated detections

Automated identification should not be treated as definitive evidence without appropriate human verification.

---

# ⚠️ Limitations

### 1. Pre-recorded Video

The current demonstration focuses on uploaded/test surveillance videos.

### 2. Dataset Diversity

A larger and more diverse dataset could improve robustness across:

* Lighting conditions
* Camera angles
* Occlusion
* Crowd density
* Pose variations

### 3. Recognition Robustness

Real-world surveillance can introduce:

* Low-resolution footage
* Partial visibility
* Motion blur
* Different clothing
* Facial variations

### 4. Deployment

The current project is designed around local deployment.

Large-scale deployment would require additional infrastructure and optimization.

---

# 🚀 Future Enhancements

## 📹 Live CCTV Integration

Integrate live CCTV streams for continuous monitoring.

```text
CCTV Camera
     │
     ▼
Live Stream
     │
     ▼
Frame Processing
     │
     ▼
Person Re-ID
     │
     ▼
Alert
```

---

## 🧠 Multimodal Recognition

Combine multiple signals:

```text
Face
 +
Pose
 +
Gait
 +
Clothing
 +
Context
 =
More Robust Re-Identification
```

---

## ⚡ Edge AI

Deploy optimized models closer to CCTV cameras to reduce latency and network dependency.

---

## 📊 Advanced Analytics

Add:

* Detection statistics
* Alert trends
* Camera-wise analytics
* Time-based analytics
* Detection history
* Monitoring dashboards

---

## 🎨 UI/UX Improvements

Future versions can improve the operational experience through:

* Modern dashboards
* Responsive layouts
* Better information hierarchy
* Real-time status indicators
* Interactive alert management
* Improved accessibility
* Better visualization of detection results

---

## 🔐 Privacy-Preserving Architecture

Future versions should incorporate:

* Data anonymization
* Secure biometric storage
* Access control
* Data retention policies
* Privacy-aware processing
* Appropriate consent and governance mechanisms

---

# 🎓 Academic Context

This project demonstrates the integration of:

```text
Deep Learning
      +
Machine Learning
      +
Computer Vision
      +
Video Processing
      +
Database Systems
      +
Web Application
      =
Intelligent Surveillance Platform
```

It demonstrates how machine learning models can be integrated into a practical application workflow rather than being limited to standalone model experimentation.

---

# 📚 Research Areas

This project connects several technical areas:

* Person Re-Identification
* Computer Vision
* Deep Learning
* Convolutional Neural Networks
* Machine Learning
* Random Forest
* Support Vector Machines
* Video Analytics
* Intelligent Surveillance
* Public Safety
* Database Systems
* Web Applications

---

# 📌 Project Highlights

<div align="center">

|          🧠 AI         |    👤 Recognition    |  🎥 Surveillance |
| :--------------------: | :------------------: | :--------------: |
| CNN Feature Extraction |     Person Re-ID     | Video Monitoring |
|      Random Forest     | Suspicious Detection | Alert Management |
|   SVM Classification   |   Feature Matching   |   Admin Review   |

</div>

---

# ⚖️ Responsible Use

This repository is intended for **educational, academic, and research purposes**.

Person re-identification and biometric surveillance can have significant privacy, security, and ethical implications.

Any real-world deployment should be designed with appropriate:

* Privacy protections
* Legal compliance
* Data governance
* Human oversight
* Security controls
* Responsible AI practices

---

# 👨‍💻 Author

<div align="center">

## Ganesh Vindekoti

### AI & ML Graduate • UI/UX Designer • Full-Stack Developer

<br>

<a href="https://github.com/ganesh87967">
<img src="https://img.shields.io/badge/GitHub-ganesh87967-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://www.linkedin.com/in/ganesh-vindekoti-630191278/">
<img src="https://img.shields.io/badge/LinkedIn-Ganesh%20Vindekoti-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

</div>

---

# ⭐ Support

If you found this project interesting or useful:

⭐ Star the repository

🍴 Fork the repository

💬 Share your feedback

---

<div align="center">

### 🚆 Intelligent Surveillance

### 🧠 Deep Learning

### 👤 Person Re-Identification

### 🚨 Public Safety

**Built with Python, Machine Learning & Deep Learning**

</div>
```
