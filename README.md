<div align="center">

# 🚆 Smart Surveillance in Indian Railways

### Deep Learning-Based Person Re-Identification for Public Safety

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=2500&pause=800&color=6366F1&center=true&vCenter=true&width=850&lines=Intelligent+Railway+Surveillance;Deep+Learning+%2B+Computer+Vision;Automated+Person+Re-Identification;Real-Time+Video+Monitoring+%26+Alerts"/>

<br>

<img src="https://img.shields.io/badge/Python-3.7.2-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/CNN-Deep%20Learning-FF6F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest%20%7C%20SVM-6366F1?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Database-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/Domain-Railway%20Safety-16A34A?style=for-the-badge"/>

<br><br>

<a href="https://github.com/ganesh87967">
<img src="https://img.shields.io/badge/GitHub-Ganesh%20Vindekoti-181717?style=for-the-badge&logo=github"/>
</a>

<a href="https://www.linkedin.com/in/ganesh-vindekoti-630191278/">
<img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin"/>
</a>

</div>

---

# 📌 Overview

**Smart Surveillance in Indian Railways** is a deep learning and machine learning-based **Person Re-Identification (Re-ID)** system designed to support public safety in railway environments.

The system extracts high-level **facial and pose features using Convolutional Neural Networks (CNNs)** and uses machine learning classifiers such as **Random Forest and Support Vector Machine (SVM)** to identify suspicious individuals from surveillance footage.

The platform provides separate workflows for **railway administrators and employees**, allowing administrators to manage suspicious-person datasets and train models, while employees can upload and monitor railway surveillance videos.

When a suspicious individual is identified, the system generates and stores an alert for administrative review.

---

# 🎯 Problem Statement

Traditional person identification systems often depend on handcrafted visual features.

These approaches can struggle when there are variations in:

- Lighting
- Pose
- Camera angle
- Appearance
- Clothing
- Surveillance conditions

Manual monitoring of multiple surveillance feeds is also labor-intensive and can result in missed detections.

The project addresses these limitations by using **CNN-based feature extraction combined with machine learning classification** for automated person re-identification. :contentReference[oaicite:1]{index=1}

---

# 💡 Proposed Solution

The system follows an automated pipeline:

```text
Suspicious Person Dataset
            │
            ▼
      Dataset Upload
            │
            ▼
     CNN Feature Extraction
            │
            ▼
    Face + Pose Features
            │
            ▼
    ┌───────┴────────┐
    ▼                ▼
Random Forest       SVM
    │                │
    └───────┬────────┘
            ▼
     Model Comparison
            │
            ▼
     Selected Classifier
            │
            ▼
    CCTV / Test Video
            │
            ▼
   Person Re-Identification
            │
       ┌────┴────┐
       ▼         ▼
    Match      No Match
       │
       ▼
  Alert Logged
       │
       ▼
 Admin Review
