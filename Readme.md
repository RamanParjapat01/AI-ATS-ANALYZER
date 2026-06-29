# 🚀 AI-Powered ATS Resume Analyzer

A sophisticated Applicant Tracking System (ATS) designed to bridge the gap between candidate resumes and job descriptions using Generative AI. This system performs deep-text analysis to provide actionable insights for entry-level engineering roles.

---

## 🛠️ Technical Architecture

* **Core Engine:** Built on **Google Gemini 3.5 Flash** for high-speed, low-latency resume evaluation.
* **Data Parsing:** Implements `pypdf` for reliable extraction of text data from PDF structures.
* **Frontend:** Developed using **Streamlit**, customized with 3D-transform CSS for a modern, sci-fi inspired user experience.
* **Prompt Engineering:** Optimized system prompts to deliver:
    * **ATS Compatibility Score (0-100)**
    * **Gap Analysis (Missing Keywords)**
    * **Constructive Profile Feedback**

---

## 📂 Project Structure

```text
├── app.py              # Main Application Logic
├── style.css           # 3D UI/UX Stylesheet
├── requirements.txt    # Project Dependencies
├── .gitignore          # Environment/Cache Exclusion
└── README.md           # Documentation