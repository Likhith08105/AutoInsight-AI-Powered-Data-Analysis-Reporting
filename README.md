# 🚀 AutoInsight – AI-Powered Data Analysis & Reporting

**AutoInsight** is an intelligent Flask-based data analysis web app that allows users to upload CSV datasets and instantly generate **structured analytical reports** including statistical summaries, missing value detection, and formatted HTML reports — all with one click.

---

## 🧩 Features

- 📂 Upload any CSV file (auto-detects encoding)
- 📊 Instant statistical summary (mean, std, count, etc.)
- ⚠️ Missing value detection per column
- 🎨 Clean, structured HTML report output
- 💾 All reports automatically saved in `/reports`
- 🧠 Extensible for AI-based insights & visualizations

---

## 🏗️ Project Structure

```
AutoInsight/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── reports/
│   └── report_YYYYMMDD_HHMMSS.html
│
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AutoInsight.git
cd AutoInsight
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App
```bash
python run.py
```

Now open your browser and visit:  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 Output Example

After uploading a CSV, the app generates a report like:
```
reports/report_20251006_153212.html
```

The report includes:
- Dataset statistical overview  
- Missing value summary  
- Timestamp  
- Clean structured HTML styling  

---

## 🚀 Future Enhancements

- Integration with **OpenAI API** for AI-driven insights  
- Interactive charts with **Plotly/Seaborn**  
- Advanced data cleaning recommendations  
- Export as PDF or Excel  

---

## 🧑‍💻 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML, CSS |
| **Data Analysis** | Pandas, NumPy |
| **Visualization (Future)** | Matplotlib, Seaborn, Plotly |
| **Deployment** | Render / Streamlit Cloud (optional) |

---

## 🏷️ GitHub Tags
```
#Flask #Python #DataAnalysis #AI #MachineLearning #PortfolioProject #AutoInsight
```

---

## 🧑‍🎓 Author

Likhith kumar Paidimarri<Likhith Kumar Paidimarri> 
Final Year B.Tech | Data Science & AI Enthusiast  
[LinkedIn](https://www.linkedin.com/in/likhith-kumar-paidimarri-312603258/) • [GitHub](https://github.com/Likhith08105)

---

## 📜 License

This project is open-source under the **MIT License**.
