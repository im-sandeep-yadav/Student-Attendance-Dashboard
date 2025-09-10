# 📊 Student Attendance Dashboard

## 📌 Project Overview
The **Student Attendance Dashboard** is a Python-based project that helps analyze student attendance records.  
It calculates attendance percentages, categorizes students into performance groups, and generates visual insights such as **bar charts, pie charts, and PDF reports**.  
An interactive **Streamlit app** is also included for real-time exploration.

---

## 🚀 Features
- ✅ Import student attendance dataset (CSV)  
- ✅ Calculate **Attendance %** for each student  
- ✅ Categorize students:  
  - Low (<40%)  
  - Medium (40–75%)  
  - High (>75%)  
- ✅ Generate **Bar Chart** (student-wise attendance %)  
- ✅ Generate **Pie Chart** (category distribution)  
- ✅ Save processed dataset & insights  
- ✅ Export **detailed PDF presentation**  
- ✅ Optional: Run interactive **Streamlit dashboard**  

---

## 🗂️ Repository Structure
```
Student-Attendance-Dashboard/
├── data/                  # Dataset files
│   └── students.csv
├── src/                   # Core processing script
│   └── dashboard.py
├── streamlit/             # Streamlit web app
│   └── attendance_dashboard.py
├── notebooks/             # Jupyter Notebook demo
│   └── student_dashboard.ipynb
├── presentation/          # PDF presentation generator
│   └── generate_presentation.py
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignore unnecessary files
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Student-Attendance-Dashboard.git
cd Student-Attendance-Dashboard
```

### 2. Create & activate virtual environment (recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 Option 1 — Run Python script
```bash
python src/dashboard.py
```
📂 Outputs will be saved in `output/` folder:
- `processed_students.csv`  
- `images/bar_chart.png`  
- `images/pie_chart.png`  
- `insights.txt`  

---

### 🔹 Option 2 — Run Jupyter Notebook
```bash
jupyter notebook notebooks/student_dashboard.ipynb
```
Walk through the step-by-step demo with code + charts.

---

### 🔹 Option 3 — Run Streamlit app (interactive)
```bash
streamlit run streamlit/attendance_dashboard.py
```
Open the given local URL in your browser to explore the dashboard interactively.  
You can upload your own CSV or use the default sample data.

---

### 🔹 Option 4 — Generate PDF Presentation
1. Run script first:
   ```bash
   python src/dashboard.py
   ```
   (This generates charts and processed data.)  
2. Then create PDF (optional script in presentation/):
   ```bash
   python presentation/generate_presentation.py
   ```
📄 Output: `presentation/Student_Attendance_Dashboard_Presentation_Detailed.pdf`

---

## 📋 Requirements
- Python 3.8+  
- Libraries: `pandas`, `matplotlib`, `streamlit`, `reportlab`, `jupyter`  

(Install all via `pip install -r requirements.txt`)

---

## 👨‍💻 Author
**Your Name**  
📧 Email: your.email@example.com  
🔗 GitHub: https://github.com/your-username

---

## 📝 License
This project is open-source and available under the MIT License.
