💻 Computer Vision: DeepFake Video Detection System
This repository contains the code and architecture for an advanced Deep Learning system designed to detect manipulated video content, commonly known as "DeepFakes." The system analyzes spatio-temporal inconsistencies in video frames to classify footage as either authentic or fake.



✨ Features
The system's features are structured around three core functional modules:

Video Ingestion & Preprocessing: Handles file input, extracts individual frames, and uses advanced algorithms (like Dlib or MTCNN) to locate and normalize faces, ensuring consistent input for the Deep Learning model.

Spatio-temporal Inference Engine (Core ML): Performs the primary task of Prediction/Classification. It utilizes a deep learning architecture (e.g., CNN-LSTM) to analyze both the visual artifacts within individual frames (spatial features) and the subtle, unnatural movement inconsistencies across frames (temporal features).

Real-time Reporting & Visualization: Generates a final REAL or FAKE verdict based on an aggregate probability score. It produces a time-series report detailing the model's confidence level for every segment of the video, pinpointing exactly where manipulation was likely to have occurred.

High Reliability: A non-functional requirement targeting an Area Under the ROC Curve (AUC) metric of at least 0.95 on unseen data to ensure high accuracy.



⚙️ Installation and Setup

1)Clone the Repository:

2)Setup Environment: Create and activate a Python virtual environment.

3)Install Dependencies:  pip install numpy pandas matplotlib tensorflow/torch opencv-python 

4)Model Placement: Ensure your trained Deep Learning model file (cvt_deepfake_model.h5 or equivalent) is in the correct directory (as defined in deepfake_detector.py).

5)Run the Detector:python deepfake_detector.py



🏗️ Application Logic Highlights
The system operates based on a structured workflow that ensures all data is properly handled before and after the core ML task.

DeepFakeDetector Class: The core of the application, designed to be highly modular by separating logic into distinct methods representing the three major functional modules.

Module 1 (preprocess_video): The data flow starts here. It converts the raw video input into a sequential array of normalized, cropped facial images (tensors).

Module 2 (run_inference): This engine takes the image sequence and feeds it through the Spatiotemporal Model. The CNN layers extract artifacts (spatial features), and the LSTM/Transformer layers analyze the movement patterns over time (temporal features) to produce a "Fake Probability" for every frame.

Module 3 (generate_report): The post-processing stage. It averages the frame probabilities to generate the final aggregate score and classification verdict. It is also responsible for persistent system logging and saving the crucial time-series report plot for analytical use.

Model Selection Rationale: A Convolutional Vision Transformer (CVT) is the preferred architecture, as it effectively handles both spatial and temporal feature extraction necessary for robust deepfake detection.
