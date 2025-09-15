# Network Intrusion Detection using Machine Learning

This project implements and compares **Deep Neural Networks (DNN)** and **Support Vector Machines (SVM)** for detecting network intrusions using the benchmark **KDDCup99** and **NSL-KDD** datasets.

---

## 🔐 Key Features
- Preprocessing of network traffic datasets (handling missing values, outliers, and class imbalance).
- Implementation of a **7-layer DNN model** for intrusion detection.
- Proposed **two-stage SVM classifier** (one-class for DoS detection + four-class classifier for other intrusions).
- Performance evaluation using **Accuracy, Precision, Recall, and F1-score**.
- Comparative analysis of DNN vs. SVM models.

---

## 📊 Results
- **DNN:** High overall accuracy (~99% on KDDCup99, ~97% on NSL-KDD) but poor detection of R2L & U2R attacks.
- **SVM:** Achieved **better detection accuracy** for minority classes (R2L, U2R), with overall accuracy of **99% on KDDCup99** and **98% on NSL-KDD**.
- Reduced false alarms and improved classification balance.

---

## 🚀 Applications
- Real-time **Intrusion Detection Systems (IDS)** in enterprise networks.
- Can be integrated with firewalls and monitoring tools for enhanced cybersecurity.
- Useful in academic research on **ML-based cybersecurity**.

---

## 🛠️ Tech Stack
- **Python** (NumPy, Pandas, Scikit-learn, TensorFlow/Keras)
- **Jupyter Notebook** for implementation & visualization

---

## 📌 Future Work
- Apply **feature engineering** to improve detection of rare intrusions.
- Explore **hybrid models (DNN + SVM)** for even higher accuracy.
- Extend system for **real-time deployment** with streaming data.

---

## 📎 Datasets
- [KDDCup99](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)
- [NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html)
