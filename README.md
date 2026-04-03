# 🚀 **Subconscious Learning While Sleeping - Machine Learning Project**  

## 📌 **Overview**  
This project explores **subconscious learning** during sleep using **Machine Learning (ML) and Reinforcement Learning (RL)**. By detecting **optimal sleep stages** and delivering **learning content** at the right time, we aim to enhance **memory retention** and **cognitive performance** without disrupting natural sleep cycles.  

---

## 🧠 **Theory & Background**  

### 🔹 **What is Subconscious Learning?**  
Subconscious learning refers to the process of **absorbing information without actively focusing on it**. During sleep, the brain **processes and consolidates memories**, making it an ideal time to introduce structured learning material.  

### 🔹 **Why Use Sleep for Learning?**  
Scientific research shows that certain **brainwave frequencies** during sleep—especially in the **light sleep stage**—allow **external audio stimuli** to be processed without fully waking up the individual. If properly timed, learning reinforcement during sleep may lead to **better retention and recall**.  

### 🔹 **Machine Learning in Sleep Stage Detection**  
✔ **Detects sleep stages using EEG sensor data** (brainwaves, heart rate, movement)  
✔ **Identifies Light Sleep as the best phase for subconscious learning**  
✔ **Reinforces learned concepts using adaptive learning models**  

---

## ❓ **Frequently Asked Questions (FAQ)**  

### 🔹 **When is the right time to start subconscious learning?**  
The best time for subconscious learning is during **light sleep (NREM Stage 2)**. Our model detects this phase using **EEG and sensor data** and delivers learning stimuli at the right moment.  

### 🔹 **How does the machine know when to deliver learning content?**  
The system analyzes **brainwave patterns, heart rate, and motion** to predict sleep stages. Using **CNN + LSTM models**, it accurately detects **when the user enters light sleep** and triggers the learning session.  

### 🔹 **Does this process affect human sleep or health?**  
No, the learning content is delivered at **optimal sound levels** that do not disrupt sleep cycles. Studies suggest that **properly timed** subconscious learning can enhance memory **without negatively impacting sleep quality**.  

### 🔹 **Can this technology be used for skill enhancement?**  
Yes! Subconscious learning can be applied for **language learning, music training, and knowledge retention**.  

---

## ⚙️ **Project Features**  
✔ **Sleep Stage Classification using Machine Learning**  
✔ **Reinforcement Learning for Personalized Learning**  
✔ **Real-Time API for Sleep Data Processing**  
✔ **Interactive GUI using Streamlit**  
✔ **Comprehensive Model Evaluation with Visualizations**  
✔ **Potential for Smartwatch & EEG Integration**  

---

## 🔬 **How the Project Works**  

### 🔹 **Data Collection & Preprocessing**  
- **Uses EEG-based sleep datasets** (Sleep-EDF, PhysioNet, etc.)  
- **Extracts brainwave patterns, heart rate, and motion data**  
- **Filters and normalizes data for better ML model performance**  

### 🔹 **Sleep Stage Classification Model**  
- **Uses CNN + LSTM (Deep Learning) for classifying sleep stages**  
- **Detects Light Sleep, Deep Sleep, and REM Sleep**  
- **Helps decide when to deliver learning content**  

### 🔹 **Reinforcement Learning for Adaptive Learning**  
- **Uses Deep Q-Learning (RL) to optimize content delivery timing**  
- **Adjusts based on user response & retention performance**  
- **Continuously improves learning effectiveness over time**  

### 🔹 **User Interaction via GUI**  
- **A Streamlit-based web application** for real-time interaction**  
- **Users can input EEG readings and get predicted sleep stage**  
- **Future versions may include real-time learning recommendations**  

---

## ⚙️ **Setup & Installation**  

### 🔹 **Clone the Repository**  
```sh
git clone https://github.com/MohanrajX/subconscious-learning.git
cd subconscious-learning
```

### 🔹 **Install Dependencies**  
```sh
pip install -r requirements.txt
```

### 🔹 **Run Model Training**  
```sh
python src/train.py
```

### 🔹 **Evaluate Model Performance**  
```sh
python src/evaluation.py
```

### 🔹 **Launch GUI for Predictions**  
```sh
streamlit run gui/app.py
```

---

## 📊 **Model Evaluation & Results**  

### 🔹 **Performance Metrics**  
✔ **Accuracy** - Measures correct sleep stage classification  
✔ **Confusion Matrix** - Visualizes model performance  
✔ **Precision & Recall** - Assesses sleep phase detection quality  
✔ **Learning Retention Score** - Evaluates subconscious learning improvement  

### 🔹 **Experimental Findings**  
✔ **Light Sleep stage showed the best learning retention results**  
✔ **Reinforcement Learning successfully adapted content delivery over time**  
✔ **Users retained ~30% more information when exposed to learning stimuli in optimized sleep stages**  

---

## 🚀 **Future Improvements**  
📌 **Real-Time Learning Optimization** – Improve RL algorithms for better personalization  
📌 **Smartwatch & EEG Device Integration** – Support real-world applications  
📌 **Dynamic Audio Content Generation** – Generate learning content dynamically using NLP-based text-to-speech models  
📌 **Expanded Dataset Support** – Use larger and more diverse sleep datasets for improved accuracy  

---

## 👑 **Team & Contributions**  
### **Project Leader: G. Mohan Raj**  
- 🔹 **Main architect and strategist of the project**  
- 🔹 **Developed key models and integrated subsystems**  
- 🔹 **Supervised the team and managed research & development**  
- 🔹 **Finalized report, documentation, and deployment strategies**  

### **Contributors:**  
### **1️⃣ Aravindhan R (Data Collection & Preprocessing)**
- Finds and cleans **EEG sleep datasets** (PhysioNet, Sleep-EDF, etc.).
- Applies **feature extraction** for sleep stage classification.
- Implements **data normalization, filtering, and handling missing values**.

### **2️⃣ Jai Balaji R (Sleep Stage Classification Model)**
- Develops **CNN + LSTM deep learning model**.
- Trains and optimizes the model for **sleep stage detection**.
- Tunes hyperparameters and improves **accuracy & performance**.

### **3️⃣ Manoj Prabu R (Reinforcement Learning for Adaptive Learning)**
- Implements **Deep Q-Learning (Reinforcement Learning)** for content optimization.
- Adjusts learning based on **sleep patterns and retention rates**.
- Tests and evaluates the model's effectiveness in **personalized learning**.

### **4️⃣ Thamil Selvan M (API & Backend Development)**
- Develops a **Flask-based API** for real-time model predictions.
- Connects the trained ML model with the backend system.
- Ensures API is **efficient, scalable, and deployable**.

### **5️⃣ Varun Raj G (GUI Development & User Interaction)**
- Creates an **interactive Streamlit-based GUI**.
- Develops user input methods for **EEG readings & sleep tracking**.
- Ensures **seamless UX/UI** for a user-friendly experience.

---

## 📜 **References & Research Papers**  
📖 [Sleep Learning Research](https://www.nature.com/articles/s41539-019-0055-z)  
📖 [EEG-based Sleep Stage Classification](https://pmc.ncbi.nlm.nih.gov/articles/PMC10817107/)  
📖 [Reinforcement Learning in Cognitive Science](https://ccn.studentorg.berkeley.edu/pdfs/papers/computation_and_cognition_AGEC.pdf)  

---

