import os
import pandas as pd
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

# Define Blueprint (must match the name used in __init__.py)
main = Blueprint('main', __name__)

# --- Folder Paths ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATASET_FOLDER = os.path.join(BASE_DIR, 'datasets')
REPORT_FOLDER = os.path.join(BASE_DIR, 'reports')

# Create folders if not exist
os.makedirs(DATASET_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


@main.route('/')
def index():
    return render_template('index.html', title='AutoInsight - Upload Data')


@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Save uploaded CSV into datasets/
    filename = secure_filename(file.filename)
    dataset_path = os.path.join(DATASET_FOLDER, filename)
    file.save(dataset_path)

    try:
        df = pd.read_csv(dataset_path)
    except Exception as e:
        return f"Error reading CSV: {e}", 500

    # Generate Data Summary
    summary_html = df.describe(include='all').to_html(classes='table table-striped', justify='center')

    # Save summary to reports/
    report_filename = f"summary_{os.path.splitext(filename)[0]}.html"
    report_path = os.path.join(REPORT_FOLDER, report_filename)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(render_template("summary.html", title="Dataset Summary", tables=[summary_html]))

    # Show summary in browser
    return render_template("summary.html", title="Dataset Summary", tables=[summary_html])