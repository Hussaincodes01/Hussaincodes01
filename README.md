<div align="center">

```
██╗██╗██╗   ██╗ █████╗ ██████╗ 
╚═╝╚═╝╚██╗ ██╔╝██╔══██╗██╔══██╗
         ╚████╔╝ ███████║██║  ██║
          ╚██╔╝  ██╔══██║██║  ██║
           ██║   ██║  ██║██████╔╝
           ╚═╝   ╚═╝  ╚═╝╚═════╝ 
```

# Hi, I'm Jiyad Hussain 👋
### CS Undergrad · AI/ML Engineer · Kaggler · Builder

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jiyad-hussain-50379134b/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hussaincodes01)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hussainbased@gmail.com)

> *"I spend my days cooking, kaggling, colabing, and exploring different video games apart from work."*

</div>

---

## 🧠 About Me

I'm a **B.Tech Computer Science** student at **Amity University, Noida** (CGPA: 8.0, graduating 2028), obsessed with building AI that actually does something useful — from detecting microscopic PCB defects to translating 3000-year-old Akkadian cuneiform.

- 🔬 Deep Learning · NLP · Computer Vision · Model Deployment
- 🏆 Top 10 Kaggle competition finisher | NVIDIA Certified in Deep Learning
- ⚡ Favourite stack: `PyTorch` + `HuggingFace` + `FastAPI` + `Docker`
- 🍳 Off-screen: cooking, football, video games & wisdom exchange

---

## 🚀 Project Index

> Click any project to explore the repository.

### 🔴 [PCB-Defect-Detection](https://github.com/Hussaincodes01/PCB-Defect-Detection) — *Ongoing*
**Bi-Directional Surface Defect Recognition with Geometric & Photometric Priors**

```
📦 Stack: YOLOv5 · Intel MiDaS · PyTorch · Albumentations · OpenCV
```

| What | How |
|------|-----|
| Novel tri-modal YOLOv5 architecture | Fuses RGB + Depth + Illumination streams via attention |
| Custom 1,500-instance dataset | 11 defect classes across top-surface & back-side PCB |
| Depth & illumination maps | Synthetically generated via Intel MiDaS-Small — no 3D sensors needed |
| Class-aware augmentation pipeline | Preserves YOLO bounding box labels mathematically, eliminates annotation drift |
| Industrial robustness | Handles variable lighting conditions; future scope: edge hardware deployment |

---

### 🟡 [English-to-Akkadian-Translation](https://github.com/Hussaincodes01/English-to-akkadian-translation)
**Akkadian → English Translation Using Byte-Level Transformers** · *Kaggle: Deep Past Challenge*

```
📦 Stack: ByT5 · HuggingFace Transformers · Pandas · Python
```

| What | How |
|------|-----|
| ByT5-based translation pipeline | chrF++ score of **35+** on public leaderboard |
| Custom bucketed batching | Groups samples by length → less padding, faster GPU utilization |
| Vectorized post-processing | Normalizes transliterations, removes repeated n-grams, fixes punctuation |
| End-to-end reproducible pipeline | Data → inference → post-process → CSV export in one script |

---

### 🟢 [Extremism-Text-Detection](https://github.com/Hussaincodes01/Extremism-Text-Detection)
**Social Media Extremism Detection using NLP** · *Kaggle: Top 10 Finish*

```
📦 Stack: Scikit-Learn · XGBoost · NLTK · TF-IDF · Python
```

| What | How |
|------|-----|
| Full NLP pipeline | TF-IDF n-grams + word embeddings → supervised classifiers |
| Thorough data cleaning | Lowercasing, stopword removal, tokenization, emoji/URL stripping, slang normalization |
| Multi-model experimentation | Naive Bayes · SVM · Logistic Regression · Random Forest · XGBoost |
| Selection criteria | Best F1-score on extremist class on held-out validation set |
| Competition result | 🏆 **Top 10** in Kaggle competition |

---

### 🔵 [Text-Token-Classifier-AI-VS-Human-Text](https://github.com/Hussaincodes01/Text-Token-Classifier-AI-VS-Human-Text)
**AI vs Human Text Classification with DeBERTa-Large**

```
📦 Stack: DeBERTa-Large · HuggingFace Transformers · Jupyter · Python
```

| What | How |
|------|-----|
| Architecture | DeBERTa-Large fine-tuned for binary text classification |
| Datasets | HC3 + WikiText-103 benchmark datasets |
| Goal | Distinguish AI-generated vs human-written text at token level |
| Reproducible | Full pipeline in Jupyter Notebook |

---

### 🟣 [HackPair](https://github.com/Hussaincodes01/HackPair)
**Real-Time Code Collaboration for Hackathon Teams**

```
📦 Stack: TypeScript · VS Code Extension API · WebSockets
```

| What | How |
|------|-----|
| Self-hosted VS Code extension | Zero-config, no cloud, no Docker, no setup |
| Real-time collaboration | See teammates' cursors, code, and file trees instantly |
| Built for hackers | Designed specifically for fast-paced hackathon environments |

---

## 🛠️ Tech Arsenal

<div align="center">

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)

**ML / DL Frameworks**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21F?style=flat-square&logo=huggingface&logoColor=black)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-006600?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

**Deployment & MLOps**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![ONNX](https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white)
![Weights & Biases](https://img.shields.io/badge/W&B-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black)

**Data & Visualization**

![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat-square)

</div>

---

## 🏆 Achievements

```
🥇  NVIDIA Certified — Fundamentals of Deep Learning (Oct 2025)
🏅  Top 10 — Kaggle: Social Media Extremism Detection Competition
🎯  Kaggle: Deep Past Challenge — chrF++ Score 35+ on Akkadian Translation
```

---

## 📊 GitHub Stats

<div align="center">

![Jiyad's GitHub Stats](https://github-readme-stats.vercel.app/api?username=Hussaincodes01&show_icons=true&theme=radical&hide_border=true&count_private=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Hussaincodes01&layout=compact&theme=radical&hide_border=true)

![GitHub Streak](https://streak-stats.demolab.com?user=Hussaincodes01&theme=radical&hide_border=true)

</div>

---

## 📬 Let's Connect

<div align="center">

Whether you want to talk about deep learning architectures, Kaggle strategies, or swap recipes — I'm always up for a good conversation.

[![LinkedIn](https://img.shields.io/badge/Connect_on_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jiyad-hussain-50379134b/)
[![Email](https://img.shields.io/badge/Drop_an_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hussainbased@gmail.com)

---

*"Build things. Break things. Learn things. Repeat."*

![Profile Views](https://komarev.com/ghpvc/?username=Hussaincodes01&color=blueviolet&style=flat-square)

</div>
